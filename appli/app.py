"""
interface graphique pour projet 12 jours

Il contient les composants de la spécification.
"""
# declaration des paquets

import tkinter as tk  # nécessaire pour interface graphique
from tkinter import scrolledtext as stext
from tkinter import filedialog as FD
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

        self.charge_btn = tk.Button(master=self.button_frame, 
            text="Charger", command=self.charger_fichiers)
        self.charge_btn.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.ouvrir_btn = tk.Button(master=self.button_frame, 
            text="Ouvrir", command=self.ouvrir_text)
        self.ouvrir_btn.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.supprimer_btn = tk.Button(master=self.button_frame, 
            text="Supprimer", command=self.supprimer_fichiers)
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

        self.ajouter_btn = tk.Button(master=self.mot_button_frame, 
            text="Ajouter", command=self.ajouter_mots_cles)
        self.ajouter_btn.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.mot_supprimer_btn = tk.Button(master=self.mot_button_frame, 
        text="Supprimer", command=self.supprimer_mot_cles)
        self.mot_supprimer_btn.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.filtrer_btn = tk.Button(master=self.mot_button_frame,
                text="Filtrer", command=self.filtrage_par_mot_cle)
        self.filtrer_btn.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.chemins_de_text = []
        self.dirname = ""
        self.liste_de_chemin = []

    def charger_fichiers(self):
        "charge les chemins à la liste"
        chemins = FD.askopenfilenames()
        if not chemins:
            return
        self.chemins_de_text = list(chemins)
        self.liste_chemin.delete(0, tk.END)
        for chemin in self.chemins_de_text:
            name = os.path.basename(chemin)
            self.dirname = os.path.dirname(chemin)
            self.liste_chemin.insert(tk.END, name)
        return

    def supprimer_fichiers(self):
        "supprime les chemins de la liste et chemin_de_text"
        chemin = self.liste_chemin.curselection()
        indice_de_selection = chemin[0]
        name = self.liste_chemin.get(indice_de_selection)
        chemins = []
        supprime_chemin = os.path.join(self.dirname, name)
        print("chemin à supprimer:", supprime_chemin)
        print("chemins", str(self.chemins_de_text))
        for chem in self.chemins_de_text:
            if supprime_chemin != chem:
                chemins.append(chem)
        self.chemins_de_text = chemins
        print("nouveaux chemins:", str(self.chemins_de_text))
        self.liste_chemin.delete(indice_de_selection)
        return
    
    def ouvrir_text(self):
        "Ouvre le texte et visualise dans la zone de texte"
        selection = self.liste_chemin.curselection()
        indice_de_selection = selection[0]
        name = self.liste_chemin.get(indice_de_selection)
        abschemin = os.path.join(self.dirname, name)
        with open(abschemin, "r", encoding='utf-8') as f:
            text = f.read()
        self.zone_affichage_text.delete(1.0, tk.END)
        self.zone_affichage_text.insert(tk.END, text)

    def ajouter_mots_cles(self):
        "Ajoute des mots clés sais à la liste"
        mot_actuel = self.entre.get()
        if mot_actuel and mot_actuel != "valeur par défaut":
            self.mbox.insert(tk.END, mot_actuel)
        return

    def supprimer_mot_cles(self):
        "supprime des mots cles de la liste des mots cles"
        selection = self.mbox.curselection()
        for indice in selection:
            self.mbox.delete(indice)
    
    def lire_contenu_texte(self, chemin: str) -> str:
        "Lit  le contenu du texte"
        with open(chemin, 'r', encoding='utf-8') as f:
            texte = f.read()
        return texte

    def controle_de_texte(self, texte: str, mot_cles: str) -> bool:
        "Controle si le mot cles existe dans le texte"
        return bool(mot_cles in texte)

    def garder(self, chemin: str, resultat_de_control: bool) -> None:
        "garde le chemin si resultat de control est vrai" 
        if resultat_de_control:
            self.liste_de_chemin.append(chemin)
        return

    def affichage(self):
        ""
        self.liste_chemin.delete(0, tk.END)
        for chemin in self.liste_de_chemin:
            name = os.path.basename(chemin)
            self.liste_chemin.insert(tk.END, name)
        return

    def filtrage_par_mot_cle(self):
        "Filtre la liste des chemins par mot cles"
        selection = self.mbox.curselection()
        indice = selection[0]
        mot = self.mbox.get(indice)
        for chemin in self.chemins_de_text:
            contenu = self.lire_contenu_texte(chemin)
            control = self.controle_de_texte(contenu, mot)
            self.garder(chemin, control)
        self.affichage()
        return
        



if __name__ == "__main__":
    root = tk.Tk()
    monapp = MainWindow(root)
    root.mainloop()
