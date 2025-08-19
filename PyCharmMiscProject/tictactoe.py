import numpy as np
import pygame
import math
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
ROWS=3
COLUMNS=3
WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
CIRCLE = pygame.image.load('images/circle.png')
CROSS = pygame.image.load('images/cross.png')
def mark(rows, cols, player):
    board[rows][cols]=player

def is_valid_mark(rows, cols):
    return board[rows][cols]==0

def is_board_full():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c]==0:
                return False
    return True
def draw_lines():
    pygame.draw.line(Window, BLACK, (200,0), (200, 600), 10)
    pygame.draw.line(Window, BLACK, (400, 0), (400, 600), 10)
    pygame.draw.line(Window, BLACK, (0, 200), (600, 200), 10)
    pygame.draw.line(Window, BLACK, (0, 400), (600, 400), 10)

def draw_board():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c]==1:
                Window.blit(CIRCLE, ((c*200)+50, (r*200)+50))
            elif board[r][c]==2:
                Window.blit(CROSS, ((c*200)+50, (r*200)+50))
    pygame.display.update()

def is_winning_move(player):
    if player==1:
        announcement = "Player 1 Won"
    else:
        announcement = "Player 2 Won"
    for r in range(ROWS):
        if board[r][0]==player and board[r][1]==player and board[r][2]==player:
            print(announcement)
            return True

    for c in range(COLUMNS):
        if board[0][c]==player and board[1][c]==player and board[2][c]==player:
            print(announcement)
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print(announcement)
        return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        print(announcement)
        return True
    return False


board = np.zeros((ROWS, COLUMNS))
game_over = False
turn = 0

pygame.init()
Window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tic Tac Toe")
Window.fill(WHITE)
draw_lines()
pygame.display.update()
pygame.time.wait(2000)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

            if turn % 2 == 0:
                row = math.floor(event.pos[1]/200)
                col = math.floor(event.pos[0]/200)
                if is_valid_mark(row, col):
                    mark(row, col, 1)
                    if is_winning_move(1):
                        game_over = True
                else:
                    turn -= 1
            else:
                row = math.floor(event.pos[1] / 200)
                col = math.floor(event.pos[0] / 200)
                if is_valid_mark(row, col):
                    mark(row, col, 2)
                    if is_winning_move(2):
                        game_over = True
                else:
                    turn -= 1
            turn += 1
            print(board)
            draw_board()
    if game_over:
        print("Game Over")



