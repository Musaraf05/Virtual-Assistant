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
from googletrans import Translator
from gtts import gTTS
import playsound

dictionary = PyDictionary()

translator = Translator()

# Add a global variable for language selection
selected_language = "english"  # Default to English


# Set up logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize pyttsx3 engine globally
engine = pyttsx3.init()
voices = engine.getProperty('voices')

for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} - {voice.languages} - {voice.id}")

engine.setProperty('voice', voices[108].id)
# Set speaking rate (optional)
engine.setProperty('rate', 200)  # Adjust rate as needed
engine.setProperty('volume', 1.0)

tamil_jokes = [
    "மாதம் 30 நாட்கள் தான், ஆனா பள்ளி செல்லும் நாட்கள் மட்டும் 300 நாளா இருக்கும்!",
    "கணக்கு ஆசிரியர் எப்போதும் தன்னம்பிக்கையாக இருப்பார், ஏனென்றால் அவர் எப்போதும் தீர்வுகளை கொண்டிருப்பார்!",
    "வாத்தியார்: உன் வீட்டில் யார் யார் இருக்காங்க? மாணவன்: நான், அப்பா, அம்மா, YouTube, Netflix!",
    "என் நண்பன் Examக்கு முன்னாடி மட்டும்தான் படிப்பான். அதனால் அவனுக்கு Exam FEVER!",
    "நண்பன்: என்ன da இன்னிக்கு அடிக்கிற கோழி எப்படி? \nநானா: அது Gym போன கோழியாம். \nநண்பன்: ஏன் da அப்படி சொல்ற? \nநானா: அதுக்கு சோறு தான் நிறைய இருக்கு, mutta ஏதும் இல்ல!",
    "மனைவி: நீ எப்போ மேனேஜர் ஆக போற? \nகணவர்: நான் தான் மனைவி, பசங்க, வீடு, EMI எல்லாத்தையும் மேனேஜ் பண்றேன், அத விட என்ன மேனேஜர் வேணும்?",
    "மாணவன்: ஐயா, நான் கேட்ட கேள்விக்கு மட்டும் பதில் சொல்லுங்க \nஆசிரியர்: அதுக்கு மேல நீ ஏதாவது கேட்டியா?",
    "நண்பன்: என்ன da! Exam paper புடிச்சு உசிரோடயே குலுக்குற? \nநானா: டூப்பு answer எல்லாம் காற்றில ஏறி விடாம பார்க்கணும்!",
    "வாத்தியார்: நீ 10 ரூபாய்ல என்ன எல்லாம் வாங்குவாய்? \nமாணவன்: ஒரு குட்டி சிப்ஸ் பேக், ஒரு சர்பட், ஒரு பேனா! \nவாத்தியார்: டேய், யார் கிட்ட வாங்குவே? \nமாணவன்: என் அப்பா கிட்ட!",
    "அம்மா: டீங்க, இன்று வெளிய போகணும் \nஅப்பா: ஏன்? \nஅம்மா: வீட்டில் கல்யாணம் நடக்குது! \nஅப்பா: நம்ம வீட்லயா? \nஅம்மா: ஆமாம், என் தோழிக்கு!",
    "நண்பன்: Bro, நீ Mobile Bill எப்படி சம்பாதிக்குற? \nநானா: நீ மொபைல் போச்சொல்லாதே, அது 'சம்பாதிக்குற'தா இல்ல, 'தீர்த்து விடுற'தா சொல்லு!",
    "கணவன்: ஏங்க, என்ன பொண்ணுங்க அல்ட்ரா மெகா HD Clear பார்ப்பாங்க? \nமனைவி: ஏன்? \nகணவன்: அந்த Glasses எடுத்து TV Remote எடுத்துட்டாங்க!",
    "வாத்தியார்: நீ ஏன் Late வந்தே? \nமாணவன்: Sir, ஒரு Bike மேல 3 பேரு புறப்பட்டோம், ஆனால் Police சொன்னாங்க, 'தெரியுமா, இவ்ளோ பேரு ஒன்னா போக கூடாது' \nஅதனால ஒரு நிமிஷம் Police station போயிட்டு வந்தேன்!",
    "நண்பன்: Bro, நான் ஒரு புதிய App லaunch பண்ணியிருக்கேன் \nநானா: என்ன app? \nநண்பன்: நீ போட்ட Joke, நா கேட்ட புன்னகை!",
]

