import streamlit as st

def page_4():
    st.title('About Epilepsy')
    st.markdown("""
        <div class="content-box">
            <div class="content">
                <h3>Epilepsy:</h3>
                <p>Epilepsy is a neurological condition that causes unprovoked, recurrent seizures. Doctors diagnose epilepsy when you have two or more seizures with no other identifiable cause.According to the World Health Organization (WHO), epilepsy affects 60 million people around the world.Anyone can develop epilepsy, but it most commonly onsets in young children and older adults. Men develop epilepsy more often than women, possibly due to higher exposure to risk factors like alcohol use and head trauma.
                </p>
                <h3>Living with Epilepsy:</h3>
                <ul>
                    <li>Keep a seizure diary to help identify possible triggers so you can avoid them.</li>
                    <li>Wear a medical alert bracelet to let people know that you have epilepsy so you get the right medical help if you have a seizure and can’t speak.</li>
                    <li>Teach the people closest to you about seizures and what to do in an emergency.</li>
                    <li>Seek professional help if you have — or think you have — symptoms of depression or anxiety.</li>
                    <li>Engage in health-promoting activities like eating a nutrient-rich, balanced diet and getting regular exercise.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
        .content-box {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 5px 5px 10px #888888;
            margin-bottom: 20px;
        }
        .content {
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

def main():
    page_4()

if __name__ == "__main__":
    main()
