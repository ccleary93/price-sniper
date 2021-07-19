from bs4 import BeautifulSoup
import requests
import time
import random


# START AT PAGE 2 for url to work properly - goes up to page 136. 48 results per page
pgn = 2

title_list = []
price_list = []

while pgn < 6:
    # load page number into url, get page data, load into beautifulsoup
    url = f"https://www.ebay.co.uk/b/Video-Games/139973/bn_450842?LH_Sold=1&mag=1&rt=nc&_pgn={pgn}&_sop=13"
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

# console list for matching description to console
consoles = ["PS4", "PLAYSTATION 4", "XBOX ONE", "PLAYSTATION 3","PS3","XBOX 360","PLAYSTATION 2","PS2","GAMECUBE"]

# create list of dicts with description, console, price for loading into database
# this is also the first check; if the description cannot be matched to a console, the item is skipped
load_data = []
error_count = 0
for i in range(0,len(title_list)):
        for console in consoles:
            if title_list[i].find(console) > 0:
                load_dict.append({"title":title_list[i],
                                "console":console,
                                "price":price_list[i]})
                break
            else:
                pass
print(load_dict)

from title_matcher import TitleMatcher

title_matcher = TitleMatcher()

title_matcher.print_ps4()
