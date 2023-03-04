from tkinter import *
from PIL import ImageTk, Image 
import appWindowSetting, music,WelcomeGUI, GameGUI



def Result(userchoice,computerchoice,result):
    GameGUI.GameTop.withdraw() #getting rid of the game options
    global ResultTop,ResultTopBackground

    #creating the result window and defining size 
    ResultTop= Toplevel()
    result_width=500
    result_height=500
    appWindowSetting.GUI_setting(ResultTop,result_width,result_height)

    #creating the canvas 
    ResultTop_canvas = Canvas(ResultTop,width=result_width, height=result_height, bd=0,highlightthickness=0)
    ResultTop_canvas.pack(fill='both', expand=True)


    if result =="win":
        music.WinMusic()
        ResultTopBackground = ImageTk.PhotoImage(Image.open("imgg/win.gif"))
    elif result =="lose":
        music.LoseMusic()
        ResultTopBackground = ImageTk.PhotoImage(Image.open("imgg/lose.gif"))
    else:
        music.TieMusic()    
        ResultTopBackground = ImageTk.PhotoImage(Image.open("imgg/draw.gif"))    

    #result GUI background image
    ResultTop_canvas.create_image(0,0,image= ResultTopBackground ,anchor="nw") 


    newrountdButton = Button(ResultTop_canvas,text="New game",command= NewRound)
    ResultTop_canvas.create_window(250,465,anchor="nw",window=newrountdButton, width=100)

    button_quit = Button(ResultTop_canvas,text="Exit game",command= WelcomeGUI.root.quit)
    ResultTop_canvas.create_window(375,465,anchor="nw",window=button_quit, width=100)
   
    ResultTop_canvas.create_text(200,30 , text="Computer has chosen: "+ computerchoice +"\nYou have chosen: " + userchoice, font = ("Helvetica",20), fill="red")


def NewRound():
    if WelcomeGUI.play==True:
        music.playmusic()
    ResultTop.destroy()
    GameGUI.GameTop.deiconify()

 
   