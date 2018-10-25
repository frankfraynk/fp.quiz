import random as ra
import bs4 as bs
import urllib.request
namesauce = urllib.request.urlopen('https://www.babble.com/pregnancy/1000-most-popular-boy-names/').read()
namesoup = bs.BeautifulSoup(namesauce,'lxml')
tNames = ['barbara','Tim','percy','Noah','Tami','Khaled','susie','Santa']
ol = namesoup.find('ol')
for li in ol.findAll('li'):
    tNames.append(li.text)




def getNameData(rName):

    uName = rName.lower()
    lscore = len(uName)
    vscore = 0
    i = 0
    ll = ""
    repeat = False
    guilty = False
    tscore = 0

    for letter in uName:
        if letter in ['a','e','i','o','u']:

            if letter != 'y':
                vscore += 1
            else:
                vscore += .5

        elif letter in ["z","k","p","b","v"]:
            vscore += 3

        if ll == letter:
            repeat = True
        ll = letter
        i += 1

    if rName[0].islower():
        vscore = vscore ** 2
        guilty = True
    tscore = lscore + vscore
    if repeat:
        tscore += len(uName)


    result = [tscore, guilty, repeat]
    return result
f = open("NameData.txt", "w+")

for names in tNames:

    nameData = getNameData(names)


    f.write("\n" + names + ":\n  Total Data Score: " +  str(nameData[0]) + '\n  Guilty: ' + str(nameData[1]) +'\n  Repeater: ' + str(nameData[2]))
