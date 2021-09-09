import sqlite3


db = sqlite3.connect("sale-database.db")
cursor = db.cursor()



class ID_Indexer():
    def __init__(self):
        self.tables = ["gamecube", "ps2", "ps3", "ps4", "xbox_360", "xbox_one"]
        self.previous_scrape_start = 0

    def load_last_id(self):
        cursor.execute('''SELECT ebay_id FROM first_item_index WHERE ID = (SELECT MAX(ID) FROM first_item_index);''')
        try:
            self.previous_scrape_start = int(str(cursor.fetchall()).split(sep="(")[1].split(sep=",")[0])
        except IndexError:
            self.previous_scrape_start = 0
        return self.previous_scrape_start

    def load_last_20(self, console):
        cursor.execute(f"SELECT ebay_id FROM {console} ORDER BY id DESC LIMIT 20")
        return cursor.fetchall()