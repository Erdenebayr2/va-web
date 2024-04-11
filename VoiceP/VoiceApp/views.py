from django.shortcuts import render
from datetime import datetime
import requests
from playsound import playsound

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
