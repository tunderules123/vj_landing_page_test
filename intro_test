import streamlit as st

# Initialize session state to control the pre-landing page
if "show_intro" not in st.session_state:
    st.session_state["show_intro"] = True  # Show intro page on first load

# If user has not pressed Enter, show the intro page
if st.session_state["show_intro"]:
    st.markdown(
        """
        <style>
        /* Center everything */
        .full-page {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: #1E1E1E;  /* Dark background */
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: white;
            font-family: 'Inter', sans-serif;
            text-align: center;
            z-index: 9999;
        }

        /* Style for VJ Lens text */
        .title {
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 20px;
        }

        /* Magnifying glass container */
        .magnifying-glass {
            position: relative;
            width: 80px;
            height: 80px;
            border: 6px solid white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
        }

        /* Handle of the magnifying glass */
        .magnifying-glass::after {
            content: "";
            position: absolute;
            bottom: -25px;
            right: -25px;
            width: 40px;
            height: 8px;
            background-color: white;
            transform: rotate(45deg);
        }

        /* Eye inside magnifying glass */
        .eye {
            width: 30px;
            height: 20px;
            background-color: white;
            border-radius: 50%;
            position: absolute;
            animation: move-eye 2s infinite alternate;
        }

        /* Eye animation - looks left & right */
        @keyframes move-eye {
            0% { transform: translateX(-10px); }
            100% { transform: translateX(10px); }
        }

        /* Explanation text */
        .explanation {
            font-size: 18px;
            width: 60%;
            margin-bottom: 20px;
        }

        /* Prompt text */
        .prompt {
            font-size: 16px;
            color: #FAC898;
            font-weight: bold;
            margin-top: 10px;
        }
        </style>

        <div class="full-page">
            <div class="title">VJ Lens</div>
            <div class="magnifying-glass">
                <div class="eye"></div>
            </div>
            <div class="explanation">
                VJ Lens helps educators analyze survey data using AI, providing deep insights into teacher confidence, advocacy, and more.
            </div>
            <div class="prompt">Press "Enter" to continue...</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Capture "Enter" key press
    user_input = st.text_input("", key="enter_prompt")

    if user_input == "":
        st.session_state["show_intro"] = False  # Hide the intro page
        st.experimental_rerun()

else:
    st.write("✅ Intro complete! This is where the real app will load.")
