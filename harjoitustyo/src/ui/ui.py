from tkinter import Tk
from ui.login_view import LoginView
from ui.main_view import MainView
from ui.settings_view import SettingsView
from ui.leaderboard_view import LeaderboardView
from ui.instructions_view import InstructionsView
from ui.game_end_view import GameEndView
from services.ui_logic import UILogic


class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka"""

    def __init__(self, root: Tk, ui_logic: UILogic):
        """Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan palvelun.

        Args:
            root: Käyttöliittymästä vastaava tkinter.Tk objekti
            ui_logic: Käyttöliittymälogiikasta vastaava luokka
        """
        self.root = root
        self.current_view = None
        self.hidden = False
        self.ui_logic = ui_logic

    def start(self):
        """Kutsutaan, kun sovellus käynnistyy.
        Avaa ensiki kirjautumisvalikon.

        Returns:
            None
        """
        self.show_login_view()

    def hide_current_view(self):
        """Tuhoaa tämän hetkisen ikkunan

        Returns:
            None
        """
        if self.current_view:
            self.current_view.destroy()
        self.current_view = None

    def show_ui(self):
        """Tuo käyttöliittymän takaisin esiin.
        Esimerkiksi, kun peli loppuu.

        Returns:
            None
        """
        if self.hidden:
            self.root.deiconify()
            self.hidden = False

    def hide_ui(self):
        """Piilottaa käyttöliittymän.
        Esimerkiksi, kun peli alkaa.

        Returns:
            None
        """
        if not self.hidden:
            self.root.withdraw()
            self.hidden = True

    def show_login_view(self):
        """Tuhoaa nykyisen näkymän, ja avaa kirjautumisnäkymän

        Returns:
            None
        """
        self.hide_current_view()
        self.show_ui()
        self.current_view = LoginView(
            self.root, self.ui_logic, self.show_main_view)
        self.current_view.pack()

    def show_main_view(self):
        """Tuhoaa nykyisen näkymän, ja avaa päänäkymän

        Returns:
            None
        """
        self.hide_current_view()
        self.show_ui()
        self.current_view = MainView(self.root,
                                     self.ui_logic,
                                     self.hide_ui,
                                     self.show_main_view,
                                     self.show_settings_view,
                                     self.show_instructions_view,
                                     self.show_leaderboard_view,
                                     self.show_game_end_view)
        self.current_view.pack()

    def show_settings_view(self):
        """Tuhoaa nykyisen näkymän, ja avaa asetuksetnäkymän

        Returns:
            None
        """
        self.hide_current_view()
        self.show_ui()
        self.current_view = SettingsView(
            self.root, self.ui_logic, self.show_main_view)
        self.current_view.pack()

    def show_leaderboard_view(self):
        """Tuhoaa nykyisen näkymän, ja avaa tulostaulunäkymän

        Returns:
            None
        """
        self.hide_current_view()
        self.show_ui()
        self.current_view = LeaderboardView(
            self.root, self.ui_logic, self.show_main_view)
        self.current_view.pack()

    def show_instructions_view(self):
        """Tuhoaa nykyisen näkymän, ja avaa ohjenäkymän

        Returns:
            None
        """
        self.hide_current_view()
        self.show_ui()
        self.current_view = InstructionsView(self.root, self.show_main_view)
        self.current_view.pack()

    def show_game_end_view(self, points=0):
        """Tuhoaa nykyisen näkymän, ja avaa pelinpäättymisnäkymän

        Returns:
            None
        """
        self.hide_current_view()
        self.show_ui()
        self.current_view = GameEndView(self.root,
                                        self.ui_logic,
                                        self.hide_ui,
                                        self.show_main_view,
                                        self.show_game_end_view,
                                        points=points)
        self.current_view.pack()