def setLanguage():
    global selected_language
    speak("Which language would you like to use? Say 'English' or 'Tamil'.")
    language_choice = takeCommand()  # Capture user input
    
    if language_choice in ["english", "இங்கிலீஷ்"]:
        selected_language = "english"
        speak("Language changed to English.")
    elif language_choice in ["tamil", "தமிழ்"]:
        selected_language = "tamil"
        speak("மொழி தமிழ் ஆக மாற்றப்பட்டது.")
    else:
        speak("Sorry, I didn't understand. Please say 'English' or 'Tamil'.")

# Speak function
def speak(audio):
    if selected_language == "tamil":
        # Convert English text to Tamil using Google Text-to-Speech
        tts = gTTS(text=audio, lang='ta')
        tts.save("temp.mp3")
        playsound.playsound("temp.mp3")
    else:
        if engine._inLoop:
            engine.endLoop()
        engine.say(audio)
        engine.runAndWait()

# Wishing function
def wishMe():
    setLanguage()  # Ask for language first
    hour = int(datetime.datetime.now().hour)
    if selected_language == "tamil":
        if 0 <= hour < 12:
            speak("காலை வணக்கம்!")  # "Good Morning!"
        elif 12 <= hour < 18:
            speak("மதிய வணக்கம்!")  # "Good Afternoon!"
        else:
            speak("மாலை வணக்கம்!")  # "Good Evening!"
        speak("நான் உங்கள் ROSTA, உங்களுக்கு எப்படி உதவலாம்?")  # "I am your ROSTA, how can I help you?"
    else:
        if 0 <= hour < 12:
            speak("Good Morning!")
        elif 12 <= hour < 18:
            speak("Good Afternoon!")
        else:
            speak("Good Evening!")
        speak("I am your ROSTA, How may I help you!")

