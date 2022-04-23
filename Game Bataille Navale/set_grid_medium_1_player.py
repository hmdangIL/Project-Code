import sys
import os
import pygame
import index
import war_one_player
import list_ship_medium


listShip = list_ship_medium.listShip
grid1 = index.Grid(10, (200, 350), listShip)

# confirm grid player 1
button1 = index.Button("Confirm grid", (50, 50), 30)
button3 = index.Button("WAR", (100, 100), 30)

# setting for the infinity loop
clock = pygame.time.Clock()
FPS = 60

# create the main function
def main():
    running = True
    # clear the data in 2 file gridData
    open("gridDataPlayer1.txt", "w").close()
    while running:
        clock.tick(FPS)
        index.window.blit(index.bg_img, (0, 0))
        grid.draw()
        button1.draw()
        button2.draw()
        button3.draw()
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
            while os.path.getsize("gridDataPlayer1.txt") == 0:
                if button1.click(event):
                    grid.save("gridDataPlayer1.txt")
            while not os.path.getsize("gridDataPlayer1.txt") == 0:
                if button3.click(event):
                    war_one_player.main()

if __name__ == "__main__":
    main()