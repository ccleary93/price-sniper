import string

class DataCleanser():
    def __init__(self):
        self.whitelist = list(" " + string.ascii_lowercase + string.ascii_uppercase + string.digits)

    def remove_punctuation(self, string):
        return "".join([char for char in string if char in self.whitelist]).lower()
