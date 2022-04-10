from tkinter import Tk
from ui.login_view import LoginView
from ui.main_view import MainView


class UI:

    def __init__(self, root: Tk):
        self.root = root
        self.current_view = None
        self.hidden = False

    def start(self):
        self.show_login_view()

    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = None

    def show_ui(self):
        if self.hidden:
            self.root.deiconify()
            self.hidden = False

    def hide_ui(self):
        if not self.hidden:
            self.root.withdraw()
            self.hidden = True

    def show_login_view(self):
        self.hide_current_view()
        self.show_ui()
        self.current_view = LoginView(self.root, self.show_main_view)
        self.current_view.pack()

    def show_main_view(self):
        self.hide_current_view()
        self.show_ui()
        self.current_view = MainView(self.root, self.hide_ui, self.show_main_view)
        self.current_view.pack()

