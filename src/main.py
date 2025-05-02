import tkinter as tk
from gui import MemoryGameGUI

def main():
    root = tk.Tk()
    game_gui = MemoryGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()