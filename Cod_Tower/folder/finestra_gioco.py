import pygame
import json
import math
import folder.content as content
import folder.finestra_gioco_win as FinestraGiocoWin
import folder.finestra_gioco_lose as FinestraGiocoLose
import random

# Dimensioni dello schermo
SCREEN_WIDTH = content.SIZE_FRAME_X
SCREEN_HEIGHT = content.SIZE_FRAME_Y
NUMEOR_ORADA_MASSIMA = 20

# Costanti per le dimensioni della cella
CELL_SIZE = 128  # La dimensione della cella della griglia
GRID_SIZE = 11  # La dimensione della griglia (10x10)

class FinestraDiGioco:
    def __init__(self, screen):
        self.screen = screen
        self.torrette = []
        self.nemici = []
        self.path_rects = []
        self.griglia_celle = 10  # La dimensione della griglia (10x10)
        self.load_map("valley")
        self.soldi = 250  # Soldi iniziali
        self.vita_base = 1000

        # Carica immagini torrette
        self.sniper_img = pygame.image.load("assets/img/sniper.png").convert_alpha()
        self.minigun_img = pygame.image.load("assets/img/minigun.png").convert_alpha()
        self.rocket_img = pygame.image.load("assets/img/rocket.png").convert_alpha()

        self.background_img = pygame.image.load("assets/img/background_game.png").convert()  # Assicurati che l'immagine sia in un formato supportato

        self.turret_options = [
            {"tipo": "sniper", "prezzo": 1500, "immagine": self.sniper_img},
            {"tipo": "minigun", "prezzo": 250, "immagine": self.minigun_img},
            {"tipo": "rocket", "prezzo": 750, "immagine": self.rocket_img},
        ]
        self.selected_slot = None  # Track selected slot for turret purchase
        self.show_turret_menu = False  # To toggle turret selection menu visibility

    def load_map(self, nome):
        with open(f"assets/mappe/{nome}.json") as file:
            GAME_MAP_DATA = json.load(file)
            self.path = GAME_MAP_DATA["path"]
            self.slot = GAME_MAP_DATA["slot"]
            self.nome = GAME_MAP_DATA["nome"]

        # Carica immagini strada e curva
        self.path_img = pygame.image.load("assets/img/strada.png").convert_alpha()

        # Calcola il fattore di scala per adattare la mappa allo schermo
        self.scale_x = SCREEN_WIDTH / (GRID_SIZE * CELL_SIZE)  # Calcola la scala orizzontale
        self.scale_y = SCREEN_HEIGHT / (GRID_SIZE * CELL_SIZE)  # Calcola la scala verticale

        cambio_direzione = False
        for i in range(1, len(self.path)):
            x0, y0 = self.path[i - 1]
            x1, y1 = self.path[i]
            dx = x1 - x0
            dy = y1 - y0

            if dx != 0:
                step = 1 if dx > 0 else -1
                for x in range(x0, x1, step):
                    px = x * CELL_SIZE * self.scale_x
                    py = y0 * CELL_SIZE * self.scale_y
                    rect = self.path_img.get_rect(topleft=(px, py))
                    self.path_rects.append({"rect":rect,"img":self.path_img})

            elif dy != 0:
                step = 1 if dy > 0 else -1
                for y in range(y0, y1, step):
                    px = x0 * CELL_SIZE * self.scale_x
                    py = y * CELL_SIZE * self.scale_y
                    rect = self.path_img.get_rect(topleft=(px, py))
                    self.path_rects.append({"rect":rect,"img":pygame.transform.rotate(self.path_img, 90)})

    def disegna_mappa(self):
        for path in self.path_rects:
            self.screen.blit(path["img"],path["rect"].topleft)
            

        
    def aggiorna_nemici(self):
        for nemico in self.nemici:
            nemico.aggiorna(self.screen,self)
        self.nemici = [n for n in self.nemici if n.vita > 0]

    def aggiorna_torrette(self):
        for torretta in self.torrette:
            torretta.aggiorna(self.nemici,self.screen,self)

    def compra_torretta(self, tipo_torretta, posizione_slot):
        if self.soldi >= tipo_torretta["prezzo"]:
            self.soldi -= tipo_torretta["prezzo"]
            nuova_torretta = Torretta(tipo_torretta["tipo"], posizione_slot, tipo_torretta["immagine"], tipo_torretta["prezzo"])
            self.torrette.append(nuova_torretta)
            self.show_turret_menu = False  # Hide menu after purchase

    def mostra_soldi(self):
        font = pygame.font.Font(None, 36)
        testo_soldi = font.render(f"Soldi: {self.soldi}", True, (255, 255, 255))
        self.screen.blit(testo_soldi, (10, 10))

    def mostra_wave(self):
        font = pygame.font.Font(None, 36)
        testo_soldi = font.render(f"Wave: {self.numero_ondata} / {NUMEOR_ORADA_MASSIMA} ", True, (255, 255, 255))
        self.screen.blit(testo_soldi, (SCREEN_WIDTH- SCREEN_WIDTH*0.5, 10))

    def mostra_vita_base(self):
        font = pygame.font.Font(None, 36)
        testo_soldi = font.render(f"Vita: {self.vita_base}", True, (255, 255, 255))
        self.screen.blit(testo_soldi, (SCREEN_WIDTH- SCREEN_WIDTH*0.1, 10))

    def disegna_menu_torrette(self,menu_x,menu_y):
     menu_width = 400
     menu_height = len(self.turret_options) * 120 + 120

    # Disegna il background del menu
     pygame.draw.rect(self.screen, (30, 30, 30), (menu_x, menu_y, menu_width, menu_height), border_radius=15)
     pygame.draw.rect(self.screen, (255, 255, 255), (menu_x, menu_y, menu_width, menu_height), width=3, border_radius=15)

     font_title = pygame.font.Font(None, 48)
     title_text = font_title.render("SELEZIONA TORRETTA", True, (255, 255, 255))
     self.screen.blit(title_text, (menu_x + 10, menu_y + 20))

     mouse_pos = pygame.mouse.get_pos()
     mouse_click = pygame.mouse.get_pressed()[0]

     # Disegna le torrette disponibili nel menu
     for i, turret in enumerate(self.turret_options):
         y_offset = menu_y + 80 + i * 110

         self.screen.blit(turret["immagine"], (menu_x + 40, y_offset))

         font_price = pygame.font.Font(None, 36)
         price_text = font_price.render(f"${turret['prezzo']}", True, (255, 255, 255))
         self.screen.blit(price_text, (menu_x + 120, y_offset + 25))

         button_rect = pygame.Rect(menu_x + 30, y_offset, 300, 80)
         pygame.draw.rect(self.screen, (0, 255, 0), button_rect, 2 if button_rect.collidepoint(mouse_pos) else 1)

         if mouse_click and button_rect.collidepoint(mouse_pos):
               self.compra_torretta(turret, self.selected_slot)

      # Aggiungi il pulsante "Annulla"
     cancel_button_rect = pygame.Rect(menu_x + 30, menu_y + menu_height - 100, 300, 80)
     pygame.draw.rect(self.screen, (255, 0, 0), cancel_button_rect, 2 if cancel_button_rect.collidepoint(mouse_pos) else 1)

     cancel_font = pygame.font.Font(None, 36)
     cancel_text = cancel_font.render("ANNULLA", True, (255, 255, 255))
     self.screen.blit(cancel_text, (menu_x + 120, menu_y + menu_height - 85))

     # Se clicchi su "Annulla", chiude il menu
     if mouse_click and cancel_button_rect.collidepoint(mouse_pos):
          self.show_turret_menu = False  # Chiude il menu

    def genera_ondata(self):
        for i in range(self.numero_ondata * 4):
           self.nemici.append(Terminator(self.path, self.scale_x, self.scale_y,self.numero_ondata-1))
    
        for i in range(self.numero_ondata * 3):
           self.nemici.append(Assault(self.path, self.scale_x, self.scale_y,self.numero_ondata-1))
    
        for i in range(self.numero_ondata * 2):
            self.nemici.append(Tank(self.path, self.scale_x, self.scale_y,self.numero_ondata-1))


    def run(self):
        running = True
        self.show_turret_menu_pos = [0,10]
        clock = pygame.time.Clock()
        self.numero_ondata = 0
        
        self.genera_ondata()

        while running:
            if len(self.nemici) == 0:
                self.numero_ondata += 1
                if self.numero_ondata > NUMEOR_ORADA_MASSIMA:
                   gioco = FinestraGiocoWin.FinestraDiGiocoWin(self.screen)
                   gioco.run()
                else:
                   self.genera_ondata()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Termina il ciclo se l'utente chiude la finestra
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False  # Termina il ciclo se l'utente preme "Esc"

            # Disegna lo sfondo ripetuto
            for x in range(0, SCREEN_WIDTH, self.background_img.get_width()):
                for y in range(0, SCREEN_HEIGHT, self.background_img.get_height()):
                    self.screen.blit(self.background_img, (x, y))

            # Disegna mappa
            self.disegna_mappa()

            # UI - Mostra i soldi
            self.mostra_soldi()
            
            self.mostra_vita_base()

            self.mostra_wave()

            # Gestisci il menu per acquistare torrette
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            # Gestisci il clic sulla mappa per aprire il menu
            for slot in self.slot:
                slot_pos = tuple(slot)  # Convertiamo slot_pos in una tupla
                x, y = slot_pos

                # Se la torretta è già stata comprata, mostra la torretta al posto del "+"
                if any(t.posizione == slot_pos for t in self.torrette):
                    torretta_presenti = [t for t in self.torrette if t.posizione == slot_pos]
                else:
                    # Pulsante per acquistare torretta (con il simbolo "+")
                    BUY_BUTTON = content.Button(
                        image=None,
                        pos=(x * CELL_SIZE, y * CELL_SIZE+50),
                        text_input="X",
                        font=content.get_font(20),
                        base_color="White",
                        hovering_color="Green"
                    )
                    BUY_BUTTON.changeColor(PLAY_MOUSE_POS)
                    BUY_BUTTON.update(self.screen)

                    # Verifica il clic del mouse
                    if pygame.mouse.get_pressed()[0]:
                        if BUY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                            self.selected_slot = slot_pos
                            self.show_turret_menu = True  # Mostra il menu delle torrette
                            self.show_turret_menu_pos = PLAY_MOUSE_POS

            # Menu delle torrette
            if self.show_turret_menu:
                self.disegna_menu_torrette(self.show_turret_menu_pos[0]+50,self.show_turret_menu_pos[1]-100)  # Passa la posizione del mouse per il menu

            self.aggiorna_nemici()
            self.aggiorna_torrette()


            pygame.display.update()
            clock.tick(3000)

        pygame.quit()

