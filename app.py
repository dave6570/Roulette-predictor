
import streamlit as st
import random
import time
from PIL import Image
import base64

st.set_page_config(page_title="Roulette Predictor AI", layout="centered")

# Load image of roulette wheel
st.title("Roulette Predictor AI")
st.caption("Fun simulation with realistic wheel & AI predictions")

# Display the wheel image (static placeholder)
wheel_image = Image.open("images/roulette_wheel.png")
wheel_placeholder = st.image(wheel_image, caption="Roulette Wheel", use_column_width=True)

# Spin button
if st.button("Spin Now"):
    with st.spinner("Spinning the wheel..."):
        # Simulate spin delay
        for i in range(10):
            time.sleep(0.1)

        # Simulated click sound (will work locally with proper HTML/audio)
        sound_file = "sounds/click.mp3"
        audio_html = f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{base64.b64encode(open(sound_file, "rb").read()).decode()}" type="audio/mp3">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

        # Predict a random number
        numbers = list(range(0, 37))
        predicted_number = random.choice(numbers)
        prediction_range = [(predicted_number + i) % 37 for i in range(-3, 4)]

        st.success(f"The ball is likely to land around **{predicted_number}**")
        st.markdown(f"### Recommended bets: {prediction_range}")
        st.caption("This prediction is for fun and educational purposes.")
