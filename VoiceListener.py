
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import threading
class _TTS:

    engine = None
    rate = None
    def __init__(self):
        self.engine = pyttsx3.init()


    def start(self,text_):
        self.engine.say(text_)
        self.engine.runAndWait()

flag = 'False'
 

opts = {
    "alias": ('гецка','лецка','бецка','пецка','Игарь','игорь','элисс','элис','эл','элыс','элиса','элиска',
              ),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси'),
    "cmds": {
        "ctime": ('текущее время','сейчас времени','который час'),
        "stupid1": ('расскажи анекдот','рассмеши меня','ты знаешь анекдоты'),
        "trigger_Name": ('о себе насте','о себе анастасии')
    }
}
 



def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()
    

    
    

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Распознано: " + voice)
   
        if voice.startswith(opts['alias']):
            # обращаются к Элисс
            cmd = voice
 
            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()
           
            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()
           
            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])
 
    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
        
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")
   
 
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
   
    return RC
 
def execute_cmd(cmd):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
        
    elif cmd == 'stupid1':
         #рассказать анекдот
         speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")
    
    elif cmd == 'trigger_Name':
        speak("Привет Настя я Элис, самый простой и примитивный голосовой ассистен, Вячеслав создал меня, я еще совсем проста, но ты сегодня очень красива")
        
    else:
        print('Команда не распознана, повторите!')
        
# Runner 
r= sr.Recognizer()
m = sr.Microphone(device_index=0)

with m as source:
    r.adjust_for_ambient_noise(source)

    speak_engine = pyttsx3.init()
    
    speak("Добрый день создатель")
    speak("Игорь к вашим услугам")
stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)