class Nemico:
    def __init__(self, immagini, path, vita, velocita, scale_x=1.0, scale_y=1.0):
       self.immagini = immagini
       self.path = path
       self.vita_massima = vita
       self.vita = vita
       self.velocita = velocita + random.random() * 0.3
       self.indice_punto = 0
       self.scale_x = scale_x
       self.scale_y = scale_y
       self.x, self.y = path[0][0] * CELL_SIZE * scale_x, path[0][1] * CELL_SIZE * scale_y
       self.image = immagini[0]
       self.rect = self.image.get_rect(center=(self.x, self.y))


    def aggiorna(self,screen,finestra_di_gioco):
        if self.indice_punto < len(self.path) - 1:
            x1, y1 = self.path[self.indice_punto]
            x2, y2 = self.path[self.indice_punto + 1]

            x1 *= CELL_SIZE * self.scale_x
            y1 *= CELL_SIZE * self.scale_y
            x2 *= CELL_SIZE * self.scale_x
            y2 *= CELL_SIZE * self.scale_y

            dx, dy = x2 - x1, y2 - y1
            distanza = math.hypot(dx, dy)

            if distanza != 0:
                dx /= distanza
                dy /= distanza

            self.x += dx * self.velocita
            self.y += dy * self.velocita

            if math.hypot(self.x - x2, self.y - y2) < 20:
                self.indice_punto += 1

            self.rect.center = (self.x+CELL_SIZE/2, self.y+CELL_SIZE/2)

            self.disegna(screen)
        else: 
            finestra_di_gioco.vita_base -= self.vita
            self.vita = 0
            if finestra_di_gioco.vita_base < 0:
                gioco = FinestraGiocoLose.FinestraDiGiocoLose(finestra_di_gioco.screen)
                gioco.run()


    def disegna(self,screen):
        screen.blit(self.image, self.rect.topleft)

        # Barra della vita
        barra_larghezza = self.rect.width
        rapporto_vita = self.vita / self.vita_massima
        barra_colore = (0, 255, 0) if rapporto_vita > 0.5 else (255, 0, 0)
        pygame.draw.rect(screen, (0, 0, 0), (self.rect.left, self.rect.top - 10, barra_larghezza, 5))
        pygame.draw.rect(screen, barra_colore, (self.rect.left, self.rect.top - 10, barra_larghezza * rapporto_vita, 5))

