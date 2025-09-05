import streamlit as st
import random

# -------------- Page Config --------------
st.set_page_config(page_title="🪄 Magic Number Game", page_icon="🎮", layout="centered")

# -------------- Custom CSS --------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
    }
    .stButton button {
        background-color: #33A1FF;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #1B8FFF;
        color: white;
    }
    .magic-text {
        font-size: 26px;
        font-weight: bold;
        color: #FF5733;
        text-align: center;
    }
    .creator {
        font-size: 16px;
        font-weight: bold;
        color: #8B00FF;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# -------------- App Title --------------
st.markdown("<h1 style='text-align:center;'>🪄 Magic Number Guessing Game 🧙‍♂️</h1>", unsafe_allow_html=True)
st.markdown("<p class='creator'>✨ Created by Areeb ✨</p>", unsafe_allow_html=True)

# -------------- User Input --------------
name = st.text_input("👉 Enter your Name to Start:")
start_game = st.button("🎮 Start Game")

# -------------- Game Logic --------------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.add_number = random.choice([2, 4, 6, 8, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

steps = [
    "🧠 Step 1: Think of any number in your mind.",
    "✖️ Step 2: Now double the number you thought.",
    f"➕ Step 3: Add {st.session_state.add_number} to your total value.",
    "➗ Step 4: Divide the value into two parts and remove one part.",
    "🔄 Step 5: Now subtract your original number.",
    "🎯 Step 6: Magic Reveal... ✨"
]

if start_game and name.strip():
    st.session_state.step = 1

if st.session_state.step > 0 and st.session_state.step <= len(steps):
    st.markdown(f"<p class='magic-text'>{steps[st.session_state.step-1]}</p>", unsafe_allow_html=True)

    if st.session_state.step < len(steps):
        if st.button("➡️ Next Step"):
            st.session_state.step += 1
    else:
        # Final Reveal
        st.balloons()
        st.success(f"🎉 {name}, your final number is **{st.session_state.add_number // 2}** 😎✨")

        # Wrong Answer Option
        if st.button("🤔 Not Correct? Learn Why"):
            st.info(f"""
            📘 **Math Explanation**  

            Let your number = X  

            Step 1: Double → 2X  
            Step 2: Add {st.session_state.add_number} → 2X + {st.session_state.add_number}  
            Step 3: Divide by 2 → (2X + {st.session_state.add_number}) / 2 = X + {st.session_state.add_number // 2}  
            Step 4: Subtract your number (X) → {st.session_state.add_number // 2}  

            ✅ No matter what you choose, the result is always **{st.session_state.add_number // 2}** 🎯
            """)

        # Restart Game
        if st.button("🔄 Restart Game"):
            st.session_state.step = 0
            st.session_state.add_number = random.choice([2, 4, 6, 8, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
