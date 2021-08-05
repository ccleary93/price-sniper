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

    def get_matches(self, game, input_data):
        for line in input_data:
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

    def check_match(self,game):
        console_schema = {
            "PS4": self.ps4_data,
            "PLAYSTATION 4": self.ps4_data,
            "PS3": self.ps3_data,
            "PLAYSTATION 3": self.ps3_data,
            "PS2": self.ps2_data,
            "PLAYSTATION 2": self.ps2_data,
            "XBOX ONE": self.xbone_data,
            "XBOX 360": self.xbox360_data,
            "GAMECUBE": self.gamecube_data
        }
        console_data = console_schema[game["console"]]
        return self.get_matches(game, console_data)
