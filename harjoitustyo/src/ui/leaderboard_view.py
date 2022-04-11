from tkinter import ttk, constants


class LeaderboardView:
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
        back_button = ttk.Button(
            master=self.frame,
            text="Takaisin päävalikkoon",
            command=self.show_main_view
        )

        info_label = ttk.Label(master=self.frame, text="Tulostaulu")

        own_best_label = ttk.Label(master=self.frame, text="Parhaat pisteesi: x")
        own_total_label = ttk.Label(master=self.frame, text="Pisteitä kaikenkaikkiaan: x")
        own_time_label = ttk.Label(master=self.frame, text="Peliaika: x")

        top_ten_label = ttk.Label(master=self.frame, text="Parhaat 10")

        back_button.grid(row=0, column=0, sticky=constants.EW, padx=10, pady=10)
        info_label.grid(row=1, column=0, sticky=constants.EW, padx=10, pady=10)
        own_best_label.grid(row=2, column=0, sticky=constants.EW, padx=10, pady=10)
        own_total_label.grid(row=3, column=0, sticky=constants.EW, padx=10, pady=10)
        own_time_label.grid(row=4, column=0, sticky=constants.EW, padx=10, pady=10)
        top_ten_label.grid(row=5, column=0, sticky=constants.EW, padx=10, pady=10)

        for i in range(1, 11):
            top_label = ttk.Label(master=self.frame, text=str(i) + ". Pelaaja" + str(i) + " x")
            top_label.grid(row=(5 + i), column=0, sticky=constants.EW, padx=10, pady=10)
