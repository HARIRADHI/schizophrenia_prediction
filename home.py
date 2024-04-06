import streamlit as st
import subprocess
def home():
    st.title('Welcome to schizophrenia predictor!')
    st.header('------------------------------------')
    st.markdown('**What is The Problem?**')
    st.write("""Write Your problem statement here""")
    


    st.header('---------------------------')
    st.markdown('**Key Features:**')
    st.write('- Feature 1: <>')
    st.write('- Feature 2: <>')
    st.write('- Feature 3: <>')
    

    
    # Read the contents of the CSS file
    with open(r"app.css", "r") as f:
        css = f.read()

    # Embed the CSS styles using st.markdown
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    if st.button("Click here to Know Whether you have schizophrenia or not!"):
        command = "streamlit run noikani.py"
        subprocess.run(['start', 'cmd', '/k', command], shell=True)

home()
