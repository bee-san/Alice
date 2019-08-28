class words:
    """class to look at words
    can remove repeadted words"""
    def __init__(self, text):
        self.text = text
        self.deleteWords = ["you", "your", "yours", "like", "maybe", "just"]
        # TODO lowercase for delete words
        self.list_text = self.text.split(" ")
    def repeatedWords(self):
        """
        Deletes repeadted words in text
        """
        for counter in range(1, len(self.list_text)):
            if self.list_text[counter - 1].strip() == self.list_text[counter].strip():
                self.list_text.remove(self.list_text[counter])
    def checkForBadWords(self):
        """removes bad words from the text"""
        for word in self.deleteWords:
            self.list_text.remove(word)
