from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.amazon.com/Console-Horizon-Forbidden-Bundle-PlayStation-5/dp/B0B16656Z2", headers={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    })
soup = BeautifulSoup(response.text, 'html.parser')
price_raw = soup.find("span", class_="a-offscreen").getText()
price = float(price_raw.strip("$"))
print(price)