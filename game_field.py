from tkinter import *
from functools import partial
from game_manager import GameManager

class GameField:

    def __init__(self, root):
        self.root = root
        self.bg = PhotoImage(file='assets/Tic-tac-toe.png')
        self.circle = PhotoImage(file='assets/circle.png')
        self.x_img = PhotoImage(file='assets/x.png')
        self.empty = PhotoImage(file='assets/empty.png')
        self.init_game_field()
        self.init_game_manager()


    def init_game_manager(self):
        self.game_manager = GameManager()
    def init_game_field(self):
        self.canvas = Canvas(self.root, width=600, height=600)
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.bg, anchor='nw')
        self.buttons = [[], [], []]
        for c in range(3):
            for r in range(3):
                button = Button(image=self.empty, bd=0, highlightthickness=0, command=partial(self.hande_click, (c, r)))
                button.config(pady=50, padx=30)
                x = 50 + (200 * c)
                y = 50 + (200 * r)
                self.canvas.create_window(x, y, anchor='nw', window=button)
                self.buttons[c].append(button)


    def hande_click(self, pos):
        res = self.game_manager.make_turn(pos)
        if not res == "USED CELL":
            image_to_change = self.circle if self.game_manager.turn else self.x_img
            self.buttons[pos[0]][pos[1]].configure(image=image_to_change)
            if self.game_manager.over:
                self.canvas.destroy()
                self.winner_title = Label(text=f"Winner: {self.game_manager.winner}")
                self.winner_title.pack()
                self.should_restart()


    def should_restart(self):
        self.restart_btn = Button(text="restart", command=self.restart)
        self.restart_btn.pack()

    def restart(self):
        self.init_game_manager()
        self.init_game_field()
        self.restart_btn.destroy()
        self.winner_title.destroy()
