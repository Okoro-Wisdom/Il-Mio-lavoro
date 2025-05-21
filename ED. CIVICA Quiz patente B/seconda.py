import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import random
import os
from domande import DOM as questions
from tkinter import messagebox
import libretto.patente_AM as istruzione
import home_page as inizio


class quiz:
    def __init__(self, root):
        self.root = root
        self.indice_domanda = 0
        self.immagini_cache = {}
        self.errori = 0
        self.errori_totali = 0
        self.domande_sbagliate = []

        random.shuffle(questions)
        
        font_titolo = tkFont.Font(family="Georgia", size=35, weight="bold")
        font_button = tkFont.Font(family="Calibri", size=15)
        font_verofalso = tkFont.Font(family="Calibri", size=25)
        self.titolo = tk.Frame(self.root, height=1, bg="#0d6bde")
        self.titolo.pack(fill="x", side="top")

        self.btnAvvio = tk.Label(self.titolo, text="Quiz 2025", width=15, height=1, font=font_titolo, bg="#0d6bde", )
        self.btnAvvio.pack(pady=20, side="left")

        self.lbl_errori = tk.Label(self.titolo, text=f"Domanda {self.errori_totali}", font=("Arial", 16), bg="#aec9d1", fg="white")
        self.lbl_errori.pack(pady=20, side="left", padx=30)

        self.immagine = tk.Frame(self.root, height=1, bg="#2cc4db")
        self.immagine.pack(fill="x", expand=False, side="top")

        self.label_immagini = tk.Label(self.immagine, bg="#2cc4db", highlightbackground="black", highlightthickness=2, bd=2, relief="solid")
        self.label_immagini.pack(pady=20, padx=20)

        self.frame_domanda = tk.Frame(self.root, height=1,bg="#37649e",)
        self.frame_domanda.pack(fill="x", expand=False)

        self.label_domanda = tk.Label(self.frame_domanda, text="", font=("Arial", 16),height=2)
        self.label_domanda.pack()
        
        self.btn_home = tk.Button(self.titolo, text="Home",font=font_button,width=20, command=self.home)
        self.btn_home.pack(pady=20,side="left", padx=30)

        self.istruine = tk.Button(self.titolo, text="Istruzioni",font=font_button,width=20,  command=self.istruzione)
        self.istruine.pack(pady=20, side="left", padx=30)


        self.Tempo = [30, 0]
        self.lbl_tempo = tk.Label(self.titolo, text=f"{self.Tempo[0]:02d}:{self.Tempo[1]:02d}", font=("Arial", 20), bg="lightblue", )
        self.lbl_tempo.pack(pady=20, padx=30, side="right")

        self.timerafter_id = self.root.after(1000, self.timer)

        # Bottoni risposta
        
        self.risposta_frame = tk.Frame(self.root,bg="white")
        self.risposta_frame.pack(expand=True,fill="y")
        tk.Button(self.risposta_frame, text="Vero", width=20,font=font_verofalso,bg="green", command=lambda: self.verifica_risposta("True")).pack(side="left", padx=20,pady=10)
        tk.Button(self.risposta_frame, text="Falso", width=20,font=font_verofalso,bg="red", command=lambda: self.verifica_risposta("False")).pack(side="left", padx=20)

        # Bottoni navigazione
        btn_frame = tk.Frame(self.root,bg="white")
        btn_frame.pack(expand=True,fill="y")

        self.btn_prev = tk.Button(btn_frame, text="    <<<<    ",font = font_button, command=self.prima_domanda)
        self.btn_prev.pack(side="left", padx=20)

        self.btn_next = tk.Button(btn_frame, text="    >>>>    ",font = font_button, command=self.prossima_domanda)
        self.btn_next.pack(side="left", padx=20)
        
        
        
        
        self.mostra_domanda()

    def timer(self):
        self.Tempo[1] -= 1
        if self.Tempo[1] < 0:
            self.Tempo[0] -= 1
            self.Tempo[1] = 59
            if self.Tempo[0] <= 0:
                messagebox.showinfo("Tempo Scaduto", f"Tempo finito! Errori: {self.errori}")
        self.lbl_tempo.config(text=f"{self.Tempo[0]:02d}:{self.Tempo[1]:02d}")
        self.timerafter_id = self.root.after(1000, self.timer)

    def mostra_domanda(self):
        domanda = questions[self.indice_domanda]
        percorso_img = domanda.get("img", "")
        testo_domanda = domanda.get("Domanda", "")

        self.label_domanda.config(text=testo_domanda)

        if percorso_img:
            percorso_completo = os.path.join(os.getcwd(), percorso_img)
            if percorso_img not in self.immagini_cache:
                try:
                    img = Image.open(percorso_completo)
                    img_resized = img.resize((300, 300))
                    foto = ImageTk.PhotoImage(img_resized)
                    self.immagini_cache[percorso_img] = foto
                except Exception as e:
                    print(f"Errore caricamento immagine: {e}")
                    self.label_immagini.config(image="", text="Errore immagine")
                    return
            self.label_immagini.config(image=self.immagini_cache[percorso_img], text="")
            self.label_immagini.image = self.immagini_cache[percorso_img]
        else:
            self.label_immagini.config(text="(Nessuna immagine)", image="")

    def verifica_risposta(self, risposta_utente):
        domanda = questions[self.indice_domanda]
        risposta_corretta = domanda.get("Risposta", "").strip()

        if risposta_utente != risposta_corretta:
            self.errori += 1
            if risposta_utente not in self.domande_sbagliate:
               self.domande_sbagliate.append(domanda.get("Domanda", ""))

        self.prossima_domanda()

    def prossima_domanda(self):
        if self.indice_domanda < len(questions) - 1:
            self.indice_domanda += 1
            self.errori_totali += 1
            self.lbl_errori.config(text=f"Domanda {self.errori_totali}")
            self.mostra_domanda()
        if self.errori_totali == 20:
            msg = f"Fine quiz!\nErrori totali: {self.errori}\n"
            if self.domande_sbagliate:
                    msg += "\nDomande sbagliate:\n" + "\n".join(f"- {d}" for d in self.domande_sbagliate)
                    messagebox.showinfo("Risultati", msg)
                    for iframe in self.root.winfo_children():
                     iframe.destroy()
                    inizio.Home_page(self.root)
            else:
                    msg = f"Fine quiz\nNon hai risposto a tutte le domande"
                    messagebox.showinfo("Bocciato",msg)
                    for iframe in self.root.winfo_children():
                     iframe.destroy()
                    inizio.Home_page(self.root)
          

    def prima_domanda(self):
        if self.indice_domanda > 0:
            self.indice_domanda -= 1
            self.errori_totali -= 1
            self.errori -= 1
            if self.errori_totali <= 0:
                self.errori = 0
                self.errori_totali = 0
            self.lbl_errori.config(text=f"Domanda {self.errori_totali}")
            self.mostra_domanda()
        else:
            messagebox.showinfo("Quiz","Questa è la prima domanda")

    def home(self):
        response = messagebox.askyesno("Confirm", "Dovrai ricominciare l'esame") 
        if response:    
            for iframe in self.root.winfo_children():
                iframe.destroy()
            inizio.Home_page(self.root)
    def istruzione(self):
        response = messagebox.askyesno("Confirm", "Dovrai ricominciare l'esame")     
        if response:
            for iframe in self.root.winfo_children():
                iframe.destroy()
            istruzione.patente_AM(self.root)
    

                