from cgitb import text
from faulthandler import disable
from platform import java_ver
from random import *
from tkinter import *
from venv import create
from PIL import ImageTk, Image 
from functools import partial
import pygame

global userchoice
play=True 

def playmusic():
    pygame.mixer.init()
    pygame.mixer.music.load("audio\music.mp3")
    pygame.mixer.music.play(loops=100)

playmusic()

root = Tk()
root.title('Rock Paper Scissors Game')
root.iconbitmap('imgg\icon.ico')

global root_width,root_height,x,y
root_width=1027
root_height=637
screen_width= root.winfo_screenwidth()
screen_height= root.winfo_screenheight()
x=(screen_width/2)-(root_width/2)
y=(screen_height/2)-(root_height/2)
root.geometry(f'{root_width}x{root_height}+{int(x)}+{int(y)}')
root.resizable(width=False,height=False)

#background image of the root 
root_bg = ImageTk.PhotoImage(Image.open("imgg/root_bg.gif")) 

#creating canvas
RootCanvas = Canvas(root,width=root_width, height=root_height, bd=0,highlightthickness=0)
RootCanvas.pack(fill='both', expand=True)
RootCanvas.create_image(0,0,image=root_bg,anchor="nw")
 



def musicToggle():
    global play
    if play==True:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    play = ~ play


def MainMenu(UserNameField):
    root.deiconify()
    RulesTop.withdraw()
    UserNameField.delete(0, 'end')
    


def greetingUser(UserNameField):
    root.withdraw()
    global RulesTop, greetingBackground, img_rules
    RulesTop = Toplevel()    
    RulesTop.resizable(width=False,height=False)
    RulesTop.geometry(f'{root_width}x{root_height}+{int(x)}+{int(y)}')
    RulesTop.title('Rock Paper Scissors Game')
    RulesTop.iconbitmap('imgg\icon.ico')

 
    greetingBackground = ImageTk.PhotoImage(Image.open("imgg/greeting.gif")) 
    RulesTopCanvas = Canvas(RulesTop,width=root_width, height=root_height, bd=0,highlightthickness=0)
    RulesTopCanvas.pack(fill='both', expand=True)
    RulesTopCanvas.create_image(0,0,image= greetingBackground ,anchor="nw") 


    GreetingUser = "Hello " + UserNameField.get() + "!"
    GameRules = "\nThe rules of the game are simple, you will compete against the computer.\nWhen the game starts, click on an item of your choice,\nThe computer picks randomly each round. \n \n Rules are simple:\n Rock crushes scissors, \n paper covers rock,\n and scissors cut paper."

    RulesTopCanvas.create_text(0,150 , text=GreetingUser+GameRules , font = ("Helvetica",18), fill="black",justify="left",anchor="nw")
 
    img_rules = ImageTk.PhotoImage(Image.open("imgg/img_rules.gif").resize((280, 280), Image.ANTIALIAS)) 
    RulesTopCanvas.create_image(700,210, anchor=NW, image=img_rules)     
   



    startgameButton=Button(RulesTopCanvas,text="Start game",font=("Helvetica",16), width = 15, height=5, fg="red",bd=0, command= StartGame)
    #make this into a window, and add the window into the canvas 
    mybutton_window = RulesTopCanvas.create_window(400,275,anchor="nw",window=startgameButton)

    musicButton = Button(RulesTopCanvas,text=" Music",command=musicToggle)
    musicButton_window = RulesTopCanvas.create_window(775,605,anchor="nw",window=musicButton, width=100)

    button_quit = Button(RulesTopCanvas,text="Start menu",command= partial(MainMenu, UserNameField) )
    mybutton_window = RulesTopCanvas.create_window(650,605,anchor="nw",window=button_quit, width=100)

    button_quit = Button(RulesTopCanvas,text=" exit game",command= RulesTop.quit)
    mybutton_window = RulesTopCanvas.create_window(900,605,anchor="nw",window=button_quit, width=100)

RootCanvas.create_text(520,350 , text="Welcome!", font = ("Helvetica",50), fill="white")
RootCanvas.create_text(605,520 , text="Please Enter your name to start the game!", font = ("Helvetica",20), fill="white")


#UserNameField
    #define field
UserNameField=Entry(root, font=("Helvetica",24), width=10, fg="#0000FF",bd=0)
    #add entry box to canvas: 1- create window, 2- put widget in window, 3- put window in canvas
UserNameWindow = RootCanvas.create_window(350,550,anchor="nw",window=UserNameField)

