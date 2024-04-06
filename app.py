import streamlit as st
import subprocess
#import note

with open("app.css","r") as readFile:
        css = readFile.read()
st.markdown(f"<style>{css}</style>",unsafe_allow_html=True)

#st.set_page_config(initial_sidebar_state="collapsed")
user = "guru"
password = '123'
page = st.sidebar.radio("Go to", ["Login"])

if 'authenticated' not in st.session_state:
    # If not authenticated, show the login form
    st.title("Login to access the app")
    username_input = st.text_input("Username:")
    password_input = st.text_input("Password ", type="password")
    if st.button("Login"):
        if password_input == password:
            # If the password is correct, set the authenticated state
            st.session_state.authenticated = True
            command = "streamlit run home.py"
            subprocess.run(['start', 'cmd', '/k', command], shell=True)
            st.success("Logged in successfully!")
            
        elif password_input:
            st.error("Incorrect password. Please try again.")
        
else:
    # Display the selected page
    if page == "Login":
        st.title("You are logged in")
        
         
         
    
