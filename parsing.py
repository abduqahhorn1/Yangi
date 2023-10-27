import requests
import bs4

URL = "https://olcha.uz/ru/category/telefony-gadzhety-aksessuary/telefony?page=2"

response = requests.get(URL)
soup = bs4.BeautifulSoup(response.text , "lxml")

all_names = soup.find_all('div' , class_ = "subtitle-item")
all_price = soup.find_all('div' , class_ = "currency product-card")
all_image = soup.find_all('div' , class_ = "currency product-card-old-price regular")

i = 0
for p in all_names:
    print(p.text)
    print(all_price[i].text)
    print(all_image[i].find('img')['src'])
    print()
    i += 1
# print(response.text)