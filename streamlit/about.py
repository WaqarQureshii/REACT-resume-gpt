import streamlit as st

def app():
    st.header("REACT-Resume")

    pro_tab, prem_tab = st.tabs(['Pro', 'Premium'])
    with pro_tab:
        st.header("PRO Version")
        st.write("Have your resume edited and modified, based on your input.")
    with prem_tab:
        st.header("PREMIUM Version")
        st.write("In addition to the benefits from Pro, you can easily store your resume inputs for your next edit instead of having to input them in for each new job description.")