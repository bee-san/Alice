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
"""
import argparse
from requests import get
from collections import OrderedDict


parser = argparse.ArgumentParser(description='Blog')
parser.add_argument('-f','--file', help='Blog post as a .md [Markdown] file', required=False)
parser.add_argument('-u','--url', help='Url of your blog [required for UTM tags]', required=False)
parser.add_argument('-g','--ghost', help='Your ghost blogs content API', required=False)
parser.add_argument('-c','--capitalselinks', help='Capitalise all links. You will be presented with each link and get to decide which ones to capitalise', required=False)
args = vars(parser.parse_args())

if len(args) <= 1:
    print("error no arguments supplied. Use --help for help")
    exit(1)

if args['ghost'] != None:
    # uses Ghost's content api to get the posts and parses them
    r = get("https://brandonskerritt-2.ghost.io/ghost/api/v2/content/posts/?key=6ef88b4f6b24eff0247a358cf0")
    responseJson = r.json()
    # creates an ordered dict of title: id so we can easily ask the user what post they want to edit
    titlesValue = {}
    for number, titles in enumerate(responseJson['posts']):
        titlesValue[titles['title']] = number
    titlesValue = OrderedDict(titlesValue)

    # just prints the ordered dict and makes it look pretty
    print("ID ----  Title")
    print("-------------")
    for k in titlesValue:
        print(titlesValue[k], " ---- ", k)
    whatBlogPost = int(input(("What blog post would you like to use? Enter it in the ID number ")))

    # gets the blog post title from the ID
    for title, num in titlesValue.items():
        if whatBlogPost == num:
            titleOfPost = title

    # TODO next: get the HTML info in and actually start editign this biatttchh :)
if args['file'] != None:
    f = open("{}".format(args['file']), "r")
    text = f.read()
    f.close()
    import links
    newLinksobj = links.linksServant(text, mdorhtml="md", websiteurl="skerritt.blog")
    newLinksobj.getLinksMark()    
    newLinksobj.addUTMTags()
    newLinksobj.check404()

def mainCode(newLinksobj):
    newLinksobj.getLinksMark()    
    newLinksobj.addUTMTags()
    newLinksobj.check404()
    if args['capitalselinks'] != None:
        print("yeet")
