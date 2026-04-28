from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load trained model
model = pickle.load(open('Diabetes.pkl', 'rb'))


# Home route
@app.route('/')
def home():
    return render_template('index.html')


# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        Pregnancies = int(request.form['Pregnancies'])
        Glucose = int(request.form['Glucose'])
        BloodPressure = int(request.form['BloodPressure'])
        SkinThickness = int(request.form['SkinThickness'])
        Insulin = int(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = int(request.form['Age'])

        # Prepare input for model
        values = np.array([[Pregnancies, Glucose, BloodPressure,
                            SkinThickness, Insulin, BMI,
                            DiabetesPedigreeFunction, Age]])

        # Predict
        prediction = model.predict(values)[0]

        # Result
        result = "Diabetic" if prediction == 1 else "Not Diabetic"

        # Send result to HTML
        return render_template('result.html', prediction_text=result)

    except Exception as e:
        return f"Error occurred: {e}"


# Run app (Render compatible)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)