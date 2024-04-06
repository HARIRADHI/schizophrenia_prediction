import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import time
import subprocess


# Load the data and train the model
data = pd.read_csv("data.csv")
features = data.drop("Class_label", axis=1)
target = data["Class_label"]
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Read the contents of the CSS file
with open(r"C:\Users\RAMKUMAR K\Desktop\GURU\app.css", "r") as f:
    css = f.read()

# Embed the CSS styles using st.markdown
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
   

# Define the prediction function
def predict_schizophrenia(alpha, beta, theta, delta, delusions, hallucinations, disorganized_speech, lack_of_thinking):
    new_data = pd.DataFrame({
        "alpha": [alpha],
        "beta": [beta],
        "theta": [theta],
        "delta": [delta],
        "delusions": [delusions],
        "hallucinations": [hallucinations],
        "disorganized_speech": [disorganized_speech],
        "lack_of_thinking": [lack_of_thinking]
    })
    prediction = model.predict(new_data)[0]
    return prediction

# Streamlit UI
def main():
    st.title('Schizophrenia Prediction')
    st.write('Enter the values below to predict whether the person has schizophrenia or not.')

    col1,col2 = st.columns(2)
    alpha = col1.number_input("Enter the alpha value:",min_value=4.0,max_value=7.9, value=4.0)
    beta = col1.number_input("Enter the beta value:",min_value=12.0,max_value = 15.0, value=12.0)
    theta = col1.number_input("Enter the theta value:", min_value = 7.5,max_value = 9.5,value=7.5)
    delta = col1.number_input("Enter the delta value:", min_value = 3.0,max_value = 5.0,value=3.0)
    delusions = col2.number_input("Enter the delusions value:", max_value = 1.0,value=0.0)
    hallucinations = col2.number_input("Enter the hallucinations value:",max_value = 1.0, value=0.0)
    disorganized_speech = col2.number_input("Enter the disorganized speech value:",max_value = 1.0, value=0.0)
    lack_of_thinking = col2.number_input("Enter the lack of thinking value:",max_value = 1.0, value=0.0)

    if st.button('Predict'):
        prediction = predict_schizophrenia(alpha, beta, theta, delta, delusions, hallucinations, disorganized_speech, lack_of_thinking)
        if prediction == 1:
            st.write("Schizophrenia is likely")
            st.write("Wait! you'll be redirected......")
            time.sleep(3)
            command = "streamlit run likely.py"
            subprocess.run(['start', 'cmd', '/k', command], shell=True)

            
        else:
            st.write("Schizophrenia is unlikely")

main()
