import streamlit as st

# Track whether user has pressed Enter
if "entered" not in st.session_state:
    st.session_state["entered"] = False

def show_landing_page():
    """
    Displays a landing page with:
    - Full-screen MP4 video as background
    - A semi-transparent white overlay
    - Large single-line text "Vocal Justice Lens"
    - Press 'Enter' prompt
    """
    st.markdown(
        """
        <style>
        /* Remove margins/padding and hide scrollbars */
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
        }

        /* Full-screen background video */
        .video-background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: -1; /* behind everything */
        }

        /* White overlay, semi-transparent, so video is visible */
        .overlay {
            position: fixed;
            top: 0; 
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.5); 
            /* Lower alpha => more video visibility 
               If you want more white, increase to 0.7 or 0.8 */
            z-index: 0; /* behind text, above video */
        }

        /* Container for text/elements above overlay */
        .landing-container {
            position: relative;
            z-index: 1; /* above overlay */
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

        /* Title: single line, large text, no wrap */
        .landing-title {
            font-size: 8vw;  /* big text, but a bit smaller than 10vw to avoid line breaks */
            font-weight: bold;
            color: #000000;  /* black text */
            white-space: nowrap; /* force single line */
            margin: 0 auto;
        }

        /* Explanation text below title */
        .explanation {
            font-size: 1.2rem;
            color: #000000; 
            max-width: 60%;
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

    # Embed the video as a background + semi-transparent overlay
    st.markdown(
        """
        <video class="video-background" autoplay loop muted playsinline>
            <!-- Replace with your correct raw MP4 URL -->
            <source src="https://github.com/tunderules123/vj_landing_page_test/raw/refs/heads/main/VJ_Lens_Animation.mp4" type="video/mp4">
            <!-- fallback text -->
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

    # Listen for Enter
    user_input = st.text_input("", key="landing_input")
    if user_input == "":
        st.session_state["entered"] = True
        st.experimental_rerun()

def after_enter():
    """ Placeholder after user presses Enter. """
    st.write("You pressed Enter! This is just a placeholder for now.")

if not st.session_state["entered"]:
    show_landing_page()
else:
    after_enter()
