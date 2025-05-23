import pygame
import sys
import folder.content as content
from folder.finestra_gioco import FinestraDiGioco
from folder.finestra_opzioni import FinestraDiOpzioni

class MainMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((content.SIZE_FRAME_X, content.SIZE_FRAME_Y))
        pygame.display.set_caption("Menu")
        self.BG = pygame.image.load("assets/img/background_main.png").convert()

        # Creazione dei bottoni
        self.play_button = content.Button(
            image=pygame.image.load("assets/img/Play Rect.png"),
            pos=(640, 250),
            text_input="PLAY",
            font=content.get_font(75),
            base_color="#d7fcd4",
            hovering_color="White"
        )
        self.options_button = content.Button(
            image=pygame.image.load("assets/img/Options Rect.png"),
            pos=(640, 400),
            text_input="OPTIONS",
            font=content.get_font(75),
            base_color="#d7fcd4",
            hovering_color="White"
        )
        self.quit_button = content.Button(
            image=pygame.image.load("assets/img/Quit Rect.png"),
            pos=(640, 550),
            text_input="QUIT",
            font=content.get_font(75),
            base_color="#d7fcd4",
            hovering_color="White"
        )

    def run(self):
        while True:
            self.screen.blit(self.BG, (0, 0))
            mouse_pos = pygame.mouse.get_pos()


            menu_text = content.get_font(100).render("Cod Tower", True, "#b68f40")
            menu_rect = menu_text.get_rect(center=(640, 100))
            self.screen.blit(menu_text, menu_rect)

           
            for button in [self.play_button, self.options_button, self.quit_button]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.checkForInput(mouse_pos):
                        gioco = FinestraDiGioco(self.screen)
                        gioco.run()
                    elif self.options_button.checkForInput(mouse_pos):
                        opzioni = FinestraDiOpzioni(self.screen)
                        opzioni.run()
                    elif self.quit_button.checkForInput(mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()


menu = MainMenu()
menu.run()
