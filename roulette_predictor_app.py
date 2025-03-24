
import streamlit as st
import random

# Wheel layouts
wheels = {
    "European (0)": [
        0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6,
        27, 13, 36, 11, 30, 8, 23, 10, 5, 24,
        16, 33, 1, 20, 14, 31, 9, 22, 18, 29,
        7, 28, 12, 35, 3, 26
    ],
    "American (0, 00)": [
        '0', 28, 9, 26, 30, 11, 7, 20, 32, 17, 5,
        22, 34, 15, 3, 24, 36, 13, 1, '00', 27,
        10, 25, 29, 12, 8, 19, 31, 18, 6, 21,
        33, 16, 4, 23, 35, 14, 2
    ],
    "Triple-Zero (0, 00, 000)": [
        '0', 28, 9, 26, 30, 11, 7, 20, 32, 17, 5,
        22, 34, 15, 3, 24, 36, 13, 1, '00', 27,
        10, 25, 29, 12, 8, 19, 31, 18, 6, 21,
        33, 16, 4, 23, 35, 14, 2, '000'
    ]
}

st.title("Roulette Predictor AI")
st.markdown("Fun simulation using simple physics and AI-style logic.")

# Select wheel type
wheel_type = st.selectbox("Choose Roulette Wheel Type:", list(wheels.keys()))
wheel_numbers = wheels[wheel_type]

# Custom inputs
st.subheader("Spin Settings")
wheel_rps = st.slider("Wheel Speed (rotations/sec)", 1.0, 5.0, 3.5)
ball_rps = st.slider("Ball Speed (rotations/sec)", 2.0, 8.0, 4.8)
time_until_drop = st.slider("Time Until Ball Drops (sec)", 5.0, 15.0, 9.2)
dealer_start = st.selectbox("Dealer Start Number at Top", wheel_numbers)

# Button to simulate
if st.button("Spin Now"):
    # Calculate position
    wheel_total_rotations = wheel_rps * time_until_drop
    wheel_offset_fraction = wheel_total_rotations % 1
    slots_forward = round(wheel_offset_fraction * len(wheel_numbers))
    start_index = wheel_numbers.index(dealer_start)
    landing_index = (start_index + slots_forward) % len(wheel_numbers)

    predicted_center = wheel_numbers[landing_index]
    prediction_range = []
    for i in range(-3, 4):
        idx = (landing_index + i) % len(wheel_numbers)
        prediction_range.append(wheel_numbers[idx])

    st.success(f"Predicted landing zone: around number **{predicted_center}**")
    st.markdown(f"### Recommended bets: {prediction_range}")
    st.caption("This is a fun prediction tool — no guarantees!")

# Footer
st.markdown("---")
st.caption("Created as a roulette AI concept by ChatGPT.")
