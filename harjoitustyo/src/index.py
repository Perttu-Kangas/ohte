from tkinter import Tk
from ui.ui import UI
from initialize_database import initialize_database
from services.ui_logic import UILogic

initialize_database()

window = Tk()
window.title("Matopeli")
window.resizable(False, False)
window.geometry("400x300")
ui = UI(window, UILogic())
ui.start()
window.mainloop()
