"""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░▌           ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌               ▐░▌     ▐░▌          ▐░▌          
▐░█▄▄▄▄▄▄▄█░▌▐░▌               ▐░▌     ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌               ▐░▌     ▐░▌          ▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░▌               ▐░▌     ▐░▌          ▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌               ▐░▌     ▐░▌          ▐░▌          
▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ 
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
github: brandonskerritt

Class designed to deal with all links on a webpage. It does:
* Automatic UTM param adding
* Checking for 404 links and trying to correct them if there's an error
* Capitalising links (if the user wants to)
"""
# python class designed to hold all links and deal with links
import re
import requests
class linksServant:
    def __init__(self, text, mdorhtml, websiteurl):
        self.text = text
        self.mdorhtml = mdorhtml
        self.websiteurl = "skerritt.blog"
        self.returnObject = {
            "errors": {}
        }
    def run(self):
        self.getLinksMark()
        self.addUTMTags()
        self.check404()
    def getLinksMark(self):
        if self.mdorhtml == "md":
            # Anything that isn't a square closing bracket
            name_regex = "[^]]+"
            # http:// or https:// followed by anything but a closing paren
            url_regex = "http[s]?://[^)]+"

            # regex to find the links
            markup_regex = '\[({0})]\(\s*({1})\s*\)'.format(name_regex, url_regex)
            self.links = re.findall(markup_regex, self.text)
            self.LINKSDONTTOUCH = self.links
            
    def addUTMTags(self):
    # would be cool if main.py was a class
    # so one of the attributes could be the main url....
    # adds utm tags to all links
        for num, match in enumerate(self.links):
            withUtm = match[1]+"?utm_source={}&utm_medium=blog&utm_campaign={}".format(self.websiteurl, self.websiteurl)
            self.text = self.text.replace(match[1], withUtm)
            self.links[num] = withUtm
    def check404(self):
        for counter, link in enumerate(self.links):
            check = self.check404eachLink(link)
            if check:
                # if 404, then check to see if non utm version doesn't 404
                # it it doesnt, dont apply utm tags :)
                oldLink = self.LINKSDONTTOUCH[counter]
                self.links = oldLink
                link = check404eachLink(oldLink)
                if link:
                    self.returnObject['errors']['link']
                else:
                    print("The UTM tag wasn't added to the link as it resulted in a HTTP 404 error ", oldLink)
        print("these are the links ", self.links)
    def check404eachLink(self, link):
        # checks to see if a link is a 404
        # arguments: link (the url to check)
        try:
            r = requests.get(link)
            if r.status_code == 404:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
    def finishLinkEditing(self):
        # edits all the links in the text to match the new links
        for counter, link in enumerate(self.links):
            text = text.replace(LINKSDONTTOUCH[counter], link)
