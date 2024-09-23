import streamlit as st
from streamlit_option_menu import option_menu
import firebase_admin
from firebase_admin import credentials, initialize_app, storage, firestore


config = st.secrets['firebase'].to_dict()

cred = credentials.Certificate(config)

# check if the app is already initialized
try:
    firebase_admin.get_app()
except ValueError as e:
    # if not, then initialize it
    initialize_app(cred, {'storageBucket': st.secrets['firebase_storage']})

class global_state:
    def __init__(self):
        self.email=''
        self.subscription = ''
        
if global_state not in st.session_state:
    st.session_state.global_state = global_state()

global_state = st.session_state.global_state



# class MultiApp:
#     def __init__(self):
#         self.apps=[]
#     def add_app(self, title, function):
#         self.apps.append({
#             "title": title,
#             "function": function
#         })
#     def run():
#         with st.sidebar:
#              app = option_menu(
#                  menu_title="REACT-Resume",
#                  options=["About", "Your Account", "Pro"],
#                  icons=["info-circle-fill", "person-circle", "patch-check"],
#                  default_index=0
#              )
#         inner_call = False if global_state.email else True

#         if app=="About":
#             about.app(global_state, inner_call)
#         if app=="Your Account":
#             your_account.app(global_state, inner_call)
#         if app=="Pro":
#             pro.app(global_state, inner_call)
#         # if app=="Premium":
#         #     premium.app()
#         # if app=="Your pre-filled information":
#         #     premium_storage.app()
    
#     run()