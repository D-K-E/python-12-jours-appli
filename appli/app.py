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

        # elements de liste
        self.list_frame = tk.Frame(master=self.tool_frame)
        self.list_frame.pack(side=tk.TOP, fill=tk.Y, expand=1)

        self.cbar = tk.Scrollbar(master=self.list_frame)
        self.cbar.pack(side=tk.RIGHT, fill=tk.Y, expand=1)

        self.liste_chemin = tk.Listbox(
            master=self.list_frame, yscrollcommand=self.cbar.set
        )
        self.liste_chemin.pack(side=tk.LEFT, fill=tk.Y, expand=1)
        for i in range(0, 200):
            self.liste_chemin.insert(tk.END, "chemin " + str(i))
        #
        self.cbar.config(command=self.liste_chemin.yview)

        # fin des elements de liste
        # cadre des boutons
        self.button_frame = tk.Frame(master=self.tool_frame)
        self.button_frame.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.charge_btn = tk.Button(master=self.button_frame, text="Charger")
        self.charge_btn.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.ouvrir_btn = tk.Button(master=self.button_frame, text="Ouvrir")
        self.ouvrir_btn.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.supprimer_btn = tk.Button(master=self.button_frame, text="Supprimer")
        self.supprimer_btn.pack(side=tk.TOP, fill=tk.X, expand=1)
        # fin de cadre des boutons

        # cadre de listes des mots cles
        self.mot_frame = tk.Frame(master=self.tool_frame)
        self.mot_frame.pack(side=tk.TOP, fill=tk.Y, expand=1)

        self.mbar = tk.Scrollbar(master=self.mot_frame)
        self.mbar.pack(side=tk.RIGHT, fill=tk.Y, expand=1)

        self.mbox = tk.Listbox(master=self.mot_frame, yscrollcommand=self.mbar.set)
        self.mbox.pack(side=tk.LEFT, fill=tk.Y, expand=1)
        for m in range(10, 120):
            self.mbox.insert(tk.END, "mot " + str(m))
        #
        self.mbar.config(command=self.mbox.yview)
        # fin cadre de liste des mots cles

        # cadre d'entre 
        self.entre_frame = tk.Frame(master=self.tool_frame)
        self.entre_frame.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.entre = tk.Entry(master=self.entre_frame)
        self.entre.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.entre.delete(0, tk.END)
        self.entre.insert(0, "valeur par défaut")

        # fin cadre d'entre
        # cadre des boutons des mots
        self.mot_button_frame = tk.Frame(master=self.tool_frame)
        self.mot_button_frame.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.ajouter_btn = tk.Button(master=self.mot_button_frame, text="Ajouter")
        self.ajouter_btn.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.mot_supprimer_btn = tk.Button(master=self.mot_button_frame, text="Supprimer")
        self.mot_supprimer_btn.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.filtrer_btn = tk.Button(master=self.mot_button_frame,
                text="Filtrer")
        self.filtrer_btn.pack(side=tk.TOP, fill=tk.X, expand=1)



if __name__ == "__main__":
    root = tk.Tk()
    monapp = MainWindow(root)
    root.mainloop()
