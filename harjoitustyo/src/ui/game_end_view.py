from tkinter import ttk, constants
from services.snake_game import SnakeGame
from services.ui_logic import UILogic


class GameEndView:
    def __init__(self, root, ui_logic: UILogic, hide_ui, show_main_view, show_game_end_view, points=0):
        self.root = root
        self.ui_logic = ui_logic
        self.frame = None
        self.hide_ui = hide_ui
        self.show_main_view = show_main_view
        self.show_game_end_view = show_game_end_view

        self.points = points

        self.initialize()

    def pack(self):
        self.frame.pack()

    def destroy(self):
        self.frame.destroy()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        info_label = ttk.Label(
            master=self.frame, text="Peli päättyi " +
            self.ui_logic.player.name + ", pisteesi "
                                    + str(self.points) + "!")
        start_game_button = ttk.Button(
            master=self.frame,
            text="Aloita uusi peli",
            command=self.handle_start_game
        )
        back_button = ttk.Button(
            master=self.frame,
            text="Takaisin päävalikkoon",
            command=self.show_main_view
        )

        info_label.grid(row=0, column=0, sticky=constants.EW, padx=10, pady=10)
        start_game_button.grid(
            row=1, column=0, sticky=constants.EW, padx=10, pady=10)
        back_button.grid(row=3, column=0, sticky=constants.EW,
                         padx=10, pady=10)

    def handle_start_game(self):
        self.hide_ui()

        snake_game = SnakeGame(self.ui_logic.player)
        snake_game.start(self.show_game_end_view)
