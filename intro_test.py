import streamlit as st

# Track whether user has pressed Enter
if "entered" not in st.session_state:
    st.session_state["entered"] = False

def show_landing_page():
    """
    Displays a dramatic landing page with:
    - Full-screen MP4 video as background
    - White overlay to appear mostly white
    - Large black text for 'Vocal Justice Lens'
    - Explanation text
    - Press 'Enter' prompt
    """
    st.markdown(
        """
        <style>
        /* Remove body margin/padding and hide scrollbars */
        body {
            margin: 0; 
            padding: 0;
            overflow: hidden;
        }

        /* Full-screen video as background */
        .video-background {
            position: fixed;
            top: 0; 
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: -1; /* behind everything */
        }

        /* White overlay (slightly transparent) so the page looks white
           but still shows the animation behind it */
        .overlay {
            position: fixed;
            top: 0; 
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.8); 
            z-index: 0; /* behind text, above video */
        }

        /* Container for all content in front of overlay */
        .landing-container {
            position: relative;
            z-index: 1; /* on top of overlay */
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        /* Giant title, black text */
        .landing-title {
            font-size: 10vw;  /* scales with viewport width */
            font-weight: bold;
            color: #000000;   /* black text */
            text-align: center;
            max-width: 90%;
            margin: 0 auto;
        }

        /* Explanation text below title */
        .explanation {
            font-size: 1.2rem;
            color: #000000; 
            max-width: 60%;
            text-align: center;
            margin: 20px auto;
        }

        /* Prompt for user to press Enter */
        .enter-prompt {
            margin-top: 20px;
            font-size: 1rem;
            color: #FF5733; /* bright orange for emphasis */
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Embed the video as a background and a white overlay on top
    st.markdown(
        """
        <video class="video-background" autoplay loop muted playsinline>
            <source src="Yhttps://github.com/tunderules123/vj_landing_page_test/raw/refs/heads/main/VJ_Lens_Animation.mp4" type="video/mp4">
            <!-- Fallback if browser doesn't support video -->
            Your browser does not support the video tag.
        </video>

        <div class="overlay"></div>

        <div class="landing-container">
            <div class="landing-title">Vocal Justice Lens</div>
            <div class="explanation">
                VJ Lens helps educators analyze survey data using AI, 
                providing deep insights into teacher confidence, advocacy, and more.
            </div>
            <div class="enter-prompt">Press "Enter" to continue...</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Detect user pressing Enter
    user_input = st.text_input("", key="landing_input")
    if user_input == "":
        # If user hits Enter with empty input, we interpret that as continuing
        st.session_state["entered"] = True
        st.experimental_rerun()

def after_enter():
    """
    Placeholder after user presses Enter.
    """
    st.write("You pressed Enter! This is just a placeholder.")
    st.write("Integrate this logic into your main app or redirect as needed.")

# Main logic
if not st.session_state["entered"]:
    show_landing_page()
else:
    after_enter()
