# rock papar sisiisors


import random as r

listofChoice = ["rock", "paper", "sissors"]
usermatchPoints = int()
pcmatchPoints = int()

while usermatchPoints < 2 or pcmatchPoints < 2:
    if usermatchPoints > 1 or pcmatchPoints > 1:
        break
    theinput = input("please Enter Your chioice \n")
    pcChoice = r.randint(0, 2)
    temp = listofChoice[pcChoice]
    temp2 = temp[0]
    if usermatchPoints > 1 or pcmatchPoints > 1:
        break
    elif temp2 == theinput[0]:
        print("its Tie")
        print("=============")
    elif temp2 == "r" and theinput[0] == "s":
        print("you lost this Round ")
        print("=============")
        pcmatchPoints += 1
    elif temp2 == "r" and theinput[0] == "p":
        print("you wom this Round ")
        print("=============")

        usermatchPoints += 1
    elif temp2 == "p" and theinput[0] == "r":
        print("you lost this Round ")
        print("=============")

        pcmatchPoints += 1
    elif temp2 == "p" and theinput[0] == "s":
        print("you won this Round ")
        print("=============")
        usermatchPoints += 1
    elif temp2 == "s" and theinput[0] == "p":
        print("you lost this Round ")
        pcmatchPoints += 1
    elif temp2 == "s" and theinput[0] == "r":
        print("you won this Round ")
        print("=============")
        usermatchPoints += 1
    else:
        break

if pcmatchPoints > 1:
    print("pc won\n")
    print(pcmatchPoints)
elif usermatchPoints > 1:
    print("YYYYYO won\n")
    print(usermatchPoints)
