from functools import partial
from tkinter import *
from PIL import ImageTk, Image 
import appWindowSetting,GameRules,music,WelcomeGUI,GreetingUserGUI

#GUI function for the game window

def StartGame(RulesTop):
    #define the buttons and images as global variable to be visible on the canvas. 
    global GameTop,paper_img,rock_img, scissors_img, paper_button,rock_button,scissors_button,GameTopBackground,BacktoRuleButton 

    RulesTop.withdraw()  #getting rid of the old window  (greetingGUI window ) 
    #defining the canvas 

    GameTop = Toplevel()
    app_width=1027
    app_height=637
    GameTopBackground = ImageTk.PhotoImage(Image.open("imgg/gamebg.gif"))
    appWindowSetting.GUI_setting(GameTop,app_width,app_height)

    GameTop_canvas = Canvas(GameTop,width=app_width, height=app_height, bd=0,highlightthickness=0)
    GameTop_canvas.pack(fill='both', expand=True)
    GameTop_canvas.create_image(0,0,image= GameTopBackground ,anchor="nw") 



#adding the images of rock paper scissors as buttons
    rock_img = ImageTk.PhotoImage(Image.open("imgg\\rock.gif").resize((100, 100), Image.ANTIALIAS))
    rock_button = Button(GameTop_canvas,image = rock_img,command=partial(GameRules.gamerules, "rock"))
    GameTop_canvas.create_window(350,450,anchor="nw",window=rock_button, width=100)

    paper_img = ImageTk.PhotoImage(Image.open("imgg\paper.gif").resize((100, 100), Image.ANTIALIAS))
    paper_button = Button(GameTop_canvas,image = paper_img,command=partial(GameRules.gamerules, "paper"))
    GameTop_canvas.create_window(500,450,anchor="nw",window=paper_button, width=100)

    scissors_img = ImageTk.PhotoImage(Image.open("imgg\scissors.gif").resize((100, 100), Image.ANTIALIAS))
    scissors_button = Button( GameTop_canvas,image = scissors_img,command=partial(GameRules.gamerules, "scissors"))
    GameTop_canvas.create_window(650,450,anchor="nw",window=scissors_button, width=100)

    buttonQuit = Button(GameTop_canvas,text="Exit game",command= WelcomeGUI.root.quit)
    GameTop_canvas.create_window(900,600,anchor="nw",window=buttonQuit, width=100)

    musicButton = Button(GameTop_canvas,text="Music",command= music.musicToggle)
    GameTop_canvas.create_window(750,600,anchor="nw",window=musicButton, width=100)

    BacktoRuleButton = Button(GameTop_canvas,text="Go Back to Rules pages",command=BacktoRules)
    GameTop_canvas.create_window(550,600,anchor="nw",window=BacktoRuleButton, width=150)
 
#button to go back to the previous GUI (rules GUI)
def BacktoRules():   
    GameTop.destroy()
    GreetingUserGUI.greetingUser(WelcomeGUI.UserNameField)

