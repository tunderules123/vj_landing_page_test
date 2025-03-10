import streamlit as st

# We'll store a boolean in session state to track if user pressed Enter
if "entered" not in st.session_state:
    st.session_state["entered"] = False

def show_landing_page():
    """
    Displays a white-background landing page with:
    - Large "Vocal Justice Lens" text (~60% screen width)
    - Embedded MP4 video
    - Explanation text
    - Prompt for user to press Enter
    """
    st.markdown(
        """
        <style>
        /* Make entire background white */
        body {
            background-color: #FFFFFF !important;
            margin: 0;
            padding: 0;
        }

        /* Full-screen container */
        .landing-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh; /* full viewport height */
        }

        /* Title styling - super large, bold, ~60% width */
        .landing-title {
            font-size: 10vw; /* scale with viewport width for drama */
            font-weight: bold;
            color: #000000; /* black text */
            text-align: center;
            max-width: 60%;
            margin: 0 auto;
        }

        /* Video container: center the video */
        .video-container {
            margin: 30px 0;
        }

        /* Explanation text styling */
        .explanation {
            font-size: 1.2rem;
            color: #333333;
            max-width: 60%;
            text-align: center;
            margin: 20px auto;
        }

        /* Enter prompt styling */
        .enter-prompt {
            margin-top: 20px;
            font-size: 1rem;
            color: #FFA500;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="landing-container">
            <div class="landing-title">Vocal Justice Lens</div>
            <div class="video-container">
                <!-- Replace 'YOUR_VIDEO_RAW_URL.mp4' with the actual raw link to your MP4 -->
                <video width="400" autoplay loop muted playsinline>
                    <source src="https://github.com/tunderules123/vj_landing_page_test/raw/refs/heads/main/VJ_Lens_Animation.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            <div class="explanation">
                VJ Lens helps educators analyze survey data using AI, providing deep insights 
                into teacher confidence, advocacy, and more.
            </div>
            <div class="enter-prompt">Press "Enter" to continue...</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Listen for "Enter"
    user_input = st.text_input("", key="landing_input")
    if user_input == "":
        st.session_state["entered"] = True
        st.experimental_rerun()

def after_enter():
    """
    This is just a placeholder for what happens after user presses Enter.
    Currently it shows a simple message.
    """
    st.write("You pressed Enter! This is just a placeholder.")
    st.write("Integrate this logic into your main app or redirect as needed.")

# Decide what to show
if not st.session_state["entered"]:
    show_landing_page()
else:
    after_enter()
