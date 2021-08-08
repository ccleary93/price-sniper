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

while pgn < 4:
    url = f"https://www.ebay.co.uk/b/Video-Games/139973/bn_450842?LH_Sold=1&mag=1&rt=nc&_pgn={pgn}&_sop=13"
    connection = requests.get(url)
    print(connection)
    ingredients = connection.text
    soup = BeautifulSoup(ingredients,"html.parser")
    title_list += [title.text for title in soup.find_all(name="h3", class_="s-item__title s-item__title--has-tags")]
    price_list += [price.text for price in soup.find_all(name="span", class_="s-item__price")]
    id_list += [url["href"].split(sep="itm/")[1].split(sep="?")[0] for url in soup.find_all(name="a", class_="s-item__link")]
    # data cleansing may be required on prices - job lots can have £5.50 to £15.00 in this field - take the lower number from the HTML
    pgn += 1
    time.sleep(random.randint(180,320)/100)

print(title_list)
print(price_list)
print(len(title_list))
print(len(price_list))
print(id_list)
print(len(id_list))

consoles = ["PS4", "PLAYSTATION 4", "XBOX ONE", "PLAYSTATION 3","PS3","XBOX 360","PLAYSTATION 2","PS2","GAMECUBE"]

load_dict = []
error_count = 0
for i in range(0,len(title_list)):
        for console in consoles:
            if title_list[i].lower().find(console.lower()) >= 0:
                load_dict.append({"description":title_list[i],
                                "console":console,
                                "price":price_list[i],
                                  "title":""})
                break
            else:
                pass
