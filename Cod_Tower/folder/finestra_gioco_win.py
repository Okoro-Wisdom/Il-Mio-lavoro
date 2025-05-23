import pygame, sys
import folder.content as content

class FinestraDiGiocoWin:
    def __init__(self, screen):
        self.screen = screen
        # Pulsante per rifare il gioco (Restart)
        self.button_restart = content.Button(
            image=None,
            pos=(420, 460),
            text_input="RESTART",
            font=content.get_font(75),
            base_color="Black",
            hovering_color="Green"
        )
        # Pulsante per uscire
        self.button_exit = content.Button(
            image=None,
            pos=(860, 460),
            text_input="Exit",
            font=content.get_font(75),
            base_color="Black",
            hovering_color="Green"
        )

    def run(self):
        running = True
        while running:
            self.screen.fill("white")  # Sfondo bianco
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            # Messaggio di vittoria
            OPTIONS_TEXT = content.get_font(45).render("You won!", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

            # Aggiorna e disegna i bottoni
            self.button_restart.changeColor(OPTIONS_MOUSE_POS)
            self.button_restart.update(self.screen)

            self.button_exit.changeColor(OPTIONS_MOUSE_POS)
            self.button_exit.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_restart.checkForInput(OPTIONS_MOUSE_POS):
                        # Implementa la logica per rifare il gioco
                        running = False
                        # Potresti voler chiamare una funzione per riavviare il gioco
                        # ad esempio: self.restart_game()
                    elif self.button_exit.checkForInput(OPTIONS_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
