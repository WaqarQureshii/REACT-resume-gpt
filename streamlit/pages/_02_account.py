import streamlit as st

import asyncio
from typing import Optional
from httpx_oauth.clients.google import GoogleOAuth2
from httpx_oauth.oauth2 import OAuth2Token
import jwt

from firebase_admin import auth, exceptions, credentials, initialize_app

from streamlit.main import global_state

#Initialize Google OAuth2 client
client_id = st.secrets["client_id"]
client_secret=st.secrets["client_secret"]
redirect_url = st.secrets["redirect_url"] if not st.secrets['testing_mode'] else st.secrets["redirect_url_test"]
client = GoogleOAuth2(client_id=client_id, client_secret=client_secret)

print(f"account > before app(): {global_state.email}")
def app(global_state,inner_call=False):
    print(f"account > beginning app(): {global_state.email}")
    def decode_user(token: str):
        """
        :param token: jwt token
        :return:
        """
        decoded_data = jwt.decode(jwt=token, options={"verify_signature": False})
        return decoded_data

    async def get_authorization_url(client: GoogleOAuth2, redirect_url: str) -> str:
        authorization_url = await client.get_authorization_url(
            redirect_url,
            scope=["email"],
            extras_params={"access_type": "offline"},
        )

        return authorization_url

    def markdown_button(
        url: str, text: Optional[str] = None, color="#FD504D", sidebar: bool = True
    ):
        markdown = st.sidebar.markdown if sidebar else st.markdown

        markdown(
            f"""
        <a href="{url}" target="_blank">
            <div style="
                display: inline-flex;
                -webkit-box-align: center;
                align-items: center;
                -webkit-box-pack: center;
                justify-content: center;
                font-weight: 400;
                padding: 0.25rem 0.75rem;
                border-radius: 0.25rem;
                margin: 0px;
                margin-bottom: 2px;
                line-height: 1.6;
                width: auto;
                user-select: none;
                background-color: {color};
                color: rgb(255, 255, 255);
                border: 1px solid rgb(255, 75, 75);
                text-decoration: none;
                ">
                {text}
            </div>
        </a>
        """,
            unsafe_allow_html=True,
        )

    async def get_access_token(
        client: GoogleOAuth2, redirect_url: str, code: str
    ) -> OAuth2Token:
        token = await client.get_access_token(code, redirect_url)

        return token

    def get_access_token_from_query_params(
        client: GoogleOAuth2, redirect_url: str
    ) -> OAuth2Token:
        query_params = st.query_params()
        code = query_params["code"][0]
        token = asyncio.run(
            get_access_token(client=client, redirect_url=redirect_url, code=code)
        )

        # Clear query params
        st.query_params.update({"token":token})
        return token


    def show_login_button(
        text: Optional[str] = "Login with Google", color="#FD504D", sidebar: bool = True
    ):
        authorization_url = asyncio.run(
            get_authorization_url(client=client, redirect_url=redirect_url)
        )
        if not global_state.email:
            markdown_button(authorization_url, text, color, sidebar)
            get_logged_in_user_email()

    def get_logged_in_user_email():
        try:
            token_from_params = get_access_token_from_query_params(client, redirect_url)
        except Exception as e:
            print(e)
            return None

        user_info = decode_user(token=token_from_params["id_token"])
        print(user_info)
        global_state.email = user_info["email"]
        print(global_state.email)
        # Check if the user exists in Firebase Authentication
        user = get_or_create_firebase_user(global_state.email)
        st.rerun()
    
    def get_or_create_firebase_user(email: str):
        try:
            # Attempt to get the user by email
            user = auth.get_user_by_email(email)
            return user
        except exceptions.FirebaseError as e:
            user = auth.create_user(email=email)
            return user


    if inner_call:
        show_login_button(
                text='Login with Google', color='#FD504D', sidebar=True
            )

    if not inner_call:
        st.title('Welcome to :bold[TerraSketecher!] ')


        if not get_logged_in_user_email() and not global_state.email:

            show_login_button(
                text="Login With Google", 
            )
        print(f"account > app().notinnercall : {global_state.email}")

        user_email = global_state.email
        print(user_email)
        if user_email:
            
            st.write("Welcome! " + str(user_email))
            print('Email: ',user_email)


            if st.button("Logout", type="primary", key="logout_non_required"):
                global_state.email = ''
                st.rerun()


if __name__ == '__main__':
    print(f"account > if __name__")
    app(global_state)