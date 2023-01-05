
import tkinter as tk
import random




count = 0

class MainScreens():
    def __init__(self):
        self.rootgeo = "700x650"
        self.root = tk.Tk()
        self.root.geometry(self.rootgeo)
        self.count = 1
        self.ppoints = 0
        self.aipoints = 0


    #Choices
    def playerChoiceOne(self):
        self.playerChoice = 1
        self.aidecision = random.randint(1,3)
        self.check()

    def playerChoiceTwo(self):
        self.playerChoice = 2
        self.aidecision = random.randint(1,3)
        self.check()

    def playerChoiceThree(self):
        self.playerChoice = 3
        self.aidecision = random.randint(1,3)
        self.check()

    #Choices
    
    def first_screen(self):
        self.WelcomeTxt =tk.Label(self.root, text = "Rock, Paper, Scissors Remake!", font = ("Arial", 18))
        self.WelcomeTxt.pack()

        self.ConfText= tk.Label(self.root, text="Please Enter Your Name Below: ", font=('Arial', 13))
        self.ConfText.place(x=250, y=70)

        self.nameEntry = tk.Entry()
        self.nameEntry.place(x=300,y=100)

        self.ConfText2 = tk.Label(self.root, text="Please Enter How Many Times You Want to Play:", font=("Arial", 13))
        self.ConfText2.place(x=200, y=170)

        self.playTimeEntry = tk.Entry()
        self.playTimeEntry.place(x=300, y=200)
        
        self.subButton = tk.Button(self.root, text="Submit", font=('Arial', 13),command =lambda : self.getName())
        self.subButton.place(x=330, y=250)
        self.root.mainloop()
    
    def second_screen(self):
        #Buttons
        rockButton = tk.Button(self.root, text="Rock", height=5, width=10,font=('Arial', 13),command = lambda : self.playerChoiceOne())
        paperButton = tk.Button(self.root, text="Paper",height=5, width=10, font=('Arial', 13),command = lambda : self.playerChoiceTwo())
        scissorButton = tk.Button(self.root, text="Scissors",height=5, width=10, font=('Arial', 13), command = lambda : self.playerChoiceThree())
        #Placing the Buttons
        rockButton.place(x=10, y=499)
        paperButton.place(x=300, y=499)
        scissorButton.place(x=599, y=499)
        #Points
        self.pointsTable = tk.Label(self.root, text=f'{self.name} : {self.ppoints}, AI : {self.aipoints}', font=("Arial", 15))
        self.pointsTable.pack()

    def EmptyPointsBox(self):
        self.pointsTable.config(text=" ")
        
    def check(self):

            
            
            if self.aidecision == 1  and self.playerChoice == 2:
                if self.count == self.playingTimes:
                    if self.ppoints < self.aipoints:
                        self.pointsTable.config(text="AI WON!")
                    elif self.aipoints < self.ppoints:
                        self.pointsTable.config(text=f"{self.name} WON!")
                    elif self.aipoints == self.ppoints:
                        self.pointsTable.config(text="TIE")
                else:
                    self.ppoints += 1
                    self.pointsTable.config(text=f'{self.name} : {self.ppoints}, AI : {self.aipoints}')
                    
                    self.count+=1
                

            if self.aidecision == 1 and self.playerChoice == 1:
                
                if self.count == self.playingTimes:
                    if self.ppoints < self.aipoints:
                        self.pointsTable.config(text="AI WON!")
                    elif self.aipoints < self.ppoints:
                        self.pointsTable.config(text=f"{self.name} WON!")
                    elif self.aipoints == self.ppoints:
                        self.pointsTable.config(text="TIE")
                else:
                    self.pointsTable.config(text=f'{self.name} : {self.ppoints}, AI : {self.aipoints}')
                    self.count+=1

            if self.aidecision == 1 and self.playerChoice == 3:
                
                if self.count == self.playingTimes:
                    if self.ppoints < self.aipoints:
                        self.pointsTable.config(text="AI WON!")
                    elif self.aipoints < self.ppoints:
                        self.pointsTable.config(text=f"{self.name} WON!")
                    elif self.aipoints == self.ppoints:
                        self.pointsTable.config(text="TIE")
                else:
                    self.aipoints += 1
                    self.pointsTable.config(text=f'{self.name} : {self.ppoints}, AI : {self.aipoints}')
                    
                    self.count+=1
            
                
            if self.aidecision == 2 and self.playerChoice == 2:
                
                if self.count == self.playingTimes:
                    if self.ppoints < self.aipoints:
                        self.pointsTable.config(text="AI WON!")
                    elif self.aipoints < self.ppoints:
                        self.pointsTable.config(text=f"{self.name} WON!")
                    elif self.aipoints == self.ppoints:
                        self.pointsTable.config(text="TIE")
                else:
                    self.pointsTable.config(text=f'{self.name} : {self.ppoints}, AI : {self.aipoints}')
                    self.count+=1
            
            if self.aidecision == 2 and self.playerChoice == 1:
                if self.count == self.playingTimes:
                    if self.ppoints < self.aipoints:
                        self.pointsTable.config(text="AI WON!")
                    elif self.aipoints < self.ppoints:
                        self.pointsTable.config(text=f"{self.name} WON!")
                    elif self.aipoints == self.ppoints:
                        self.pointsTable.config(text="TIE")
                else:
                    self.ppoints += 1
                    self.pointsTable.config(text=f'{self.name} : {self.ppoints}, AI : {self.aipoints}')
                    
                    self.count+=1
                    
                    
                
            
            if self.aidecision == 2  and self.playerChoice == 3:
               
                if self.count == self.playingTimes:
                    if self.ppoints < self.aipoints:
                        self.pointsTable.config(text="AI WON!")
                    elif self.aipoints < self.ppoints:
                        self.pointsTable.config(text=f"{self.name} WON!")
                    elif self.aipoints == self.ppoints:
                        self.pointsTable.config(text="TIE")
                else:
                    self.ppoints += 1
                    self.pointsTable.config(text=f'{self.name} : {self.ppoints}, AI : {self.aipoints}')
                    
                    self.count+=1
                    
                    
                
            
            if self.aidecision == 3 and self.playerChoice == 1:              
                if self.count == self.playingTimes:
                    if self.ppoints < self.aipoints:
                        self.pointsTable.config(text="AI WON!")
                    elif self.aipoints < self.ppoints:
                        self.pointsTable.config(text=f"{self.name} WON!")
                    elif self.aipoints == self.ppoints:
                        self.pointsTable.config(text="TIE")
                else:
                    self.ppoints += 1
                    self.pointsTable.config(text=f'{self.name} : {self.ppoints}, AI : {self.aipoints}')
                    
                    self.count+=1
                    
                    
                

            
            if self.aidecision == 3 and self.playerChoice == 2:
                if self.count == self.playingTimes:
                    if self.ppoints < self.aipoints:
                        self.pointsTable.config(text="AI WON!")
                    elif self.aipoints < self.ppoints:
                        self.pointsTable.config(text=f"{self.name} WON!")
                    elif self.aipoints == self.ppoints:
                        self.pointsTable.config(text="TIE")
                else:
                    self.aipoints += 1
                    self.pointsTable.config(text=f'{self.name} : {self.ppoints}, AI : {self.aipoints}')
                    
                    self.count+=1
                    
                    
                
            
            if self.aidecision == 3 and self.playerChoice == 3:

                if self.count == self.playingTimes:
                    if self.ppoints < self.aipoints:
                        self.pointsTable.config(text="AI WON!")
                    elif self.aipoints < self.ppoints:
                        self.pointsTable.config(text=f"{self.name} WON!")
                    elif self.aipoints == self.ppoints:
                        self.pointsTable.config(text="TIE")
                else:
                    self.pointsTable.config(text=f'{self.name} : {self.ppoints}, AI : {self.aipoints}')
                    self.count+=1
                

    def getName(self):
        self.name = self.nameEntry.get()
        self.playingTimes = int(self.playTimeEntry.get())
        self.WelcomeTxt.destroy()
        self.ConfText.destroy()
        self.ConfText2.destroy()
        self.playTimeEntry.destroy()
        self.nameEntry.destroy()
        self.subButton.destroy()
        self.second_screen()
        print(self.name)
        print(self.playingTimes)
        
    


    




loginScrenn = MainScreens()

loginScrenn.first_screen()