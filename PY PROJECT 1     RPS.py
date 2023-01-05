import math
import time
import random
#Rock paper scissors

#variables
ppoints = 0
aipoints = 0
#variables
print("Welcome to Rock Paper Scissors!")

playingtime = input("Please Enter How Many Times You Want To Play: ")
name = input("Whats your name: ")


#main program
for i in range(int(playingtime)):
    def inp():
        global decision  
        decision = input("Please choose between rock or paper or scissors: ")  
        dec()
        global aidecision
        aidecision = random.randint(1,6)
    
    def dec():
        if decision == "rock" or decision == "paper" or decision == "scissors":
            pass
        else:
            print("wrong choice")
            inp()
    inp()

    

    if aidecision == 1 or aidecision == 4 and decision == "paper":
        print(name + " won!")
        ppoints += 1

    elif aidecision == 1 or aidecision == 4 and decision == "rock":
        print("tie")

    elif aidecision == 1 or aidecision == 4 and decision == "scissors":
        print("AI won!")
    
        aipoints += 1
    elif aidecision == 2 or aidecision == 5 and decision == "paper":
        print("tie")
    
    elif aidecision == 2 or aidecision == 5 and decision == "rock":
        print("AI won")
        aipoints += 1
    
    elif aidecision == 2 or aidecision == 5 and decision == "scissors":
        print(name + " won")
        ppoints += 1
    
    elif aidecision == 3 or aidecision == 6 and decision == "rock":
        print(name + " won")
        ppoints += 1
    
    elif aidecision == 3 or aidecision == 6 and decision == "paper":
        print("AI won")
        aipoints += 1
    
    elif aidecision == 3 or aidecision == 6 and decision == "scissors":
        print("tie")
#main program


#ending
if ppoints > aipoints:
    print(name + " won the round!")
    
else:
    print("ai won the round!")
#ending
    

#restarting
rest = input("Do you want to restart? yes or no: ")

if rest == "yes":
    print("Run the code again to restart")

