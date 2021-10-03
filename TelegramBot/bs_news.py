from bs4 import BeautifulSoup
import requests


def get_news():
    try:
        response = requests.get(
            "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
        )
    except Exception as e:
        print("Some error")
        print(e)

    soup = BeautifulSoup(response.text, "html.parser")
    news = []
    for h3 in soup.find_all("h3")[:10]:
        news.append(h3.a.string)
    return news
