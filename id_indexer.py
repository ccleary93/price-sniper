import sqlite3


db = sqlite3.connect("sale-database.db")
cursor = db.cursor()



class ID_Indexer():
    def __init__(self):
        self.tables = ["gamecube", "ps2", "ps3", "ps4", "xbox_360", "xbox_one"]
        self.id_lister = 0

    def load_last_id(self):
        cursor.execute('''SELECT ebay_id FROM first_item_index WHERE ID = (SELECT MAX(ID) FROM first_item_index);''')
        self.id_lister = int(str(cursor.fetchall()).split(sep="(")[1].split(sep=",")[0])
        return self.id_lister