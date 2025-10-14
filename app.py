from flask import Flask, render_template, request, flash, session
import pickle
import numpy as np
import os

app = Flask(__name__)
app.secret_key = 'chronic_disease_prediction_secret_key_2024'  # Secret key for session management

# Load the model once when the app starts
MODEL_PATH = 'chronic_model.pkl'

def load_model():
    """Load the chronic disease prediction model"""
    try:
        if os.path.exists(MODEL_PATH):
            with open(MODEL_PATH, 'rb') as file:
                model = pickle.load(file)
            print("Model loaded successfully!")
            return model
        else:
            print(f"Model file {MODEL_PATH} not found")
            return None
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# Initialize model as None, will load on first prediction request
chronic_model = None

@app.route('/')
def index():
    """Display the main page with navigation to different test pages"""
    return render_template('index.html')

@app.route('/blood-test')
def blood_test():
    """Display the blood test form page"""
    return render_template('blood_test.html')

@app.route('/urine-test')
def urine_test():
    """Display the urine test form page"""
    return render_template('urine_test.html')

@app.route('/medical-history')
def medical_history():
    """Display the medical history form page"""
    return render_template('medical_history.html')

@app.route('/submit-blood-test', methods=['POST'])
def submit_blood_test():
    """Handle blood test form submission and redirect to urine test"""
    # Store blood test data in session
    from flask import session
    session['pcv'] = request.form['pcv']
    session['hemoglobin'] = request.form['hemoglobin']
    session['serum_creatinine'] = request.form['serum_creatinine']
    session['blood_urea'] = request.form['blood_urea']
    session['blood_glucose'] = request.form['blood_glucose']
    
    flash('Blood test results saved! Please proceed to urine test.', 'success')
    return render_template('urine_test.html')

@app.route('/submit-urine-test', methods=['POST'])
def submit_urine_test():
    """Handle urine test form submission and redirect to medical history"""
    # Store urine test data in session
    from flask import session
    session['specific_gravity'] = request.form['specific_gravity']
    session['albumin'] = request.form['albumin']
    session['rbc_count'] = request.form['rbc_count']
    
    flash('Urine test results saved! Please complete your medical history.', 'success')
    return render_template('medical_history.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle final form submission and make prediction"""
    from flask import session
    global chronic_model
    try:
        # Store medical history data in session
        session['hypertension'] = request.form['hypertension']
        session['diabetes'] = request.form['diabetes']
        
        # Check if all required data is in session
        required_fields = ['pcv', 'hemoglobin', 'serum_creatinine', 'blood_urea', 'blood_glucose',
                          'specific_gravity', 'albumin', 'rbc_count', 'hypertension', 'diabetes']
        
        missing_fields = [field for field in required_fields if field not in session]
        if missing_fields:
            flash(f'Missing data for: {", ".join(missing_fields)}. Please complete all steps.', 'error')
            return render_template('index.html', error="Incomplete data")
        
        # Load model if not already loaded
        if chronic_model is None:
            chronic_model = load_model()
            if chronic_model is None:
                flash('Model not available. Please check if chronic_model.pkl exists and is valid.', 'error')
                return render_template('results.html', error="Model not available")
        
        # Extract data from session
        pcv = float(session['pcv'])
        hemoglobin = float(session['hemoglobin'])
        serum_creatinine = float(session['serum_creatinine'])
        blood_urea = float(session['blood_urea'])
        blood_glucose = float(session['blood_glucose'])
        specific_gravity = float(session['specific_gravity'])
        albumin = float(session['albumin'])
        rbc_count = float(session['rbc_count'])
        hypertension = int(session['hypertension'])
        diabetes = int(session['diabetes'])
        
        print(f"Final prediction with: PCV={pcv}, Hemoglobin={hemoglobin}, Creatinine={serum_creatinine}")
        print(f"Blood Urea={blood_urea}, Glucose={blood_glucose}, Specific Gravity={specific_gravity}")
        print(f"Albumin={albumin}, RBC={rbc_count}, Hypertension={hypertension}, Diabetes={diabetes}")

        # Prepare input array for prediction
        input_features = np.array([[
            pcv, hemoglobin, serum_creatinine, blood_urea,
            blood_glucose, specific_gravity, albumin,
            rbc_count, hypertension, diabetes
        ]])
        
        # Make prediction
        prediction = chronic_model.predict(input_features)[0]
        
        # Interpret prediction result
        if prediction == 1:
            result = "Chronic Kidney Disease Detected"
            result_class = "positive"
        else:
            result = "No Chronic Disease Detected"
            result_class = "negative"
        
        # Clear session data after prediction
        for field in required_fields:
            session.pop(field, None)
        
        return render_template('results.html', 
                             prediction_result=result, 
                             result_class=result_class,
                             all_data={
                                 'pcv': pcv, 'hemoglobin': hemoglobin, 'serum_creatinine': serum_creatinine,
                                 'blood_urea': blood_urea, 'blood_glucose': blood_glucose,
                                 'specific_gravity': specific_gravity, 'albumin': albumin, 'rbc_count': rbc_count,
                                 'hypertension': hypertension, 'diabetes': diabetes
                             })
        
    except ValueError as e:
        flash('Please enter valid numeric values for all fields.', 'error')
        return render_template('medical_history.html', error="Invalid input values")
    
    except Exception as e:
        flash(f'An error occurred during prediction: {str(e)}', 'error')
        return render_template('medical_history.html', error="Prediction error")

if __name__ == '__main__':
    app.run(debug=True)
