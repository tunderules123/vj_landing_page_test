import streamlit as st

# Custom CSS
st.markdown("""
    <style>
        @keyframes neonBackground {
            0% { background: radial-gradient(circle at 30% 30%, #ff00ff, #000000); }
            50% { background: radial-gradient(circle at 70% 70%, #ff33cc, #000000); }
            100% { background: radial-gradient(circle at 30% 30%, #ff00ff, #000000); }
        }

        body {
            animation: neonBackground 5s infinite alternate;
            background-size: cover;
            height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: white;
            font-family: 'Arial', sans-serif;
        }

        h1 {
            font-size: 50px;
            font-weight: bold;
        }

        svg {
            width: 150px;
            height: 150px;
        }

        @keyframes moveEye {
            0%, 100% { transform: translateX(-10px); }
            50% { transform: translateX(10px); }
        }

        #eye {
            animation: moveEye 2s infinite alternate;
        }
    </style>
""", unsafe_allow_html=True)

# Main UI
st.markdown("<h1>Vocal Justice Lens</h1>", unsafe_allow_html=True)

# SVG Animation
st.markdown("""
    <svg width="200" height="200" viewBox="0 0 200 200">
        <circle cx="90" cy="90" r="60" stroke="white" stroke-width="5" fill="none" />
        <line x1="140" y1="140" x2="180" y2="180" stroke="white" stroke-width="5" />
        <circle cx="90" cy="90" r="30" fill="white" />
        <circle id="eye" cx="90" cy="90" r="10" fill="black" />
    </svg>
""", unsafe_allow_html=True)

# Description
st.markdown("<p>VJ Lens helps educators analyze survey data using AI, providing deep insights into teacher confidence, advocacy, and more.</p>", unsafe_allow_html=True)

# Press Enter Prompt
st.markdown("<p><b>Press 'Enter' to continue...</b></p>", unsafe_allow_html=True)

# Wait for Enter Key
if st.button("Enter"):
    st.switch_page("main_app.py")
