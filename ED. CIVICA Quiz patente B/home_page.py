import tkinter as tk
import tkinter.font as tkFont  
from libretto import patente_AM as instruzione1
from seconda import quiz as domande
from PIL import Image, ImageTk
from tkinter import messagebox
from home import PatentinoApp as patente
class Home_page():
    def __init__(self, root):
        self.root = root
        self.root.config(bg = "white")
        font_titolo = tkFont.Font(family="Arial", size=35, weight="bold")   
        self.root.title("Home Page")
        
        # Frame for the title section
        font_titolo = tkFont.Font(family="Arial", size=45, weight="bold")

        self.titolo = tk.Frame(self.root, height=1, bg="#0d6bde")
        self.titolo.pack(fill="x", side="top")

        self.tit = tk.Label(self.titolo, text="Quiz 2025", width=15, height=1, font=font_titolo, bg="#0d6bde", fg="white")
        self.tit.pack(pady=20)
        #Frame buttom
        sotto = tk.Frame(self.root, bg="#34abeb")
        sotto.pack(fill="x", expand=False,side="top")
        
        label_sotto = tk.Label(sotto, text="Creato da Okoro Ebosetale Wisdom", font=("Arial",20),height=1,bg="#34abeb")
        label_sotto.pack()
        
        #Frame centrale
        centro = tk.Frame(self.root,bg="blue")
        centro.pack(pady=30,padx=30,expand=True)
        
        avvia = tk.Button(centro,text="Prova",font=("Arial",20),width=25, height=1,borderwidth=2, relief="groove", command=self.interfaccia, fg="#000000", bg="#42f542")
        avvia.pack(pady=15,padx=15)
        inst = tk.Button(centro,text="Instruzioni",font=("Arial",20),width=25, height=1,borderwidth=2, relief="groove", command=self.istruzione, fg="#000000", bg="#42f542")
        inst.pack(pady=15,padx=15)
        back = tk.Button(centro,text="Indietro",font=("Arial",20),width=25, height=1,borderwidth=2, relief="groove", command=self.back, fg="#000000", bg="#42f542")
        back.pack(pady=15,padx=15)
        Esci = tk.Button(centro,text="Esci",font=("Arial",20),width=25, height=1,borderwidth=2, relief="groove", command=self.root.destroy, fg="#000000", bg="#42f542")
        Esci.pack(pady=15,padx=15)
        
        # Prima immagine
        image1 = Image.open("patente_2.jpg") 
        image1 = image1.resize((450, 260))
        self.img_logo_europea_1 = ImageTk.PhotoImage(image1)
        self.logo_europea_1 = tk.Label(self.root, image=self.img_logo_europea_1, borderwidth=5, relief="solid")
        self.logo_europea_1.image = self.img_logo_europea_1  
        self.logo_europea_1.place(x=15, y=420)

        # Seconda immagine
        image2 = Image.open("patente_immagine.jpg") 
        image2 = image2.resize((450, 260))
        self.img_logo_europea_2 = ImageTk.PhotoImage(image2)
        self.logo_europea_2 = tk.Label(self.root, image=self.img_logo_europea_2, borderwidth=5, relief="solid")
        self.logo_europea_2.image = self.img_logo_europea_2  
        self.logo_europea_2.place(x=1000, y=420)  
        # Label titolo sotto
        self.titolo_sotto = tk.Label(self.root, text="Driver Licence 2025",font = font_titolo,bg="white").place( y = 200,x = 445   )
    def istruzione(self):
        for iframe in self.root.winfo_children():
            iframe.destroy()
        instruzione1.patente_AM(self.root)
    def interfaccia(self):
        rispondi = messagebox.askyesno("Confirm", "Hai letto le istruzioni?")   
        if rispondi:
            for iframe in self.root.winfo_children():
                iframe.destroy()
            domande(self.root)
        else:
            messagebox.showerror("Error", "Devi prima leggere le istruzioni!!!")
    def back(self):
        for iframe in self.root.winfo_children():
            iframe.destroy()
        patente(self.root)
        
        
        