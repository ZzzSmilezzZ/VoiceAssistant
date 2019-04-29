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
            elif ("google chrome" in statement) or ("Google chrome" in statement) or ("Google Chrome" in statement):
                os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
            elif ("firefox" in statement) or ("mozilla" in statement) or ("mozilla firefox" in statement) or ("firefox mozilla" in statement):
                os.startfile(r"C:\Program Files\Mozilla Firefox\firefox.exe")
        elif "close" in statement:
            if "browser" in statement:
                os.system("TASKKILL /IM chrome.exe")
        elif "find" in statement:
            if "in google" in statement:
                webbrowser.open_new_tab("https://www.google.com/search?q=" + statement[statement.find("find") + 5:statement.find("in google") - 1:1])
            elif ("in youtube" in statement) or ("on youtube" in statement):
                webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + statement[statement.find("find") + 5:statement.find("youtube") - 4:1])


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