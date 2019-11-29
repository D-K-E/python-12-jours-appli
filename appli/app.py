"""
interface graphique pour projet 12 jours

Il contient les composants de la spécification.
"""
# declaration des paquets

import tkinter as tk  # nécessaire pour interface graphique
from tkinter import scrolledtext as stext
import os  # pour manipulation des chemins
# fin declaration des paquets
class MainWindow:
    def __init__(self, master):
        # declaration de cadre principal
        self.main_frame = tk.Frame(master=master)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        # les elements de cadre principal
        self.label_titre = tk.Label(master=self.main_frame,
            text="Application 12 jours",
            font=("FreeSerif", 16)
            )
        self.label_titre.pack(side=tk.TOP, fill=tk.X, 
                            expand=0)
        self.sub_frame = tk.Frame(master=self.main_frame)
        self.sub_frame.pack(side=tk.TOP, fill=tk.BOTH, 
        expand=1)

        # fin des elements de cadre principal

        # elements de sub_frame
        self.zone_affichage_text = stext.ScrolledText(
            master=self.sub_frame
        )
        self.zone_affichage_text.pack(
                side=tk.LEFT,
                fill=tk.BOTH,
                expand=1
        )
        self.tool_frame = tk.Frame(master=self.sub_frame)
        self.tool_frame.pack(side=tk.LEFT,
                             fill=tk.Y,
                             expand=1)
        # fin des elements de sub_frame


if __name__ == "__main__":
    root = tk.Tk()
    monapp = MainWindow(root)
    root.mainloop()
