from tkinter import ttk, constants, StringVar
from services.ui_logic import UILogic


class LoginView:
    def __init__(self, root, ui_logic: UILogic, show_main_view):
        """Luokan konstruktori. Luo uuden kirjautumisnäkymän.

        Args:
            root: Käyttöliittymästä vastaava tkinter.Tk objekti
            ui_logic: Käyttöliittymälogiikasta vastaava luokka
            show_main_view: Päävalikkonäkymän avaus metodi
        """
        self.root = root
        self.frame = None
        self.show_main_view = show_main_view

        self.login = ui_logic.login
        self.login_entry = None

        self.error = None
        self.error_var = None

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
        login_label = ttk.Label(master=self.frame, text="Pelaajanimi:")
        self.login_entry = ttk.Entry(master=self.frame)
        login_button = ttk.Button(
            master=self.frame,
            text="Kirjaudu",
            command=self.handle_login
        )
        self.error_var = StringVar(master=self.frame)
        self.error = ttk.Label(
            master=self.frame, textvariable=self.error_var, foreground="RED")
        self.error.grid(row=3, column=0, sticky=constants.EW, padx=10, pady=10)

        login_label.grid(row=0, column=0, sticky=constants.W, padx=10, pady=10)
        self.login_entry.grid(row=0, column=1, sticky=constants.EW,
                              padx=10, pady=10)
        login_button.grid(row=2, column=0, columnspan=2,
                          sticky=constants.EW, padx=10, pady=10)

        self.hide_error()

    def show_error(self, message):
        """Näyttää virheviestin

        Args:
            message: Merkkijono, joka sisältää virheviestin

        Returns:
            None
        """
        self.error_var.set(message)
        self.error.grid()

    def hide_error(self):
        """Piilottaa virheviestin"""
        self.error.grid_remove()

    def handle_login(self):
        """Kirjautuu sisään ja avaa päänäkymän"""
        playername = self.login_entry.get()
        if len(playername) < 4 or len(playername) > 20:
            self.show_error("Nimen tulee olla 4-20 merkkiä!")
            return

        self.login(playername)
        self.show_main_view()
