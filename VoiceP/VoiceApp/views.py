from django.shortcuts import render
from datetime import datetime
import requests, datetime, os
from bs4 import BeautifulSoup
import speech_recognition as sr
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
import webbrowser
import pyautogui
import time

def synthesize(text):
    url = "https://api.chimege.com/v1.2/synthesize"
    headers = {
        'Content-Type': 'plain/text',
        'Token': '1d02fae212b76b8c77f9558e94f710fa226e0d7884601e91d4b7ecf3a9c3dc5e',
    }
    r = requests.post(
        url, data=text.encode('utf-8'), headers=headers)
    with open("output.wav", 'wb') as out:
        out.write(r.content)

def ords(x):
    url = "https://gogo.mn/horoscope/western/today"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(x)
    ord = x
    zurhai = soup.find("div", {"id": f"zodiac-switcher-mobile-{ord}"}).text.split("\n")
    zurhai = [element for element in zurhai if element != '']
    ordnud = soup.find_all("div", class_=f"zodiac-body-{ord}")[1].text.split("\n")
    ordnud = [element for element in ordnud if element != '']
    ordnud = [line.strip() for line in ordnud if line.strip()]
    return zurhai[0], ord[0]

def weather():
    url = "https://ikon.mn/wetter"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    agaar = soup.find("div", class_="wfc").text.split("\n")
    agaar = [element for element in agaar if element != '']
    agaar = [line.strip() for line in agaar if line.strip()]
    agaar.insert(1,'Шөнө')
    agaar.insert(4,'Өдөр')
    agaar.insert(6,'Салхи')
    agaar.remove('|')
    return agaar

def index(request):
    # time.sleep(5)
    # x = 'Сайн байна уу. Би бол Хоолойн туслах. би таны өдөр тутмын үйл ажиллагаанд туслах болно.'
    # synthesize(x)
    # play(AudioSegment.from_file('output.wav'))
    return render(request, 'index.html')

def talk(request):
    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%A")
    context = {}
    if request.method == 'POST':
        listener = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print('listening..')
                voice = listener.listen(source)
                command = listener.recognize_google(voice,language='MN')
                context['data'] = command
                if 'сайн уу' in command:
                    x = 'сайн таньд юугаар туслах уу?'
                    synthesize(x)
                    play(AudioSegment.from_file('output.wav'))
                elif 'өнөөдөр' in command:
                    days = {'Monday':'Даваа','Tuesday':'Мягмар','Wednesday':'Пүрэв','Thursday':'Пүрэв','Friday':'Баасан','Saturday':'Бямба','Sunday':'Ням'}
                    quest = f'Өнөөдөр {days[formatted_date]} гараг'
                    print(quest)
                    synthesize(quest)
                    play(AudioSegment.from_file('output.wav'))
                elif 'Чи юу хийж чадах вэ' in command:
                    x = 'Би_таньд_цаг_агаар_хэлэх, зурхай_хэлэх,_цаг_хэлэх_гэх_мэт_зүйлсийг_хийж_чадна.'
                    synthesize(x)
                    play(AudioSegment.from_file('output.wav'))
                elif 'фэйсбүүк' in command:
                    url = 'https://www.facebook.com'
                    webbrowser.open_new(url)
                    x = 'фэйсбүүк нээгдлээ'
                    synthesize(x)
                    play(AudioSegment.from_file('output.wav'))

                elif 'цонхыг хаа' in command:
                    time.sleep(2)
                    x = 'Цонхыг хааж байна'
                    synthesize(x)
                    play(AudioSegment.from_file('output.wav'))
                    pyautogui.hotkey('ctrl', 'w')

                elif 'цаг агаар' in command:
                    x = weather()
                    # weather_text = ' '.join(x)
                    # print(weather_text)
                    x = x[-1]
                    print(x)
                    synthesize(x)
                    play(AudioSegment.from_file('output.wav'))

                elif 'зурхай' in command:
                    x = 'ямар орд вэ'
                    synthesize(x)
                    play(AudioSegment.from_file('output.wav'))
                    listener = sr.Recognizer()
                    try:
                        with sr.Microphone() as source:
                            print('listening..')
                            voice = listener.listen(source)
                            commands = listener.recognize_google(voice,language='MN')
                            if 'мэлхий' in commands:
                                x = 'melhii'
                                print(ords(x))
                                synthesize(ords(x))
                                play(AudioSegment.from_file('output.wav'))
                    except:
                        pass
                elif 'унтраа' in command:
                    time.sleep(3)
                    x = 'Компьютерийг унтрааж байна'
                    synthesize(x)
                    play(AudioSegment.from_file('output.wav'))
                    pyautogui.hotkey('alt', 'f4')

                else:
                    x = 'Уучлаарай та асуултаа давтана уу'
                    synthesize(x)
                    play(AudioSegment.from_file('output.wav'))

        except:
            pass
    return render(request, 'voice.html',context=context)

def write(request):
    context = {}
    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%A")
    if request.method=='POST':
        chat = request.POST.get('chat')
        if 'Өнөөдөр' in chat:
            days = {'Monday':'Даваа','Tuesday':'Мягмар','Wednesday':'Пүрэв','Thursday':'Пүрэв','Friday':'Баасан','Saturday':'Бямба','Sunday':'Ням'}
            context['chat'] = f'Өнөөдөр - {days[formatted_date]} - гараг.'
        elif 'Чи юу хийж чадах вэ' in chat:
            x = 'Би_таньд_цаг_агаар_хэлэх,_өдрийн_тэмдэглэл_хөтлөх,_зурхай_хэлэх,_цаг_хэлэх_зэргийг_хийж_чадна.'
            context['chat'] = x

        elif 'зурхай' in chat:
            context['chat'] = ords()

        elif 'цаг агаар' in chat:
            context['chat'] = weather()
        else:
            pass
    return render(request, 'chat.html',context=context)