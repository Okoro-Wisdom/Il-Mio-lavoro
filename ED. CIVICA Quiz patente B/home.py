import tkinter as tk
from tkinter.font import Font
class Base(tk.Frame):
    # Costruttore
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Scheda patentino 2025")
        self.master.geometry("1920x1080")
        self.master.resizable(0,0) 
        self.pack()
        self.crea_widgets()

    def crea_widgets(self):
        #font
        font_titolo = Font(family = "Calibri",size = 20)
        #titolo
        self.lbltitolo = tk.Label(self, text = "Scheda patentino 2025",font = font_titolo, fg = "#ff0000",bg = "#e0ffff")
        self.lbltitolo.pack(fill=tk.BOTH,expand=True)
        #Label esercizi
        self.lbles1 = tk.Label(self, text = "1")
        self.lbles1.pack(side=tk.LEFT)
        self.lbles2 = tk.Label(self, text = "2")
        self.lbles2.pack(side=tk.LEFT)
        

        self.btnEsci = tk.Button(self,text = "Esci",font = font_titolo,command=self.master.destroy)
        self.btnEsci.pack(side = tk.LEFT)
def main():    
    root = tk.Tk()   
    app = Base(master=root) 
    app.mainloop() 
main()