import numpy as np
import pygame as pg
#import sys


BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)

ROWS = 6
COLUMNS = 9

def draw_grid(grid):
    # Set the screen background
    #screen.fill(BLUE)
    for column in range(COLUMNS):
        for row in range(ROWS):
            pg.draw.rect(screen, BLUE, (column*CELL_SIZE, row*CELL_SIZE+CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pg.draw.circle(screen, WHITE, (int(column*CELL_SIZE+CELL_SIZE/2), int(row*CELL_SIZE+CELL_SIZE+CELL_SIZE/2)), RADIUS)
    
    for column in range(COLUMNS):
        for row in range(ROWS):      
            if grid[row][column] == 1:
                pg.draw.circle(screen, RED, (int(column*CELL_SIZE+CELL_SIZE/2), height-int(row*CELL_SIZE+CELL_SIZE/2)), RADIUS)
            elif grid[row][column] == 2: 
                pg.draw.circle(screen, YELLOW, (int(column*CELL_SIZE+CELL_SIZE/2), height-int(row*CELL_SIZE+CELL_SIZE/2)), RADIUS)
    pg.display.update()

def find_empty_row(grid, column):
    for row in range(ROWS):
        if grid[row][column] == 0:
            return row

def is_winning(grid, piece):
    # Check horizontal cells for win --
    for column in range(COLUMNS-4):
        for row in range(ROWS):
            if grid[row][column] == piece and grid[row][column+1] == piece and grid[row][column+2] == piece and grid[row][column+3] == piece and grid[row][column+4] == piece:
                return True

    # Check vertical cells for win |
    for column in range(COLUMNS):
        for row in range(ROWS-4):
            if grid[row][column] == piece and grid[row+1][column] == piece and grid[row+2][column] == piece and grid[row+3][column] == piece and grid[row+4][column] == piece:
                return True

    # Check diagonals for win - positive slopes /
    for column in range(COLUMNS-4):
        for row in range(ROWS-4):
            if grid[row][column] == piece and grid[row+1][column+1] == piece and grid[row+2][column+2] == piece and grid[row+3][column+3] == piece and grid[row+4][column+4] == piece:
                return True

    # Check diagonals for win - negative slopes \
    for column in range(COLUMNS-4):
        for row in range(4, ROWS):
            if grid[row][column] == piece and grid[row-1][column+1] == piece and grid[row-2][column+2] == piece and grid[row-3][column+3] == piece and grid[row-4][column+4] == piece:
                return True

               
def is_full(grid):

    for col in range(COLUMNS):
        for row in range(ROWS):
            if grid[row][col] == 0:
                return False
    return True
 
 
grid = np.zeros((ROWS,COLUMNS), int)
game_over = False
turn = 0

pg.init()

CELL_SIZE = 60

width = COLUMNS * CELL_SIZE
height = (ROWS+1) * CELL_SIZE

WINDOW_SIZE = [width, height]
MARGIN = 5
RADIUS = int(CELL_SIZE/2 - MARGIN)

pg.display.set_caption("Connect 5")
screen = pg.display.set_mode(WINDOW_SIZE)

draw_grid(grid)
pg.display.update()

fontType = pg.font.SysFont("Arial",30)

while not game_over:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
            #sys.exit()
        if event.type == pg.MOUSEMOTION:
            pg.draw.rect(screen, WHITE, (0,0, width, CELL_SIZE))
            posx = event.pos[0]
            col = posx // CELL_SIZE
            if turn == 0:
                pg.draw.circle(screen, RED, (int(CELL_SIZE * col + CELL_SIZE/2), int(CELL_SIZE/2)), RADIUS)
            else: 
                pg.draw.circle(screen, YELLOW, (int(CELL_SIZE * col + CELL_SIZE/2), int(CELL_SIZE/2)), RADIUS)
        pg.display.update()

        if event.type == pg.MOUSEBUTTONDOWN:
            pg.draw.rect(screen, WHITE, (0,0, width, CELL_SIZE))
            posx = event.pos[0]
            col = posx // CELL_SIZE
            row = find_empty_row(grid, col)
            # Player 1 moves
            if turn == 0:
                if grid[ROWS-1][col] == 0:
                    grid[row][col] = 1

                    if is_winning(grid, 1):
                        label = fontType.render("Player 1 won!", 1, BLACK)
                        screen.blit(label, (width/2 - 70,10))
                        game_over = True


            # Player 2 moves
            else:               
                if grid[ROWS-1][col] == 0:
                    grid[row][col] = 2

                    if is_winning(grid, 2):
                        label = fontType.render("Player 2 won!", 1, BLACK)
                        screen.blit(label, (width/2 - 70,10))
                        game_over = True
                        
                    if is_full(grid):
                        label = fontType.render("Nobody wins! Game over!", 1, BLACK)
                        screen.blit(label, (width/2 - 130,10))
                        game_over = True
            print(np.flip(grid, 0))
            draw_grid(grid)

            turn += 1
            # turn always 0 or 1
            turn = turn % 2
            
            if game_over:
                pg.time.wait(3000)
                # quit pygame to avoid hanging on exit
                pg.quit()
                