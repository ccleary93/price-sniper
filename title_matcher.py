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

    def print_ps4(self):
        print(self.ps4_data)

    def check_match_ps4(self, game):
        for line in self.ps4_data:
            if game["description"].find(line.lower()) >= 0:
                if game["title"] == "":
                    game["title"] = line
                else:
                    if len(line) > len(game["title"]):
                        game["title"] = line
        if game["title"] != "":
            print(game)
        #continue

    def check_match_ps3(self, game):
        for line in self.ps3_data:
            if game["description"].find(line.lower()) >= 0:
                if game["title"] == "":
                    game["title"] = line
                else:
                    if len(line) > len(game["title"]):
                        game["title"] = line
        if game["title"] != "":
            print(game)

    def check_match_ps2(self, game):
        for line in self.ps2_data:
            if game["description"].find(line.lower()) >= 0:
                if game["title"] == "":
                    game["title"] = line
                else:
                    if len(line) > len(game["title"]):
                        game["title"] = line
        if game["title"] != "":
            print(game)

    def check_match_xbone(self, game):
        for line in self.xbone_data:
            if game["description"].find(line.lower()) >= 0:
                if game["title"] == "":
                    game["title"] = line
                else:
                    if len(line) > len(game["title"]):
                        game["title"] = line
        if game["title"] != "":
            print(game)

    def check_match_xbox_360(self, game):
        for line in self.xbox360_data:
            if game["description"].find(line.lower()) >= 0:
                if game["title"] == "":
                    game["title"] = line
                else:
                    if len(line) > len(game["title"]):
                        game["title"] = line
        if game["title"] != "":
            print(game)

    def check_match_gamecube(self, game):
        for line in self.gamecube_data:
            if game["description"].find(line.lower()) >= 0:
                if game["title"] == "":
                    game["title"] = line
                else:
                    if len(line) > len(game["title"]):
                        game["title"] = line
        if game["title"] != "":
            print(game)