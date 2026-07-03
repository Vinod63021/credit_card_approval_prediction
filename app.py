from flask import Flask, request, render_template
import pickle
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

# Force Flask to reload HTML changes immediately
app.config['TEMPLATES_AUTO_RELOAD'] = True 

# Load the trained model using a relative path
# It will look for the model in the exact same folder as this app.py file
MODEL_PATH = 'approval_model.pkl'

try:
    with open(MODEL_PATH, 'rb') as file:
        model = pickle.load(file)
        print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Capture data from the HTML form
        data = {
            'CODE_GENDER': request.form.get('gender'),
            'FLAG_OWN_CAR': request.form.get('car'),
            'FLAG_OWN_REALTY': request.form.get('realty'),
            'AMT_INCOME_TOTAL': float(request.form.get('income')),
            'NAME_INCOME_TYPE': request.form.get('income_type'),
            'NAME_EDUCATION_TYPE': request.form.get('education'),
            'NAME_FAMILY_STATUS': request.form.get('family_status'),
            'NAME_HOUSING_TYPE': request.form.get('housing'),
            'DAYS_BIRTH': -float(request.form.get('age')) * 365.25,
            'DAYS_EMPLOYED': -float(request.form.get('years_employed')) * 365.25,
            'CNT_FAM_MEMBERS': float(request.form.get('family_members'))
        }

        # 2. Convert to DataFrame
        input_df = pd.DataFrame([data])

        # 3. Apply the EXACT same preprocessing steps used in your notebook
        # Convert text columns to dummy variables (0s and 1s)
        input_df = pd.get_dummies(input_df)
        
        # --- THE MAGIC FIX: Align the web data with the model's memory ---
        model_columns = model.feature_names_in_ 
        input_df = input_df.reindex(columns=model_columns, fill_value=0)
        
        # 4. Make prediction
        prediction = model.predict(input_df)
        
        # 5. Interpret result
        if prediction[0] == 1:
            result = "Oops! You should try again. Application Denied."
            status = "denied"
        else:
            result = "Congratulations! Your application is approved."
            status = "approved"
            
        return render_template('index.html', prediction_text=result, status=status)

    except Exception as e:
        return render_template('index.html', prediction_text=f"An error occurred: {e}", status="error")

if __name__ == "__main__":
    app.run(debug=True)