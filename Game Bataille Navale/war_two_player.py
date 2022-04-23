import sys
import pygame
import index
import time



# setting for the infinity loop
clock = pygame.time.Clock()
FPS = 60


# create the main function
def main():
    grid1 = index.Grid(10, (200, 300), getData="Player1")
    grid2 = index.Grid(10, (1200, 300), getData="Player2")


    turn = "player1"
    
    running = True
    while running:
        clock.tick(FPS)
        index.window.blit(index.bg_img, (0, 0))
        grid1.draw()
        grid2.draw()
        # draw text name player
        # draw text the number target remain grid.countTargetAlive()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if turn == "player1":
                # draw text turn
                grid1.resetTurn()
                grid1.offAttacked()
                grid2.onAttacked()
                grid2.attacked(event)
                if grid2.countTargetAlive() == 0:
                    print("New page1")
                if grid2.changeTurn():
                    turn = "player2"
            if turn == "player2":
                # draw text turn
                grid2.resetTurn()
                grid2.offAttacked()
                grid1.onAttacked()
                grid1.attacked(event)
                if grid1.countTargetAlive() == 0:
                    print('New page2')
                if grid1.changeTurn():
                    turn = "player1"



if __name__ == "__main__":
    main()
