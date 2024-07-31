import streamlit as st
import speech_recognition as sr
import requests
import csv
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import streamlit.components.v1 as components
import os

# Function to read the most recent row from CSV
def read_most_recent_row(csv_filename):
    with open(csv_filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    return rows[-1] if rows else None

# Function to generate a response using the provided prompt
def generate_response_llms(prompt):
    url = "https://chat-gpt26.p.rapidapi.com/"

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    headers = {
        "x-rapidapi-key": "6ce8754ec7msh19a016b83cda399p1823c8jsnefa4fb321746",
        "x-rapidapi-host": "chat-gpt26.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'choices' in data and data['choices']:
            content = data['choices'][0]['message']['content']
            return content
    return "Unable to generate response"

# Function to convert text to speech
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    sound = AudioSegment.from_mp3("output.mp3")
    play(sound)

# Function to convert speech to text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

st.title("VisionAI")

# CSS to style the button
st.markdown(
    """
    <style>
    .big-button {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .big-button button {
        padding: 20px 40px;
        font-size: 24px;
        cursor: pointer;
        text-align: center;
        color: #fff;
        background-color: #4CAF50;
        border: none;
        border-radius: 15px;
        box-shadow: 0 9px #999;
        width: 75%;
    }
    .big-button button:hover {background-color: #3e8e41}
    .big-button button:active {
      background-color: #3e8e41;
      box-shadow: 0 5px #666;
      transform: translateY(4px);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the button
if st.button("Click me", key="big_button"):
    text_to_speech("Listening... Please speak now.")
    user_input_type = speech_to_text()

    # Placeholder for the most recent row reading
    most_recent_row = read_most_recent_row('results_data.csv')
    if most_recent_row:
        frame_id, timestamp, frame_path, caption, depth = most_recent_row

        prompt_scene_description =  "Imagine you are an AI visual assistant when I give you the objects in the frame and they are near or far and the caption of the frame you give a detailed description of the scene to help a visually impaired person to remove the pixel values and everything as the information is not essential to analyze the scene, generate the response descriptively and concisely without numbers."
        promt_based_on_scene = "You are an AI assistant helping a visually impaired individual with navigating an unknown environment given the scene description and objects present in the scene answer the following question. And do not answer anything beyond the scope of the scene description, if asked anything bizarre tell I'm not sure no such thing present in scene."

        prompt_scene_description = "Objects: " + depth + " Caption: " + caption  + " "+ prompt_scene_description
        scene_description = generate_response_llms(prompt_scene_description)

        if user_input_type.lower() == "describe the scene":
            response = scene_description
        elif user_input_type.lower() == 'answer questions based on scene':
            if not scene_description:
                prompt = "Objects: " + depth + " Caption: " + caption + " " + prompt_scene_description
                scene_description = generate_response_llms(prompt)
            
            text_to_speech("Ask your question")
            question = speech_to_text()
            if question:
                prompt = "Objects: " + depth + " Scene_description: " + scene_description + " " + promt_based_on_scene + " " + question
                response = generate_response_llms(prompt)
        else:
            prompt = user_input_type
            response = generate_response_llms(prompt)
        
        text_to_speech(response)
    else:
        text_to_speech("No data found in the CSV file.")
