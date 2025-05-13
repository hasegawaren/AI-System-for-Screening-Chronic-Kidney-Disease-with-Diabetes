# AI System for Screening Chronic Kidney Disease with Diabetes

A web-based medical support tool designed to help healthcare professionals assess the risk of **Chronic Kidney Disease (CKD)** in diabetic patients. The system accepts patient input, predicts CKD risk using a pre-trained machine learning model, and calculates the **eGFR** value to classify kidney function levels.

**Published in:** Thai Journal of Health Technology, Vol. 5 No. 2 (2024)  
[View Article (PDF)](https://thaihta.org/journal/file/files/ThaiHTJ_5-2-06.pdf)

## Project Overview

This application simulates a clinical decision support tool, providing:
- Risk prediction for CKD using a pre-trained model
- eGFR (Estimated Glomerular Filtration Rate) calculation
- Classification of kidney function into G1–G5 stages
- Simple and intuitive web interface for data entry and result interpretation

---

## Features

- Input form for entering patient clinical data  
- Real-time CKD risk prediction using a `.joblib` model  
- Automatic calculation of **eGFR** based on sex, age, and serum creatinine  
- Classification into **G1–G5** stages with readable explanation  
- Clean UI rendered with Jinja2 templating via Flask

---

## Tech Stack

| Layer        | Technology                         |
|--------------|-------------------------------------|
| **Frontend** | HTML, CSS, Jinja2 Templates         |
| **Backend**  | Python, Flask, NumPy, Joblib        |
| **Model**    | Pre-trained `.joblib` file (not trained in this project) |
| **Tools**    | Git, VS Code                        |


## Getting Started

### 1. Clone this repo
git clone https://github.com/hasegawaren/AI-System-for-Screening-Chronic-Kidney-Disease-with-Diabetes.git
cd AI-System-for-Screening-Chronic-Kidney-Disease-with-Diabetes
### 2. Install dependencies (if needed)
```bash
pip install flask numpy joblib
### 3. Run the app
```bash
python app.py
### 4. Open browser
```bash
Go to http://localhost:5000

## My Role
- Developed frontend input form using HTML + CSS
- Implemented backend logic in Flask (Python) to:
    Load and use the .joblib model
    Process form inputs
    Calculate eGFR and classify kidney stage
- Rendered results dynamically using Jinja2 templates
- Supported academic publication (but did not train the ML model)
⚠️ Note: The machine learning model (selected.joblib) was provided and not trained in this repository.
 
![image](https://github.com/user-attachments/assets/b6f80770-897b-4a07-a540-9db3ef1cab6a)
![image](https://github.com/user-attachments/assets/5248ffbb-23ba-414f-8c74-94a38522d884)
![image](https://github.com/user-attachments/assets/66bd367a-3652-4b97-b276-036269f6d40e)