def tamil_meaning(word):
    translator = Translator()
    try:
        translated = translator.translate(word, src='ta', dest='en')
        meaning_in_english = dictionary.meaning(translated.text)
        if meaning_in_english:
            first_part_of_speech = next(iter(meaning_in_english))
            first_definition = meaning_in_english[first_part_of_speech][0] 
            # Now translating the meaning back to Tamil
            meaning_in_tamil = translator.translate(first_definition, src='en', dest='ta')
            one_sentence_meaning = f"{word} என்பதின் அர்த்தம்: {meaning_in_tamil.text}."
            speak(one_sentence_meaning)
            print(one_sentence_meaning)
        else:
            speak("மன்னிக்கவும், இந்த வார்த்தைக்கு அர்த்தம் கிடைக்கவில்லை.")
    except Exception as e:
        speak("மன்னிக்கவும், அர்த்தம் பெறுவதில் சிக்கல் உள்ளது.")
        print(f"பிழை: {e}")

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
    day = ["முதல்", "இரண்டாவது", "மூன்றாவது"] if selected_language == "tamil" else ["first", "second", "third"]  
    for ar in articles:
            head.append(ar["title"]) 
    for i in range(min(3, len(head))):  # Ensure we don't go out of range
            if selected_language == "tamil":
                print(f"இன்றைய {day[i]} செய்தி: {head[i]}")
                speak(f"இன்றைய {day[i]} செய்தி: {head[i]}")
            else:
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
    if selected_language == "tamil":
        speak("நீங்கள் எந்த மொழியை தொகுக்க விரும்புகிறீர்கள்?")
    else:
        speak("Which language would you like to compile?")

    language = takeCommand()  # Capture user input
    
    # Dictionary for mapping Tamil inputs to English URLs
    compiler_urls = {
        'python': 'https://www.programiz.com/python-programming/online-compiler/',
        'java': 'https://www.programiz.com/java-programming/online-compiler/',
        'c plus plus': 'https://www.programiz.com/cpp-programming/online-compiler/',
        'c': 'https://www.programiz.com/c-programming/online-compiler/',
        'html': 'https://www.programiz.com/html/online-compiler/',
        'css': 'https://www.programiz.com/html/online-compiler/',
        'r': 'https://www.programiz.com/r/online-compiler/',
        'javascript': 'https://www.programiz.com/javascript/online-compiler/',
        # Tamil mappings
        'பைத்தான்': 'https://www.programiz.com/python-programming/online-compiler/',
        'ஜாவா': 'https://www.programiz.com/java-programming/online-compiler/',
        'சி பிளஸ் பிளஸ்': 'https://www.programiz.com/cpp-programming/online-compiler/',
        'சி': 'https://www.programiz.com/c-programming/online-compiler/',
        'எச்.டி.எம்.எல்': 'https://www.programiz.com/html/online-compiler/',
        'சி.எஸ்.எஸ்': 'https://www.programiz.com/html/online-compiler/',
        'ஆர்': 'https://www.programiz.com/r/online-compiler/',
        'ஜாவாஸ்கிரிப்ட்': 'https://www.programiz.com/javascript/online-compiler/'
    }

    # Find the matching compiler URL
    if language in compiler_urls:
        if selected_language == "tamil":
            speak(f"{language} தொகுப்பியைத் திறக்கிறேன்.")
        else:
            speak(f"Opening {language} compiler for you.")
        
        webbrowser.open(compiler_urls[language])
    else:
        if selected_language == "tamil":
            speak("மன்னிக்கவும், அந்த மொழிக்கான தொகுப்பி இல்லை.")
        else:
            speak("Sorry, I don't have a compiler for that language.")


