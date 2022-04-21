import sys
import pygame
import index
import war_one_player

# create the Ship

# big Ship
ship1 = index.Ship((35, 195), (1000, 300))
# medium ship
ship2 = index.Ship((35, 120), (1100, 300))
ship3 = index.Ship((35, 120), (1200, 300))
# small ship
ship4 = index.Ship((35, 35), (1300, 300))
ship5 = index.Ship((35, 35), (1300, 350))
ship6 = index.Ship((35, 35), (1300, 400))

listShip = [ship1, ship2, ship3, ship4, ship5, ship6]



grid1 = index.Grid(10, (200, 350), listShip)


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
            for ship in listShip:
                ship.handle_event(event)
            if button1.click(event):
                grid1.save()
                war_one_player.main()

if __name__ == "__main__":
    main()