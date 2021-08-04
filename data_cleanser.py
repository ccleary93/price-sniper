class DataCleanser():
    def __init__(self):
        self.punctuation = ["!","(",")","-","[","]","{","}",";",":","'",'"',".","?","&"]

    def remove_punctuation(self, string):
        no_punct = ""
        for char in string:
            if char not in self.punctuation:
                no_punct += char
        return no_punct.lower()
