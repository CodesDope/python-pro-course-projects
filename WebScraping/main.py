from bs4 import BeautifulSoup
import requests

try:
    response = requests.get(
        "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    )
    # print(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    for h3 in soup.find_all("h3")[:10]:
        print(h3.a.string)
except Exception as e:
    print("Some error")
    print(e)
