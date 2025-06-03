# python --version
# pip install virtualenv   (optional)
# python -m venv env
# .\env\Scripts\activate   windows
# source env/bin/activate  macos
# pip install opencv-python numpy pyautogui mediapipe pyttsx3 smtplib SpeechRecognition wikipedia webbrowser pywhatkit pyjokes speedtest-cli requests PyQt5 PyDictionary PyPDF2
#pip install -r requirements.txt

import pyttsx3
import smtplib
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import cv2
import pywhatkit
import pyjokes
import speedtest
import requests
from requests import get
import random
import pyautogui
from requests.api import head
from email.message import EmailMessage
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from ASTORGUI import Ui_ASTOR
import logging
import sys
from email import message
import imp
from time import time
from weakref import WeakKeyDictionary
from PyDictionary import PyDictionary
from wikipedia import exceptions
import time 
import PyPDF2
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from email.mime.text import MIMEText

dictionary = PyDictionary()

# Set up logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize pyttsx3 engine globally
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# Set speaking rate (optional)
engine.setProperty('rate', 200)  # Adjust rate as needed
engine.setProperty('volume', 1.0)
# Speak function
def speak(audio):
    if engine._inLoop:
        engine.endLoop()
    engine.say(audio)
    engine.runAndWait()

# Wishing function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your ROSTA, How may I help you!")

