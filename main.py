from tkinter import *
from game_field import GameField
root = Tk(sync=True)
root.config(width=600, height=600)
root.geometry('600x600')
root.title("Tic tac toe")

game_field = None

def play_button():
    global game_field
    game_field = GameField(root)
    play.destroy()

play = Button(text="Play", command=play_button, font=("Arial", 48), borderwidth=0, highlightthickness=0, highlightcolor='#FFFFFF', highlightbackground='#ffffff')
play.pack()

root.mainloop()