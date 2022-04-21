import sys
import pygame
import index



# setting for the infinity loop
clock = pygame.time.Clock()
FPS = 60


# create the main function
def main():
    grid1 = index.Grid(10, (200, 300), getData=False)
    gridAuto = index.Grid(10, (1200, 300), getData="Random")

    
    running = True
    while running:
        clock.tick(FPS)
        index.window.blit(index.bg_img, (0, 0))
        grid1.draw()
        gridAuto.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            grid1.attack(event)
            gridAuto.attack(event)

if __name__ == "__main__":
    main()