import streamlit as st
import pandas as pd
import joblib
import base64
import io

# Load the model
model = joblib.load("C:\\Users\\Sarrang\\FindDefault\\saved models\\voting_clf.joblib")
st.title('Fraudulent Transaction Detection')

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded file
    df = pd.read_csv(uploaded_file)

    # Detect fraudulent transactions using the model
    predictions = model.predict(df)

    # Add a column to the DataFrame indicating fraudulence
    df['Fraudulent'] = predictions

    # Map numerical predictions to strings for display
    df['Fraudulent'] = df['Fraudulent'].map({0: 'No', 1: 'Yes'})

    # Apply conditional formatting to highlight fraudulent transactions
    def highlight_fraud(row):
        if row['Fraudulent'] == 'Yes':
            return ['background-color: red'] * len(row)
        else:
            return [''] * len(row)

    styled_df = df.style.apply(highlight_fraud, axis=1)

    # Display the styled DataFrame
    st.write(styled_df)