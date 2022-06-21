from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

model = pickle.load(open('Loan_Prediction.pkl', 'rb'))
 
@app.route('/',methods=['GET'])


def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        ApplicantIncome = int(request.form['income'])
    
        Gender = request.form['gender']
        if(Gender =='Male'):
            Gender=1
        else:
            Gender=0
            

        Married=request.form['Merital']
        if(Married=='No'):
            Married=0
        else:
            Married=1
        
        Education=request.form['Education']
        if(Education=='Graduate'):
            Education=1
        else:
            Education=0
            
    
        Credit_History=request.form['Credit_History']
        if(Credit_History == '1.0'):
            Credit_History=1.0
        else:
            Credit_History=0.0
            
        Property_Area=request.form['Property_Area'] #{"Urban":1,"Semiurban":2,"Rural":0}
        if(Property_Area=='Rural'):
            Property_Area=0
        elif(Property_Area == 'Semiurban'):
            Property_Area=2
        else:
            Property_Area=1
            
        Self_Employed=request.form['Self_Employed']
        if(Self_Employed=='No'):
            Self_Employed=0
        else:
            Self_Employed=1
        
        Dependents=request.form['Dependents']
        if(Dependents == '0'):
            Dependents=0
        elif(Dependents == '1'):
            Dependents=1
        elif(Dependents == '2'):
            Dependents=2
        else:
            Dependents=3
        
        LoanAmount = float(request.form['amount'])    
        
        prediction=model.predict([[Married,Dependents , Self_Employed, Gender, Property_Area,
       Credit_History, Education, ApplicantIncome, LoanAmount]])

        ans = prediction
        
        if ans:
            return render_template('index.html',prediction_text="🎉 Congratulations 🎉 You Are Eligible for Loan")
        else:
            return render_template('index.html',prediction_text="😔 Sorry! You Are Eligible for Loan")
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)

