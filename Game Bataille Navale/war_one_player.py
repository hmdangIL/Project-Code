import sys
import pygame
import index
import set_grid



# setting for the infinity loop
clock = pygame.time.Clock()
FPS = 60


# create the main function
def main():
    grid1 = index.Grid(15, (200, 300), getData=True)

    
    running = True
    while running:
        clock.tick(FPS)
        index.window.blit(index.bg_img, (0, 0))
        grid1.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            grid1.attack(event)

if __name__ == "__main__":
    main()