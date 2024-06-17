import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import openAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "d093053d72bc40248998159804e0e67d"
def speak(text) : 
    engine.say(text)
    engine.runAndWait()
    
def aiProcess(command) :
    client = openAI() (
    api_key = "sk-proj-GzuB6ELwYvYCZwiSn9X0T3BlbkFJghVYEixnRYvRq0TrRyXs"
)
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a Virtual assistant named jarvis, skilled in general tasks like Alexa and Google Mini"},
        {"role": "user", "content": command}
    ]
    )
    return completion.choices[0].message.content
    
    
def processCommand(c) :
    # print(c)
    if "open google" in c.lower() :
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower() :
        webbrowser.open("https://www.facebook.com")
    elif "open youTube" in c.lower() :
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower() :
        webbrowser.open("https://www.linkedin.com")
    elif c.lower().startswith("play") :
        songs = c.lower().split(" ")[1]
        link = musiclibrary.music[songs]
        webbrowser.open(link)
    elif "news" in c.lower() :
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articales = data.get('articales', [])
            for artical in articales :
                speak(artical['title'])
                
    else :
        #let open ai handle the request
        output = aiProcess(c)
        speak(output)
        pass
        
   
      
if __name__ == "__main__" :
    speak("Initializing Jarvis...")
    
    while True:
        # Listen for the wake word "Jarvis"
        # Obtain audio from the microphone
        
        r = sr.Recognizer()
        print("recognizing...")
        try:
            # print("Sphinx thinks you said "+r.recognize_sphinx(audio))
            with sr.Microphone() as source:
                print("Listening...!")
                audio = r.listen(source,timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis") :
                speak("Ya")
                #Listen for a Command
                with sr.Microphone() as source:
                    print("Jarvis Active...!")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
                
        
        except sr.UnknownValueError:
            print("Sphinx could not understood audio")
            
        except Exception as e :
            print("Error; {0}".format(e))