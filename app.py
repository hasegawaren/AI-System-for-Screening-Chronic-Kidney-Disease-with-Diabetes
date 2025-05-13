from flask import Flask, render_template, request
import numpy as np
import joblib

model = joblib.load("selected.joblib")
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        Sex = request.form.get('sex')
        Age = request.form.get('age')
        Diabetesduration = request.form.get('diabetesduration')
        BMI = request.form.get('bmi')
        SBP = request.form.get('sbp')
        DBP = request.form.get('dbp')
        HbA1c = request.form.get('hba1c')
        FBG = request.form.get('fbd')
        TG = request.form.get('tg')
        HDLC = request.form.get('hdlc')
        LDLC = request.form.get('ldlc')
        serum_creatinine = request.form.get('serum_creatinine')
        arr = np.array([[Age, Diabetesduration, BMI, SBP, DBP, HbA1c, FBG, TG, HDLC, LDLC, serum_creatinine]])
        pred = model.predict(arr)

        if pred == 1: 
            serum_creatinine = float(serum_creatinine)
            age = float(Age)
            if Sex == 'Female':
                egfr = 194 * (serum_creatinine**-1.094) * (age**-0.287) * 0.739
            else:
                egfr = 194 * (serum_creatinine**-1.094) * (age**-0.287)

            if egfr >= 90:
                egfr_class = "G1 Normal or High"
            elif 60 <= egfr < 90:
                egfr_class = "G2 Mildly Decreased"
            elif 45 <= egfr < 59:
                egfr_class = "G3a Mildly to Moderately Decreased"
            elif 30 <= egfr < 44:
                egfr_class = "G3b Moderate to Severely Decreased"
            elif 15 <= egfr < 29:
                egfr_class = "G4 Severely Decreased"
            else:
                egfr_class = "G5 Kidney Failure"

            egfr_str = "{:.2f}".format(egfr)
            return render_template('result.html', ckd=pred, egfr=egfr_str, egfr_class=egfr_class)
        else:
            return render_template('result.html', ckd=pred)

if __name__ == "__main__":
    app.run(debug=True)