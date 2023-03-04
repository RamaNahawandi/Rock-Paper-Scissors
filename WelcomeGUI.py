from tkinter import *
from PIL import ImageTk, Image 
from functools import partial
import  appWindowSetting,music

#call the music function to run through the whole program background. 
play=True
music.playmusic()


#defining the application main window width/height settings and other config
root = Tk()
app_width=1027
app_height=637

RootbackgroundImg= ImageTk.PhotoImage(Image.open("imgg/root_bg.gif")) 
appWindowSetting.GUI_setting(root,app_width,app_height)

#creating the canvas of the welcomeGUI window 
RootCanvas = Canvas(root,width=app_width, height=app_height, bd=0,highlightthickness=0)
RootCanvas.pack(fill='both', expand=True)
RootCanvas.create_image(0,0,image=RootbackgroundImg,anchor="nw")

#Greeting users in the canvas
RootCanvas.create_text(520,350 , text="Welcome!", font = ("Helvetica",50), fill="white")
RootCanvas.create_text(605,520 , text="Please Enter your name to start the game!", font = ("Helvetica",20), fill="white")
    
#creating the "Enter Name" entry field and button to navigate to the GreetinGUI 
UserNameField=Entry(root, font=("Helvetica",24), width=10, fg="#0000FF",bd=0)
RootCanvas.create_window(350,550,anchor="nw",window=UserNameField)

#imported here and not at the top to solve the  mutual/circular (cyclic) imports since 2 modules are calling eachothers
import GreetingUserGUI
EnterNameButton=Button(root,text="Enter Name",font=("Helvetica",16), width = 10, fg="red",bd=0, command= partial(GreetingUserGUI.greetingUser, UserNameField))
RootCanvas.create_window(550,550,anchor="nw",window=EnterNameButton)

buttonQuit = Button(root,text="Exit game",command= root.quit)
RootCanvas.create_window(900,600,anchor="nw",window=buttonQuit, width=100)

musicButton = Button(RootCanvas,text="Music",command=music.musicToggle)
RootCanvas.create_window(750,600,anchor="nw",window=musicButton, width=100)