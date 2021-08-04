class TitleMatcher:
    def __init__(self):
        with open("game_lists/ps4_games.csv","r",encoding="utf-8") as file:
            self.ps4_data = file.readlines()
        self.ps4_data = [line.rstrip() for line in self.ps4_data]
        with open("game_lists/ps3_games.csv","r",encoding="utf-8") as file:
            self.ps3_data = file.readlines()
        self.ps3_data = [line.rstrip() for line in self.ps3_data]
        with open("game_lists/ps2_games.csv","r",encoding="utf-8") as file:
            self.ps2_data = file.readlines()
        self.ps2_data = [line.rstrip() for line in self.ps2_data]
        with open("game_lists/xbone_games.csv","r",encoding="utf-8") as file:
            self.xbone_data = file.readlines()
        self.xbone_data = [line.rstrip() for line in self.xbone_data]
        with open("game_lists/xbox360_games.csv","r",encoding="utf-8") as file:
            self.xbox360_data = file.readlines()
        self.xbox360_data = [line.rstrip() for line in self.xbox360_data]
        with open("game_lists/gamecube_games.csv","r",encoding="utf-8") as file:
            self.gamecube_data = file.readlines()
        self.gamecube_data = [line.rstrip() for line in self.gamecube_data]

        def check_match(self,game):
        # first check for the console to determine what list to search
        if game["console"] == "PS4" or game["console"] == "PLAYSTATION 4":
            # iterate through lines
            for line in self.ps4_data:
                # if the line matches the game description, the title from the list gets added to the title field of the dict
                # if title field is empty, it goes straight in. If there's already something in there, the longer match goes in
                # longer match is more likely to be the correct one eg 'assassins creed' vs 'assassins creed 2'
                if game["description"].find(line) >= 0:
                    if game["title"] == "":
                        game["title"] = line
                    else:
                        if len(line) > len(game["title"]):
                            game["title"] = line
            if game["title"] != "":
                game["price"] = float(game["price"].split(sep="£")[1])
                return game
            else:
                return False
        elif game["console"] == "PS3" or game["console"] == "PLAYSTATION 3":
            for line in self.ps3_data:
                if game["description"].find(line) >= 0:
                    if game["title"] == "":
                        game["title"] = line
                    else:
                        if len(line) > len(game["title"]):
                            game["title"] = line
            if game["title"] != "":
                game["price"] = float(game["price"].split(sep="£")[1])
                return game
            else:
                return False
        elif game["console"] == "PS2" or game["console"] == "PLAYSTATION 2":
            for line in self.ps2_data:
                if game["description"].find(line) >= 0:
                    if game["title"] == "":
                        game["title"] = line
                    else:
                        if len(line) > len(game["title"]):
                            game["title"] = line
            if game["title"] != "":
                game["price"] = float(game["price"].split(sep="£")[1])
                return game
            else:
                return False
        elif game["console"] == "XBOX ONE":
            for line in self.xbone_data:
                if game["description"].find(line) >= 0:
                    if game["title"] == "":
                        game["title"] = line
                    else:
                        if len(line) > len(game["title"]):
                            game["title"] = line
            if game["title"] != "":
                game["price"] = float(game["price"].split(sep="£")[1])
                return game
            else:
                return False
        elif game["console"] == "XBOX 360":
            for line in self.xbox360_data:
                if game["description"].find(line) >= 0:
                    if game["title"] == "":
                        game["title"] = line
                    else:
                        if len(line) > len(game["title"]):
                            game["title"] = line
            if game["title"] != "":
                game["price"] = float(game["price"].split(sep="£")[1])
                return game
            else:
                return False
        elif game["console"] == "GAMECUBE":
            for line in self.gamecube_data:
                if game["description"].find(line) >= 0:
                    if game["title"] == "":
                        game["title"] = line
                    else:
                        if len(line) > len(game["title"]):
                            game["title"] = line
            if game["title"] != "":
                game["price"] = float(game["price"].split(sep="£")[1])
                return game
            else:
                return False
