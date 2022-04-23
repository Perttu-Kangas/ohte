from tkinter import ttk, constants, StringVar


class LoginView:
    def __init__(self, root, show_main_view, login):
        self.root = root
        self.frame = None
        self.show_main_view = show_main_view

        self.login = login
        self.login_entry = None

        self.error = None
        self.error_var = None

        self.initialize()

    def pack(self):
        self.frame.pack()

    def destroy(self):
        self.frame.destroy()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        login_label = ttk.Label(master=self.frame, text="Pelaajanimi:")
        self.login_entry = ttk.Entry(master=self.frame)
        login_button = ttk.Button(
            master=self.frame,
            text="Kirjaudu",
            command=self.handle_login
        )
        self.error_var = StringVar(master=self.frame)
        self.error = ttk.Label(master=self.frame, textvariable=self.error_var, foreground="RED")
        self.error.grid(row=3, column=0, sticky=constants.EW, padx=10, pady=10)

        login_label.grid(row=0, column=0, sticky=constants.W, padx=10, pady=10)
        self.login_entry.grid(row=0, column=1, sticky=constants.EW,
                         padx=10, pady=10)
        login_button.grid(row=2, column=0, columnspan=2,
                          sticky=constants.EW, padx=10, pady=10)

        self.hide_error()

    def show_error(self, message):
        self.error_var.set(message)
        self.error.grid()

    def hide_error(self):
        self.error.grid_remove()

    def handle_login(self):
        playername = self.login_entry.get()
        if len(playername) < 4 or len(playername) > 20:
            self.show_error("Pelaajanimen tulee olla 4-20 merkkiä pitkä!")
            return

        self.login(playername)
        self.show_main_view()
