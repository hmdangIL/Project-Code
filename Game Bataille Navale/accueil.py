import sys
import pygame
import index
import one_player_add


# create the button
button1 = index.Button("One player", (300, 300))
button2 = index.Button("Two player", (300, 500))

# setting for the infinity loop
clock = pygame.time.Clock()
FPS = 60

# create the main function
def main():
    running = True
    while running:
        clock.tick(FPS)
        index.window.blit(index.bg_img, (0, 0))
        button1.draw()
        button2.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if button1.click(event):
                one_player_add.main()

main()