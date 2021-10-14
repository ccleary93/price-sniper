# price sniper

This is a web scraper project designed to collect sold videogame item data from ebay.

The project came about when I wanted to find a programmatic way of identifying ebay auctions where the item was underpriced relative to its average sale price, so I could purchase videogames for resale.

Finding that the ebay sold items API had been deprecated, and that its replacement was only accessible to approved ebay partners, I set out to create a web scraper that would build a Postgresql database of sold games so I could replicate the API's functionality.


## The scraper

The scraper runs periodically, and uses beautifulsoup to parse the HTML of ebay's sold items / videogames / ordered by 'ended recently' page. The details of each result are loaded into 4 lists: title_list, price_list, postage_list and id_list. The scraper continues to cycle through each page until it finds a result which has previously been logged, then the loop terminates.

This process takes place over lines 13 - 91 of main.py.

## Loading the data

Once the loop has terminated, the script attempts to match the sold item description to a console, and then to a game which exists for that console. This is largely handled by the TitleMatcher class. All non-alphanumeric characters are removed from the description by the DataCleanser class.

Finally a connection is established to the Postgresql database using psycopg2 and the data is loaded. The stored data appears thus:

![scraped data as logged in the database](https://i.ibb.co/h2YbBRk/pgadmin.png)

The ebay ID of the first item found is also logged - this will be used the next time the scraper runs to determine when the loop should terminate.

Sales for each console are logged in a separate table. The database schema therefore looks like the below, with a separate table for each console:

![enter image description here](https://i.ibb.co/d6hwpZF/schema.png)

