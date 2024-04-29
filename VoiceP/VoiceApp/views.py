from django.shortcuts import render
<<<<<<< Updated upstream
from datetime import datetime
import requests
from playsound import playsound
=======
import requests, datetime

>>>>>>> Stashed changes

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


def index(request):
<<<<<<< Updated upstream
    answer = ''
    value = ''
    if request.method == 'POST':
        value = request.POST.get('text')
        if value == 'сайн уу':
            answer = 'сайн байна уу'
            synthesize(answer)
            playsound('output.wav')

    context = {
        'questions':value,
        'answer': answer
    }
    return render(request, 'index.html', context=context)
=======
    context = {}
    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%A")
    if request.method=='POST':
        chat = request.POST.get('chat')
        if 'Өнөөдөр' in chat:
            context['chat'] = f'Өнөөдөр {formatted_date} гараг.'
        if 'Чи юу хийж чадах вэ' in chat:
            context['chat'] = 'Би таньд цаг агаар хэлэх, өдрийн тэмдэглэл хөтлөх, зурхай хэлэх, цаг хэлэх зэргийг хийж чадна.'

        else:
            pass

    return render(request, 'index.html',context=context)
>>>>>>> Stashed changes
