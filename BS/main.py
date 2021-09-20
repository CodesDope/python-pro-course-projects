from values import text
from bs4 import BeautifulSoup


soup = BeautifulSoup(text, "html.parser")

print(soup.prettify())

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.a)
print(soup.find_all("a"))
print(soup.find_all("p"))
print(soup.get_text())

tag_with_id_third = soup.find(id="third")

print(tag_with_id_third)
print(tag_with_id_third.attrs)
print(soup.find_all("li", class_="li_cls"))
print(soup.select("#third"))
print(soup.select_one(".li_cls"))
