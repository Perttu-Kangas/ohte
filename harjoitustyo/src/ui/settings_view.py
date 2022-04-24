from tkinter import ttk, constants, StringVar
from enums.game_enums import Difficulty, Color
from services.ui_logic import UILogic


class SettingsView:
    def __init__(self, root, ui_logic: UILogic, show_main_view):
        self.root = root
        self.ui_logic = ui_logic
        self.frame = None
        self.show_main_view = show_main_view

        self.difficulty_var = None
        self.snake_var = None
        self.apple_var = None
        self.background_var = None

        self.initialize()

    def pack(self):
        self.frame.pack()

    def destroy(self):
        self.frame.destroy()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        back_button = ttk.Button(
            master=self.frame,
            text="Takaisin päävalikkoon",
            command=self.back_to_main_view
        )

        info_label = ttk.Label(master=self.frame, text="Asetukset")

        difficulty_label = ttk.Label(master=self.frame, text="Vaikeusaste:")
        self.difficulty_var = StringVar()
        self.difficulty_var.set(self.ui_logic.player.difficulty.name)
        list_difficulty = list(map(lambda difficulty: difficulty.name, Difficulty))
        difficulty_choice = ttk.OptionMenu(
            self.frame,
            self.difficulty_var,
            self.ui_logic.player.difficulty.name,
            *list_difficulty
        )

        list_color = list(map(lambda color: color.name, Color))

        snake_color_label = ttk.Label(master=self.frame, text="Madon väri:")
        self.snake_var = StringVar()
        self.snake_var.set(self.ui_logic.player.snake_color.name)
        snake_color_choice = ttk.OptionMenu(
            self.frame,
            self.snake_var,
            self.ui_logic.player.snake_color.name,
            *list_color
        )

        apple_color_label = ttk.Label(master=self.frame, text="Omenan väri:")
        self.apple_var = StringVar()
        self.apple_var.set(self.ui_logic.player.apple_color.name)
        apple_color_choice = ttk.OptionMenu(
            self.frame,
            self.apple_var,
            self.ui_logic.player.apple_color.name,
            *list_color
        )

        board_color_label = ttk.Label(
            master=self.frame, text="Pelikentän väri:")
        self.background_var = StringVar()
        self.background_var.set(self.ui_logic.player.background_color.name)
        board_color_choice = ttk.OptionMenu(
            self.frame,
            self.background_var,
            self.ui_logic.player.background_color.name,
            *list_color
        )

        back_button.grid(row=0, column=0, sticky=constants.EW,
                         padx=10, pady=10)
        info_label.grid(row=1, column=0, sticky=constants.EW, padx=10, pady=10)
        difficulty_label.grid(
            row=2, column=0, sticky=constants.W, padx=10, pady=10)
        difficulty_choice.grid(
            row=2, column=1, sticky=constants.EW, padx=10, pady=10)
        snake_color_label.grid(
            row=3, column=0, sticky=constants.W, padx=10, pady=10)
        snake_color_choice.grid(
            row=3, column=1, sticky=constants.EW, padx=10, pady=10)
        apple_color_label.grid(
            row=4, column=0, sticky=constants.W, padx=10, pady=10)
        apple_color_choice.grid(
            row=4, column=1, sticky=constants.EW, padx=10, pady=10)
        board_color_label.grid(
            row=5, column=0, sticky=constants.W, padx=10, pady=10)
        board_color_choice.grid(
            row=5, column=1, sticky=constants.EW, padx=10, pady=10)

    def back_to_main_view(self):
        self.ui_logic.player.difficulty = Difficulty[self.difficulty_var.get()]
        self.ui_logic.player.snake_color = Color[self.snake_var.get()]
        self.ui_logic.player.apple_color = Color[self.apple_var.get()]
        self.ui_logic.player.background_color = Color[self.background_var.get()]
        self.ui_logic.save_player()
        self.show_main_view()
