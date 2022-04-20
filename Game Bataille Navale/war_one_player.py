import sys
import pygame
import index
import set_grid





# setting for the infinity loop
clock = pygame.time.Clock()
FPS = 60


# create the main function
def main():
    running = True
    while running:
        clock.tick(FPS)
        index.window.blit(index.bg_img, (0, 0))
        set_grid.grid1.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            set_grid.grid1.attack(event)

if __name__ == "__main__":
    main()