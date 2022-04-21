import sys
import pygame
import index
import war_one_player


ship1 = index.Ship((30, 120), (1500, 300))
ship2 = index.Ship((30, 120), (1700, 300))


listShip = [ship1, ship2]



grid1 = index.Grid(15, (200, 250), listShip)


button1 = index.Button("WAR", (100, 100))

# setting for the infinity loop
clock = pygame.time.Clock()
FPS = 60

# create the main function
def main():
    running = True
    while running:
        clock.tick(FPS)
        index.window.blit(index.bg_img, (0, 0))
        grid1.draw()
        button1.draw()
        for ship in listShip:
            ship.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            grid1.handle_event(event)
            # grid1.attack(event)
            for ship in listShip:
                ship.drag_drop(event)
            if button1.click(event):
                grid1.save()
                war_one_player.main()

if __name__ == "__main__":
    main()