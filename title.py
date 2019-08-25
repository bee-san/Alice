class titleServant:
    """
    works out h1, h2 ordering and also how many of each one is used
    """
    def __init__(self, text, mdorhtml):
        self.text = text
        self.mdorhtml = mdorhtml
        self.titles = []
        self.markdownHeaders = {
            "#": 1,
            "##": 2,
            "###": 3,
            "####": 4,
            "#####": 5
        }
        self.htmlHeaders = {
            "h1": 1
        }
    def run(self):
        self.getTitles()
        self.linkBreakdown()
        self.titleOrdering()
    def getTitles(self):
        """gets all items in a text"""

        # for every line in the text
        # if that text starts with a markdown header
        # append it to a dictionary with a numerical value
        if self.mdorhtml == "md":
            for line in self.text.split("\n").strip():
                for val, key in self.markdownHeaders.iteritems():
                    if line.startswith(val):
                        self.titles.append([line, self.markdownHeaders.get(val)])
    def linkBreakdown(self):
        links = {
            "h1": 0,
            "h2": 0,
            "h3": 0,
            "h4": 0,
            "h5": 0
        }
        for link in self.titles:
            if link[1] == 1:
                links['h1'] += 1
            elif link[1] == 2:
                links['h2'] += 1
            elif links[1] == 3:
                links['h3'] += 1
            elif links[1] == 4:
                links['h4'] += 1
            elif links[1] == 5:
                links['h5'] += 1
        print("Here is the breakdown of each type of heading used in this post: ")
        print(links)
        self.linksBreakdown = links
    def titleOrdering(self):
        counter = 0
        for number in range(1, len(self.titles)):
            if (abs(self.titles[number][1] - self.titles[counter][1]) > 1) and (self.titles[number][1] != 1 or self.titles[number][1] != 2):
                print(f"Heading error detected. The heading {self.titles[number][0]} has a heading value of {self.titles[number][1]} but the previous title {self.titles[counter][0]} has value of {self.titles[counter][1])}")
            counter += 1

"""
So the post should always start with a H1
the next title should either be a H1, or a H2
the title after H2 is either H3, or H1

So the title is either the one after it, the one before it, or a h1 or h2 ?

so it'd make sense to store the titles in the order we see them into a list
maybe we can store it with a dictionary like:
[{"Ciphey": 1}, {"Why you need this": 2}]

This is because dictionaries aren't ordered, but we could make a queue?
Then when we've finished making this, we loop through the list to find out if the ordering looks dodgy?

An ordering should look bad if:
* The difference between the current element and the element before it is more than 1
* If so and the current element isn't a h1 or h2 tag, then report it
* n

# start at 1 because there is no previous
for counter, item in enumerate(range(1, len(items))):
    if abs(item[1] - items[counter]) > 1 and (item[1] != 1 or item[1] != 2):
        print("uh oh accident!)

"""