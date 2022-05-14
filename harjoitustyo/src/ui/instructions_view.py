from tkinter import ttk, constants


class InstructionsView:
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

        info_label = ttk.Label(master=self.frame, text="Peliohjeet")

        move_label = ttk.Label(master=self.frame, text="1. Liikuminen tapahtuu nuolinäppäimillä")
        points_label = ttk.Label(master=self.frame, text="2. Pisteitä saa syömällä omenoita")
        border_label = ttk.Label(master=self.frame, text="3. Osuessa reunaan tai matoon peli loppuu")

        back_button.grid(row=0, column=0, sticky=constants.EW,
                         padx=10, pady=10)
        info_label.grid(row=1, column=0, sticky=constants.EW, padx=10, pady=10)
        move_label.grid(row=3, column=0, sticky=constants.EW, padx=10, pady=10)
        points_label.grid(row=4, column=0, sticky=constants.EW, padx=10, pady=10)
        border_label.grid(row=5, column=0, sticky=constants.EW, padx=10, pady=10)
