import streamlit as st
import time
import random
import pickle
from values import seiz, no_seiz,predict_seizure

model = pickle.load(open('EE_model.pkl', 'rb'))
def pred(input_data):
    inputt = np.array(input_data).reshape(1,-1)
    prediction = model.predict(inputt)[0]
    return prediction

def page_2():
    st.title('Epileptic Seizure Prediction')
    st.write("Enter the EEG readings of the mentioned channels")
    val1 = st.number_input('# FP1-F7', min_value=-0.000081100000000, max_value=0.000174457000000, format="%.15f")
    val2 = st.number_input('C3-P3', min_value=-0.000011900000000, max_value=0.000058400000000, format="%.15f")
    val3 = st.number_input('P3-O1', min_value=-0.000004490000000, max_value=0.000126789000000, format="%.15f")
    val4 = st.number_input('P4-O2', min_value=0.000017400000000, max_value=0.000163907000000, format="%.15f")
    val5 = st.number_input('P7-O1', min_value=0.000005670000000, max_value=0.000145934000000, format="%.15f")
    val6 = st.number_input('P7-T7', min_value=-0.000067000000000, max_value=0.000012700000000, format="%.15f")
    val7 = st.number_input('T8-P8-0', min_value=-0.000179145000000, max_value=0.000115067000000, format="%.15f")
    input_data = [val1, val2, val3, val4, val5, val6, val7]
    
    if st.button('Predict'):
        with st.spinner("Predicting..."):
            delay = random.randint(5, 10)
            time.sleep(delay)
            prediction = predict_seizure(input_data)   
        if prediction == 0:
            st.error('A seizure is going to occur in a few minutes. Take necessary precautions!!!')
            st.write("**Take a look at the Precautions section for more information.**")
        else:
            st.success('No seizure is going to occur . Keep calm and carry on!')

def main():
    page_2()

if __name__ == "__main__":
    main()
