import random as ra


def getNameData(rName):

    uName = rName.lower()
    lscore = len(uName)
    vscore = 0
    i = 0
    ll = ""
    repeat = False
    guilty = False


    for letter in uName:
        if letter in ['a','e','i','o','u']:

            if letter != 'y':
                vscore += 1
            else:
                vscore += .5
                
        elif letter in ["z","k","p","h","v"]:
            guilty = True
            
        if ll == letter:
            repeat = True
            
        ll = letter
        i += 1
    
    return vscore,lscore

tNames = ['Barbara','Tim','Percy','Noah','Tami','Khaled','Susie','Santa']
s = tNames[ra.randint(0,(len(tNames)-1))]
print(s,getNameData(s))

