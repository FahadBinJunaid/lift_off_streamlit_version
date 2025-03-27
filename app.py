import streamlit as st
import pyttsx3
import pygame
import time


# Set the page config for better layout and theme
st.set_page_config(page_title="Liftoff Countdown App", page_icon="🚀", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #0b0c2e;
            color: white;
        }
        .stApp {
            background-color: #0b0c2e;
        }
        .stButton > button {
            background-color: #ff5500;
            color: white;
            border-radius: 10px;
            font-size: 18px;
            padding: 12px;
            width: 100%;
        }
        .stButton > button:hover {
            background-color: #ff3300;
        }
        h1, h2, h3, h4, h5, h6, p, label, span {
            color: #ffffff !important;
        }
        div[data-testid="stExpander"] div[role="button"] {
            color: white !important;
        }
        div[data-testid="stExpander"] div.streamlit-expanderContent {
            color: white !important;
            opacity: 1 !important;
        }
        div[data-testid="stExpander"] p, 
        div[data-testid="stExpander"] ul li, 
        div[data-testid="stExpander"] span {
            color: white !important;
            opacity: 1 !important;
        }
        .centered-image img {
            display: block;
            margin: auto;
            width: 600px; /* Keep it 600px as you wanted */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🚀 Liftoff Countdown with TTS and Sound 🎉")

# Description
st.write("🌟 **Welcome to the Liftoff Countdown App!**")
st.write("⏳ **Click the button below to start a countdown from 10 to 1 and trigger a liftoff sound and message!** 🚀🔥")

# Expander with details
with st.expander("ℹ️ **How this app works**"):
    st.write("""
    - 📝 **Click the "Start Countdown" button** to start the countdown from 10 seconds. ⏳  
    - 🎤 The app will **read out loud** each countdown number using text-to-speech.  
    - 🚀 At the end of the countdown, it will display **'Liftoff!'** and play a liftoff sound!  
    - 🎶 If the sound doesn't play, an error message will appear.  
    """)
    
# Initialize pygame for sound
pygame.mixer.init()

def speak(text):
    """ Function to run pyttsx3 text-to-speech """
    engine = pyttsx3.init()
    engine.setProperty("rate", 200)
    engine.setProperty("volume", 1.0)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)  # Use female voice
    engine.say(text)
    engine.runAndWait()

def play_countdown_and_liftoff():
    """ Function to handle countdown, text-to-speech, and sound playback """
    countdown_placeholder = st.empty()  # Placeholder to dynamically update contdown on UI
    liftoff_placeholder = st.empty()  # Placeholder for liftoff message
    gif_placeholder = st.empty()  # Placeholder for GIF display
    
    # Countdown Loop
    for i in range(10, 0, -1):
        countdown_placeholder.markdown(
            f"<h1 style='text-align:center; color: #ff6600; font-size: 80px;'>{i}</h1>", 
            unsafe_allow_html=True)
        speak(str(i))  # Speak sequentially

# Remove Countdown Numbers
    countdown_placeholder.empty()
    
    # Liftoff Message
    liftoff_placeholder.markdown(
        "<h1 style='text-align:center; color: #ff3300; font-size: 80px;'>🔥🚀 Liftoff! 🎉</h1>", 
        unsafe_allow_html=True) 
    
    speak("Liftoff!")  # Speak "Liftoff!" 

    # Remove liftoff
    liftoff_placeholder.empty()
    
    
    # Center the image using Streamlit columns (without deprecated use_column_width)
    col1, col2, col3 = st.columns([1, 2, 1])  # Middle column wider for centering
    with col2:
        gif_placeholder.image("rocket.gif", width=600)
        time.sleep(1)
        
    # Play liftoff Sound (Start sound and GIF together)
    try:
        pygame.mixer.music.load("liftoff.wav")
        pygame.mixer.music.play()
        
        # Wait for GIF to complete (assuming GIF length is 4 seconds, adjust if needed)
        gif_duration = 4  # Set to actual GIF duration
        time.sleep(gif_duration)
        gif_placeholder.empty()  # Remove GIF after it plays once
        
        # Wait for sound to finish before removing GIF
        while pygame.mixer.music.get_busy():
            time.sleep(0.5)  # Check every 0.5 sec if sound is still playing
        
    except Exception as e:
        st.error(f"Error playing sound: {e}")

    
st.title("🚀 Liftoff Countdown with TTS and Sound")
st.write("Click the button below to start the countdown!")

if st.button("Start Countdown 🚀"):
    play_countdown_and_liftoff()  # Run function 
