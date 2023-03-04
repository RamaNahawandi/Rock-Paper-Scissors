import pygame,WelcomeGUI

def playmusic():
    pygame.mixer.init()
    pygame.mixer.music.load("audio\music.mp3")
    pygame.mixer.music.play(loops=100)

def musicToggle():

    if WelcomeGUI.play==True:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    WelcomeGUI.play = ~ WelcomeGUI.play

def WinMusic():
    if WelcomeGUI.play==True:
        pygame.mixer.music.load("audio/win.mp3")
        pygame.mixer.music.play(loops=1)


def LoseMusic():
    if WelcomeGUI.play==True:
        pygame.mixer.music.load("audio/lose.mp3")
        pygame.mixer.music.play(loops=1)

def TieMusic():
    if WelcomeGUI.play==True:
        pygame.mixer.music.load("audio/draw.mp3")
        pygame.mixer.music.play(loops=1)
        