print(load_dict)
#load_dict = [{'description': 'Need for Speed Rivals (Xbox One), Very Good Xbox One,xbox_one Video Games', 'console': 'XBOX ONE', 'price': '£6.09', 'title': ''}, {'description': 'Ps4 Overwatch Origins Edition ', 'console': 'PS4', 'price': '£10.50', 'title': ''}, {'description': 'Mad Max - PlyStation Hits (Sony PlayStation 4, 2020)', 'console': 'PLAYSTATION 4', 'price': '£5.99', 'title': ''}, {'description': 'Super Monkey Ball 2 (GameCube, 2002)', 'console': 'GAMECUBE', 'price': '£13.50', 'title': ''}, {'description': "Eternal Darkness: Sanity's Requiem (Nintendo GameCube, 2002)", 'console': 'GAMECUBE', 'price': '£20.00', 'title': ''}, {'description': 'Star Wars: Battlefront (PS4)', 'console': 'PS4', 'price': '£3.00', 'title': ''}, {'description': 'Shenmue III (PS4, 2019) with Collectable Sleeve', 'console': 'PS4', 'price': '£10.20', 'title': ''}, {'description': 'saints row 1,2,3 xbox 360', 'console': 'XBOX 360', 'price': '£4.50', 'title': ''}, {'description': 'Forza Horizon 4  (Xbox One)', 'console': 'XBOX ONE', 'price': '£23.99', 'title': ''}, {'description': 'Xbox 360 Game - Band Hero', 'console': 'XBOX 360', 'price': '£2.49', 'title': ''}, {'description': 'Steep (PS4)', 'console': 'PS4', 'price': '£6.50', 'title': ''}, {'description': 'Dying Light (PlayStation 4) Survival Horror PEGI 18 Excellent Condition', 'console': 'PLAYSTATION 4', 'price': '£8.67', 'title': ''}, {'description': 'PS3 Mafia 2 II - PlayStation 3 - including manual & map', 'console': 'PLAYSTATION 3', 'price': '£4.94', 'title': ''}, {'description': 'Splinter Cell Trilogy Classics HD + Blacklist - PlayStation 3 PS3 Games', 'console': 'PLAYSTATION 3', 'price': '£29.95', 'title': ''}, {'description': 'Doom (PS4, 2016)', 'console': 'PS4', 'price': '£3.21', 'title': ''}, {'description': 'Farming Simulator 17 (Microsoft Xbox One, 2016) Xbox One. 1', 'console': 'XBOX ONE', 'price': '£8.50', 'title': ''}, {'description': 'Batman Arkham City PENGUIN STEELBOOK edition ps3 Inc Slipcover ', 'console': 'PS3', 'price': '£5.99', 'title': ''}, {'description': 'Kingdom Hearts III       PS4 Game  ', 'console': 'PS4', 'price': '£4.99', 'title': ''}, {'description': 'Battlefield 1 (Sony PlayStation 4, 2016)', 'console': 'PLAYSTATION 4', 'price': '£2.00', 'title': ''}, {'description': 'The Legend of Zelda: The Wind Waker (Nintendo GameCube, 2003)', 'console': 'GAMECUBE', 'price': '£23.00', 'title': ''}, {'description': 'The Legend of Zelda: The Wind Waker (Nintendo GameCube, 2003)', 'console': 'GAMECUBE', 'price': '£23.00', 'title': ''}, {'description': 'Call Of Duty Modern Warfare 2 Xbox 360 - Tested Good Condition', 'console': 'XBOX 360', 'price': '£2.99', 'title': ''}, {'description': 'Uncharted The Lost Legacy PlayStation Hits Sony Playstation 4 PS4 Game', 'console': 'PS4', 'price': '£5.70', 'title': ''}, {'description': 'ps4 the crew', 'console': 'PS4', 'price': '£3.20', 'title': ''}, {'description': 'Beijing 2008 Olympic Games (PS3) - USED *VGC* ', 'console': 'PS3', 'price': '£7.97', 'title': ''}, {'description': 'Destiny 2 Xbox One Game Pegi 16 Includes Redemption Code', 'console': 'XBOX ONE', 'price': '£2.85', 'title': ''}, {'description': 'Red Dead Redemption 2 Xbox One, Map Included.', 'console': 'XBOX ONE', 'price': '£14.99', 'title': ''}, {'description': 'ps4 minecraft game', 'console': 'PS4', 'price': '£16.15', 'title': ''}, {'description': 'Hitman 2 (PS4, 2018)', 'console': 'PS4', 'price': '£11.29', 'title': ''}, {'description': 'Death Stranding (PS4, 2019)', 'console': 'PS4', 'price': '£14.50', 'title': ''}, {'description': 'Sports Champions 2 (PS3), Very Good PlayStation 3, Playstation 3 Video Games', 'console': 'PLAYSTATION 3', 'price': '£7.50', 'title': ''}, {'description': 'Portal Runner (Sony Playstation 2, 2001)', 'console': 'PLAYSTATION 2', 'price': '£1.20', 'title': ''}, {'description': 'ps4 need for speed rivals', 'console': 'PS4', 'price': '£5.50', 'title': ''}, {'description': 'PLAYSTATION 4 GAMES BUNDLE', 'console': 'PLAYSTATION 4', 'price': '£12.99', 'title': ''}, {'description': '9 x Xbox 360 Games Untested Job Lot Including Skyrim, Fallout, CoD Etc', 'console': 'XBOX 360', 'price': '£4.20', 'title': ''}, {'description': 'Turok (Xbox 360), Good Xbox 360, Xbox 360 Video Games', 'console': 'XBOX 360', 'price': '£3.77', 'title': ''}, {'description': 'Sony Uncharted: The Lost Legacy [PS4], , Used; Good Game', 'console': 'PS4', 'price': '£7.04', 'title': ''}, {'description': 'Rayman Revolution ps2', 'console': 'PS2', 'price': '£4.90', 'title': ''}, {'description': 'Destroy All Humans (PS4, 2020)', 'console': 'PS4', 'price': '£11.50', 'title': ''}, {'description': "The Legend of Zelda - Collector's Edition (GameCube, 2003)", 'console': 'GAMECUBE', 'price': '£36.55', 'title': ''}]

