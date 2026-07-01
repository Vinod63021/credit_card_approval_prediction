=========================================================
Credit Approval Prediction System
=========================================================

1. PROJECT OVERVIEW
-------------------
This project is a web-based application that predicts whether 
a credit card applicant is "High Risk" or "Low Risk" based 
on their financial and personal history. It utilizes a 
trained Random Forest model and a Flask web server.

2. PREREQUISITES
----------------
Ensure you have Python installed (3.8+ recommended). 
You will need the following libraries installed:

    pip install flask pandas scikit-learn imbalanced-learn

3. PROJECT STRUCTURE
--------------------
Ensure your files are arranged as follows:

    D:\Skillwallet_project\
    │
    ├── app.py                # Main Flask application
    ├── approval_model.pkl    # The trained ML model
    ├── templates\            # Folder for HTML files
    │   └── index.html        # The web interface
    └── creditcard_csv\       # Folder containing your data
        ├── application_record.csv
        └── credit_record.csv

4. HOW TO EXECUTE
-----------------
1. Open your Terminal or Command Prompt.
2. Navigate to the project folder:
   cd D:\Skillwallet_project
3. Start the Flask application:
   python app.py
4. Once the server starts, you will see a message like:
   * Running on http://127.0.0.1:5000
5. Open your web browser and go to: http://127.0.0.1:5000

5. TROUBLESHOOTING
------------------
- "File Not Found" errors: Ensure your CSV files are inside 
  the 'creditcard_csv' folder.
- "Old Website" appearing: Press Ctrl + F5 (Windows) or 
  Cmd + Shift + R (Mac) in your browser to perform a 
  Hard Refresh.
- Server not starting: Ensure you have closed any previous 
  instances of the terminal/server (Ctrl + C).
