import speech_recognition as sr
import webbrowser
import sys
import os
import winsound



# def jarvis_say(phrase):
#     print(phrase)

# def set_noise_mask():
#     jarvis_say("Generating noise mask...")
#     with microphone as source:
#         recognizer.adjust_for_ambient_noise(source)
#     print("Complete")
microphone = sr.Microphone()
recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.3
recognizer.non_speaking_duration = 0.2
recognizer.dynamic_energy_adjustment_ratio = 0.2



def execute(statement):
        if "open" in statement:
            if "google" in statement:
                webbrowser.open_new('https://www.google.ru')
            elif "youtube" in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
            elif "translator" in statement:
                webbrowser.open_new("https://translate.google.ru/?hl=ru")
            elif "manager" in statement:
                os.system('taskmgr')
            elif "overwatch" in statement:
                os.startfile(r"C:\Program Files (x86)\Overwatch\Overwatch Launcher.exe")
            elif "browser" in statement:
                os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        elif "close" in statement:
            if "browser" in statement:
                os.system("TASKKILL /IM chrome.exe")

        if ("shutdown" in statement) or ("shut down" in statement):
            sys.exit("closed")

def listening():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Starting listening...")
        winsound.MessageBeep(-1)
        try:
            audio = recognizer.listen(source)
            statement = recognizer.recognize_google(audio)
            statement = statement.lower()
            print("You said: ", statement)
            execute(statement)
        except Exception:
            None

# try:
#     while True:
#         listening()
# except sr.UnknownValueError:
#     print("Google cloud doesn't work :(")