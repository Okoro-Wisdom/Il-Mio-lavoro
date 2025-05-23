import pygame , sys
import folder.content as content
class FinestraDiOpzioni:
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        running = True
        while running:
            self.screen.fill("yellow")
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            # Testo della schermata opzioni
            OPTIONS_TEXT = content.get_font(45).render("How the game works", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(630, 140))

            # Testo lungo
            text_lines = [
                "- In questo gioco devi uccidere i robot che stanno correndo verso la tua base.",
                "- Puoi difenderti piazzando delle torrette nelle X che vedi nella mappa.",
                "- Queste torrette costano soldi,che guadagni ogni volta che danneggi i robot",
                "- Hai in tutto 1000 di vita e se un robot arriva nella tua base perdi della vita",
                "- Puoi vedere il numero delle wave in alto in centro",
                "- Quando piazzi una torretta sappi che non potrai toglierlo",
                "- Arriva a wave 20 per vincere e diventare il protettore del nuovo GEN",
                                        
            ]
            font = pygame.font.Font(None, 35)
            rendered_lines = [font.render(line, True, "Black") for line in text_lines]
            # Posizione iniziale
            x, y = 150, 250
            line_spacing = 10  # Spazio tra le linee

            # Disegna le linee sullo schermo
            for rendered_line in rendered_lines:
                self.screen.blit(rendered_line, (x, y))
                y += rendered_line.get_height() + line_spacing
            self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

            # Bottone BACK
            OPTIONS_BACK = content.Button(
                image=None,
                pos=(620, 640),
                text_input="BACK",
                font=content.get_font(75),
                base_color="Black",
                hovering_color="Green"
            )

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        running = False  # Torna al menu principale

            pygame.display.update()
