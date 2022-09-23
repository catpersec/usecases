import requests
from bs4 import BeautifulSoup
import pprint
import os

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

athing = soup.find_all(name='h3', class_='title')
items = []

for single_movie in athing:
    x = single_movie.getText().split(sep=") ")
    # print(x)
    if len(x) > 1:
        temp_dict = {
            "place": int((x[0]).strip()),
            "title": x[1]
        }
        items.append(temp_dict)

# pprint.pprint(items)
sorted_data = sorted(items, key=lambda x: x.get('place'), reverse=False)

os.remove("file.txt")
for _ in sorted_data:
    with open('file.txt', 'a', encoding="utf8") as f:
        f.write(f"{_['place']}. {_['title']}\n")