import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url('data:image/jpeg;base64,{bin_str}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }}
    
    .content-box {{
        background-color: rgba(255, 255, 255, 0.7); /* semi-transparent white background */
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.5); /* shadow effect */
        text-align: center;
        max-width: 600px;
        margin : 60px;
    }}

    .title {{
        font-size: 36px;
        font-weight: bold;
        color: #000000; /* black text */
        margin-bottom: 20px;
    }}

    .description {{
        font-size: 20px;
        color: #000000; /* black text */
        margin-bottom: 30px;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

def page_1():
    set_background("brain2.jpeg")
    content = """
    <div class='content-box'>
        <p class='title'>Epileptic Seizure Prediction</p>
        <p class='description'><b>This app predicts whether there's an upcoming seizure based on EEG readings.<br>Simply input your EEG readings in the Prediction page and click 'Predict' to get started.<b></p>
    </div>
    """
    st.markdown(content, unsafe_allow_html=True)

if __name__ == "__main__":
    page_1()
