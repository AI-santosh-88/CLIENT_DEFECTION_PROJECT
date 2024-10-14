import streamlit as st
import pandas as pd
import numpy as np
import joblib
import base64

# Load the trained model
model = joblib.load("final_gb_classifier.pkl")






# Function to preprocess input data
def preprocess_input(data):
    df = pd.DataFrame(data, index=[0])
    df['InternetService'] = df['InternetService'].map({'DSL': 0, 'Fiber optic': 1, 'No': 2})
    df['Contract'] = df['Contract'].map({'Month-to-month': 0, 'One year': 1, 'Two year': 2})
    df['PaymentMethod'] = df['PaymentMethod'].map({'Electronic check': 0, 'Mailed check': 1, 'Bank transfer (automatic)': 2, 'Credit card (automatic)': 3})
    return df

# Function to set a background image
import os

# def add_bg_from_local(image_file):
#     if not os.path.isfile(image_file):
#         st.error(f"Image file '{image_file}' not found.")
#         return
#     with open(image_file, "rb") as image:
#         encoded_string = base64.b64encode(image.read()).decode()
#     page_bg_img = f'''
#     <style>
#     body {{
#     background-image: url("data:image/jpg;base64,{encoded_string}");
#     background-size: cover;
#     background-position: center;
#     }}
#     </style>
#     '''
#     st.markdown(page_bg_img, unsafe_allow_html=True)


import os
import base64
import streamlit as st

def add_bg_from_local(image_file):
    if not os.path.isfile(image_file):
        st.error(f"Image file '{image_file}' not found.")
        return

    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()

    page_bg_img = f'''
    <style>
    .stApp {{
    background-image: url("data:image/jpg;base64,{encoded_string}");
    background-size: cover;
    background-position: center;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Call the function to set background
add_bg_from_local('trial1.jpg')





# Call the function to add the background image
# add_bg_from_local('trial1.jpg')


# Streamlit UI
st.title("Client Defection Prediction")

# Collect user inputs
gender = st.radio("Gender", [0, 1])
senior_citizen = st.radio("Senior Citizen", [0, 1])
partner = st.radio("Partner", [0, 1])
dependents = st.radio("Dependents", [0, 1])
phone_service = st.radio("Phone Service", [0, 1])
multiple_lines = st.radio("Multiple Lines", [0, 1])
internet_service = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
online_security = st.radio("Online Security", [0, 1, 2])
online_backup = st.radio("Online Backup", [0, 1, 2])
device_protection = st.radio("Device Protection", [0, 1, 2])
tech_support = st.radio("Tech Support", [0, 1, 2])
streaming_tv = st.radio("Streaming TV", [0, 1])
streaming_movies = st.radio("Streaming Movies", [0, 1])
contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
paperless_billing = st.radio("Paperless Billing", [0, 1])
payment_method = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
monthly_charges = st.number_input("Monthly Charges", value=0.0)
total_charges = st.number_input("Total Charges", value=0.0)
tenure_group = st.number_input("Tenure Group", value=0)

# Make prediction
if st.button("Predict"):
    user_data = {
        'gender': gender,
        'SeniorCitizen': senior_citizen,
        'Partner': partner,
        'Dependents': dependents,
        'PhoneService': phone_service,
        'MultipleLines': multiple_lines,
        'InternetService': internet_service,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'Contract': contract,
        'PaperlessBilling': paperless_billing,
        'PaymentMethod': payment_method,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'tenure_group': tenure_group
    }
    
    processed_data = preprocess_input(user_data)
    
    try:
        prediction = model.predict(processed_data)
        if prediction[0] == 1:
            st.write("The customer is likely to churn.")
        else:
            st.write("The customer is likely to stay.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.write("Created with ❤️ by Santosh")
