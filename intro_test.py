import streamlit as st
import time

###############################################
# 0. PAGE CONFIG
###############################################
st.set_page_config(page_title="Vocal Justice Lens", layout="wide")

###############################################
# 1. SESSION STATE FOR LANDING PAGE
###############################################
if "entered" not in st.session_state:
    st.session_state["entered"] = False

###############################################
# 2. LANDING PAGE
###############################################
def show_landing_page():
    """
    Displays a white-background landing page with:
    - Large "Vocal Justice Lens" title (60% width)
    - Embedded MP4 animation
    - Explanation text
    - Prompt to press Enter
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
            font-size: 10vw; /* scale with viewport width for dramatic effect */
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

    # Build the landing page layout
    st.markdown(
        """
        <div class="landing-container">
            <div class="landing-title">Vocal Justice Lens</div>
            <div class="video-container">
                <!-- Replace 'YOUR_VIDEO_URL.mp4' with the actual link to your MP4 animation -->
                <video width="400" autoplay loop muted playsinline>
                    <source src="YOU