# test data below - comment out the while loop above and use this dict for testing to reduce calls to ebay
#load_dict = [{'description': 'Nintendo GameCube mario kart double dash game', 'console': 'GAMECUBE', 'price': '£28.00', 'title': ''}, {'description': 'Resident Evil 2 Xbox One', 'console': 'XBOX ONE', 'price': '£5.50', 'title': ''}, {'description': 'Playstation 3 - MINECRAFT PLAYSTATION EDITION - Game Complete PAL VGC PS3', 'console': 'PLAYSTATION 3', 'price': '£12.99', 'title': ''}, {'description': 'Final Fantasy XV Day One Edition Sony Playstation 4 PS4 PAL VV042', 'console': 'PS4', 'price': '£4.99', 'title': ''}, {'description': 'Predator Hunting Grounds PS4 Brand New Sealed', 'console': 'PS4', 'price': '£15.59', 'title': ''}, {'description': 'Fight Night Champion xbox 360', 'console': 'XBOX 360', 'price': '£8.00', 'title': ''}, {'description': 'Worms W.M.D. All-Stars (Playstation 4 PS4) Great Condition', 'console': 'PS4', 'price': '£7.95', 'title': ''}, {'description': 'Mortal kombat 11 ps4 steelbook', 'console': 'PS4', 'price': '£11.50', 'title': ''}, {'description': 'Call of Duty: World at War - Xbox 360 / Xbox One Game ', 'console': 'XBOX ONE', 'price': '£3.99', 'title': ''}, {'description': 'Wolfenstein 2 The New Collossus PS4 (Playstation 4)', 'console': 'PS4', 'price': '£5.50', 'title': ''}, {'description': 'Jumanji: The Video Game (PS4, 2019)', 'console': 'PS4', 'price': '£10.00', 'title': ''}, {'description': 'The amazing spiderman 2 xbox one Rare', 'console': 'XBOX ONE', 'price': '£40.00', 'title': ''}, {'description': 'FIFA 17 (PS4) - USED *VGC* ', 'console': 'PS4', 'price': '£2.44', 'title': ''}, {'description': 'Call Of Duty Black Ops 4/IIII ~ Xbox One (Immaculate Condition)', 'console': 'XBOX ONE', 'price': '£7.45', 'title': ''}, {'description': 'Anthem - Microsoft Xbox One', 'console': 'XBOX ONE', 'price': '£2.50', 'title': ''}, {'description': "Deus Ex: Human Revolution: Director's Cut (Xbox 360) .. Never Played. ", 'console': 'XBOX 360', 'price': '£13.00', 'title': ''}, {'description': 'Fifa 21 100k Coins Ps4/5 - Fast delivery!', 'console': 'PS4', 'price': '£5.50', 'title': ''}, {'description': 'Cobra Kai: PlayStation 4, PS4. Unwanted gift. Played once, literally brand new.', 'console': 'PS4', 'price': '£16.00', 'title': ''}, {'description': 'Sonic Generations - Sony PS3', 'console': 'PS3', 'price': '£8.99', 'title': ''}, {'description': 'Cloudy With a Chance of Meatballs PS3 (Sony PlayStation 3, 2009)', 'console': 'PLAYSTATION 3', 'price': '£7.00', 'title': ''}, {'description': 'Nintendo GameCube welcome to animal crossing game', 'console': 'GAMECUBE', 'price': '£38.00', 'title': ''}, {'description': 'Plants vs Zombies: Garden Warfare 2 (PS4)', 'console': 'PS4', 'price': '£8.95', 'title': ''}, {'description': 'Tomb Raider: Underworld  (PS3) - Game Complete Mint ', 'console': 'PS3', 'price': '£3.50', 'title': ''}, {'description': 'LARA CROFT TOMB RAIDER THE ANGEL OF DARKNESS PLAYSTATION 2 game PS2 with manual ', 'console': 'PLAYSTATION 2', 'price': '£5.01', 'title': ''}, {'description': 'cyberpunk 2077 ps4 game', 'console': 'PS4', 'price': '£20.00', 'title': ''}, {'description': 'PS2 Tomb Raider Anniversary Pre Enjoyed', 'console': 'PS2', 'price': '£4.75', 'title': ''}, {'description': 'Showdown: Legends Of Wrestling - Sony Ps2 Game -Playstation 2 -Complete -UK PAL ', 'console': 'PLAYSTATION 2', 'price': '£9.89', 'title': ''}, {'description': 'Call of Duty: Ghosts (Sony PlayStation 3, 2013)', 'console': 'PLAYSTATION 3', 'price': '£0.99', 'title': ''}, {'description': 'Dead By Daylight ~ Xbox One (Great Condition) - Disc Only', 'console': 'XBOX ONE', 'price': '£14.95', 'title': ''}, {'description': 'Burnout Paradise Remastered - Xbox One | TheGameWorld', 'console': 'XBOX ONE', 'price': '£8.50', 'title': ''}, {'description': 'forza motorsport 3 xbox 360', 'console': 'XBOX 360', 'price': '£1.50', 'title': ''}, {'description': 'Metroid Prime 2: Echoes - Nintendo Gamecube', 'console': 'GAMECUBE', 'price': '£19.00', 'title': ''}, {'description': 'Eternal Darkness: Sanitys Requiem (Nintendo GameCube, 2002)', 'console': 'GAMECUBE', 'price': '£28.99', 'title': ''}, {'description': 'Need for Speed: Underground 2 (PlayStation 2, 2004) Complete', 'console': 'PLAYSTATION 2', 'price': '£4.99', 'title': ''}, {'description': 'Need For Speed NFS Heat Xbox One Brand New Sealed ', 'console': 'XBOX ONE', 'price': '£16.00', 'title': ''}, {'description': 'FINAL FANTASY XV DAY ONE EDITION XBOX ONE', 'console': 'XBOX ONE', 'price': '£2.50', 'title': ''}, {'description': 'Mafia Trilogy Microsoft Xbox One - New & Sealed - Free Post', 'console': 'XBOX ONE', 'price': '£22.95', 'title': ''}, {'description': 'Anima: Gate of Memories PS4 PlayStation4 (includes Original Soundtrack CD)', 'console': 'PS4', 'price': '£4.20', 'title': ''}, {'description': 'Batman: The Telltale Series (Microsoft Xbox One)', 'console': 'XBOX ONE', 'price': '£3.75', 'title': ''}, {'description': '®️®️ Assassins Creed Odyssey Xbox One game inc Manual. VGC', 'console': 'XBOX ONE', 'price': '£10.25', 'title': ''}, {'description': 'Half-Life 2: The Orange Box - Xbox 360 Excellent Condition, Complete', 'console': 'XBOX 360', 'price': '£5.69', 'title': ''}, {'description': 'Shadow of the Tomb Raider - PLAYSTATION 4 PS4', 'console': 'PS4', 'price': '£7.99', 'title': ''}, {'description': 'Street Fighter 30th Anniversary PS4 PlayStation4 VGC', 'console': 'PS4', 'price': '£7.50', 'title': ''}, {'description': 'Wario Ware Inc. Mega Party Games - Nintendo GameCube - PAL', 'console': 'GAMECUBE', 'price': '£30.00', 'title': ''}, {'description': 'Def Jam Vendetta - Sony Ps2 Game - Playstation 2 - Complete - UK PAL ', 'console': 'PLAYSTATION 2', 'price': '£5.89', 'title': ''}, {'description': 'Minecraft Story Mode The Complete Adventure Episodes 1-8 Xbox 360 ', 'console': 'XBOX 360', 'price': '£10.00', 'title': ''}, {'description': 'Star Wars: Revenge of the Sith Video Game for Sony PlayStation PS2 PAL TESTED', 'console': 'PS2', 'price': '£3.99', 'title': ''}, {'description': 'The Witcher 3 - Game of The Year Edition (PlayStation 4,2016)', 'console': 'PLAYSTATION 4', 'price': '£9.80', 'title': ''}, {'description': 'NBA 2K16 PlayStation 4 PS4 FREE POSTAGE ', 'console': 'PS4', 'price': '£3.50', 'title': ''}, {'description': 'LEGO Indiana Jones 2 The Adventure Continues Playstation 3 Ps3 FAST P&P ', 'console': 'PLAYSTATION 3', 'price': '£6.99', 'title': ''}, {'description': 'Little Nightmares 2 Day playstation 4 (PS4)', 'console': 'PS4', 'price': '£21.00', 'title': ''}, {'description': 'Sega megadrive ultimate collection ps3 *see pictures*', 'console': 'PS3', 'price': '£4.99', 'title': ''}, {'description': 'Call Of Duty Modern Warfare Remastered - Xbox One Game. Case and disc. ', 'console': 'XBOX ONE', 'price': '£12.49', 'title': ''}]

print("load_dict_len:  " + str(len(load_dict)))

from title_matcher import TitleMatcher
from data_cleanser import DataCleanser

title_matcher = TitleMatcher()

data_cleanser = DataCleanser()

db = sqlite3.connect("sale-database.db")
cursor = db.cursor()

database_schema = {
    "PS4":"ps4",
    "PLAYSTATION 4":"ps4",
    "PS3":"ps3",
    "PLAYSTATION 3":"ps3",
    "PS2":"ps2",
    "PLAYSTATION 2": "ps2",
    "XBOX ONE":"xbox_one",
    "XBOX 360":"xbox_360",
    "GAMECUBE":"gamecube"
}

for console in consoles:
    for game in [game for game in load_dict if game["console"] == console]:
        game["description"] = data_cleanser.remove_punctuation(game["description"])
        if title_matcher.check_match(game):
            cursor.execute(f"INSERT INTO '{database_schema[game['console']]}'(title,description,console,price) VALUES('{game['title']}','{game['description']}','{game['console']}',{game['price']})")
            db.commit()
        else:
            pass
