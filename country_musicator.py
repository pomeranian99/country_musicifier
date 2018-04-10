# import libraries
# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

keepGoing = True

def replace_all(text, dic):
    for a, b in dic.iteritems():
        text = text.replace(a, b)
    return text

askFileName = raw_input("Give a name for the file we're going to create: ")
file = open(askFileName, "a+")

while (keepGoing):
    needURL = True
    while (needURL):
        askURL = raw_input("Which URL are we scraping? ")
        if "http" in askURL:
            needURL = False
        else:
            print ("Sorry, you didn't give me a URL. Try again ...")

    page = urllib2.urlopen(askURL)
    soup = BeautifulSoup(page, 'html.parser')

    listOfParts = soup.find_all('td')

    # the 20th element in the list contains the lyrics
    stringOfParts = str(listOfParts[19])
    listOfParts = stringOfParts.split("<br/>")

    # remove crufty substring chunks
    reps = {"</br>": "", "<br>": "", "</td>": "", "\n": " ", "\r": " ", "              ": "", "  ": " "}
    reps2 = {"  ": " "}
    totalLyrics = ""
    counter = 1

    for i in listOfParts:
        if "href" in i:
            continue
        else:
            if "<script" in i:
                continue
            else:
                totalLyrics = totalLyrics + i
        counter = counter + 1

    # get rid of the html cruft
    finalLyrics = replace_all(totalLyrics, reps)

    # nix double spaces
    while ("  " in finalLyrics):
        reduced = replace_all(finalLyrics, reps2)
        finalLyrics = reduced

    finalLyrics = finalLyrics.lower()

    file.write(finalLyrics)

    needAnswer = True
    while (needAnswer):
        cont = raw_input("Add another song? Y or N ... ")
        if cont == "Y":
            needAnswer = False
        elif cont == "N":
            needAnswer = False
            keepGoing = False
        else:
            print ("Sorry, I need a Y or N ...")

print ("Okay, we're all done!")
file.close()
