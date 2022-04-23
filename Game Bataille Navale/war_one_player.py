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
    gridAuto = index.Grid(10, (1200, 300), getData="Random Medium")


    turn = "player1"
    
    running = True
    while running:
        clock.tick(FPS)
        index.window.blit(index.bg_img, (0, 0))
        grid1.draw()
        gridAuto.draw()
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
                gridAuto.onAttacked()
                gridAuto.attacked(event)
                if gridAuto.countTargetAlive() == 0:
                    print('New page1')   
                if gridAuto.changeTurn():
                    turn = "auto"
            if turn == "auto":
                # draw text turn
                gridAuto.resetTurn()
                gridAuto.offAttacked()
                grid1.onAttacked()
                grid1.randomAttacked()
                grid1.attacked(event)
                if grid1.countTargetAlive() == 0:
                    print('New page2')
                if grid1.changeTurn():
                    turn = "player1"




if __name__ == "__main__":
    main()
