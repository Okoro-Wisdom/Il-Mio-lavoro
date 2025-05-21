from PIL import Image, ImageTk
import tkinter as tk
from tkinter.font import Font
from domande import DOM as questions
import random 

import home_page as pagina_base
class PatentinoApp(tk.Frame):
    def __init__(self, root):
        self.root = root

        # Background
        self.bg_label = tk.Label(self.root, bg="#f542bf") 
        self.bg_label.place(relwidth=1, relheight=1) 

        # Font
        font_titolo = Font(family="Georgia", size=45, weight="bold")
        font_titolo2 = Font(family="Segoe UI", size=40)
        font_titolo3 = Font(family="Segoe UI", size=50)
        font_button = Font(family="Calibri", size=40)

        # Titolo
        self.lbl_titolo_1 = tk.Label(self.root, text="SCHEDA PATENTINO 2025", font=font_titolo, bg="#d368e3")
        self.lbl_titolo_1.place(x=620, y=50)
        
        # Titolo 2 
        self.lbl_titolo_2 = tk.Label(self.root, text="Patente interistituzionale della", font=font_titolo2, bg="#d368e3")
        self.lbl_titolo_2.place(x=620, y=130)
        
        # Titolo 3
        self.lbl_titolo_3 = tk.Label(self.root, text="REGIONE\nPIEMONTE ", font=font_titolo3, bg="#d368e3")
        self.lbl_titolo_3.place(x=840, y=240)
        
        # Logo bandiera piemonte
        image = Image.open("bandiera_piemonte.png") 
        image = image.resize((180, 170))
        self.img_logo = ImageTk.PhotoImage(image)
        self.logo = tk.Label(self.root, image=self.img_logo, borderwidth=5, relief="solid")
        self.logo.image = self.img_logo  
        self.logo.place(x=620, y=240)
        
        # Logo bandiera europea
        image = Image.open("bandiera_europea.png") 
        image = image.resize((500, 310))
        self.img_logo_europea = ImageTk.PhotoImage(image)
        self.logo_europea = tk.Label(self.root, image=self.img_logo_europea, borderwidth=5, relief="solid")
        self.logo_europea.image = self.img_logo_europea  
        self.logo_europea.place(x=70, y=50)
        
        # Logo guida
        image = Image.open("guida.png") 
        image = image.resize((500, 310))
        self.img_logo_guida = ImageTk.PhotoImage(image)
        self.logo_guida = tk.Label(self.root, image=self.img_logo_guida, borderwidth=5, relief="solid")
        self.logo_guida.image = self.img_logo_guida  
        self.logo_guida.place(x=70, y=440)
        
        # Bottone Avvio
        self.btnAvvio = tk.Button(self.root, text="Avvio", font=font_button, width=25, height=1,borderwidth=2, relief="groove", command=self.interfaccia, fg="#000000", bg="#42f542")
        self.btnAvvio.place(x=670, y=500)

        # Bottone Esci
        self.btnEsci = tk.Button(self.root, text="Esci", font=font_button, width=25, height=1,borderwidth=2, relief="groove", command=self.root.destroy, fg="#000000", bg="#e62727")
        self.btnEsci.place(x=670, y=620)
        
        # Inizializza contatori
        self.corrent_count = 0
        self.correct_count = 0
        self.error_count = 0

    def interfaccia(self):
        for iframe in self.root.winfo_children():
            iframe.destroy()
        pagina_base.Home_page(self.root)

# Avvio dell'app
def main():
    root = tk.Tk()
    root.title("Scheda patentino 2025")
    root.geometry("1480x800")
    root.resizable(0, 0)
    PatentinoApp(root)
    root.mainloop()

main()