class Torretta:
    def __init__(self, tipo, posizione, immagine, prezzo):
        self.tipo = tipo
        self.posizione = posizione
        self.immagine_orig = immagine  # Salva l'immagine originale per ruotarla
        self.immagine = immagine
        self.prezzo = prezzo
        self.rect = self.immagine.get_rect(center=(posizione[0] * CELL_SIZE, posizione[1] * CELL_SIZE+50))
        
        # Impostazioni specifiche per ogni tipo di torretta
        self.danno = {"sniper": 300, "minigun": 15, "rocket": 70}[tipo]
        self.velocita_fuoco = {"sniper": 100, "minigun": 10, "rocket": 80}[tipo]
        self.raggio = {"sniper": 550, "minigun": 300, "rocket": 200}[tipo]  # Differenti raggi per ogni tipo di torretta
        self.timer_attacco = 0
        self.angolo = 0

    def aggiorna(self, nemici,screen,finestra_di_gioco):
        self.timer_attacco += 1
        bersaglio = None

        # Trova il nemico nel raggio di attacco
        for nemico in nemici:
            distanza = math.hypot(nemico.rect.centerx - self.rect.centerx,
                                  nemico.rect.centery - self.rect.centery)
            if distanza <= self.raggio:  # Considera il raggio diverso per ogni torretta
                bersaglio = nemico
                break  # Colpisce solo il primo nemico a portata

        if bersaglio:
            # Calcola l'angolo della torretta verso il nemico
            dx = bersaglio.rect.centerx - self.rect.centerx
            dy = bersaglio.rect.centery - self.rect.centery
            self.angolo = math.degrees(math.atan2(-dy, dx)) - 90  # Calcola angolo diretto

            # Normalizza l'angolo per evitare valori negativi
            if self.angolo < 0:
                self.angolo += 360

            # Gestisci l'attacco in base alla velocità di fuoco
            if self.timer_attacco >= self.velocita_fuoco:
                if self.tipo == "rocket":
                    # Danno ad area per il razzo
                    raggio_esplosione = 70
                    for nemico in nemici:
                        distanza = math.hypot(nemico.rect.centerx - bersaglio.rect.centerx,
                                              nemico.rect.centery - bersaglio.rect.centery)
                        if distanza <= raggio_esplosione:
                            nemico.vita -= int(self.danno * 0.7)  # I razzi fanno danno a più nemici
                else:
                    bersaglio.vita -= self.danno  # Danno diretto al nemico
                
                finestra_di_gioco.soldi += 2
                
                self.timer_attacco = 0  # Reset del timer per il prossimo attacco
        self.disegna(screen)

    def disegna(self,screen):
        # Ruota l'immagine verso l'angolo calcolato
        immagine_rotata = pygame.transform.rotate(self.immagine_orig, self.angolo)
    
        # Calcola il nuovo rect per l'immagine ruotata
        nuovo_rect = immagine_rotata.get_rect(center=self.rect.center)

        # Posiziona l'immagine ruotata nel punto giusto
        screen.blit(immagine_rotata, nuovo_rect.topleft)

        # (Opzionale) Visualizza il raggio d'azione per il debug
        #pygame.draw.circle(screen, (255, 0, 0), self.rect.center, self.raggio, 1)

class Terminator(Nemico):
    def __init__(self, path, scale_x=1.0, scale_y=1.0,ondata = 0):
        img = pygame.image.load("assets/img/terminator.png").convert_alpha()
        super().__init__([img], path, vita=200+(ondata*10), velocita=1.2, scale_x=scale_x, scale_y=scale_y)

class Assault(Nemico):
    def __init__(self, path, scale_x=1.0, scale_y=1.0,ondata = 0):
        img = pygame.image.load("assets/img/assault.png").convert_alpha()
        super().__init__([img], path, vita=100+(ondata*10), velocita=1.8, scale_x=scale_x, scale_y=scale_y)

class Tank(Nemico):
    def __init__(self, path, scale_x=1.0, scale_y=1.0,ondata = 0):
        img = pygame.image.load("assets/img/tank.png").convert_alpha()
        super().__init__([img], path, vita=700+(ondata*10), velocita=0.7, scale_x=scale_x, scale_y=scale_y)
