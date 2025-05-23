import pygame, sys
import folder.content as content

class FinestraDiGiocoLose:
    def __init__(self, screen):
        self.screen = screen

       
        self.button_redo = content.Button(
            image=None,
            pos=(420, 460),
            text_input="REDO",
            font=content.get_font(75),
            base_color="Black",
            hovering_color="Green"
        )

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
            self.screen.fill((0, 0, 255))  # Colore blue
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

           
            OPTIONS_TEXT = content.get_font(45).render("You lost.", True, (0, 0, 0))
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)


            self.button_redo.changeColor(OPTIONS_MOUSE_POS)
            self.button_redo.update(self.screen)

            self.button_exit.changeColor(OPTIONS_MOUSE_POS)
            self.button_exit.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_redo.checkForInput(OPTIONS_MOUSE_POS):        
                        running = False 
                    elif self.button_exit.checkForInput(OPTIONS_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
