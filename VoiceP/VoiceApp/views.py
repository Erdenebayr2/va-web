from django.shortcuts import render
from datetime import datetime
import requests, datetime
from bs4 import BeautifulSoup

def synthesize(text):
    url = "https://api.chimege.com/v1.2/synthesize"
    headers = {
        'Content-Type': 'plain/text',
        'Token': 'API_TOKEN',
    }
    r = requests.post(
        url, data=text.encode('utf-8'), headers=headers)
    with open("output.wav", 'wb') as out:
        out.write(r.content)
print(synthesize('Сайн байна уу'))

def ords():
    url = "https://gogo.mn/horoscope/western/today"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    ord = input("ymr ord: ")
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
    agaar.insert(1,'Өдөр')
    agaar.insert(4,'Шөнө')
    agaar.insert(6,'Салхи')
    agaar.remove('|')
    return agaar

def index(request):
    context = {}
    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%A")
    if request.method=='POST':
        chat = request.POST.get('chat')
        if 'Өнөөдөр' in chat:
            context['chat'] = f'Өнөөдөр {formatted_date} гараг.'
        elif 'Чи юу хийж чадах вэ' in chat:
            context['chat'] = 'Би таньд цаг агаар хэлэх, өдрийн тэмдэглэл хөтлөх, зурхай хэлэх, цаг хэлэх зэргийг хийж чадна.'

        elif 'зурхай' in chat:
            context['chat'] = ords()

        elif 'цаг агаар' in chat:
            context['chat'] = weather()
        else:
            pass
    return render(request, 'index.html',context=context)
