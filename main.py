from bs4 import BeautifulSoup
import requests
import time
import random
import sqlite3



# START AT PAGE 2 - goes up to page 136. 48 results per page
pgn = 2

title_list = []
price_list = []
id_list = []
postage_list = []

from id_indexer import ID_Indexer
id_indexer = ID_Indexer
end_index = id_indexer().load_last_id()
continue_scrape = True

while pgn < 5 and continue_scrape:
    url = f"https://www.ebay.co.uk/b/Video-Games/139973/bn_450842?LH_Sold=1&mag=1&rt=nc&_pgn={pgn}&_sop=13"
    connection = requests.get(url)
    print(connection)
    ingredients = connection.text
    soup = BeautifulSoup(ingredients,"html.parser")
    title_list += [title.text for title in soup.find_all(name="h3", class_="s-item__title s-item__title--has-tags")]
    price_list += [price.text for price in soup.find_all(name="span", class_="s-item__price")]
    postage_list += [str(0) if postage.text == "Free postage" else postage.text.split(sep="£")[1].split(sep=" ")[0] for postage in soup.find_all(name="span", class_="s-item__shipping s-item__logisticsCost")]
    id_list += [url["href"].split(sep="itm/")[1].split(sep="?")[0] for url in soup.find_all(name="a", class_="s-item__link")]
        if end_index in id_list:
        title_list = title_list[0:id_list.index(end_index)]
        price_list = price_list[0:id_list.index(end_index)]
        postage_list = postage_list[0:id_list.index(end_index)]
        id_list = id_list[0:id_list.index(end_index)]
        continue_scrape = False
    # job lots can have eg £5.50 to £15.00 in this field - job lots should be ignored
    pgn += 1
    time.sleep(random.randint(180,320)/100)

print(title_list)
print(price_list)
print(len(title_list))
print(len(price_list))
print(id_list)
print(len(id_list))
print(postage_list)
print(len(postage_list))

if len(title_list) != len(price_list) or len(title_list) != len(postage_list) or len(title_list) != len(id_list):
    print("lists do not match")
    exit()

consoles = {"PLAYSTATION 2":"PS2",
            "PS2":"PS2",
            "PLAYSTATION 3":"PS3",
            "PS3":"PS3",
            "PS4":"PS4",
            "PLAYSTATION 4":"PS4",
            "XBOX ONE":"XBOX ONE",
            "XBOX 360":"XBOX 360",
            "GAMECUBE":"GAMECUBE"}

load_dict = []
error_count = 0
for i in range(0,len(title_list)):
        for console in consoles.keys():
            if title_list[i].lower().find(console.lower()) >= 0 and id_list[i] not in unique_id_check:
                load_dict.append({"description":title_list[i],
                                "console":consoles[console],
                                "price":price_list[i],
                                "postage":postage_list[i],
                                "ebay_id":id_list[i],
                                "title":""})
                break
            else:
                pass
