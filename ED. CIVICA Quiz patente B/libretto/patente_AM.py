import tkinter as tk
import tkinter.font as tkFont
import libretto.esame_teoria as teoria
import home_page as inizio
import seconda as esame_quiz
import tkinter.messagebox as messagebox
class patente_AM():
    def __init__(self, root):
        self.root = root

        # Font    
        self.fancy_font = tkFont.Font(
            family="Comic Sans MS", 
            size=12, 
            slant="italic", 
        )
        self.title_font = tkFont.Font(
            family="Helvetica",
            size=32, 
            weight="bold",
            slant="italic",
        )

        self.subtitle_font = tkFont.Font(
            family="Arial", 
            size=18, 
            weight="bold",
        )

        # Frame superiore (per il titolo)
        self.top_frame = tk.Frame(self.root, pady=20)
        self.top_frame.pack(fill='x')
        self.top_frame.config(bg="lightblue")
        self.label_titolo = tk.Label(self.top_frame, text="Patente AM", bg="lightblue", font=self.title_font)
        self.label_titolo.pack(pady=20, padx=30, side="left")

        # Frame sottotitolo
        self.middle_frame = tk.Frame(self.root, pady=10, bg='white')
        self.middle_frame.pack(fill="x")
        self.label_sottotitolo = tk.Label(self.middle_frame, text="Istruzioni", font=self.subtitle_font, bg="white")
        self.label_sottotitolo.pack(pady=10, padx=30, side="left")

        # Frame centro
        self.label_testo = tk.Frame(self.root, pady=0)
        self.label_testo.pack(fill="x", expand=True)
        self.label_testo.config(bg="white")
        self.label1 = tk.Label(
            self.label_testo, 
            text="""La patente AM può essere conseguita a 14 anni e consente di guidare:

            --> Ciclomotori a due ruote o tre ruote con velocità massima di costruzione non superiore a 45 km/h, la cui cilindrata è inferiore o uguale a 50 cm³ se a combustione interna, oppure 
                 la cui potenza nominale continua massima è inferiore o uguale a 4 kW per i motori elettrici
            --> Quadricicli leggeri la cui massa a vuoto è inferiore o pari a 350 kg, esclusa la massa delle batterie per i veicoli elettrici, la cui velocità massima per costruzione è inferiore o uguale 
                 a 45 km/h e la cui cilindrata del motore è inferiore o pari a 50 cm³ per i 
                 motori ad accensione comandata; o la cui potenza massima netta è inferiore o uguale a 4 kW per gli altri motori, a combustione interna;
                 o la cui potenza nominale continua massima è inferiore o uguale a 4 kW per i motori elettrici 
            
            -->Come si consegue la patente AM nelle nostre Autoscuole
                 Nelle nostre autoscuole puoi frequentare un corso che ti prepara alla guida del ciclomotore sia per quanto riguarda la teoria sia per la pratica. Le lezioni sono svolte da insegnanti
                 preparati che ti aiutano ad assimilare progressivamente i concetti e i movimenti fondamentali, grazie all’innovativo Metodo La Nuova Guida.

                 Per conseguire la Patente AM dovrai aver compiuto 14 anni, frequentare lezioni teoriche e corsi di guida e superare la prova 
                 teorica e quella pratica. Una volta superata la prova teorica, nella nostra autoscuola riceverai il Foglio Rosa, che ha validità dodici mesi e consente le esercitazioni su strada.""" ,
            font=self.fancy_font, 
            bg='lightblue', 
            justify="left",
            anchor="w",
            width=40,
            height=20,
            relief="raised",
            bd=2,
            highlightbackground="lightblue", 
            highlightcolor="orange"
        )
        self.label1.pack(pady=10, padx=10, side="left", fill="x", expand=True)

        #Button prossimo
        button_pre = tk.Button(self.middle_frame,text=">>>>",borderwidth=2, relief="groove",width=30,height=2,command=self.prossima)
        button_pre.pack(padx=10,pady=20,side="right")
        
        #Button home
        button_home = tk.Button(self.top_frame,text="Home",borderwidth=2, relief="groove",width=30,height=2,command=self.home)
        button_home.pack(padx=10,pady=20,side="right")
        

        # Frame inferiore (per i bottoni)
        self.bottom_frame = tk.Frame(self.root, pady=10)
        self.bottom_frame.pack()

        #Button esercitazione 
        button_pre = tk.Button(self.top_frame,text="Quiz esame",borderwidth=2, relief="groove",width=30,height=2,command=self.esame)
        button_pre.pack(padx=10,pady=20,side="right")

        

    def prossima(self):
        for iframe in self.root.winfo_children():
            iframe.destroy()
        teoria.istruzioni(self.root)
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

   
        

