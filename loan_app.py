
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import warnings
import streamlit as st 
import joblib

data = pd.read_csv('after_univariate.csv')

st.set_page_config(page_title="Loan Risk Analysis", layout="wide")
st.title("Loan Risk Prediction Dashboard")
st.image("https://images.pexels.com/photos/4968639/pexels-photo-4968639.jpeg?auto=compress&cs=tinysrgb&w=600"
             )

st.header("Make Predictions")
st.write("Enter feature values to predict loan approval : ")

def getInput():
        
    age = st.slider('How old are you : '.title() , min_value=18 , max_value=69 , step=1)
        
    annualincome = st.slider('What is your annual income :'.title() , min_value=10000.0, max_value=500000.0,step=100.0)
    
    creditscore = st.slider('What about credit score : '.title() , min_value=300 , max_value=800 , step=1)
        
    employmentstatus = st.selectbox("What's your employment status :".title(),
                                        ['Employed', 'Self-Employed', 'Unemployed'])
        
    educationlevel = st.selectbox("What's your educatio level :".title(),
                                        ['Master', 'Associate', 'Bachelor', 'High School', 'Doctorate'])
        
    experience = st.slider('How many years of experience : '.title() , min_value=0 , max_value=52 , step=1)
        
    loanamount = st.slider('What is loan amount you need : '.title() , 
                               min_value=3600.0 , max_value=185000.0 , step=100.0) 
        
        
    loanduration = st.slider('What about loan duration in months : '.title() , 
                               min_value=12 , max_value=120 , step=1) 
    
    maritalstatus = st.selectbox("What's your marital status :".title(),
                                        ['Married', 'Single', 'Divorced', 'Widowed'])
        
    numberofdependents = st.select_slider('Select number of dependences'.title() , [0 , 1 , 2 , 3, 4, 5, 6])
        
    homeownershipstatus = st.selectbox("What's your home owner status :".title(),
                                        ['Own', 'Mortgage', 'Rent', 'Other'])
        
    monthlydebtpayments = st.slider('What about monthly dept payments : '.title() , 
                               min_value=50 , max_value=3000 , step=5)
        
        
    creditcardutilizationrate = st.slider('What is credit card utilization rate : '.title() , 
                               min_value=0.0 , max_value=1.0 , step=0.01)
        
        
    numberofopencreditlines = st.selectbox('Select number of open credit lines'.title() ,
                                                   [0 , 1 , 2 , 3, 4, 5, 6, 7, 8])
        
    numberofcreditinquiries = st.selectbox('Select number of open credit inquiries'.title() ,
                                                   [0 , 1 , 2 , 3, 4])
        
    debttoincomeratio = st.slider('What about dept to income ratio : '.title() , 
                               min_value=0.0 , max_value=5.0 , step=0.001)
        
    bankruptcyhistory = st.selectbox('What about bank ruptcy history :'.title() ,
                                                   [0 , 1])
        
    loanpurpose = st.selectbox("What's your loan purpose :".title(),
                                        ['Home', 'Debt Consolidation', 'Education', 'Other', 'Auto'])
        
    previousloandefaults = st.selectbox('What about previous loan defaults :'.title() ,
                                                   [0 , 1])
        
    paymenthistory = st.slider('What is your paymenthistory : '.title() , 
                               min_value=8 , max_value=45 , step=1)
        
    lengthofcredithistory = st.slider('What is your length of credit history : '.title() , 
                               min_value=1 , max_value=30 , step=1)
        
    savingsaccountbalance = st.slider('What about saving account balance : '.title() , 
                               min_value=70 , max_value=200100 , step=100)
        
    checkingaccountbalance = st.slider('What about checking account balance : '.title() , 
                               min_value=24 , max_value=52580 , step=10)
        
    totalassets = st.slider('What is your total assets : '.title() , 
                               min_value=2000 , max_value=2619700 , step=100)
        
    totalliabilities = st.slider('What is your total liabilities : '.title() , 
                               min_value=370 , max_value=1417400 , step=100)
        
    monthlyincome = st.slider('What is your monthly income : '.title() , 
                               min_value=1200.0 , max_value=25000.0 , step=5.0)
        
    utilitybillspaymenthistory = st.slider('What about utility bills payment history : '.title() , 
                               min_value=0.0 , max_value=1.0 , step=0.001)
        
    jobtenure = st.slider('What about your jobtenure : '.title() , 
                               min_value=0 , max_value=52 , step=1)
        
    networth = st.slider('What is your networth : '.title() , 
                               min_value=-1253500 , max_value=2603500 , step=100)
        
    interestrate = st.slider('What about interest rate : '.title() , 
                               min_value=0.0 , max_value=1.0 , step=0.001)
        
    monthlyloanpayment = st.slider('What is your monthly loan payment : '.title() , 
                               min_value=90.0 , max_value=11000.0 , step=10.0)
        
    riskscore = st.slider('What about risk score : '.title() , 
                               min_value=28.0 , max_value=185.0 , step=1.0)
        
    return pd.DataFrame(
    data=[ 
            [age, annualincome, creditscore, employmentstatus,
       educationlevel, experience, loanamount, loanduration,
       maritalstatus, numberofdependents, homeownershipstatus,
       monthlydebtpayments, creditcardutilizationrate,
       numberofopencreditlines, numberofcreditinquiries,
       debttoincomeratio, bankruptcyhistory, loanpurpose,
       previousloandefaults, paymenthistory, lengthofcredithistory,
       savingsaccountbalance, checkingaccountbalance, totalassets,
       totalliabilities, monthlyincome, utilitybillspaymenthistory,
       jobtenure, networth, interestrate, monthlyloanpayment,
       riskscore]
        ] , 
                 columns=['age', 'annualincome', 'creditscore', 'employmentstatus',
       'educationlevel', 'experience', 'loanamount', 'loanduration',
       'maritalstatus', 'numberofdependents', 'homeownershipstatus',
       'monthlydebtpayments', 'creditcardutilizationrate',
       'numberofopencreditlines', 'numberofcreditinquiries',
       'debttoincomeratio', 'bankruptcyhistory', 'loanpurpose',
       'previousloandefaults', 'paymenthistory', 'lengthofcredithistory',
       'savingsaccountbalance', 'checkingaccountbalance', 'totalassets',
       'totalliabilities', 'monthlyincome', 'utilitybillspaymenthistory',
       'jobtenure', 'networth', 'interestrate', 'monthlyloanpayment',
       'riskscore'])
    
test = getInput()
st.dataframe(test)
model = joblib.load('RF_model.h5')

st.write('Accepted' if model.predict(test) == 1 else 'Denied')
