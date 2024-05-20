import streamlit as st
from page1 import page_1
from page2 import page_2
from page3 import page_3
from page4 import page_4

def main():
    # Define a sidebar navigation menu
    st.sidebar.title("Navigation")
    page_selection = st.sidebar.selectbox("Go to", ["Home","About Epilepsy","Prediction", "Precautions"])

    # Display the selected page
    if page_selection == "Home":
        page_1()
    elif page_selection == "About Epilepsy":
        page_4()
    elif page_selection == "Prediction":
        page_2()
    elif page_selection == "Precautions":
        page_3()

if __name__ == "__main__":
    main()
