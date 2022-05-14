from tkinter import ttk, constants
from services.ui_logic import UILogic


class LeaderboardView:
    def __init__(self, root, ui_logic: UILogic, show_main_view):
        """Luokan konstruktori. Luo uuden tulostaulunäkymän.

        Args:
            root: Käyttöliittymästä vastaava tkinter.Tk objekti
            ui_logic: Käyttöliittymälogiikasta vastaava luokka
            show_main_view: Päävalikkonäkymän avaus metodi
        """
        self.root = root
        self.ui_logic = ui_logic
        self.frame = None
        self.show_main_view = show_main_view

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
        back_button = ttk.Button(
            master=self.frame,
            text="Takaisin päävalikkoon",
            command=self.show_main_view
        )

        info_label = ttk.Label(master=self.frame, text="Tulostaulu")

        back_button.grid(row=0, column=0, sticky=constants.EW,
                         padx=10, pady=10)
        info_label.grid(row=1, column=0, sticky=constants.EW, padx=10, pady=10)

        self.own_best_init()
        self.three_best_init()

    def own_best_init(self):
        """Alustaa omat parhaat tulokset näkymään"""
        player_own = self.ui_logic.get_own_best()
        player_best = "0" if player_own[0] is None else str(player_own[0])
        player_all = "0" if player_own[1] is None else str(player_own[1])
        player_time = "0" if player_own[2] is None else str(player_own[2])

        own_best_label = ttk.Label(
            master=self.frame, text="Parhaat pisteesi: " + player_best)
        own_total_label = ttk.Label(
            master=self.frame, text="Pisteitä kaikenkaikkiaan: " + player_all)
        own_time_label = ttk.Label(
            master=self.frame, text="Peliaika: " + player_time)

        own_best_label.grid(
            row=2, column=0, sticky=constants.EW, padx=10)
        own_total_label.grid(
            row=3, column=0, sticky=constants.EW, padx=10)
        own_time_label.grid(
            row=4, column=0, sticky=constants.EW, padx=10)

    def three_best_init(self):
        """Alustaa kolme parasta näkymään"""
        top_three_label = ttk.Label(master=self.frame,
                                    text="Parhaat 3 vaikeusasteella " + self.ui_logic.player.difficulty.name)
        top_three_label.grid(
            row=5, column=0, sticky=constants.EW, padx=10, pady=10)

        three_best = self.ui_logic.get_three_best()
        for i in range(3):

            name = "-"
            points = ""
            if i < len(three_best):
                name = str(three_best[i][0])
                points = str(three_best[i][1])

            top_label = ttk.Label(master=self.frame, text=str(
                i+1) + ". " + name + " " + points)
            top_label.grid(row=(5 + i+1), column=0,
                           sticky=constants.EW, padx=10)
