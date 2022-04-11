from tkinter import ttk, constants, StringVar
from entities.player import Player
from enums.game_enums import Difficulty, Color


class SettingsView:
    def __init__(self, root, show_main_view):
        self.root = root
        self.frame = None
        self.show_main_view = show_main_view

        self.initialize()

    def pack(self):
        self.frame.pack()

    def destroy(self):
        self.frame.destroy()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        player = Player("test")

        back_button = ttk.Button(
            master=self.frame,
            text="Takaisin päävalikkoon",
            command=self.show_main_view
        )

        info_label = ttk.Label(master=self.frame, text="Asetukset")

        difficulty_label = ttk.Label(master=self.frame, text="Vaikeusaste:")
        difficulty_var = StringVar()
        difficulty_var.set(player.difficulty)
        list_difficulty = list(Difficulty)
        difficulty_choice = ttk.OptionMenu(
            self.frame,
            difficulty_var,
            player.difficulty,
            *list_difficulty
        )

        list_color = list(Color)

        snake_color_label = ttk.Label(master=self.frame, text="Madon väri:")
        snake_color_var = StringVar()
        snake_color_var.set(player.snake_color)
        snake_color_choice = ttk.OptionMenu(
            self.frame,
            snake_color_var,
            player.snake_color,
            *list_color
        )

        apple_color_label = ttk.Label(master=self.frame, text="Omenan väri:")
        apple_color_var = StringVar()
        apple_color_var.set(player.apple_color)
        apple_color_choice = ttk.OptionMenu(
            self.frame,
            apple_color_var,
            player.apple_color,
            *list_color
        )

        board_color_label = ttk.Label(master=self.frame, text="Pelikentän väri:")
        board_color_var = StringVar()
        board_color_var.set(player.background_color)
        board_color_choice = ttk.OptionMenu(
            self.frame,
            board_color_var,
            player.background_color,
            *list_color
        )

        back_button.grid(row=0, column=0, sticky=constants.EW, padx=10, pady=10)
        info_label.grid(row=1, column=0, sticky=constants.EW, padx=10, pady=10)
        difficulty_label.grid(row=2, column=0, sticky=constants.W, padx=10, pady=10)
        difficulty_choice.grid(row=2, column=1, sticky=constants.EW, padx=10, pady=10)
        snake_color_label.grid(row=3, column=0, sticky=constants.W, padx=10, pady=10)
        snake_color_choice.grid(row=3, column=1, sticky=constants.EW, padx=10, pady=10)
        apple_color_label.grid(row=4, column=0, sticky=constants.W, padx=10, pady=10)
        apple_color_choice.grid(row=4, column=1, sticky=constants.EW, padx=10, pady=10)
        board_color_label.grid(row=5, column=0, sticky=constants.W, padx=10, pady=10)
        board_color_choice.grid(row=5, column=1, sticky=constants.EW, padx=10, pady=10)
