class bcolors:
 HEADER = '\033[95m'
 OKBLUE = '\033[94m'
 OKCYAN = '\033[96m'
 OKGREEN = '\033[92m'
 WARNING = '\033[93m'
 FAIL = '\033[91m'
 ENDC = '\033[0m'
 BOLD = '\033[1m'
 UNDERLINE = '\033[4m'

name = input(bcolors.UNDERLINE + bcolors.HEADER + "What is your name ? : " + bcolors.ENDC)
print(bcolors.OKCYAN + "Hey "+ name +" have you heard about new game,it's called the last hope." + bcolors.ENDC)
print(bcolors.OKCYAN + """it's about 2 team's 
first is : Human 
second is : zombies.
First is the human team :They don't have that much of the power but they do have weapon's  kill a group of 10 zombies
and second team is ! you guessed it zombies :they can come in huge number but they are weak . or in a few but they are strong.
it's really good game so what do u say?""" + bcolors.ENDC)
start = input(bcolors.UNDERLINE + bcolors.HEADER + "Do u wanna to try it? yes/no : " + bcolors.ENDC)
if start == "yes" or start == "y":
    print(bcolors.OKCYAN + """Great i know that u will love it as i did
i will bring it today after school. see you later """+ name +bcolors.ENDC)
    print(bcolors.OKCYAN + "you got the game, now let's start playing." + bcolors.ENDC)
    name1 = input(bcolors.UNDERLINE + bcolors.HEADER + "enter your in game nickname : " + bcolors.ENDC)
    print(bcolors.OKCYAN + "Hey "+ name1 +" Welcom to the last hope." + bcolors.ENDC)
    start2 = input(bcolors.UNDERLINE + bcolors.HEADER + """Choose your side,A : Human B : zombies
press A or B : """ + bcolors.ENDC)
    if start2 == "A" or start2 == "a":
        start3 = input(bcolors.UNDERLINE + bcolors.HEADER + "choose your sex Man or Woman : " + bcolors.ENDC)
        if start3 == "man" or start3 == "Man" or start3 == "Woman" or start3 == "woman" or start3 == "m" or start3 == "w":
            print(bcolors.OKBLUE + "{ Welcom to the human world }" + name1 + """,
you walking in the city and you need to gear up and you see smithy workshop you go in and asked hem that you need to gear up and he recommend.
shield and pistole, rifel, sniper, Dual pistole.
1: shield and pistole : He have a high Defense but low attack damge low movement speed .
2: rifel : He have a high attack damge, and you can shoot fast, medium movement speed  .
3: sniper : High range and high damage + medium to low movement speed but you can't fight in close range and you have low defense
4: Dual pistole : tow knives medium damage really fast movement fast attacks low defence""" + bcolors.ENDC)
            start4 = input(bcolors.UNDERLINE + bcolors.HEADER + """1: Sword and shield
1:shield and pistole
2: rifel
3: sniper
4: Dual pistole
Wat do u choose? type the weapon name : """ + bcolors.ENDC)
            if start4 == "1" or start4 == "shield and pistole":
                print(bcolors.OKBLUE + "You select Sword and shield"+ bcolors.ENDC)
            elif start4 == "2" or start4 == "rifel":
                print(bcolors.OKBLUE +"You select Longsword"+ bcolors.ENDC)
            elif start4 == "3" or start4 == "sniper":
                print(bcolors.OKBLUE +"You select sniper"+ bcolors.ENDC)
            elif start4 == "4" or start4 == "Dual pistole":
                print(bcolors.OKBLUE +"You select Dual pistole"+ bcolors.ENDC)
            print(bcolors.OKBLUE +"Someone walk's up to u,Hi are u new here ? i heard that your name is "+ name1 + "?" + bcolors.ENDC)
            start5 = input(bcolors.UNDERLINE + bcolors.HEADER + "is that correct ?" + bcolors.ENDC)
            print(bcolors.OKBLUE +"Great to see u " + name1 + " i am captain cris, i am here to say i am glad that we have a new soldier" + bcolors.ENDC)
            print(bcolors.OKBLUE + "is the new day and you are in the field you got your "+ start4 + " and you are ready to fight."+ bcolors.ENDC)
            print(bcolors.OKBLUE + "you was with your team but the battle got heated and you are alone now, you are walking and you see tow ways"+ bcolors.ENDC)
            print(bcolors.OKBLUE +"""Way 1 : long but not really safe 
Way 2 : short but really dangerous"""+ bcolors.ENDC)
            start6 = input(bcolors.UNDERLINE + bcolors.HEADER + "Which way do you wanna choose? 1/2 : " + bcolors.ENDC)
            if start6 == "1":
                print(bcolors.OKBLUE + "you are walking mid way and you see a door you do not know what is in side " + bcolors.ENDC)
                start7 = input(bcolors.UNDERLINE + bcolors.HEADER +"Do you want to go in ? yes/no"+ bcolors.ENDC)
                if start7 == "yes" or start7 == "y":
                    print(bcolors.OKBLUE +"This way will lead you outside. and you are safe here "+ bcolors.ENDC)
                    print(bcolors.OKBLUE +"""You are fighting with your team, then couple zombies attack you,"""+ bcolors.ENDC)
                    sart9= input(bcolors.UNDERLINE + bcolors.HEADER +""" 1: so do sacrfice your self for your team so he dont kill any of them ? and fight hem alone ?
 2: or you fight hem with your team ?"""+ bcolors.ENDC)
                    if sart9 == "1":
                        print(bcolors.OKBLUE +"you did kill hem but you are realy injured and you can't fight anymore{Game over}"+ bcolors.ENDC)
                    elif sart9 =="2":
                        print(bcolors.OKBLUE +"You kild hem with your team and you win the Game (Congratulation)"+ bcolors.ENDC)
                else:
                    print(bcolors.OKBLUE +"Ther is alot of zombies in here and you are dead {* Game over *}" + bcolors.ENDC )
            elif start6 == "2":
                print(bcolors.OKBLUE + """you are walking and you see a door to the left but you ignore it and you keep walking. 
on your way you see zombies in here and u have to fight them to pass over or you try to run back and go in to the door.""" + bcolors.ENDC)  
                start8 = input(bcolors.UNDERLINE + bcolors.HEADER +"Fight or the Door? : "+ bcolors.ENDC)
                if start8 == " fight" or start8 == "f":
                    print(bcolors.OKBLUE +"You passed over and you got out of there safe with out any damge"+ bcolors.ENDC)
                    print(bcolors.OKBLUE +"""You are fighting with your team, the zombies are targeting you, you know that they are looking for you,"""+ bcolors.ENDC)
                    sart9= input(bcolors.UNDERLINE + bcolors.HEADER +""" 1: so do sacrfice your self for your team so he dont kill any of them ?and fight hem alone ?
 2: or you fight hem with your team ?"""+ bcolors.ENDC)
                    if sart9 == "1":
                        print(bcolors.OKBLUE +"you did kill hem but you are realy injured and you can't fight anymore{Game over}"+ bcolors.ENDC)
                    elif sart9 =="2":
                        print(bcolors.OKBLUE +"You kild hem with your team and you win the Game (Congratulation)"+ bcolors.ENDC)
                else:
                    print(bcolors.OKBLUE +"In this door u walk in to dead end and zombies are behind you and they killded you {* Gmae over *}"+ bcolors.ENDC)

    elif start2 == "B" or start2 == "b":
        print(bcolors.OKBLUE +"{ Welcom to the zombies world }"+ bcolors.ENDC)
        print(bcolors.OKBLUE +"You woke up in forest and there are a lot of strange zombies talking!!"+ bcolors.ENDC)
        print(bcolors.OKBLUE +"So you walk toward them, slowly to hear them,but whene you are close enough ️you see that on of them is looking at you."+ bcolors.ENDC)
        print(bcolors.OKBLUE +"he walk's up to you and hit you."+ bcolors.ENDC)
        print(bcolors.OKBLUE +"you wake up in cave surround with zombies, and they ask you, you either die or help us it's up to you ? "+ bcolors.ENDC)
        start10 = input(bcolors.UNDERLINE + bcolors.HEADER +"Die or Fight ?"+ bcolors.ENDC)
        if start10 == "Fight" or start10 == "fight" or start10 == "f" or start10 == "F":
            print(bcolors.OKBLUE +"Good choice,"+ bcolors.ENDC)
            print(bcolors.OKBLUE +"""Now u are going with them to the fight,
in ur way to the fight they askd u about ur weapon to uese,
knife , bat, stick, hand combat.
1: knife : low damge but fast attacks and fast movement speed medium defence.
2: bat : high damge medium attack speed medium movement speed medium defence.
3: stick : you throw stick high range fast attack speed low defence.
4: hand combat : bruce lee attack speed medium damge high defence  """+ bcolors.ENDC)
            start11 = input(bcolors.UNDERLINE + bcolors.HEADER + """1: Sword and shield
1: knife
2: bat
3: stick
4: hand combat
Wat do u choose? type the weapon name : """ + bcolors.ENDC)
            if start11 == "1" or start11 == "knife":
                print(bcolors.OKBLUE + "You select the knife"+ bcolors.ENDC)
            elif start11 == "2" or start11 == "bat":
                print(bcolors.OKBLUE +"You select bat"+ bcolors.ENDC)
            elif start11 == "3" or start11 == "stick":
                print(bcolors.OKBLUE +"You select stick"+ bcolors.ENDC)
            elif start11 == "4" or start11 == "hand combat":
                print(bcolors.OKBLUE +"You select hand combat"+ bcolors.ENDC)
            print(bcolors.OKBLUE +"""you got your weapon and u going to the battlefield,in ur way you see the humans, at same time u arrived to the field,            
they tell you that you are frre and you can fight with them, the Human make the first move and they are fighting now,"""+bcolors.ENDC)
            start12 = input(bcolors.UNDERLINE + bcolors.HEADER +"So do u wanna go back and save the human or u will stay and fight with ur "+start11+"? stay/back" + bcolors.ENDC)
            if start12 == "stay" or start12 == "Stay" or start12 == "s":
                print(bcolors.OKBLUE +"You have a hard time fighting because they do not have team work and the human team have it so u and ur group back of and lost the fight. {Game over}  "+ bcolors.ENDC)
            elif start12 == "Back" or start12 == "go back" or start12 == "b" or start12 == "back":
                print(bcolors.OKBLUE +"when you see that ur group have no team work u did the right thing and go for the flank and win the fight for you team { Congratulation }"+ bcolors.ENDC)
        elif start10 == "Die" or start10 == "die" or start10 == "D" or start10 == "d":
            print(bcolors.OKCYAN +"they kild u {Game over}"+ bcolors.ENDC)
else:   
    print(bcolors.OKCYAN + "well it's up to " + name + " you see you later " + bcolors.ENDC)