# add button
EnterNameButton=Button(root,text="Enter Name",font=("Helvetica",16), width = 10, fg="red",bd=0, command= partial(greetingUser, UserNameField))
#make this into a window, and add the window into the canvas 
EnterNameButton_window = RootCanvas.create_window(550,550,anchor="nw",window=EnterNameButton)

buttonQuit = Button(root,text=" exit game",command= root.quit)
buttonQuit_window = RootCanvas.create_window(900,600,anchor="nw",window=buttonQuit, width=100)

musicButton = Button(RootCanvas,text=" Music",command=musicToggle)
musicButton_window = RootCanvas.create_window(750,600,anchor="nw",window=musicButton, width=100)


    
 
def NewRound():
    ResultTop.destroy()
    playmusic()
    paper_button['state'] = NORMAL
    rock_button['state'] = NORMAL
    scissors_button['state'] = NORMAL



def YouWin(userchoice):
    global ResultTop,ResultTopBackground
    ResultTop= Toplevel()
    ResultTop.resizable(width=False,height=False)

    ResultTop.title('Rock Paper Scissors Game')
    ResultTop.iconbitmap('imgg\icon.ico')
    x=(screen_width/2)-(500/2)
    y=(screen_height/2)-(500/2)

    ResultTop.geometry(f'{500}x{500}+{int(x)}+{int(y)}')

    ResultTopBackground = ImageTk.PhotoImage(Image.open("imgg/win.gif")) 
    ResultTop_canvas = Canvas(ResultTop,width=500, height=500, bd=0,highlightthickness=0)
    ResultTop_canvas.pack(fill='both', expand=True)
    ResultTop_canvas.create_image(0,0,image= ResultTopBackground ,anchor="nw") 

    ResultTop_canvas.create_text(200,30 , text="computer has chosen: "+computerchoice +"\nuser has chosen: "+userchoice  , font = ("Helvetica",20), fill="white")

    pygame.mixer.music.load("audio/win.mp3")
    pygame.mixer.music.play(loops=1)



    newrountdButton = Button(ResultTop_canvas,text="New game",command= NewRound)
    newrountdButton_window = ResultTop_canvas.create_window(250,465,anchor="nw",window=newrountdButton, width=100)

    button_quit = Button(ResultTop_canvas,text="Exit game",command= root.quit)
    mybutton_window = ResultTop_canvas.create_window(375,465,anchor="nw",window=button_quit, width=100)


def YouLost(userchoice):
    global ResultTop,ResultTopBackground
    ResultTop= Toplevel()
    ResultTop.resizable(width=False,height=False)

    ResultTop.title('Rock Paper Scissors Game')
    ResultTop.iconbitmap('imgg\icon.ico')
    x=(screen_width/2)-(500/2)
    y=(screen_height/2)-(500/2)

    ResultTop.geometry(f'{500}x{500}+{int(x)}+{int(y)}')

    ResultTopBackground = ImageTk.PhotoImage(Image.open("imgg/lose.gif")) 
    ResultTop_canvas = Canvas(ResultTop,width=500, height=500, bd=0,highlightthickness=0)
    ResultTop_canvas.pack(fill='both', expand=True)
    ResultTop_canvas.create_image(0,0,image= ResultTopBackground ,anchor="nw") 

    ResultTop_canvas.create_text(200,30 , text="computer has chosen: "+computerchoice +"\nuser has chosen: "+userchoice  , font = ("Helvetica",20), fill="red")

    pygame.mixer.music.load("audio/lose.mp3")
    pygame.mixer.music.play(loops=1)



    newrountdButton = Button(ResultTop_canvas,text="New game",command= NewRound)
    newrountdButton_window = ResultTop_canvas.create_window(250,465,anchor="nw",window=newrountdButton, width=100)

    button_quit = Button(ResultTop_canvas,text="Exit game",command= root.quit)
    mybutton_window = ResultTop_canvas.create_window(375,465,anchor="nw",window=button_quit, width=100)