# Send email function
def send_email(receiver, subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('mohamedmusaraf05@gmail.com', 'vbzernzsempipteh')  # Enter your credentials here
        email = EmailMessage()
        email['From'] = 'mohamedmusaraf05@gmail.com'
        email['To'] = receiver
        email['Subject'] = subject
        email.set_content(message)
        server.send_message(email)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I couldn't send the email.")

# Email information and sending flow
def get_email_info():
    speak("To whom do you want to send the email?")
    recipient_name = takeCommand()  # Capture recipient name
    if recipient_name:
        # Check the recipient in the email list dictionary
        recipient_name_lower = recipient_name.lower()
        if recipient_name_lower in email_list:
            receiver = email_list[recipient_name_lower]
            speak(f"Email will be sent to {recipient_name_lower}")
            speak("What is the subject of your email?")
            subject = takeCommand()
            speak("Tell me the message you want to send.")
            message = takeCommand()
            if subject and message:
                send_email(receiver, subject, message)
            else:
                speak("Subject or message not recognized. Please try again.")
        else:
            speak("Sorry, I couldn't find that recipient in the email list.")

# Email list dictionary
email_list = {
    'time': 'mohamedmusaraf8055@gmail.com',
    'run': 'a3069024@gmail.com'
}

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=f12d3c8b057a47a89fabaacf6591ca66'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        print(f"Today's {day[i]} news is: {head[i]}")
        speak(f"Today's {day[i]} news is: {head[i]}")

def pdf_reader():
    speak("Please tell me the name of the PDF file.")
    pdf_name = takeCommand()
    if pdf_name:
        # Ensure the file name ends with .pdf
        if not pdf_name.endswith('.pdf'):
            pdf_name += '.pdf'
        try:
            # Open the specified PDF file
            book_path = os.path.join(os.getcwd(), pdf_name)  # Get the file from the current directory
            book = open(book_path, 'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            speak(f"Total number of pages in {pdf_name} is {pages}")
            print(f"Total number of pages in this book {pages} ")
            speak("Please tell me the page number you want to read.")
            try:
                pg = int(takeCommand())
                if pg <= pages:
                    page = pdfReader.getPage(pg)
                    text = page.extract_text()
                    print(text)
                    speak(text)
                else:
                    speak(f"Sorry, the PDF has only {pages} pages.")
            except ValueError:
                speak("Invalid page number provided.")
        except FileNotFoundError:
            speak(f"Sorry, I couldn't find the file {pdf_name}.")
        except Exception as e:
            speak(f"An error occurred: {str(e)}")
            print(f"Error: {str(e)}")
    else:
        speak("Sorry, I didn't catch the file name.")

def open_online_compiler():
    # Prompt user to specify a language
    speak("Which language would you like to compile?")
    language = takeCommand()  # Replace this with your function to capture user input
    # Open compiler based on the selected language
    compilers = {
        'python': 'https://www.programiz.com/python-programming/online-compiler/',
        'java': 'https://www.programiz.com/java-programming/online-compiler/',
        'c plus plus': 'https://www.programiz.com/cpp-programming/online-compiler/',
        'c' : 'www.programiz.com/c-programming/online-compiler',
        'see' : 'www.programiz.com/c-programming/online-compiler',
        'html': 'https://www.programiz.com/html/online-compiler/',
        'css': 'https://www.programiz.com/html/online-compiler/',
        'r' : 'https://www.programiz.com/r/online-compiler/',
        'javascript': 'https://www.programiz.com/javascript/online-compiler'
    }
    if language in compilers:
        speak(f"Opening {language} compiler for you.")
        webbrowser.open(compilers[language])
    else:
        speak("Sorry, I don't have a compiler for that language.")

def takeCommand(retry_attempts=3):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    # Try multiple attempts for better recognition
    for attempt in range(retry_attempts):
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query.lower()
        except sr.UnknownValueError:
            # Handle cases where recognition failed but we can retry
            if attempt < retry_attempts - 1:
                speak("I did not catch that, please repeat.")
                return takeCommand(retry_attempts - 1)
            else:
                speak("Sorry, I did not catch that. Could you repeat, please?")
                return None
        except sr.RequestError as e:
            speak("Sorry, my speech recognition service is currently unavailable.")
            return None

# Command handler
def executeCommand(command):

    if 'wikipedia' in command:
        speak("Searching Wikipedia...")
        query = command.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak(f"According to Wikipedia: {results}")

    elif 'open youtube' in command:
        print("Sir, what should I search on YouTube?")
        speak("Sir, what should I search on YouTube?")
        command = takeCommand()

        if command:  # Ensure the command is not None
            speak("Searching..." + command)
            webbrowser.open("https://www.youtube.com/results?search_query=" + command)
        else:
            speak("I couldn't hear you. Please try again.")

    elif 'open calendar' in command:
        speak("Opening your calendar...")
        webbrowser.open("https://calendar.google.com/")

    elif 'open google' in command:
        print("Sir, what should I search on Google?")
        speak("Sir, what should I search on Google?")
        command = takeCommand()
        if command:  # Ensure the command is not None
            speak("Searching..." + command)
            webbrowser.open("https://www.google.com/search?q=" + command)
        else:
            speak("I couldn't hear you. Please try again.")

    elif 'play'in command:
                song = command.replace('play','')
                speak('playing' + song + 'on youtube')
                pywhatkit.playonyt(song)
                # webbrowser.open("https://www.youtube.com/results?search_query=" + song)

    elif 'search'in command:
                search = command.replace('search','')
                speak('searching' + search + 'on google')
                pywhatkit.search(search)
                # webbrowser.open("https://www.google.com/search?q=" + search)

    elif 'the time' in command:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")

    elif 'read pdf' in command:
        pdf_reader()

    elif 'tell me the news' in command:
                speak("please wait sir , i am fetching the latest news")
                news()

    elif 'internet speed' in command:
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                print(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
                speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

    elif 'increase the volume' in command:
                print("increasing the volume")
                speak("increasing the volume")
                pyautogui.press("volumeup")



    elif 'decrease the volume' in command:
                print("decreasing the volume")
                speak("decreasing the volume")
                pyautogui.press("volumedown")

    elif 'volume mute'in command:
                print("Muting the volume")
                speak("Muting the volume")
                pyautogui.press("volumemute")
            
    elif 'take a screenshot' in command:
                print("sir please tell me the name for this screenshot file")
                speak("sir please tell me the name for this screenshot file")
                name =takeCommand()
                if name:
                    name = name.lower()
                    print("Sir, please hold the screen for a few seconds, I am taking the screenshot")
                    speak("Sir, please hold the screen for a few seconds, I am taking the screenshot")
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(f"{name}.png")
                    print("I am done, the screenshot is saved in our main folder")
                    speak("I am done, the screenshot is saved in our main folder")
                else:
                    speak("Sorry, I couldn't capture the screenshot name. Please try again.")

    # In your executeCommand function, where you're sending a message
    elif 'send message' in command:
        speak("Sir, what should I send?")
        message_text = takeCommand()  # Capture the message
        if message_text:
            current_time = datetime.datetime.now()
            hour = current_time.hour
            minute = current_time.minute + 1  # Set to one minute later
            # Ensure that the minute doesn't exceed 59
            if minute >= 60:
                minute = 0
                hour += 1
                if hour >= 24:
                    hour = 0  # Reset hour to 0
            try:
                speak("Sending message...")
                pywhatkit.sendwhatmsg("+918122798055", message_text, hour, minute,8)
                speak(f"Message sent: {message_text}")
                 # Add a brief wait to ensure the message is sent
                time.sleep(3)  # Wait for 3 seconds after sending
                pyautogui.press('enter')  # Simulate pressing Enter to send the message
                # speak("Message sent successfully!")
            except Exception as e:
                speak("There was an error sending the message.")
                print(f"An error occurred: {e}")
        else:
            speak("Sorry, I couldn't understand the message. Please try again.")

    elif 'send email' in command:   
        get_email_info()  # Call this function directly
    
    elif 'meaning of' in command:
        word = command.replace('meaning of','')
        if word:
            try:
                meaning = dictionary.meaning(word)
                if meaning:
                    # Get the first part of speech and its first definition
                    first_part_of_speech = next(iter(meaning))
                    first_definition = meaning[first_part_of_speech][0]
                    one_sentence_meaning = f"The meaning of {word} is: {first_definition}."
                    speak(one_sentence_meaning)
                    print(one_sentence_meaning)
                else:
                    speak("Sorry, I couldn't find the meaning.")
                    print(f"Sorry, I couldn't find the meaning for '{word}'.")
            except Exception as e:
                speak("There was an error retrieving the meaning.")
                print(f"An error occurred while retrieving the meaning: {e}")

    elif 'who made you' in command:
                print("I was born when many bright minds came together to create an Assistant, just for you")
                speak("I was born when many bright minds came together to create an Assistant, just for you")

    elif 'where do you live' in command:
                print("So, turn left from paanwaala and then go straight till you see a Banyan tree. just kidding ,i live in the cloud")
                speak("So, turn left from paanwaala and then go straight till you see a Banyan tree. just kidding ,i live in the cloud")
            
    elif 'what can you do for me' in command:
                print("Theres a lot, you can try saying thing like play song, open whatsapp or tell todays news")
                speak("Theres a lot, you can try saying thing like play song, open whatsapp or tell todays news")    
            
    elif 'hello' in command:
                print("Namaste!")
                speak("Namaste!") 

    elif 'how are you' in command:
                print("i am feeling all charged up, ready to go!")
                speak("i am feeling all charged up, ready to go!")

    elif 'open command prompt' in command:
                speak('opening...')
                os.system('start cmd')

    elif 'open twitter' in command:
                speak("opening...")
                webbrowser.open("www.twitter.com")

    elif 'open instagram' in command:
                speak("opening...")
                webbrowser.open("www.instagram.com")

    elif 'open whatsapp' in command:
                speak("opening...")
                webbrowser.open('https://web.whatsapp.com/')

    elif 'open facebook' in command:
                speak("opening...")
                webbrowser.open("www.facebook.com")

    elif 'open gmail' in command:
                speak("opening...")
                webbrowser.open("www.gmail.com")

    elif 'open meet' in command:
                speak("opening...")
                webbrowser.open("https://meet.google.com/?pli=1")
            
    elif 'open classroom' in command:
                speak ("opening...")
                webbrowser.open("www.classroom.google.com")

    elif 'open online compiler' in command:
          open_online_compiler()

    elif 'jokes' in command or 'joke' in command:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

    elif 'open camera' in command:
        speak('Opening Camera...')
        cap = cv2.VideoCapture(0)
        img_counter = 0  # Initialize a counter for image names
        while True:
            ret, img = cap.read()
            cv2.imshow('Webcam', img)
            # Check for key presses
            key = cv2.waitKey(1) & 0xFF
            # Capture the image when space bar is pressed
            if key == ord(' '):  # Press space bar to capture image
                img_counter += 1  # Increment the counter
                img_name = f"captured_image{img_counter}.png"  # Create a unique filename
                cv2.imwrite(img_name, img)
                speak(f"Image captured and saved as {img_name}")
                print(f"Image captured and saved as {img_name}")
            # Exit if 'q' is pressed
            if key == ord('q'):  # Press 'q' to exit
                break
            # Check if the window is manually closed
            if cv2.getWindowProperty('Webcam', cv2.WND_PROP_VISIBLE) < 1:
                break
        cap.release()
        cv2.destroyAllWindows()

    elif 'ip address' in command:
                ip = get('https://api.ipify.org').text
                print(f"your IP address is {ip}")
                speak(f"your IP address is {ip}")

    elif 'what is my location' in command:
                print("wait sir, let me check your location")
                speak("wait sir, let me check your location")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    #print(geo_data)
                    city = geo_data['city']
                    #state = geo_data['state']
                    country = geo_data['country']
                    print(f"sir i am not sure, but i think we are in {city} city of {country} country")
                    speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    print("sorry sir, due to network issue i am not able to find your location") 
                    speak("sorry sir, due to network issue i am not able to find your location")
                    pass

    elif 'open virtual mouse' in command:
                print('opening virtual mouse...')
                speak('opening virtual mouse...')
                import AiVirtualMouse

    elif 'open virtual painter' in command:
                print('opening virtual painter...')
                speak('opening virtual painter...')
                import AiVirtualPainter

    elif 'exit' in command or 'quit' in command or 'bye' in command:
        speak("Goodbye!")
        sys.exit()  # Terminate the application
        
    else:
        speak("Sorry, I can't perform that action at the moment.")

# Main Application with GUI integration
class ASTORApp(QMainWindow, Ui_ASTOR):
    def __init__(self):
        super(ASTORApp, self).__init__()
        self.setupUi(self)

        # Connect buttons
        self.RUN.clicked.connect(self.startAssistant)
        self.EXIT.clicked.connect(self.closeApp)

    def startAssistant(self):
         # Adding GIFs like in rosta2.py
        self.movie = QtGui.QMovie("/Users/musaraf/Downloads/ROSTA/GUI gif/RECO.gif")
        self.Background.setMovie(self.movie)
        self.movie.start()

        self.movie = QtGui.QMovie("/Users/musaraf/Downloads/ROSTA/GUI gif/initalising.gif")
        self.initating.setMovie(self.movie)
        self.movie.start()

        self.movie = QtGui.QMovie("/Users/musaraf/Downloads/ROSTA/GUI gif/FACE ID.gif")
        self.Faceid.setMovie(self.movie)
        self.movie.start()

        wishMe()
        while True:
            command = takeCommand()
            if command:
                executeCommand(command)

    def closeApp(self):
        speak("Goodbye!")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ASTORApp()
    window.show()
    sys.exit(app.exec_())