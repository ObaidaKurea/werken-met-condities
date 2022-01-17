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


name = input(bcolors.UNDERLINE+ bcolors.HEADER + "what is your name? " + bcolors.ENDC)
print (bcolors.OKCYAN + "hey " + (name) + """ have you heard about the new game called lost
its about you the main charcter (you) and a ghost who will hunt you down its a horro/puzzle game you need 2 solve the mystrie 
to win with out the ghost seeing you you cant see the ghost but you can see his shadow"""+ bcolors.ENDC)

start = input(bcolors.UNDERLINE + bcolors.HEADER +"do you wanna start? yes/no : " + bcolors.ENDC)
if start == "yes" or start == "y":
    print(bcolors.OKCYAN +"great trun your lights off and let the fun begin")

nickname= input (bcolors.OKCYAN + "enter your name : "+bcolors.ENDC )
print(bcolors.OKCYAN + "Hello " + nickname + " welcome to Lost")
start2= input(bcolors.OKCYAN + " choose your sex man or woman? "+ bcolors.ENDC)
if start2== "man" or start2== "man" or start2== "woman" or start2== "Woman" :
    print(bcolors.OKBLUE + "(Welcome to lvl 1 of lost) " + nickname + """", you are infront of a abandoned house and behind you there is a jungle. 
    do you wanna walk into the house or the jungle""")

start4= input(bcolors.UNDERLINE + bcolors.OKBLUE +""" 1. the jungle
2. the house?
what do you wanna choose? type the area name : """  +bcolors.ENDC) 

if start4== "the jungle" :
    print(bcolors.UNDERLINE + " you choose the jungle "+ bcolors.ENDC)
elif start4== 'the house' :
    print (bcolors.OKBLUE + " you choose the house")

