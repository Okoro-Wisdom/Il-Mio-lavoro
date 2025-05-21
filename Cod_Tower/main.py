import pygame,sys
import folder.content as content
from folder.finestra_gioco import FinestraDiGioco
from folder.finestra_opzioni import FinestraDiOpzioni


def main():
    pygame.init()

    screen = pygame.display.set_mode((content.SIZE_FRAME_X, content.SIZE_FRAME_Y))
    pygame.display.set_caption("Menu")
    BG = pygame.image.load("assets/img/background_main.png").convert()

    while True:
        screen.blit(BG, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        # Titolo menu
        menu_text = content.get_font(100).render("Cod Tower", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))
        screen.blit(menu_text, menu_rect)

        # Bottoni
        play_button = content.Button(
            image=pygame.image.load("assets/img/Play Rect.png"),
            pos=(640, 250),
            text_input="PLAY",
            font=content.get_font(75),
            base_color="#d7fcd4",
            hovering_color="White"
        )
        options_button = content.Button(
            image=pygame.image.load("assets/img/Options Rect.png"),
            pos=(640, 400),
            text_input="OPTIONS",
            font=content.get_font(75),
            base_color="#d7fcd4",
            hovering_color="White"
        )
        quit_button = content.Button(
            image=pygame.image.load("assets/img/Quit Rect.png"),
            pos=(640, 550),
            text_input="QUIT",
            font=content.get_font(75),
            base_color="#d7fcd4",
            hovering_color="White"
        )

        for button in [play_button, options_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    gioco = FinestraDiGioco(screen)
                    gioco.run()
                elif options_button.checkForInput(mouse_pos):
                    opzioni = FinestraDiOpzioni(screen)
                    opzioni.run()
                elif quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main()
