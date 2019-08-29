class wordsServant:
    """class to look at words
    can remove repeadted words"""
    def __init__(self, text):
        self.text = text
        self.deleteWords = ["like", "maybe", "just"]
        # TODO lowercase for delete words
        self.list_text = self.text.split(" ")
    def repeatedWords(self):
        """
        Deletes repeadted words in text
        """
        # so whenever i delete a word
        # the length of the list goes down by 1
        # so that changes everything, so i need to keep track of them LMAO
        deletionCounter = 0
        for counter in range(1, len(self.list_text)):
            # for every word in the string
            # if that word is repeated, delete it
            try:
                if self.list_text[counter - 1].strip().lower() == self.list_text[counter].strip().lower():
                    self.list_text.remove(self.list_text[counter - deletionCounter])
                    deletionCounter += 1
            except IndexError as e:
                # basically if the counter == len of list, it errors out so we just skip it lol
                pass
        print(self.list_text)
    def checkForBadWords(self):
        """removes bad words from the text"""
        for word in self.deleteWords:
            if word in self.list_text:
                self.list_text.remove(word)

if __name__ == "__main__":
    print("and this runs oops")
    ws = wordsServant("hello hello and I I yours")
    ws.repeatedWords()
    ws.checkForBadWords()
