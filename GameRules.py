from random import *
import ResultGUI

def gamerules(userchoice):
    computerOptions = ["rock", "paper", "scissors"]
    computerchoice = computerOptions[randint(0,2)] 

    if userchoice == computerchoice:
       ResultGUI.Result(userchoice,computerchoice,"tie") 
    elif userchoice == "rock":
        if computerchoice == "paper":
            ResultGUI.Result(userchoice,computerchoice,"lose")  
        else:
            ResultGUI.Result(userchoice,computerchoice,"win")  
    elif userchoice == "paper":
        if computerchoice == "scissors":
            ResultGUI.Result(userchoice,computerchoice,"lose")       
        else:
            ResultGUI.Result(userchoice,computerchoice,"win")        
    elif userchoice == "scissors":
        if computerchoice == "rock":
            ResultGUI.Result(userchoice,computerchoice,"lose")    
        else:
            ResultGUI.Result(userchoice,computerchoice,"win") 

