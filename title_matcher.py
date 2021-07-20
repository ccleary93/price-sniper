class TitleMatcher:
    def __init__(self):
        with open("ps4_games.csv","r",encoding="utf-8") as file:
            self.ps4_data = file.readlines()
        self.ps4_data = [line.rstrip() for line in self.ps4_data]

    def print_ps4(self):
        print(self.ps4_data)
    
    def check_match_ps4(self, title):
        for line in self.ps4_data:
           if title.find(line) >= 0:
               print(title)
               continue
