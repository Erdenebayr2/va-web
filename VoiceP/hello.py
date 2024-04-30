import requests
from bs4 import BeautifulSoup

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
    return zurhai[0], ordnud


def tester():
    a = input('chat ')
    if 'tester' in a:
        x = ords()
        print(x)
tester()