import streamlit as st
import time

# Set page config
st.set_page_config(page_title="Vocal Justice Lens", layout="wide")

# Session state for tracking if user has entered
if "entered" not in st.session_state:
    st.session_state.entered = False

# If user has NOT entered, show the intro screen
if not st.session_state.entered:
    st.markdown(
        """
        <style>
        /* Full-screen background with neon effect */
        body {
            background: radial-gradient(circle at top left, #ff00ff, #5500ff, black);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
        }

        /* Title Styling */
        h1 {
            font-size: 50px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        /* Description Text */
        p {
            font-size: 18px;
            max-width: 600px;
            margin: auto;
        }

        /* Press Enter Text */
        .enter-text {
            margin-top: 20px;
            font-size: 14px;
            font-weight: bold;
            color: #FFA500;
        }

        /* Magnifying Glass Animation */
        .magnifying-glass {
            position: relative;
            width: 80px;
            height: 80px;
            margin: 20px auto;
        }

        .glass {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            border: 4px solid white;
            position: absolute;
        }

        .handle {
            width: 8px;
            height: 30px;
            background: white;
            position: absolute;
            bottom: -20px;
            left: 36px;
            transform: rotate(45deg);
        }

        /* Eye Animation */
        .eye {
            position: absolute;
            top: 25%;
            left: 25%;
            width: 50%;
            height: 50%;
            background: white;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            animation: blink 3s infinite ease-in-out;
        }

        .pupil {
            width: 20px;
            height: 20px;
            background: black;
            border-radius: 50%;
            animation: movePupil 3s infinite ease-in-out;
        }

        /* Keyframe Animations */
        @keyframes movePupil {
            0%, 100% { transform: translateX(0px); }
            40% { transform: translateX(-10px); }
            80% { transform: translateX(10px); }
        }

        @keyframes blink {
            0%, 100% { height: 50%; }
            10% { height: 10%; }
        }

        </style>

        <h1>Vocal Justice Lens</h1>
        <div class="magnifying-glass">
            <div class="glass"></div>
            <div class="handle"></div>
            <div class="eye">
                <div class="pupil"></div>
            </div>
        </div>
        <p>VJ Lens helps educators analyze survey data using AI, providing deep insights into teacher confidence, advocacy, and more.</p>
        <p class="enter-text">Press "Enter" to continue...</p>
        """,
        unsafe_allow_html=True
    )

    # Wait for user to press enter
    enter_key = st.text_input("Press Enter to continue...", key="enter")
    if enter_key:
        st.session_state.entered = True
        st.experimental_rerun()

# If user has entered, show main app
else:
    st.title("Vocal Justice Survey AI Analysis Tool")

    st.sidebar.header("Upload Your Data")
    pre_file = st.sidebar.file_uploader("Pre-Survey CSV (Onboarding)", type=["csv"])
    post_file = st.sidebar.file_uploader("Post-Survey CSV (Post-Program)", type=["csv"])

    if not pre_file or not post_file:
        st.warning("Please upload both Pre and Post CSV files.")
        st.stop()

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Simulated loading for a smooth transition
    with st.spinner("Loading data..."):
        time.sleep(3)

    # Read CSVs
    onboarding_df = pd.read_csv(pre_file)
    post_program_df = pd.read_csv(post_file)

    st.write("## Data Preview")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("**Pre-Survey (Onboarding) - First 5 Rows**")
        st.dataframe(onboarding_df.head())
    with col_b:
        st.write("**Post-Survey (Post) - First 5 Rows**")
        st.dataframe(post_program_df.head())

    # Define Composite Scores
    confidence_cols = [
        "I know how to help my students communicate persuasively about social justice issues.",
        "I know how to help my students feel confident.",
        "I know how to help my students build their critical consciousness."
    ]
    advocacy_cols = [
        "I frequently talk with my students about social justice issues.",
        "I push my school leadership to integrate social justice education into our core curriculum."
    ]

    for col in confidence_cols + advocacy_cols:
        onboarding_df[col] = pd.to_numeric(onboarding_df[col], errors='coerce')
        post_program_df[col] = pd.to_numeric(post_program_df[col], errors='coerce')

    # Create composite scores
    onboarding_df["Confidence_Composite"] = onboarding_df[confidence_cols].mean(axis=1, skipna=True)
    onboarding_df["Advocacy_Composite"] = onboarding_df[advocacy_cols].mean(axis=1, skipna=True)
    post_program_df["Confidence_Composite"] = post_program_df[confidence_cols].mean(axis=1, skipna=True)
    post_program_df["Advocacy_Composite"] = post_program_df[advocacy_cols].mean(axis=1, skipna=True)

    pre_conf_mean = onboarding_df["Confidence_Composite"].mean()
    post_conf_mean = post_program_df["Confidence_Composite"].mean()
    pre_adv_mean = onboarding_df["Advocacy_Composite"].mean()
    post_adv_mean = post_program_df["Advocacy_Composite"].mean()

    # Simulated loading of graphs
    with st.spinner("Generating graphs..."):
        time.sleep(3)

    fig, ax = plt.subplots(1, 2, figsize=(8, 4))
    ax[0].bar(["Pre", "Post"], [pre_conf_mean, post_conf_mean], color=["blue", "orange"])
    ax[0].set_title("Confidence Scores")
    ax[1].bar(["Pre", "Post"], [pre_adv_mean, post_adv_mean], color=["blue", "orange"])
    ax[1].set_title("Advocacy Scores")
    
    st.pyplot(fig)

    st.success("Analysis Complete!")
