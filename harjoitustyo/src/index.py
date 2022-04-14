from tkinter import Tk
from ui.ui import UI
from initialize_database import initialize_database

initialize_database()

window = Tk()
window.title("Matopeli")
ui = UI(window)
ui.start()
window.mainloop()
