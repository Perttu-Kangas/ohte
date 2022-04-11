from tkinter import ttk, constants


class LoginView:
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
        login_label = ttk.Label(master=self.frame, text="Pelaajanimi:")
        login_entry = ttk.Entry(master=self.frame)
        login_button = ttk.Button(
            master=self.frame,
            text="Kirjaudu",
            command=self.handle_login
        )

        login_label.grid(row=0, column=0, sticky=constants.W, padx=10, pady=10)
        login_entry.grid(row=0, column=1, sticky=constants.EW,
                         padx=10, pady=10)
        login_button.grid(row=2, column=0, columnspan=2,
                          sticky=constants.EW, padx=10, pady=10)

    def handle_login(self):
        self.show_main_view()
