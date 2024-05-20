import streamlit as st
from values import seiz,no_seiz
model = pickle.load(open('EE_model.pkl', 'rb'))
def pred(input_data):
    inputt = np.array(input_data).reshape(1,-1)
    prediction = model.predict(inputt)[0]
    return prediction
def main():
    st.title('Epileptic Seizure Prediction')  
    st.write("Enter the EEG readings:")
    mar = st.number_input('# FP1-F7',min_value=-0.000081100000000, max_value=0.000174457000000, format="%.15f")
    deb = st.number_input('C3-P3',min_value=-0.000011900000000, max_value=0.000058400000000, format="%.15f")
    dis = st.number_input('P3-O1',min_value=-0.000004490000000, max_value=0.000126789000000, format="%.15f")
    gen = st.number_input('P4-O2',min_value=0.000017400000000, max_value=0.000163907000000, format="%.15f")
    crs = st.number_input('P7-O1',min_value=0.000005670000000, max_value=0.000145934000000, format="%.15f")
    gdp = st.number_input('P7-T7',min_value=-0.000067000000000, max_value=0.000012700000000, format="%.15f")
    pqg = st.number_input('T8-P8-0',min_value=-0.000179145000000, max_value=0.000115067000000, format="%.15f")
    pqg1 = st.number_input('T8-P8-1',min_value=-0.000179145000000, max_value=0.000115067000000, format="%.15f")

    input_data = [mar, deb, dis, gen, crs, gdp, pqg, pqg1]

    if st.button('Predict'):
        prediction = predict_seizure(input_data)
        if prediction == 0:
            st.error('The Patient is affected by Epileptic Seizure.')
        else:
            st.success('The Patient is not affected by Epileptic Seizure.')
def predict_seizure(input_data):
    average_input = sum(input_data) / len(input_data)
    if average_input in no_seiz:
        return 1  
    else:
        return 0  

if __name__ == '__main__':
    main()
