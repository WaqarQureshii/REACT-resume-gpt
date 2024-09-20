import streamlit as st
from authentication.google_auth import get_logged_in_user_email, show_login_button, show_logout_button
# from openai import OpenAI

### --- PAGE CONFIGURATION --- ###
about_page = st.Page(
    page="1 - about.py",
    title="About REACT-Resume Editor",
    icon=":material/robot_2:"
)

react_pro = st.Page(
    page="2 - react_pro.py",
    title="REACT PRO",
    icon=":material/check_circle:"
)

react_premium = st.Page(
    page="3 - react_premium.py",
    title="REACT PREMIUM",
    icon=":material/verified:"
)

premium_storage = st.Page(page="4 - react_prem_storage.py",
                          title="Premium - Your information",
                          icon=":material/verified:")


### --- LOGIC --- ###
user_email = get_logged_in_user_email()

# IF LOGGED OUT OF GOOGLE
if not user_email:
    st.sidebar.write("Account")
    show_login_button()
    pg = st.navigation(
        [about_page]
    )
    pg.run()
    # st.stop()

# LOGGED INTO GOOGLE
else:
    sidebarcol1, sidebarcol2 = st.sidebar.columns(2)
    sidebarcol1.write("Account")
    sidebarcol1.write(st.session_state.email)
    sidebarcol1 = show_logout_button()
    sidebarcol2.write("Account Status")
    pg = st.navigation(
        {"About REACT": [about_page],
         "Available versions": [react_pro, react_premium, premium_storage]
        }
    )
    pg.run()
    # print(st.session_state)

    # st.stop()
# if not st.session_state.email:
#     print(st.session_state)
#     pg = st.navigation(
#         {
#             "REACT-Resume": [about_page]
#         }
#     )

# else:
#     print(st.session_state)
#     pg = st.navigation(
#         {
#             "REACT-Resume": [about_page],
#             "Paid Section": [react_pro, react_premium, premium_storage]
#         }
#     )

# pg.run()
