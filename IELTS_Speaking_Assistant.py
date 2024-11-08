import random
import time
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from gtts import gTTS
import speech_recognition as sr
import google.generativeai as genai
import threading

# --------------- INITIALIZATION SECTION ---------------

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Configure the Generative AI API for evaluation
genai.configure(api_key="Your GenAI key")
model = genai.GenerativeModel("gemini-1.5-flash")

# --------------- FILE READING SECTION ---------------

# Function to read topics and questions from a text file
def read_topics_and_questions(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    topics_and_questions = {}
    current_topic = None

    for line in lines:
        line = line.strip()
        # Detect the start of a new topic
        if line.startswith("Topic:"):
            current_topic = line[len("Topic:"):].strip()
            topics_and_questions[current_topic] = []
        # Detect a question under the current topic
        elif line.startswith("Question:"):
            if current_topic:
                question = line[len("Question:"):].strip()
                question = question.split('. ', 1)[-1].strip()
                topics_and_questions[current_topic].append(question)

    return topics_and_questions

# --------------- TEXT-TO-SPEECH SECTION ---------------

# Function to convert text to speech using gTTS
def speak_text(text):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("temp.mp3")
    os.system("open temp.mp3" if os.name == "posix" else "start temp.mp3")

# --------------- VOICE RECOGNITION SECTION ---------------

# Function to listen to the user's answer and recognize it
def listen_to_answer():
    try:
        # Display "Start Speaking" message
        speaking_label.config(text="Start Speaking")
        root.update()  # Update the GUI to show the message

        with sr.Microphone() as source:
            print("Listening to your answer...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            # Record audio for a fixed duration (e.g., 40 seconds)
            audio_data = recognizer.record(source, duration=40)

            print("Recognizing your answer...")
            # Convert the recorded audio to text using Google Speech Recognition
            answer_text = recognizer.recognize_google(audio_data)
            print("You said:", answer_text)
            
            # Clear the "Start Speaking" message after recording
            speaking_label.config(text="")
            return answer_text
    except sr.UnknownValueError:
        print("Sorry, I could not understand your answer.")
        speaking_label.config(text="")  # Clear the message if an error occurs
        return "Could not understand the answer."
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        speaking_label.config(text="")  # Clear the message if an error occurs
        return f"Error: {e}"

# --------------- COUNTDOWN TIMER SECTION ---------------

# Function to start a countdown timer for user response
def start_countdown(duration):
    def countdown():
        nonlocal duration
        if duration > 0:
            minutes, seconds = divmod(duration, 60)
            timer_label.config(text=f"Time left: {minutes:02d}:{seconds:02d}")
            duration -= 1
            # Schedule the next countdown update after 1000 milliseconds (1 second)
            root.after(1000, countdown)
        else:
            timer_label.config(text="Time's up!")
            next_question_button.config(state=tk.NORMAL)  # Enable the "Next Question" button
    
    countdown()

# --------------- EVALUATION SECTION ---------------

# Function to evaluate the user's answer using Google Generative AI
def evaluate_answer(answer_text):
    try:
        # Create a prompt for Generative AI to rate the answer
        prompt = f"""Rate this IELTS speaking answer: {answer_text}, assume that this is from my speaking, so if there is anything that you feel weird, it is because I pronounced that wrong. 
        Give me band score at the beginning please. Basically, I want you to give me: Band score - Short feedback on 4 criterias- 2 sentences each only.!"""
        response = model.generate_content(prompt)
        return response.text if response else "No feedback received."
    except Exception as e:
        print(f"Error evaluating answer: {e}")
        return None

# --------------- QUESTION HANDLING SECTION ---------------

# Function to move to the next topic
def next_topic():
    global topic_index, questions_index, topics_asked
    if topics_asked < 3 and topic_index < len(topics):
        topic = topics[topic_index]
        topic_label.config(text=f"Topic: {topic}")
        questions = topics_and_questions[topic]
        random.shuffle(questions)
        questions_index = 0

        # Enable the "Next Question" button to start the first question
        next_question_button.config(state=tk.NORMAL)
    else:
        messagebox.showinfo("End", "Thank you for using the IELTS Speaking Assistant!")
        root.quit()

def next_question():
    global topic_index, questions_index, topics_asked

    # Disable the "Next Question" button while processing the current question
    next_question_button.config(state=tk.DISABLED)

    topic = topics[topic_index]
    questions = topics_and_questions[topic]

    if questions_index < min(3, len(questions)):
        question = questions[questions_index]
        question_label.config(text=f"Question {questions_index + 1}: {question}")
        speak_text(question)  # Speak the question
        questions_index += 1
        time.sleep(5)
        start_countdown(45)  # Start 45-second countdown for the answer


        # Start a new thread for listening to the user's answer
        threading.Thread(target=process_answer).start()
    else:
        topics_asked += 1
        topic_index += 1
        next_topic()

def process_answer():
    answer_text = listen_to_answer()  # Capture the user's answer
    answer_label.config(text=f"Your answer: {answer_text}")

    # Evaluate the user's answer
    rating = evaluate_answer(answer_text)
    if rating:
        answer_label.config(text=f"Your answer: {answer_text}\nEvaluation: {rating}")
    else:
        answer_label.config(text=f"Your answer: {answer_text}\nEvaluation: Could not get feedback.")

    # Enable the "Next Question" button after evaluation
    next_question_button.config(state=tk.NORMAL)

# --------------- FUNCTION TO START THE ASSISTANT ---------------

def start_assistant():
    start_button.pack_forget()
    welcome_message = "Hello, Welcome to the IELTS Speaking Assistant. I will be your virtual Examiner today. Now, let's start with part 1."
    speak_text(welcome_message)
    root.after(7000, next_topic)

# --------------- GUI SETUP SECTION ---------------

# Initialize the main window
root = tk.Tk()
root.title("IELTS Speaking Assistant")

frame = tk.Frame(root)
frame.pack(pady=20)

# Load and display the logo
logo_path = "IELTS-logo.png"
original_logo = Image.open(logo_path).convert("RGBA")
resized_logo = original_logo.resize((220, 100), Image.Resampling.LANCZOS)
logo_image = ImageTk.PhotoImage(resized_logo)

logo_label = tk.Label(frame, image=logo_image)
logo_label.pack(pady=10)

title_label = tk.Label(frame, text="IELTS Speaking Assistant", font=("Helvetica", 18))
title_label.pack(pady=10)

topic_label = tk.Label(frame, text="", font=("Helvetica", 14), wraplength=500)
topic_label.pack(pady=5)

question_label = tk.Label(frame, text="", font=("Helvetica", 12), wraplength=500)
question_label.pack(pady=5)

# Label to display the user's answer
answer_label = tk.Label(frame, text="", font=("Helvetica", 12), wraplength=500, fg="blue")
answer_label.pack(pady=5)

# Label to display the countdown timer
timer_label = tk.Label(frame, text="", font=("Helvetica", 12), fg="red")
timer_label.pack(pady=5)

# Label to display "Start Speaking" message when recording
speaking_label = tk.Label(frame, text="", font=("Helvetica", 12), fg="green")
speaking_label.pack(pady=5)

# Start button
start_button = tk.Button(frame, text="Start", font=("Helvetica", 14), command=start_assistant)
start_button.pack(pady=20)

# "Next Question" button
next_question_button = tk.Button(frame, text="Next Question", font=("Helvetica", 14), command=next_question)
next_question_button.pack(pady=20)
next_question_button.config(state=tk.DISABLED)

# --------------- MAIN PROGRAM SECTION ---------------

# Read topics and questions from the file
file_path = "IELTS_Speaking_Formatted_Final.txt"
topics_and_questions = read_topics_and_questions(file_path)

# Prepare list of topics and shuffle them
topics = list(topics_and_questions.keys())
random.shuffle(topics)

# Initialize indices
topic_index = 0
questions_index = 0
topics_asked = 0

# Start the main GUI loop
root.mainloop()
