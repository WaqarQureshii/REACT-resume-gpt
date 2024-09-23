import streamlit as st
from authentication.google_auth import get_logged_in_user_email, show_login_button, show_logout_button

from src.main import global_state
import pages._02_account as account

def app():
    print(f"before home>check email: {global_state.email}")
    if not global_state.email:
        account.app(global_state, inner_call=True)
    st.header("[REACT]: *Resume Enhancement and Customization Tool*")
    st.write("")
    st.write("")

    # - - - SUBHEADER: PROCESS - - -
    sub_col1, sub_blank1, sub_col2, sub_blank1, sub_col3 = st.columns([4,1, 1,1, 4])

    with sub_col1:
        st.subheader("""Provide your assistant with your:""")
        st.write("Interested job description")
        st.write("Your Resume")

    with sub_col2:
        st.image("assets/home_transformation_arrow.png", caption="Detailed prompts transform your inputs")

    with sub_col3:
        st.subheader("Your Professional and Customized Output")
        st.write("Presenting resume information concicely, using nice-appropriate language while avoiding redundancy and cliché terms")
        #TODO use https://www.linkedin.com/pulse/how-use-chatgpt-rewrite-your-resume-10-prompts-brian-b-kim/
                        
    comp_col1, comp_col2, comp_col3 = st.columns(3)
    with comp_col1:
        st.subheader("PRO Version")
        st.write("Have your resume edited and modified, based on your input.")
    with comp_col2:
        st.subheader("PREMIUM Version")
        st.write("In addition to the benefits from Pro, you can easily store your resume inputs for your next edit instead of having to input them in for each new job description.")


if __name__ == '__main__':
    st.set_page_config(
        page_title="REACT-Resume Assistant",
        page_icon=":robot:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    print(f"home >if __name__: {global_state.email}")
    app()
