import pygame , sys
import folder.content as content
class FinestraDiOpzioni:
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        running = True
        while running:
            self.screen.fill("white")
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            # Testo della schermata opzioni
            OPTIONS_TEXT = content.get_font(45).render("How to play", True, "Black")
            OPTIONS_TEXT2 = content.get_font(20).render("")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

            # Bottone BACK
            OPTIONS_BACK = content.Button(
                image=None,
                pos=(640, 460),
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
