import numpy as np
import pygame as pg
from client import Network
#import sys


class Game:
    global BLUE, RED, YELLOW, WHITE, BLACK, CELL_SIZE, MARGIN, RADIUS, grid
    BLUE = (0,0,255)
    RED = (255,0,0)
    YELLOW = (255,255,0)
    WHITE = (255, 255, 255)
    BLACK = (0,0,0)
    CELL_SIZE = 60
    MARGIN = 5
    RADIUS = int(CELL_SIZE/2 - MARGIN)

    

    def __init__(self):

        self.rows = 6
        self.columns = 9
        self.width = self.columns * CELL_SIZE
        self.height = (self.rows+1) * CELL_SIZE

        #self.grid = np.zeros((self.rows,self.columns), int)

    def draw_grid(self, screen, grid):
        # Set the screen background
        #screen.fill(BLUE)
        for column in range(self.columns):
            for row in range(self.rows):
                pg.draw.rect(screen, BLUE, (column*CELL_SIZE, row*CELL_SIZE+CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pg.draw.circle(screen, WHITE, (int(column*CELL_SIZE+CELL_SIZE/2), int(row*CELL_SIZE+CELL_SIZE+CELL_SIZE/2)), RADIUS)
        
        for column in range(self.columns):
            for row in range(self.rows):      
                if grid[row][column] == 1:
                    pg.draw.circle(screen, RED, (int(column*CELL_SIZE+CELL_SIZE/2), self.height-int(row*CELL_SIZE+CELL_SIZE/2)), RADIUS)
                elif grid[row][column] == 2: 
                    pg.draw.circle(screen, YELLOW, (int(column*CELL_SIZE+CELL_SIZE/2), self.height-int(row*CELL_SIZE+CELL_SIZE/2)), RADIUS)
        pg.display.update()

    def find_empty_row(self, grid, column):
        for row in range(self.rows):
            if grid[row][column] == 0:
                return row

    def is_winning(self, grid, piece):
        # Check horizontal cells for win --
        for column in range(self.columns-4):
            for row in range(self.rows):
                if grid[row][column] == piece and grid[row][column+1] == piece and grid[row][column+2] == piece and grid[row][column+3] == piece and grid[row][column+4] == piece:
                    return True

        # Check vertical cells for win |
        for column in range(self.columns):
            for row in range(self.rows-4):
                if grid[row][column] == piece and grid[row+1][column] == piece and grid[row+2][column] == piece and grid[row+3][column] == piece and grid[row+4][column] == piece:
                    return True

        # Check diagonals for win - positive slopes /
        for column in range(self.columns-4):
            for row in range(self.rows-4):
                if grid[row][column] == piece and grid[row+1][column+1] == piece and grid[row+2][column+2] == piece and grid[row+3][column+3] == piece and grid[row+4][column+4] == piece:
                    return True

        # Check diagonals for win - negative slopes \
        for column in range(self.columns-4):
            for row in range(4, self.rows):
                if grid[row][column] == piece and grid[row-1][column+1] == piece and grid[row-2][column+2] == piece and grid[row-3][column+3] == piece and grid[row-4][column+4] == piece:
                    return True

                   
    def is_full(self,grid):

        for col in range(self.columns):
            for row in range(self.rows):
                if grid[row][col] == 0:
                    return False
        return True
 
    def get_grid(self, grid):
        return np.flip(grid, 0)
        
    def connect(self):
        global n
        n = Network()
        return n.grid
        
    def run(self):  

        game_over = False
        turn = 0
        #grid =self.grid
        grid = np.zeros((self.rows,self.columns), int)
        pg.init()

        



        WINDOW_SIZE = [self.width, self.height]
        

        screen = pg.display.set_mode(WINDOW_SIZE)
        self.draw_grid(screen, grid)
        pg.display.update()

        fontType = pg.font.SysFont("Arial",30)

        while not game_over:
            grid = self.connect()
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_over = True
                    #sys.exit()
                if event.type == pg.MOUSEMOTION:
                    
                    pg.draw.rect(screen, WHITE, (0,0, self.width, CELL_SIZE))
                    posx = event.pos[0]
                    col = posx // CELL_SIZE
                    if turn == 0:
                        pg.draw.circle(screen, RED, (int(CELL_SIZE * col + CELL_SIZE/2), int(CELL_SIZE/2)), RADIUS)
                    else: 
                        pg.draw.circle(screen, YELLOW, (int(CELL_SIZE * col + CELL_SIZE/2), int(CELL_SIZE/2)), RADIUS)
                pg.display.update()

                if event.type == pg.MOUSEBUTTONDOWN:
                    pg.draw.rect(screen, WHITE, (0,0, self.width, CELL_SIZE))
                    # Player 1 moves
                    if turn == 0:
                        posx = event.pos[0]
                        col = posx // CELL_SIZE
                        if grid[self.rows-1][col] == 0:
                            row = self.find_empty_row(grid, col)
                            grid[row][col] = 1

                            if self.is_winning(grid, 1):
                                label = fontType.render("Player 1 won!", 1, BLACK)
                                screen.blit(label, (self.width/2 - 70,10))
                                game_over = True
                    

                    # Player 2 moves
                    else:               
                        posx = event.pos[0]
                        col = posx // CELL_SIZE
                        if grid[self.rows-1][col] == 0:
                            row = self.find_empty_row(grid, col)
                            grid[row][col] = 2

                            if self.is_winning(grid, 2):
                                label = fontType.render("Player 2 won!", 1, BLACK)
                                screen.blit(label, (self.width/2 - 70,10))
                                game_over = True
                                
                            if self.is_full(grid):
                                label = fontType.render("Nobody wins! Game over!", 1, BLACK)
                                screen.blit(label, (self.width/2 - 130,10))
                                game_over = True
                    Network().send(grid)
                    self.draw_grid(screen, grid)

                    
                    if game_over:
                        pg.time.wait(3000)
                        # quit pygame to avoid hanging on exit
                        pg.quit()
                        