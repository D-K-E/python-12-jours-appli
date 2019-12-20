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
        self.label_titre = tk.Label(
            master=self.main_frame, text="Application 12 jours", font=("FreeSerif", 16)
        )
        self.label_titre.pack(side=tk.TOP, fill=tk.X, expand=0)
        self.sub_frame = tk.Frame(master=self.main_frame)
        self.sub_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # fin des elements de cadre principal

        # elements de sub_frame
        self.zone_affichage_text = stext.ScrolledText(master=self.sub_frame)
        self.zone_affichage_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.tool_frame = tk.Frame(master=self.sub_frame)
        self.tool_frame.pack(side=tk.LEFT, fill=tk.Y, expand=1)
        # fin des elements de sub_frame

        # elements de list frame
        self.list_frame = tk.Frame(master=self.tool_frame)
        self.list_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.cbar = tk.Scrollbar(master=self.list_frame)
        self.cbar.pack(side=tk.RIGHT, fill=tk.Y, expand=1)
        self.cbox = tk.Listbox(master=self.list_frame, yscrollcommand=self.cbar.set)
        for i in range(100):
            self.cbox.insert(tk.END, "chemin" + str(i))
        self.cbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.cbar.config(command=self.cbox.yview)

        # fin des elements de liste frame

        # elements de bouton frame
        self.button_frame = tk.Frame(master=self.tool_frame)
        self.button_frame.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.load_btn = tk.Button(master=self.button_frame, text="Charger")
        self.load_btn.pack(side=tk.TOP, fill=tk.X)

        self.ouvrir_btn = tk.Button(master=self.button_frame, text="Ouvrir")
        self.ouvrir_btn.pack(side=tk.TOP, fill=tk.X)

        self.suppr_btn = tk.Button(master=self.button_frame, text="Supprimer")
        self.suppr_btn.pack(side=tk.TOP, fill=tk.X)
        # fin des elements de button frame

        # elements mot frame
        self.mot_frame = tk.Frame(master=self.tool_frame)
        self.mot_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.mbar = tk.Scrollbar(master=self.mot_frame)
        self.mbar.pack(side=tk.RIGHT, fill=tk.Y, expand=1)
        self.mbox = tk.Listbox(master=self.mot_frame, yscrollcommand=self.mbar.set)
        for i in range(100):
            self.mbox.insert(tk.END, "mot " + str(i))
        self.mbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.mbar.config(command=self.mbox.yview)
        # fin mot frame

        # elements entry frame
        self.entre_frame = tk.Frame(master=self.tool_frame)
        self.entre_frame.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.champs_saisi = tk.Entry(master=self.entre_frame)
        self.champs_saisi.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.champs_saisi.delete(0, tk.END)
        self.champs_saisi.insert(0, "valeur par défaut")

        # fin entry frame

        # entry button frame
        self.ebutton_frame = tk.Frame(master=self.tool_frame)
        self.ebutton_frame.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.ajouter_button = tk.Button(master=self.ebutton_frame, text="ajouter")
        self.ajouter_button.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.filtrer_button = tk.Button(master=self.ebutton_frame, text="filtrer")
        self.filtrer_button.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.enlever_button = tk.Button(master=self.ebutton_frame, text="enlever")
        self.enlever_button.pack(side=tk.TOP, fill=tk.X, expand=1)
        # fin entry button frame


if __name__ == "__main__":
    root = tk.Tk()
    monapp = MainWindow(root)
    root.mainloop()
