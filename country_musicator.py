# import libraries
# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
finalArticle = ""
askURL = raw_input("Which URL are we scraping? ")
page = urllib2.urlopen(askURL)
soup = BeautifulSoup(page, 'html.parser')

# break the html into a list, broken up by tds
listOfParts = soup.find_all('td')

# the 20th element in the list
stringOfParts = str(listOfParts[19])
listOfParts = stringOfParts.split("<br/>")

# this is the dictionary for all the substring chunks
# I'll want to search and replace for later in the final string
reps = {"</br>": "", "<br>": "", "</td>": "", "\n": " ", "\r": " ", "              ": "", "  ": " "}
reps2 = {"  ": " "}
totalLyrics = ""
counter = 1

def replace_all(text, dic):
    for a, b in dic.iteritems():
        text = text.replace(a, b)
    return text

# take anything element that doesn't have a href or script tag
# and exclude it; everything else is appended to the final string ...
for i in listOfParts:
    if "href" in i:
        print ("Throwing out a href!!!")
    else:
        if "<script" in i:
            print ("Throwing out a script!!!")
        else:
            totalLyrics = totalLyrics + i
    counter = counter + 1

# get rid of the html cruft in the string
finalLyrics = replace_all(totalLyrics, reps)

# get rid of the double spaces in the string
while ("  " in finalLyrics):
    reduced = replace_all(finalLyrics, reps2)
    finalLyrics = reduced

#lowercase it!
finalLyrics = finalLyrics.lower()

print (finalLyrics)
