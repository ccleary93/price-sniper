from bs4 import BeautifulSoup
import requests
import time
import random

class Scraper:
    def __init__(self):
        self.pgn = 1
        self.url = f"https://www.ebay.co.uk/b/Video-Games/139973/bn_450842?rt=nc&LH_Sold=1&mag=1&_sop=13&pgn={str(self.pgn)}"


    def scrape_page(self,pgn):
        self.url = f"https://www.ebay.co.uk/b/Video-Games/139973/bn_450842?rt=nc&LH_Sold=1&mag=1&_sop=13&pgn={str(self.pgn)}"
        self.connection = requests.get(url)
        self.ingredients = self.connection.text
        self.soup = BeautifulSoup(self.ingredients,"html.parser")