def Tie(userchoice):
    global ResultTop,ResultTopBackground
    ResultTop= Toplevel()
    ResultTop.resizable(width=False,height=False)

    ResultTop.title('Rock Paper Scissors Game')
    ResultTop.iconbitmap('imgg\icon.ico')
    x=(screen_width/2)-(500/2)
    y=(screen_height/2)-(500/2)

    ResultTop.geometry(f'{500}x{500}+{int(x)}+{int(y)}')

    ResultTopBackground = ImageTk.PhotoImage(Image.open("imgg/draw.gif")) 
    ResultTop_canvas = Canvas(ResultTop,width=500, height=500, bd=0,highlightthickness=0)
    ResultTop_canvas.pack(fill='both', expand=True)
    ResultTop_canvas.create_image(0,0,image= ResultTopBackground ,anchor="nw") 

    ResultTop_canvas.create_text(200,30 ,text="computer has chosen: "+computerchoice +"\nuser has chosen: "+userchoice  , font = ("Helvetica",20), fill="red")

    pygame.mixer.music.load("audio/draw.mp3")
    pygame.mixer.music.play(loops=1)



    newrountdButton = Button(ResultTop_canvas,text="New game",command= NewRound)
    newrountdButton_window = ResultTop_canvas.create_window(250,465,anchor="nw",window=newrountdButton, width=100)

    button_quit = Button(ResultTop_canvas,text="Exit game",command= root.quit)
    mybutton_window = ResultTop_canvas.create_window(375,465,anchor="nw",window=button_quit, width=100)

    
    

def gamerules(userchoice):

    global  ResultTop,ResultTopBackground, computerchoice

    computerOptions = ["rock", "paper", "scissors"]
    computerchoice = computerOptions[randint(0,2)] 

    if userchoice == computerchoice:
        Tie(userchoice) 
    elif userchoice == "rock":
        if computerchoice == "paper":
            YouLost(userchoice)  
        else:
            YouWin(userchoice)  
    elif userchoice == "paper":
        if computerchoice == "scissors":
            YouLost(userchoice)       
        else:
            YouWin(userchoice)        
    elif userchoice == "scissors":
        if computerchoice == "rock":
            YouLost(userchoice)    
        else:
            YouWin(userchoice) 

    paper_button['state'] = DISABLED
    rock_button['state'] = DISABLED
    scissors_button['state'] = DISABLED

def BacktoRules():   
    GameTop.destroy()
    greetingUser(UserNameField)

def StartGame():
    global GameTop,paper_img,rock_img, scissors_img, paper_button,rock_button,scissors_button,GameTopBackground,BacktoRuleButton 

    RulesTop.destroy()
    GameTop = Toplevel()
    GameTop.resizable(width=False,height=False)

    GameTop.title('Rock Paper Scissors Game')
    GameTop.iconbitmap('imgg\icon.ico')
    GameTop.geometry(f'{root_width}x{root_height}+{int(x)}+{int(y)}')

    GameTopBackground = ImageTk.PhotoImage(Image.open("imgg/gamebg.gif")) 
    GameTop_canvas = Canvas(GameTop,width=root_width, height=root_height, bd=0,highlightthickness=0)
    GameTop_canvas.pack(fill='both', expand=True)
    GameTop_canvas.create_image(0,0,image= GameTopBackground ,anchor="nw") 


    rock_img = ImageTk.PhotoImage(Image.open("imgg\scissors2.gif").resize((100, 100), Image.ANTIALIAS))
    rock_button = Button(GameTop_canvas,image = rock_img,command=partial(gamerules, "rock"))
    rock_button_window = GameTop_canvas.create_window(350,450,anchor="nw",window=rock_button, width=100)


    paper_img = ImageTk.PhotoImage(Image.open("imgg\paper.gif").resize((100, 100), Image.ANTIALIAS))
    paper_button = Button(GameTop_canvas,image = paper_img,command=partial(gamerules, "paper"))
    paper_button_window = GameTop_canvas.create_window(500,450,anchor="nw",window=paper_button, width=100)

    scissors_img = ImageTk.PhotoImage(Image.open("imgg\scissors.gif").resize((100, 100), Image.ANTIALIAS))
    scissors_button = Button( GameTop_canvas,image = scissors_img,command=partial(gamerules, "scissors"))
    scissors_button_window = GameTop_canvas.create_window(650,450,anchor="nw",window=scissors_button, width=100)

    buttonQuit = Button(GameTop_canvas,text=" exit game",command= root.quit)
    buttonQuit_window = GameTop_canvas.create_window(900,600,anchor="nw",window=buttonQuit, width=100)

    musicButton = Button(GameTop_canvas,text=" Music",command=musicToggle)
    musicButton_window = GameTop_canvas.create_window(750,600,anchor="nw",window=musicButton, width=100)

    BacktoRuleButton = Button(GameTop_canvas,text="go Back to Rules pages",command=BacktoRules)
    BacktoRules_window = GameTop_canvas.create_window(550,600,anchor="nw",window=BacktoRuleButton, width=150)
 
root.mainloop()