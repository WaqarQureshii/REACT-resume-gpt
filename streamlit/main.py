import streamlit as st
import firebase_admin
from firebase_admin import credentials, initialize_app, storage, firestore, auth, exceptions

from httpx_oauth.clients.google import GoogleOAuth2

import asyncio


config = st.secrets['firebase'].to_dict()
cred = credentials.Certificate(config)
class global_state:
    def __init__(self):
        self.email =""

# check if the app is already initialized
try:
    firebase_admin.get_app()
except ValueError as e:
    # if not, then initialize it
    initialize_app(cred, {'storageBucket': st.secrets['firebase_storage']})

client_id = st.secrets["client_id"]
client_secret=st.secrets["client_secret"]
redirect_url = st.secrets["redirect_url"] if not st.secrets['testing_mode'] else st.secrets["redirect_url_test"]
client = GoogleOAuth2(client_id=client_id, client_secret=client_secret)

class global_state:
    def __init__(self):
        self.email=''
        
global_state=global_state()

async def get_access_token(client: GoogleOAuth2, redirect_url: str, code: str):
    return await client.get_access_token(code, redirect_url)

async def get_email(client: GoogleOAuth2, token: str):
    user_id, user_email = await client.get_id_email(token)
    return user_id, user_email

def get_logged_in_user_email():
    try:
        query_params = st.query_params()
        code=query_params.get('code')

        if code:
            token = asyncio.run(get_access_token(client, redirect_url, code))
            st.query_params.update(token)

            if token:
                userid, user_email = asyncio.run(get_email(client, token['access token']))

                if user_email:
                    try:
                        user = auth.get_user_by_email(user_email)
                    except exceptions.FirebaseError:
                        user = auth.create_user(email=user_email)
                    st.session_state.email = user.email
                    global_state.email = user.email

                    return user.email
        return None
    except:
        pass

def show_login_button():
    authorization_url = asyncio.run(client.get_authorization_url(
        redirect_url,
        scope=["email","profile"],
        extras_params={"access_type": "offline"}
    ))
    st.markdown(f'<a href="{authorization_url}" target="_self">Login</a>', unsafe_allow_html=True)
    get_logged_in_user_email()

def app():
    st.title("Test main.py")
    if not global_state.email:
        st.write(global_state.email)
        get_logged_in_user_email()
        if not global_state.email:
            st.write(global_state.email)
            show_login_button()
    
    if global_state.email:
        st.write(f"Welcome {global_state.email}!")
        st.write(global_state.email)
        if st.button("Logout", type="primary", key="Logout_non_required"):
            global_state.email=''
            st.rerun()

app()