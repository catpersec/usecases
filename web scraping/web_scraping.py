from bs4 import BeautifulSoup
import requests
import pprint

def retrieve_data():
    items = []
    for website_iteration in range(31):
        response = requests.get(f"https://news.ycombinator.com/news?p={website_iteration + 1}")
        yc_webpage = response.text
        soup = BeautifulSoup(yc_webpage, "html.parser")

        athing = soup.find_all(name='a', class_='titlelink')
        points = soup.find_all(name='td', class_='subtext')

        titles = []
        links = []
        upvotes = []

        for _ in athing:
            titles.append(_.getText())
            links.append(_.get("href"))

        for _ in points:
            try:
                upvotes.append(_.find(name='span', class_='score').getText())
            except:
                upvotes.append("0 points")

        for i in range(len(titles)):
            # new_dict = {}
            temp_el = {
                "article_number": i + 30 * website_iteration,
                "title": titles[i],
                "link": links[i],
                "upvotes": int(upvotes[i].split(" ")[0])
            }
            # new_dict[f"{i + 30 * website_iteration}"] = temp_el
            items.append(temp_el)

    return items


raw_data = retrieve_data()
sorted_data = sorted(raw_data, key=lambda x: x.get('upvotes'), reverse=True)

pprint.pprint(sorted_data)
