import win32com.client
import os
import speech_recognition as sr
speaker = win32com.client.Dispatch("SAPI.SpVoice")
import  webbrowser
import openai
from config import apikey
import datetime
import random

chatStr=''

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"chitra: {query}\n Jarvis: "
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "prompt": chatStr,
                    }
                ]
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    speaker.Speak(response["choices"][0]['text'])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]['text']


def ai(prompt):
    openai.api_key = apikey
    text =f"OpenAI response for Prompt: {prompt} \n ***************\n\n"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "prompt": prompt
                    }
                ]
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]['text'])
    text += response["choices"][0]['text']

    if not os.path.exists("Openai"):
        os.mkdir("Openai")


    #with open(f"Openai/prompt- {random.randint(1,44444)}","w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt ","w") as f:
        f.write(text)


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold= 1
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query=r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred, sorry from jarvis"

if __name__ == '__main__':
    print("Jarvis AI")
    s = "Hello Im Jarvis AI"
    speaker.Speak(s)
    while True:
        print("Listening.....")
        query=takeCommand()
        sites=[["google","https://www.google.com"],["youtube","https://www.youtube.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f'Opening {site[0]} sir...')
                webbrowser.open(site[1])
        '''
        if "open music" in query:
            musicPath=""
            import subprocess, sys
            opener="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, musicPath])
            
        elif "open music" in query:
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
            os.system(f"open {musicPath}")    
            
        elif "the time" in query:
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            import subprocess, sys

            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, strfTime])
            
        elif "the time" in query:
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            os.system(f" sir time is {strfTime}")
        
        el if "the time" in query:
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")    
            
            '''

        if "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        else:
            chat(query)
        #speaker.Speak(query)
#  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