def takeCommand(retry_attempts=3):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("கேட்கிறேன்..." if selected_language == "tamil" else "Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    # Try multiple attempts for better recognition
    for attempt in range(retry_attempts):
        try:
            print("அறிந்துகொள்கிறேன்..." if selected_language == "tamil" else "Recognizing...")
            language_code = 'ta-IN' if selected_language == "tamil" else 'en-IN'
            query = r.recognize_google(audio, language=language_code)
            print(f"பயனர் கூறியது: {query}\n" if selected_language == "tamil" else f"User said: {query}\n")
            return query.lower()
        except sr.UnknownValueError:
            # Handle cases where recognition failed but we can retry
            if attempt < retry_attempts - 1:
                if selected_language == "tamil":
                    speak("எனக்கு புரியவில்லை, தயவுசெய்து மீண்டும் கூறவும்.")  
                else:
                    speak("I did not catch that, please repeat.")
                return takeCommand(retry_attempts - 1)
            else:
                if selected_language == "tamil":
                      speak("மன்னிக்கவும், நான் கேட்கவில்லை. தயவுசெய்து மீண்டும் கூறவும்.")
                else:
                    speak("Sorry, I did not catch that. Could you repeat, please?")
                return None
        except sr.RequestError as e:
            if selected_language == "tamil":
                      speak("மன்னிக்கவும், என் பேச்சு அங்கீகார சேவை தற்பொழுது கிடைக்கவில்லை.")
            else:
                    speak("Sorry, my speech recognition service is currently unavailable.")
            return None

# Command handler
def executeCommand(command):
    if selected_language == "tamil":
        if 'wikipedia' in command or'விக்கிபீடியா' in command:
              speak("விக்கிபீடியாவில் தேடுகிறது...")
              query = command.replace("wikipedia", "").replace('விக்கிபீடியா', '')
              results = wikipedia.summary(query, sentences=2)
              translated_text = translator.translate(results, src='en', dest='ta').text
              speak(f"விக்கிபீடியா கூறுகிறது: {translated_text}")

        elif 'open youtube' in command or'யூடியூப் திற' in command or 'யூடியூப் திறவும்' in command:
            print("எதை YouTubeல் தேட வேண்டும்?")
            speak("எதை YouTubeல் தேட வேண்டும்?")
            command = takeCommand()
            if command:  # Ensure the command is not None
                speak("தேடப்படுகிறது..." + command)
                webbrowser.open("https://www.youtube.com/results?search_query=" + command)
            else:
                speak("நான் கேட்கவில்லை. தயவுசெய்து மீண்டும் முயற்சிக்கவும்.")

        elif 'open google' in command or 'கூகுள் திற' in command or 'google திறவும்' in command or 'கூகுள் ஓபன்' in command:
            print("Googleல் என்ன தேட வேண்டும்?")
            speak("Googleல் என்ன தேட வேண்டும்?")
            command = takeCommand()
            if command:  # Ensure the command is not None
                speak("தேடப்படுகிறது..." + command)
                webbrowser.open("https://www.google.com/search?q=" + command)
            else:
                speak("நான் கேட்கவில்லை. தயவுசெய்து மீண்டும் முயற்சிக்கவும்.")

        elif 'play' in command or 'பாடல் வாசி' in command or 'பாடல் பாடு' in command:
            song = command.replace('play', '').replace('பாடல் வாசி', '').replace('பாடல் ஓட', '').strip()
            speak(song + " பாடலை YouTube இல் இயங்கவைக்கிறேன்")
            pywhatkit.playonyt(song)
            # webbrowser.open("https://www.youtube.com/results?search_query=" + song)

        elif 'search' in command or 'தேடு' in command:
            search = command.replace('search', '').replace('தேடு', '').strip()
            speak(search + " குறித்து கூகுளில் தேடுகிறேன்")
            pywhatkit.search(search)
            # webbrowser.open("https://www.google.com/search?q=" + search)

        elif 'change language' in command or 'மொழியை மாற்று' in command:
            setLanguage()


        elif 'open calendar' in command or 'தினசரி' in command or 'கேலண்டர்' in command:
            speak("உங்கள் காலண்டரை திறக்கிறேன்...")
            webbrowser.open("https://calendar.google.com/")

        elif 'the time' in command or 'நேரம்' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"தற்போதைய நேரம் {strTime}")

        elif 'read pdf' in command or 'பிடிஎஃப் வாசி' in command:
            speak("பிடிஎஃப் கோப்பை வாசிக்கிறேன்...")
            pdf_reader()

        elif 'tell me the news' in command or 'செய்திகளை கூறு' in command:
            speak("தயவுசெய்து காத்திருக்கவும், நான் சமீபத்திய செய்திகளை எடுக்கிறேன்.")
            news()

        elif 'internet speed' in command or 'இணைய வேகம்' in command:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            print(f"சார், நம்மிடம் {dl:.2f} பிட்டுகள்/விநாடிக்கு பதிவிறக்கும் வேகம் மற்றும் {up:.2f} பிட்டுகள்/விநாடிக்கு பதிவேற்றம் வேகம் உள்ளது.")
            speak(f"சார், நம்மிடம் {dl:.2f} பிட்டுகள்/விநாடிக்கு பதிவிறக்கும் வேகம் மற்றும் {up:.2f} பிட்டுகள்/விநாடிக்கு பதிவேற்றம் வேகம் உள்ளது.")
   
        elif 'ஒலிவளர்த்து' in command or 'ஒலியை அதிகரிக்கவும்' in command:  
            print("ஒலியை அதிகரிக்கிறேன்")  
            speak("ஒலியை அதிகரிக்கிறேன்")  
            pyautogui.press("volumeup")  

        elif 'ஒலியைக் குறைக்கவும்' in command:  
            print("ஒலியை குறைக்கிறேன்")  
            speak("ஒலியை குறைக்கிறேன்")  
            pyautogui.press("volumedown")  

        elif 'ஒலியை முடக்கு' in command:  
            print("ஒலியை முடக்குகிறேன்")  
            speak("ஒலியை முடக்குகிறேன்")  
            pyautogui.press("volumemute")  

        elif 'ஸ்கிரீன் ஷாட் எடு' in command:
            print("தயவுசெய்து ஸ்கிரீன் ஷாட் கோப்பிற்கான பெயரை சொல்லுங்கள்")
            speak("தயவுசெய்து ஸ்கிரீன் ஷாட் கோப்பிற்கான பெயரை சொல்லுங்கள்")
            name = takeCommand()
            if name:
                name = name.lower()
                print("தயவுசெய்து திரையை சில விநாடிகள் நிலையாக வைத்திருங்கள், நான் ஸ்கிரீன் ஷாட் எடுக்கிறேன்")
                speak("தயவுசெய்து திரையை சில விநாடிகள் நிலையாக வைத்திருங்கள், நான் ஸ்கிரீன் ஷாட் எடுக்கிறேன்")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                print("நான் முடித்துவிட்டேன், ஸ்கிரீன் ஷாட் முக்கியமான கோப்பகத்தில் சேமிக்கப்பட்டுள்ளது")
                speak("நான் முடித்துவிட்டேன், ஸ்கிரீன் ஷாட் முக்கியமான கோப்பகத்தில் சேமிக்கப்பட்டுள்ளது")
            else:
                speak("மன்னிக்கவும், ஸ்கிரீன் ஷாட் பெயரைப் பிடிக்க முடியவில்லை. தயவுசெய்து மீண்டும் முயற்சி செய்யுங்கள்.")

        elif 'செய்தி அனுப்பு' in command:
            speak("என்ன செய்தியை அனுப்ப வேண்டும்?")
            message_text = takeCommand()  # செய்தியை பெறுதல்
            if message_text:
                current_time = datetime.datetime.now()
                hour = current_time.hour
                minute = current_time.minute + 1  
                if minute >= 60:
                    minute = 0
                    hour += 1
                    if hour >= 24:
                        hour = 0  # நேரத்தை மீட்டமைக்கவும்
                try:
                    speak("செய்தியை அனுப்புகிறேன்...")
                    pywhatkit.sendwhatmsg("+916382462598", message_text, hour, minute, 8)
                    speak(f"செய்தி அனுப்பப்பட்டது: {message_text}")
                    time.sleep(4)  
                    pyautogui.press('enter')  
                except Exception as e:
                    speak("மன்னிக்கவும், செய்தி அனுப்புவதில் சிக்கல் ஏற்பட்டுள்ளது.")
                    print(f"பிழை ஏற்பட்டுள்ளது: {e}")
            else:
                speak("மன்னிக்கவும், செய்தியைப் புரிந்துகொள்ள முடியவில்லை. தயவுசெய்து மீண்டும் முயற்சி செய்யுங்கள்.")

        elif 'மின்னஞ்சல் அனுப்பு' in command:   
            get_email_info()

        elif 'உங்களை யார் உருவாக்கினார்கள்' in command:
            print("நான் பல புத்திசாலி மனதுகள் ஒன்றாக இணைந்து உருவாக்கிய உதவியாளர்.")
            speak("நான் பல புத்திசாலி மனதுகள் ஒன்றாக இணைந்து உருவாக்கிய உதவியாளர்.")

        elif 'நீங்கள் எங்கு வாழ்கிறீர்கள்' in command:
            print("பான் கடையைக் கடந்து, ஒரு பெரிய ஆலமரம் வரை சென்று வலதுபுறம் திரும்புங்கள். நான் மேகத்தில் வசிக்கிறேன்.")
            speak("பான் கடையைக் கடந்து, ஒரு பெரிய ஆலமரம் வரை சென்று வலதுபுறம் திரும்புங்கள். நான் மேகத்தில் வசிக்கிறேன்.")

        elif 'நீங்கள் என்ன செய்ய முடியும்' in command:
            print("நான் பல செயல்களை செய்ய முடியும். நீங்கள் 'பாடல் ஒளிக்க', 'வாட்ஸ்அப் திற' அல்லது 'இன்றைய செய்திகள் சொல்' என்று சொல்லலாம்.")
            speak("நான் பல செயல்களை செய்ய முடியும். நீங்கள் 'பாடல் ஒளிக்க', 'வாட்ஸ்அப் திற' அல்லது 'இன்றைய செய்திகள் சொல்' என்று சொல்லலாம்.")

        elif 'வணக்கம்' in command:
            print("வணக்கம்!")
            speak("வணக்கம்!")

        elif 'நீங்கள் எப்படி இருக்கிறீர்கள்' in command:
            print("நான் முழுமையாக சக்தியுடன் இருக்கிறேன்!")
            speak("நான் முழுமையாக சக்தியுடன் இருக்கிறேன்!")

        elif 'கட்டளை கொடுக்கப்பட்டிருக்கும்' in command:
            speak('திறக்கப்படுகிறது...')
            os.system('start cmd')

        elif 'ட்விட்டர் திற' in command:
            speak("திறக்கப்படுகிறது...")
            webbrowser.open("www.twitter.com")

        elif 'இன்ஸ்டாகிராம் திற' in command:
            speak("திறக்கப்படுகிறது...")
            webbrowser.open("www.instagram.com")

        elif 'வாட்ஸ்அப் திற' in command:
            speak("திறக்கப்படுகிறது...")
            webbrowser.open('https://web.whatsapp.com/')

        elif 'பேஸ்புக் திற' in command:
            speak("திறக்கப்படுகிறது...")
            webbrowser.open("www.facebook.com")

        elif 'ஜிமெயில் திற' in command:
            speak("திறக்கப்படுகிறது...")
            webbrowser.open("www.gmail.com")

        elif 'மீட் திற' in command:
            speak("திறக்கப்படுகிறது...")
            webbrowser.open("https://meet.google.com/?pli=1")

        elif 'கிளாஸ்ரூம் திற' in command:
            speak("திறக்கப்படுகிறது...")
            webbrowser.open("www.classroom.google.com")

        elif 'open online compiler' in command or 'ஆன்லைன் கணிபொறி திற' in command:
            open_online_compiler()

        elif 'jokes' in command or 'joke' in command or 'நகைச்சுவை சொல்' in command or 'நகைச்சுவை' in command:
            joke = random.choice(tamil_jokes)
            speak(joke)
            print(joke)

        elif 'கேமரா திற' in command or 'கேமரா ஓபன்' in command or 'open camera' in command:
            speak('கேமரா திறக்கப்படுகிறது...')
            cap = cv2.VideoCapture(0)
            img_counter = 0  # படம் பெயரிடுவதற்கான எண்ணிக்கை
            while True:
                ret, img = cap.read()
                cv2.imshow('கேமரா', img)
                # விசைகள் சரிபார்க்கப்படுகிறது
                key = cv2.waitKey(1) & 0xFF
                # இடைவேளையில் ஸ்பேஸ் பார் அழுத்தியால் படம் பிடிக்கலாம்
                if key == ord(' '):  # 'Space bar' அழுத்தி படம் எடுக்கலாம்
                    img_counter += 1
                    img_name = f"படம்{img_counter}.png"  # தனித்துவமான பெயர்
                    cv2.imwrite(img_name, img)
                    speak(f"படம் பிடிக்கப்பட்டது, {img_name} என சேமிக்கப்பட்டது")
                    print(f"படம் பிடிக்கப்பட்டது, {img_name} என சேமிக்கப்பட்டது")
                # 'q' அழுத்தினால் வெளியேறலாம்
                if key == ord('q'):  # 'q' அழுத்தி வெளியில் செல்லலாம்
                    break
                # விண்டோ மூடப்பட்டதா என்பதை சரிபார்க்கவும்
                if cv2.getWindowProperty('கேமரா', cv2.WND_PROP_VISIBLE) < 1:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif 'artham ena' in command or 'அர்த்தம் என்ன' in command:
            word = command.replace('artham ena', '').replace('அர்த்தம் என்ன', '').strip()
            if word:
                tamil_meaning(word)
            else:
                speak("தயவுசெய்து வார்த்தையை சொல்லவும்.")



        elif 'ip முகவரி' in command or 'ip address' in command:
            try:
                ip = get('https://api.ipify.org').text
                print(f"உங்கள் IP முகவரி: {ip}")
                speak(f"உங்கள் IP முகவரி {ip}")
            except Exception as e:
                print("மன்னிக்கவும், IP முகவரியை பெற முடியவில்லை.")
                speak("மன்னிக்கவும், IP முகவரியை பெற முடியவில்லை.")

        elif 'என்னுடைய இருப்பிடம்' in command:
            print("ஒரு நிமிடம், உங்கள் இருப்பிடத்தை சரிபார்க்கிறேன்...")
            speak("ஒரு நிமிடம், உங்கள் இருப்பிடத்தை சரிபார்க்கிறேன்...")
            
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                url = f'https://get.geojs.io/v1/ip/geo/{ipAdd}.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                
                city = geo_data.get('city', 'தகவல் இல்லை')
                country = geo_data.get('country', 'தகவல் இல்லை')
                
                print(f"நான் உறுதியாக சொல்ல முடியாது, ஆனால் நாம் {city} நகரம், {country} நாட்டில் இருக்கலாம்.")
                speak(f"நான் உறுதியாக சொல்ல முடியாது, ஆனால் நாம் {city} நகரம், {country} நாட்டில் இருக்கலாம்.")
            
            except Exception as e:
                print("மன்னிக்கவும், இணைய பிரச்சனையால் உங்கள் இருப்பிடத்தை கண்டுபிடிக்க முடியவில்லை.")
                speak("மன்னிக்கவும், இணைய பிரச்சனையால் உங்கள் இருப்பிடத்தை கண்டுபிடிக்க முடியவில்லை.")


        elif 'open virtual mouse' in command or 'மெய்நிகர் மவுஸ் திற' in command:
            print('மெய்நிகர் மவுஸ் திறக்கப்படுகிறது...')
            speak('மெய்நிகர் மவுஸ் திறக்கப்படுகிறது...')
            import AiVirtualMouse

        elif 'மெய்நிகர் ஓவியர் திற' in command or 'open virtual painter' in command:
            print('மெய்நிகர் ஓவியர் திறக்கப்படுகிறது...')
            speak('மெய்நிகர் ஓவியர் திறக்கப்படுகிறது...')
            import AiVirtualPainter

        elif 'exit' in command or 'quit' in command or 'bye' in command or 'விடைபெறு' in command:
            speak("வணக்கம்! நல்ல நாளாக இருக்கட்டும்!")
            sys.exit()

        else:
            speak("மன்னிக்கவும், நான் தற்போது அந்த செயல்களை செய்ய முடியாது.")
  

    else:
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

        elif 'time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'read pdf' in command:
            pdf_reader()

        elif 'change language' in command:
            setLanguage()

        elif 'tell me the news' in command or 'tell the news' in command:
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
                
        elif 'take a screenshot' in command or 'screenshot' in command:
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

        elif 'send message' in command:
            speak("Sir, what should I send?")
            message_text = takeCommand()  # Capture the message
            if message_text:
                current_time = datetime.datetime.now()
                hour = current_time.hour
                minute = current_time.minute + 1  
                if minute >= 60:
                    minute = 0
                    hour += 1
                    if hour >= 24:
                        hour = 0  # Reset hour to 0
                try:
                    speak("Sending message...")
                    pywhatkit.sendwhatmsg("+916382462598", message_text, hour, minute,8)
                    speak(f"Message sent: {message_text}")
                    time.sleep(4)  
                    pyautogui.press('enter')  
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