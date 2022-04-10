from tkinter import Tk
from ui.ui import UI

window = Tk()
window.title("Snake Game")
ui = UI(window)
ui.start()
window.mainloop()
