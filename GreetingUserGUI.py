from tkinter import *
from PIL import ImageTk, Image 
from functools import partial
import WelcomeGUI,GameGUI,music,appWindowSetting

#GUI function with all of the buttons and images visible 
def greetingUser(UserNameField):
    #these variables have to be global in order to be visible on canvas. 
    global RulesTop, GreetingbackgroundImg, img_rules
    WelcomeGUI.root.withdraw() #getting rid of the old window  
    RulesTop = Toplevel()  #creating the rules window 
    
    app_width=1027
    app_height=637
    GreetingbackgroundImg= ImageTk.PhotoImage(Image.open("imgg/greeting.gif")) 
    appWindowSetting.GUI_setting(RulesTop,app_width,app_height)

    RulesTopCanvas = Canvas(RulesTop,width=app_width, height=app_height, bd=0,highlightthickness=0)
    RulesTopCanvas.pack(fill='both', expand=True)
    RulesTopCanvas.create_image(0,0,image= GreetingbackgroundImg ,anchor="nw") 

    GreetingUser = "Hello " + UserNameField.get() + "!"
    GameRules = "\nThe rules of the game are simple, you will compete against the computer.\nWhen the game starts, click on an item of your choice,\nThe computer picks randomly each round. \n \n Rules are simple:\n Rock crushes scissors, \n paper covers rock,\n and scissors cut paper."

    RulesTopCanvas.create_text(0,150 , text = GreetingUser + GameRules , font = ("Helvetica",18), fill="black",justify="left",anchor="nw")
 
    img_rules = ImageTk.PhotoImage(Image.open("imgg/img_rules.gif").resize((280, 280), Image.ANTIALIAS)) 
    RulesTopCanvas.create_image(700,210, anchor=NW, image=img_rules)     

    startgameButton=Button(RulesTopCanvas,text="Start game",font=("Helvetica",16), width = 15, height=5, fg="red",bd=0, command= partial(GameGUI.StartGame, RulesTop))
    RulesTopCanvas.create_window(400,275,anchor="nw",window=startgameButton)

    musicButton = Button(RulesTopCanvas,text=" Music",command= music.musicToggle)
    RulesTopCanvas.create_window(775,605,anchor="nw",window=musicButton, width=100)

    button_quit = Button(RulesTopCanvas,text="Start menu",command= partial(MainMenu, UserNameField) )
    RulesTopCanvas.create_window(650,605,anchor="nw",window=button_quit, width=100)

    button_quit = Button(RulesTopCanvas,text=" exit game",command= RulesTop.quit)
    RulesTopCanvas.create_window(900,605,anchor="nw",window=button_quit, width=100)


#button to go back to the previous GUI
def MainMenu(UserNameField):
    RulesTop.withdraw()
    WelcomeGUI.root.deiconify()
    UserNameField.delete(0, 'end')
