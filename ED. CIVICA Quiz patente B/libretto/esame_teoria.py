import tkinter as tk
import tkinter.font as tkFont
import libretto.patente_AM as patente
import home_page as inizio
from tkinter import messagebox
import seconda as esame_quiz
class istruzioni():
    def __init__(self,root):
        self.root = root

        #Font    
        fancy_font = tkFont.Font(
            family="Comic Sans MS", 
            size=11, 
            slant="italic", 
        )
        title_font = tkFont.Font(
            family="Helvetica",
            size=32, 
            weight="bold",
            slant="italic",
            
        )
        
        subtitle_font = tkFont.Font(
            family="Arial", 
            size=18, 
            weight="bold",
        )
        
        # Frame superiore (per il titolo)
        top_frame = tk.Frame(self.root, pady=20)
        top_frame.pack(fill='x')
        top_frame.config(bg="lightblue")
        label_titolo = tk.Label(top_frame,text="Esame di teoria",bg="lightblue",font=title_font)
        label_titolo.pack(pady=20,padx=30,side="left")
        # Frame sottotitolo
        middle_frame = tk.Frame(self.root,pady=10, bg='white')
        middle_frame.pack(fill="x")
        label_sottotitolo = tk.Label(middle_frame,text="Istruzioni",font=subtitle_font,bg="white")
        label_sottotitolo.pack(pady=10,padx=30, side="left")
        # Frame centro
        label_testo = tk.Frame(self.root,pady=0)
        label_testo.pack(fill="x", expand=True)
        label_testo.config(bg="white",)
        label1 = tk.Label(
            label_testo, 
            text="""La Patente AM si consegue dopo il superamento di due esami: la teoria e la pratica. 

                La prova teorica prevede 30 affermazioni, per le quali stabilire se sono Vere o False, e sono ammessi massimo 3 errori. La durata dell’esame è di 25 minuti. 

                Gli argomenti su cui verte l'esame di teoria:

                a) segnali di pericolo e segnali di precedenza
                b) segnali di divieto
                c) segnali di obbligo
                d) segnali di indicazione e pannelli integrativi
                e) norme sulla precedenza
                f) norme di comportamento
                g) segnali luminosi, segnali orizzontali
                h) fermata, sosta e definizioni stradali
                i) cause di incidenti e comportamenti dopo gli incidenti, assicurazione
                l) elementi del ciclomotore e loro uso
                m) comportamenti alla guida del ciclomotore e uso del casco
                n) valore e necessità della regola
                o) rispetto della vita e comportamento solidale
                p) la salute
                q) rispetto dell’ambiente
                r) elementari conoscenze sul funzionamento dei ciclomotori in caso di emergenza.

                """, 
            font=fancy_font, 
            bg='lightblue', 
            justify="left",
            anchor="w",
            width=40,
            relief="raised",
            bd=2,
            highlightbackground="lightblue", 
            highlightcolor="orange"
            
        )
        label1.pack(pady=10,padx=10,side="left",fill="x",expand=True)

        

        # Frame inferiore (per i bottoni)
        bottom_frame = tk.Frame(self.root, pady=10)
        bottom_frame.pack()
        
        #Button precedente 
        button_pre = tk.Button(middle_frame,text="<<<<",borderwidth=2, relief="groove",width=30,height=2,command=self.prossima)
        button_pre.pack(padx=10,pady=20,side="right")

        #Button home
        button_home = tk.Button(top_frame,text="Home",borderwidth=2, relief="groove",width=30,height=2,command=self.home)
        button_home.pack(padx=10,pady=20,side="right")

        #Button esercitazione 
        button_pre = tk.Button(top_frame,text="Quiz esame",borderwidth=2, relief="groove",width=30,height=2,command=self.esame)
        button_pre.pack(padx=10,pady=20,side="right")

        

       
    def prossima(self):
       for iframe in self.root.winfo_children():
            iframe.destroy()
       patente.patente_AM(self.root)
    def home(self):
        for iframe in self.root.winfo_children():
            iframe.destroy()
        inizio.Home_page(self.root)
    def esame(self):
        response = messagebox.askyesno("Confirm", "Iniziera l'esame,sei sicuro?")     
        if response:
            for iframe in self.root.winfo_children():
                iframe.destroy()
            esame_quiz.quiz(self.root)
        
        

