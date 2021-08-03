class DataCleanser():
    def __init__(self):
        self.punctuation = ["!","(",")","-","[","]","{","}",";",":","'",'"',".","?","&"]

# with open("gamecube_games.csv","r",encoding="utf-8") as file:
#     data = file.readlines()
#
#data = [line.rstrip() for line in data]
# for line in data:
#     for char in data:
#         char.lower()
# print(data)
#punctuation = ["!","(",")","-","[","]","{","}",";",":","'",'"',".","?","&"]

    def remove_punctuation(self, string):
        no_punct = ""
        for char in string:
            if char not in self.punctuation:
                no_punct += char
        return no_punct.lower()

# new_data = []
# for line in data:
#     no_punt = ""
#     for char in line:
#         if char not in punctuation:
#             no_punt += char
#     new_data.append(no_punt.lower())
# print(new_data)
# with open("gamecube_games.csv", "w", encoding="utf-8") as file:
#     file.writelines(new_data)

