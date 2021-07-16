from bs4 import BeautifulSoup
import requests
import time
import random


# START AT PAGE 1 - goes up to page 136. 48 results per page
pgn = 1

title_list = []
price_list = []

while pgn < 6:
    # load page number into url, get page data, load into beautifulsoup
    url = f"https://www.ebay.co.uk/b/Video-Games/139973/bn_450842?rt=nc&LH_Sold=1&mag=1&_sop=13&pgn={str(pgn)}"
    connection = requests.get(url)
    print(connection)
    ingredients = connection.text
    soup = BeautifulSoup(ingredients,"html.parser")
    # populate lists from the html tags
    title_list += [title.text for title in soup.find_all(name="h3", class_="s-item__title s-item__title--has-tags")]
    price_list += [price.text for price in soup.find_all(name="span", class_="s-item__price")]
    # iterate through pages, add delay
    pgn += 1
    time.sleep(random.randint(180,320)/100)
    
print(title_list)
print(price_list)
print(len(title_list))
print(len(price_list))