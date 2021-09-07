from bs4 import BeautifulSoup
import requests
import time
import random
import sqlite3
import datetime

# unique id check tracks the last batch of ids loaded to prevent duplicates being added to the db
# although the first_item_index table terminates the scrape loop, and in theory should prevent duplicates...
# ... as the listings should be in time order, in practice some duplicates were still being logged, possibly...
# due to an 'overlap' when an item moved between pages
unique_id_check = []

while 1 > 0:

    #wait between 260 secs and 450 secs before sending more requests
    time_delay = random.randint(260, 450)
    time.sleep(time_delay)

    current_date = datetime.datetime.now().date().strftime('%d/%m/%Y')
    current_time = datetime.datetime.now().time().strftime('%H:%M')

    # START AT PAGE 2 - goes up to page 136. 48 results per page
    pgn = 2

    title_list = []
    price_list = []
    id_list = []
    postage_list = []

    # end_index and continue_scrape used to determine where the scrape should stop, to avoid double-counting
    from id_indexer import ID_Indexer
    id_indexer = ID_Indexer
    end_index = id_indexer().load_last_id()
    continue_scrape = True

    while pgn < 5 and continue_scrape:
        # establish connection
        url = f"https://www.ebay.co.uk/b/Video-Games/139973/bn_450842?LH_Sold=1&mag=1&rt=nc&_pgn={pgn}&_sop=13"
        connection = requests.get(url)
        print(connection)
        ingredients = connection.text
        soup = BeautifulSoup(ingredients,"html.parser")

        #Get all divs that represent an item's info and iterate over them
        item_info_tags = soup.find_all(name="div", class_="s-item__info")
        for item_info_tag in item_info_tags:

            #Take title as-is
            title_list.append(item_info_tag.find(name="h3", class_="s-item__title s-item__title--has-tags").string)

            # if find_all returns only one item for price, load this. Otherwise, we have a job lot, and load "ERR"
            if len(item_info_tag.find(name="span", class_="s-item__price").find_all(name="span", class_="POSITIVE")) == 1:
                price_list.append(item_info_tag.find(name="span", class_="s-item__price").string)
            else:
                price_list.append("ERR")

            #Take postage price as 0.00 if Free Postage, "ERR" if missing or invalid, or actual value otherwise
            postage_current = item_info_tag.find(name="span", class_="s-item__shipping s-item__logisticsCost")
            if postage_current == None or len(postage_current.string) < 2:
                #error case
                postage_list.append("ERR")
            elif postage_current.string == "Free postage":
                postage_list.append("0.00")
            else:
                postage_list.append(postage_current.string.split(sep="£")[1].split(sep=" ")[0])

            #Extract Item ID from hrew
            id_current = item_info_tag.find(name="a", class_="s-item__link")
            id_list.append(int(id_current["href"].split(sep="itm/")[1].split(sep="?")[0]))

        # look for end_index in the list just scraped. If present, cut the lists down to end at end_index and terminate the PGN loop
        if end_index in id_list:
            title_list = title_list[0:id_list.index(end_index)]
            price_list = price_list[0:id_list.index(end_index)]
            postage_list = postage_list[0:id_list.index(end_index)]
            id_list = id_list[0:id_list.index(end_index)]
            continue_scrape = False

        pgn += 1

        # add delay between requests
        time.sleep(random.randint(180,320)/100)



    # schema to standardise which console identifier goes in the 'console' field of the load dict
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

    # iterate over all items
    for i in range(0,len(title_list)):
        # check for a console match. also check item id unique and postage and price not ERR
        for console in consoles.keys():
            if title_list[i].lower().find(console.lower()) >= 0 and postage_list[i] != "ERR" and price_list[i] != "ERR":
                # add a dict to load_dict for each matched item
                load_dict.append({"description":title_list[i],
                                "console":consoles[console],
                                "price":price_list[i],
                                "postage":postage_list[i],
                                "ebay_id":id_list[i],
                                "title":""})
                break
            else:
                pass


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
                # check ID not in last batch
                if game['ebay_id'] not in unique_id_check:
                    cursor.execute(f'''INSERT INTO
                    '{database_schema[game['console']]}'(title,description,price,postage,total_price,date, time, ebay_id)
                    VALUES('{game['title']}',
                    '{game['description']}',
                    {game['price']},
                    {game['postage']},
                    {game['price']+float(game['postage'])},
                    '{current_date}',
                    '{current_time}',
                    {game['ebay_id']})''')
                    db.commit()
                else:
                    pass

    # now update unique ID list
    unique_id_check = id_list