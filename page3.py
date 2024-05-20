import streamlit as st

def page_3():
    st.title('Precautions for Epileptic Seizure')
    st.write("**Here are some precautions to take if you or someone you know is affected by epileptic seizures:**")
    st.markdown("""
        <div class="precautions-box">
            <div class="precautions-content">
                <h3>General Precautions:</h3>
                <ul>
                    <li>Move to a safe area to prevent injury from falls.</li>
                    <li>Avoid operating machinery or driving if possible.</li>
                    <li>Loosen tight clothing to ensure ease of breathing.</li>
                    <li>Stay calm and reassure the person experiencing the seizure.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="precautions-box">
            <div class="precautions-content">
                <h3>During a Seizure:</h3>
                <ul>
                    <li>Gently guide the person to the floor if they are not already there.</li>
                    <li>Cushion the head to prevent head injuries.</li>
                    <li>Do not restrain movement unless necessary to prevent injury.</li>
                    <li>Time the seizure to track its duration.</li>
                    <li>Never force anything into the person's mouth.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="precautions-box">
            <div class="precautions-content">
                <h3>After a Seizure:</h3>
                <ul>
                    <li>Stay with the person until they are fully recovered.</li>
                    <li>Offer reassurance and comfort.</li>
                    <li>Help the person to rest and recover.</li>
                    <li>Seek medical attention if the seizure lasts longer than usual or if it is followed by another seizure.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
        .precautions-box {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 5px 5px 10px #888888;
            margin-bottom: 20px;
        }
        .precautions-content {
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

def main():
    page_3()

if __name__ == "__main__":
    main()
