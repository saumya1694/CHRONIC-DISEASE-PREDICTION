

# 🩺 Chronic Disease Prediction Web App

A Machine Learning-based web application built using Flask that predicts the likelihood of chronic diseases such as diabetes based on user health inputs.

---

## 🚀 Features

* Predicts diabetes using trained ML model
* User-friendly web interface
* Real-time prediction results
* Built with Flask backend and HTML/CSS frontend
* Uses Random Forest algorithm

---

## 🧠 Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas, NumPy
* HTML, CSS

---

## 📊 Dataset

* Pima Indians Diabetes Dataset
* Includes features like glucose level, BMI, age, blood pressure, etc.

---

## ⚙️ How It Works

1. User enters medical details in the web form
2. Data is processed and sent to the ML model
3. Model predicts whether the person is diabetic or not
4. Result is displayed on the web page

---

## 📁 Project Structure

```text
├── app.py
├── Diabetes.py
├── Diabetes.pkl
├── Diabetes_data.csv
├── templates/
├── static/
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/chronic-disease-prediction.git
cd chronic-disease-prediction
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Train the model (if needed)

```bash
python Diabetes.py
```

---

### 4️⃣ Run the application

```bash
python app.py
```

---

### 5️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 🧪 Sample Input

| Feature        | Value |
| -------------- | ----- |
| Pregnancies    | 6     |
| Glucose        | 160   |
| Blood Pressure | 80    |
| Skin Thickness | 35    |
| Insulin        | 180   |
| BMI            | 35    |
| DPF            | 0.8   |
| Age            | 50    |

---

## 🎯 Output

* **Diabetic** or **Not Diabetic**

---



## 🚀 Future Improvements

* Add multiple disease prediction (heart, kidney, etc.)
* Improve UI with Bootstrap or React
* Display prediction probability
* Deploy on cloud platforms (Render, AWS)

---


