from tkinter import ttk, constants
from services.snake_game import SnakeGame
from services.ui_logic import UILogic


class MainView:
    def __init__(self, root, ui_logic: UILogic, hide_ui, show_main_view,
                 show_settings_view, show_instructions_view,
                 show_leaderboard_view, show_game_end_view):
        """Luokan konstruktori. Luo uuden päänäkymän.

        Args:
            root: Käyttöliittymästä vastaava tkinter.Tk objekti
            ui_logic: Käyttöliittymälogiikasta vastaava luokka
            hide_ui: Metodi, jolla piilottaa koko näkymä
            show_main_view: Metodi, joka avaa päänäkymän
            show_settings_view: Metodi, joka avaa asetusketnäkymän
            show_instructions_view: Metodi, joka avaa ohjeetnäkymän
            show_leaderboard_view: Metodi, joka avaa tulostaulunäkymän
            show_game_end_view: Metodi, joka avaa pelinpäättymisnäkymän
        """
        self.root = root
        self.ui_logic = ui_logic
        self.frame = None
        self.hide_ui = hide_ui
        self.show_main_view = show_main_view
        self.show_settings_view = show_settings_view
        self.show_instructions_view = show_instructions_view
        self.show_leaderboard_view = show_leaderboard_view
        self.show_game_end_view = show_game_end_view

        self.initialize()

    def pack(self):
        """Avaa näkymän"""
        self.frame.pack()

    def destroy(self):
        """Tuhoaa näkymän"""
        self.frame.destroy()

    def initialize(self):
        """Alustaa näkymän"""
        self.frame = ttk.Frame(master=self.root)
        info_label = ttk.Label(
            master=self.frame, text="Tervetuloa " + self.ui_logic.player.name + "!")
        start_game_button = ttk.Button(
            master=self.frame,
            text="Aloita peli",
            command=self.handle_start_game
        )
        settings_button = ttk.Button(
            master=self.frame,
            text="Asetukset",
            command=self.show_settings_view
        )
        instructions_button = ttk.Button(
            master=self.frame,
            text="Peliohjeet",
            command=self.show_instructions_view
        )
        leaderboard_button = ttk.Button(
            master=self.frame,
            text="Tulostaulu",
            command=self.show_leaderboard_view
        )

        info_label.grid(row=0, column=0, sticky=constants.EW, padx=10, pady=10)
        start_game_button.grid(
            row=1, column=0, sticky=constants.EW, padx=10, pady=10)
        settings_button.grid(
            row=2, column=0, sticky=constants.EW, padx=10, pady=10)
        instructions_button.grid(
            row=3, column=0, sticky=constants.EW, padx=10, pady=10)
        leaderboard_button.grid(
            row=4, column=0, sticky=constants.EW, padx=10, pady=10)

    def handle_start_game(self):
        """Piilottaa käyttöliittymän, ja avaa pelin.

        Returns:
            None
        """
        self.hide_ui()

        snake_game = SnakeGame(self.ui_logic.player)
        snake_game.start(self.show_game_end_view)