print(load_dict)
#load_dict = [{'description': 'Need for Speed Rivals (Xbox One), Very Good Xbox One,xbox_one Video Games', 'console': 'XBOX ONE', 'price': '£6.09', 'title': ''}, {'description': 'Ps4 Overwatch Origins Edition ', 'console': 'PS4', 'price': '£10.50', 'title': ''}, {'description': 'Mad Max - PlyStation Hits (Sony PlayStation 4, 2020)', 'console': 'PLAYSTATION 4', 'price': '£5.99', 'title': ''}, {'description': 'Super Monkey Ball 2 (GameCube, 2002)', 'console': 'GAMECUBE', 'price': '£13.50', 'title': ''}, {'description': "Eternal Darkness: Sanity's Requiem (Nintendo GameCube, 2002)", 'console': 'GAMECUBE', 'price': '£20.00', 'title': ''}, {'description': 'Star Wars: Battlefront (PS4)', 'console': 'PS4', 'price': '£3.00', 'title': ''}, {'description': 'Shenmue III (PS4, 2019) with Collectable Sleeve', 'console': 'PS4', 'price': '£10.20', 'title': ''}, {'description': 'saints row 1,2,3 xbox 360', 'console': 'XBOX 360', 'price': '£4.50', 'title': ''}, {'description': 'Forza Horizon 4  (Xbox One)', 'console': 'XBOX ONE', 'price': '£23.99', 'title': ''}, {'description': 'Xbox 360 Game - Band Hero', 'console': 'XBOX 360', 'price': '£2.49', 'title': ''}, {'description': 'Steep (PS4)', 'console': 'PS4', 'price': '£6.50', 'title': ''}, {'description': 'Dying Light (PlayStation 4) Survival Horror PEGI 18 Excellent Condition', 'console': 'PLAYSTATION 4', 'price': '£8.67', 'title': ''}, {'description': 'PS3 Mafia 2 II - PlayStation 3 - including manual & map', 'console': 'PLAYSTATION 3', 'price': '£4.94', 'title': ''}, {'description': 'Splinter Cell Trilogy Classics HD + Blacklist - PlayStation 3 PS3 Games', 'console': 'PLAYSTATION 3', 'price': '£29.95', 'title': ''}, {'description': 'Doom (PS4, 2016)', 'console': 'PS4', 'price': '£3.21', 'title': ''}, {'description': 'Farming Simulator 17 (Microsoft Xbox One, 2016) Xbox One. 1', 'console': 'XBOX ONE', 'price': '£8.50', 'title': ''}, {'description': 'Batman Arkham City PENGUIN STEELBOOK edition ps3 Inc Slipcover ', 'console': 'PS3', 'price': '£5.99', 'title': ''}, {'description': 'Kingdom Hearts III       PS4 Game  ', 'console': 'PS4', 'price': '£4.99', 'title': ''}, {'description': 'Battlefield 1 (Sony PlayStation 4, 2016)', 'console': 'PLAYSTATION 4', 'price': '£2.00', 'title': ''}, {'description': 'The Legend of Zelda: The Wind Waker (Nintendo GameCube, 2003)', 'console': 'GAMECUBE', 'price': '£23.00', 'title': ''}, {'description': 'The Legend of Zelda: The Wind Waker (Nintendo GameCube, 2003)', 'console': 'GAMECUBE', 'price': '£23.00', 'title': ''}, {'description': 'Call Of Duty Modern Warfare 2 Xbox 360 - Tested Good Condition', 'console': 'XBOX 360', 'price': '£2.99', 'title': ''}, {'description': 'Uncharted The Lost Legacy PlayStation Hits Sony Playstation 4 PS4 Game', 'console': 'PS4', 'price': '£5.70', 'title': ''}, {'description': 'ps4 the crew', 'console': 'PS4', 'price': '£3.20', 'title': ''}, {'description': 'Beijing 2008 Olympic Games (PS3) - USED *VGC* ', 'console': 'PS3', 'price': '£7.97', 'title': ''}, {'description': 'Destiny 2 Xbox One Game Pegi 16 Includes Redemption Code', 'console': 'XBOX ONE', 'price': '£2.85', 'title': ''}, {'description': 'Red Dead Redemption 2 Xbox One, Map Included.', 'console': 'XBOX ONE', 'price': '£14.99', 'title': ''}, {'description': 'ps4 minecraft game', 'console': 'PS4', 'price': '£16.15', 'title': ''}, {'description': 'Hitman 2 (PS4, 2018)', 'console': 'PS4', 'price': '£11.29', 'title': ''}, {'description': 'Death Stranding (PS4, 2019)', 'console': 'PS4', 'price': '£14.50', 'title': ''}, {'description': 'Sports Champions 2 (PS3), Very Good PlayStation 3, Playstation 3 Video Games', 'console': 'PLAYSTATION 3', 'price': '£7.50', 'title': ''}, {'description': 'Portal Runner (Sony Playstation 2, 2001)', 'console': 'PLAYSTATION 2', 'price': '£1.20', 'title': ''}, {'description': 'ps4 need for speed rivals', 'console': 'PS4', 'price': '£5.50', 'title': ''}, {'description': 'PLAYSTATION 4 GAMES BUNDLE', 'console': 'PLAYSTATION 4', 'price': '£12.99', 'title': ''}, {'description': '9 x Xbox 360 Games Untested Job Lot Including Skyrim, Fallout, CoD Etc', 'console': 'XBOX 360', 'price': '£4.20', 'title': ''}, {'description': 'Turok (Xbox 360), Good Xbox 360, Xbox 360 Video Games', 'console': 'XBOX 360', 'price': '£3.77', 'title': ''}, {'description': 'Sony Uncharted: The Lost Legacy [PS4], , Used; Good Game', 'console': 'PS4', 'price': '£7.04', 'title': ''}, {'description': 'Rayman Revolution ps2', 'console': 'PS2', 'price': '£4.90', 'title': ''}, {'description': 'Destroy All Humans (PS4, 2020)', 'console': 'PS4', 'price': '£11.50', 'title': ''}, {'description': "The Legend of Zelda - Collector's Edition (GameCube, 2003)", 'console': 'GAMECUBE', 'price': '£36.55', 'title': ''}]

