from tkinter import ttk, constants
from entities.player import Player
from services.snake_game import SnakeGame


class MainView:
    def __init__(self, root, hide_ui, show_main_view):
        self.root = root
        self.frame = None
        self.hide_ui = hide_ui
        self.show_main_view = show_main_view

        self.initialize()

    def pack(self):
        self.frame.pack()

    def destroy(self):
        self.frame.destroy()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        info_label = ttk.Label(master=self.frame, text="Tervetuloa player!")
        start_game_button = ttk.Button(
            master=self.frame,
            text="Aloita peli",
            command=self.handle_start_game
        )
        settings_button = ttk.Button(
            master=self.frame,
            text="Asetukset"
        )
        instructions_button = ttk.Button(
            master=self.frame,
            text="Peliohjeet"
        )
        leaderboard_button = ttk.Button(
            master=self.frame,
            text="Tulostaulu"
        )

        info_label.grid(row=0, column=0, sticky=constants.EW, padx=10, pady=10)
        start_game_button.grid(row=1, column=0, sticky=constants.EW, padx=10, pady=10)
        settings_button.grid(row=2, column=0, sticky=constants.EW, padx=10, pady=10)
        instructions_button.grid(row=3, column=0, sticky=constants.EW, padx=10, pady=10)
        leaderboard_button.grid(row=4, column=0, sticky=constants.EW, padx=10, pady=10)

    def handle_start_game(self):
        self.hide_ui()

        player = Player("test")
        snake_game = SnakeGame(player, self.show_main_view)
        snake_game.start()
