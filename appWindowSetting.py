
#settings for all of the window, regarding icons, title and width/height.
def GUI_setting(window,app_width,app_height):

    window.title('Rock Paper Scissors Game')
    window.iconbitmap('imgg\icon.ico')

    #getting the user's screen size
    screen_width= window.winfo_screenwidth()
    screen_height= window.winfo_screenheight()

    #getting the x and y coordinates to be able to position the window in the center of the screen 
    x=(screen_width/2)-(app_width/2)
    y=(screen_height/2)-(app_height/2)
    window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    window.resizable(width=False,height=False)