# test data below - comment out the while loop above and use this dict for testing to reduce calls to ebay
# load_dict = [{'description': 'Cyberpunk 2077 (XBOX One, 2020)', 'console': 'XBOX ONE', 'price': '£19.99', 'postage': '0', 'ebay_id': '393475235030', 'title': ''}, {'description': 'EA Sport Fight Night Round 3 Sony Playstation 2 PS2 COMPLETE PAL', 'console': 'PS2', 'price': '£2.99', 'postage': '0', 'ebay_id': '124809545712', 'title': ''}, {'description': 'Lego Dimensions Xbox One Game Only.', 'console': 'XBOX ONE', 'price': '£14.00', 'postage': '0', 'ebay_id': '403045227178', 'title': ''}, {'description': 'Little Nightmares Xbox One Download Game (UK)', 'console': 'XBOX ONE', 'price': '£5.99', 'postage': '0', 'ebay_id': '133835552818', 'title': ''}, {'description': 'Toy Story 3: The Video Game (Sony PlayStation 3, 2010)', 'console': 'PS3', 'price': '£9.99', 'postage': '0', 'ebay_id': '363498035229', 'title': ''}, {'description': 'Metal Gear Solid V The Phantom Pain PS4 Playstation 4 **FREE UK POSTAGE**', 'console': 'PS4', 'price': '£5.95', 'postage': '0', 'ebay_id': '164783205761', 'title': ''}, {'description': 'TRIALS RISING GOLD EDITION PS4 BRAND NEW/SEALED', 'console': 'PS4', 'price': '£8.89', 'postage': '0', 'ebay_id': '234077538980', 'title': ''}, {'description': 'Yakuza 3 PlayStation 3 (PS3) PAL - VGC - No Music CD', 'console': 'PS3', 'price': '£7.99', 'postage': '0', 'ebay_id': '144136615549', 'title': ''}, {'description': 'Tekken 6 Microsoft Xbox 360', 'console': 'XBOX 360', 'price': '£5.29', 'postage': '0', 'ebay_id': '255047684848', 'title': ''}, {'description': 'Robotech Battlecry For Nintendo GameCube NTSC USA Import', 'console': 'GAMECUBE', 'price': '£19.00', 'postage': '2.69', 'ebay_id': '255075043372', 'title': ''}, {'description': 'Condemned Xbox 360 UK PAL **PLAYABLE ON XBOX ONE**', 'console': 'XBOX ONE', 'price': '£9.99', 'postage': '0', 'ebay_id': '294315667853', 'title': ''}, {'description': 'PROJECT CARS 3 - XBOX ONE / SERIES S + X', 'console': 'XBOX ONE', 'price': '£8.00', 'postage': '2.00', 'ebay_id': '334101103819', 'title': ''}, {'description': 'The LEGO Movie Videogame - Microsoft Xbox One Game - Complete With Instructions', 'console': 'XBOX ONE', 'price': '£6.95', 'postage': '0', 'ebay_id': '384320012775', 'title': ''}, {'description': 'The Escapists The Walking Dead (Xbox One), Very Good Xbox One, xbox_one Video Ga', 'console': 'XBOX ONE', 'price': '£4.60', 'postage': '0', 'ebay_id': '363494161939', 'title': ''}, {'description': 'Killzone 2 Limited Collector’s Edition Steelbook PS3 Game', 'console': 'PS3', 'price': '£10.99', 'postage': '0', 'ebay_id': '373560439056', 'title': ''}, {'description': 'Playstation 4 games joblot', 'console': 'PS4', 'price': '£25.00', 'postage': '3.20', 'ebay_id': '224565683154', 'title': ''}, {'description': 'Dragon Ball FighterZ (Xbox One Game) Brand New & Sealed. Rapid & Free Delivery!', 'console': 'XBOX ONE', 'price': '£14.68', 'postage': '0', 'ebay_id': '294292269369', 'title': ''}, {'description': 'Trials Fusion (PS4)', 'console': 'PS4', 'price': '£5.99', 'postage': '0', 'ebay_id': '284395151932', 'title': ''}, {'description': 'Tekken 4 - Platinum (PS2), Good Playstation 2 Video Games', 'console': 'PS2', 'price': '£0.99', 'postage': '1.83', 'ebay_id': '144136324208', 'title': ''}, {'description': 'Fallout 4 (Microsoft Xbox One: Windows, 2015) - New', 'console': 'XBOX ONE', 'price': '£0.99', 'postage': '0.96', 'ebay_id': '165007616170', 'title': ''}, {'description': 'YS IX : MONSTRUM NOX PACT EDITION - PS4 - NEW & SEALED', 'console': 'PS4', 'price': '£39.99', 'postage': '2.25', 'ebay_id': '284398650756', 'title': ''}, {'description': 'Frostpunk Console Signature Edition PS4 New Blister', 'console': 'PS4', 'price': '£46.96', 'postage': '3.50', 'ebay_id': '255021848267', 'title': ''}, {'description': 'Guitar Hero World Tour + Wireless guitar inc Dongle - Playstation 2 PS2 [SW4]', 'console': 'PS2', 'price': '£49.99', 'postage': '0', 'ebay_id': '284303265997', 'title': ''}]

print("load_dict_len:  " + str(len(load_dict)))

from title_matcher import TitleMatcher
from data_cleanser import DataCleanser

title_matcher = TitleMatcher()

data_cleanser = DataCleanser()

db = sqlite3.connect("sale-database.db")
cursor = db.cursor()

database_schema = {
    "PS4":"ps4",
    "PS3":"ps3",
    "PS2":"ps2",
    "XBOX ONE":"xbox_one",
    "XBOX 360":"xbox_360",
    "GAMECUBE":"gamecube"
}

cursor.execute(f'''INSERT INTO
                'first_item_index'(ebay_id)
                VALUES('{id_list[0]}')''')
db.commit

for console in consoles.keys():
    for game in [game for game in load_dict if game["console"] == console]:
        game["description"] = data_cleanser.remove_punctuation(game["description"])
        if title_matcher.check_match(game):
            cursor.execute(f'''INSERT INTO 
            '{database_schema[game['console']]}'(title,description,price,postage,total_price,ebay_id)
            VALUES('{game['title']}','{game['description']}',{game['price']},{game['postage']},{game['price']+float(game['postage'])},{game['ebay_id']})''')
            db.commit()
        else:
            pass
