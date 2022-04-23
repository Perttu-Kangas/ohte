from tkinter import Tk
from ui.login_view import LoginView
from ui.main_view import MainView
from ui.settings_view import SettingsView
from ui.leaderboard_view import LeaderboardView
from ui.instructions_view import InstructionsView
from services.ui_logic import UILogic


class UI:

    def __init__(self, root: Tk, ui_logic: UILogic):
        self.root = root
        self.current_view = None
        self.hidden = False
        self.ui_logic = ui_logic

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
        self.current_view = LoginView(self.root, self.show_main_view, self.ui_logic.login)
        self.current_view.pack()

    def show_main_view(self):
        self.hide_current_view()
        self.show_ui()
        self.current_view = MainView(self.root,
                                     self.hide_ui,
                                     self.show_main_view,
                                     self.show_settings_view,
                                     self.show_instructions_view,
                                     self.show_leaderboard_view)
        self.current_view.pack()

    def show_settings_view(self):
        self.hide_current_view()
        self.show_ui()
        self.current_view = SettingsView(self.root, self.show_main_view)
        self.current_view.pack()

    def show_leaderboard_view(self):
        self.hide_current_view()
        self.show_ui()
        self.current_view = LeaderboardView(self.root, self.show_main_view)
        self.current_view.pack()

    def show_instructions_view(self):
        self.hide_current_view()
        self.show_ui()
        self.current_view = InstructionsView(self.root, self.show_main_view)
        self.current_view.pack()
