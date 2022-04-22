import sys
import pygame
import index



# setting for the infinity loop
clock = pygame.time.Clock()
FPS = 60


# create the main function
def main():
    grid1 = index.Grid(10, (200, 300), getData=True)
    gridAuto = index.Grid(10, (1200, 300), getData="Random")


    turn = "player1"
    
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
            if turn == "player1":
                grid1.resetTurn()
                grid1.offAttacked()
                gridAuto.onAttacked()
                gridAuto.attacked(event)
                if gridAuto.changeTurn():
                    if gridAuto.lose():
                        print('New page1')   
                    else:
                        turn = "auto"
            if turn == "auto":
                gridAuto.resetTurn()
                gridAuto.offAttacked()
                grid1.onAttacked()
                grid1.randomAttacked()
                grid1.attacked(event)
                if grid1.changeTurn():
                    if grid1.lose():
                        print('New page2')
                    else:
                        turn = "player1"
                        print('turn')      

                



if __name__ == "__main__":
    main()