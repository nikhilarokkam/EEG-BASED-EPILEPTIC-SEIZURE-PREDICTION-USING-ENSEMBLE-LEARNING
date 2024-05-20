import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('EE_model.pkl', 'rb'))


def risk_potability_prediction(input_data):
    input_as_array = np.array(input_data).reshape(1,-1)
    prediction = model.predict(input_as_array)[0]
    return prediction


def main():
    st.set_page_config(page_title='EEG - Based Epileptic Seizure Prediction')
    st.title('EEG - Based Epileptic Seizure Prediction')
    st.write('This app predicts Epileptic Seizure Prediction')
    
    st.subheader('Epileptic Seizure Prediction')
    
    mar = st.number_input('# FP1-F7', format="%.7f", min_value=0.0, max_value=100.0, value=7.0, step=0.1)
    deb = st.number_input('C3-P3', format="%.7f", min_value=0.0, value=50.0, step=1.0)
    dis = st.number_input('P3-O1', format="%.7f", min_value=0.0, value=50.0, step=1.0)
    gen = st.number_input('P4-O2', format="%.7f", min_value=-0.0000303, value=50.0, step=1.0)
    crs = st.number_input('P7-O1', format="%.7f", min_value=0.0, max_value=1000.0, step=1.0)
    gdp = st.number_input('P7-T7', format="%.7f", min_value=-0.0000303, value=50.0, step=1.0)
    pqg = st.number_input('T8-P8-0', format="%.7f", min_value=0.0, value=50.0, step=1.0)
    pqg1 = st.number_input('T8-P8-1', format="%.7f", min_value=0.0, value=50.0, step=1.0)
   
   
    if st.button('Predict'):
        input_data = [mar, deb, dis, gen, crs, gdp, pqg, pqg1]
        prediction = risk_potability_prediction(input_data)
        if prediction == 0:
            st.error('The Patient is affected by  Epileptic Seizure.')
            
        else:
            st.success('The Patient is not affected by  Epileptic Seizure.')

if _name_ == '_main_':
    main()