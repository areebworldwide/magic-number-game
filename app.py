import streamlit as st
import random
from datetime import datetime
import json
import os

# ---------------- Save Result ----------------
def save_result(name, answer):
    data = {"name": name, "answer": answer, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    file = "results.json"

    if os.path.exists(file):
        with open(file, "r") as f:
            results = json.load(f)
    else:
        results = []

    results.append(data)
    with open(file, "w") as f:
        json.dump(results, f, indent=4)

# ---------------- Explain the Math ----------------
def explain_math(user_value, add_number):
    try:
        user_value = int(user_value)
        explanation = f"""
        You entered: **{user_value}**

        Let your chosen number = {user_value}  

        1️⃣ Step 1: Double → `2 * {user_value}`  
        2️⃣ Step 2: Add {add_number} → `2 * {user_value} + {add_number}`  
        3️⃣ Step 3: Divide total by 2 → `(2*{user_value} + {add_number}) / 2`  
        4️⃣ Step 4: Subtract your number ({user_value}) → `{add_number // 2}`  

        🎯 **So no matter what number you choose, the result is always {add_number // 2}!**
        """
        return explanation
    except ValueError:
        return "⚠️ Please enter a valid number!"

# ---------------- App ----------------
st.set_page_config(page_title="🪄 Magic Number Game", page_icon="🎮", layout="centered")

st.title("🪄 Magic Number Guessing Game 🧙‍♂️")
st.caption("✨ Created by Areeb ✨")

# User input
name = st.text_input("Enter your name:")

# Game state
if "step" not in st.session_state:
    st.session_state.step = 0
if "add_number" not in st.session_state:
    st.session_state.add_number = random.choice([2,4,6,8,10,20,30,40,50,60,70,80,90,100])
if "show_explain" not in st.session_state:
    st.session_state.show_explain = False

steps = [
    "🧠 Step 1: Think of any number in your mind.",
    "✖️ Step 2: Now double the number you thought.",
    f"➕ Step 3: Add {st.session_state.add_number} to your total value.",
    "➗ Step 4: Divide the total by 2.",
    "➖ Step 5: Subtract your original number.",
    "🎯 Step 6: Magic Reveal... ✨"
]

if name:
    st.write(f"Welcome, **{name}**! Ready to play? 😎")

    if st.button("Next ➡️"):
        st.session_state.step += 1
        st.session_state.show_explain = False

    if st.session_state.step < len(steps):
        st.subheader(steps[st.session_state.step])
    else:
        result = st.session_state.add_number // 2
        st.success(f"🎯 {name}, Your answer is **{result}** 😎✨")
        save_result(name, result)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Restart Game"):
                st.session_state.step = 0
                st.session_state.add_number = random.choice([2,4,6,8,10,20,30,40,50,60,70,80,90,100])
                st.session_state.show_explain = False
        with col2:
            if st.button("Not Correct? 🤔"):
                st.session_state.show_explain = True

        # Show explanation if clicked
        if st.session_state.show_explain:
            user_value = st.text_input("Enter the final number you got:")
            if user_value:
                explanation = explain_math(user_value, st.session_state.add_number)
                st.info(explanation)
else:
    st.warning("⚠️ Please enter your name to start the game!")
