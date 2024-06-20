# from BetterTicTacToe import game
import secrets

import numpy as np
import pygame
pygame.init()

WIDTH, HEIGHT = 1200, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
play_board = min(WIDTH*0.8, HEIGHT*0.8)

class Field:
    def __init__(self):
        self.field = []
        for i in range(3):
            self.field.append([])
            for j in range(3):
                self.field[i].append(Spot())

class Spot:
    def __init__(self):
        self.symbol = '.'

game = [[Field() for _ in range(3)] for _ in range(3)] # holds 9 small grids
bigboard = Field() # holds one big grid

# Constants
line_width = min(10, int(play_board / 100))
BOARD_ROWS, BOARD_COLS = 9, 9
square_size = play_board // BOARD_COLS
circle_radius = square_size // 3
circle_width = 15
cross_width = 25
space = square_size // 4

gameNotOver = True
player1 = 'X'
player2 = 'O'
AvalaibleRowMin = 1
AvalaibleColMin = 1
AvalaibleRowMax = 9
AvalaibleColMax = 9
numOfTurns = 0
SetSpot = False

# Colors
BG_COLOR = (200, 50, 111)
LINE_COLOR = (255, 100, 150)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
background = (111, 111, 111)
WHITE = (255, 255, 255)
INVERSE_COLOR = (255 - LINE_COLOR[0], 255 - LINE_COLOR[1], 255 - LINE_COLOR[2])

board = np.zeros((BOARD_ROWS, BOARD_COLS))


def update_values():
    global line_width, BOARD_ROWS, BOARD_COLS, square_size, cross_width, circle_width, circle_radius, space, INVERSE_COLOR

    line_width = min(10, int(play_board / 100))
    BOARD_ROWS, BOARD_COLS = 9, 9
    square_size = play_board // BOARD_COLS
    circle_radius = square_size // 3
    circle_width = min(15, int(play_board / 66))
    cross_width = min(25, int(play_board / 40))
    space = square_size // 5
    INVERSE_COLOR = (255 - LINE_COLOR[0], 255 - LINE_COLOR[1], 255 - LINE_COLOR[2])


def draw_figures(): #vykresluje symboly
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if game[i][j].field[k][l].symbol == "o":
                        pygame.draw.circle(screen, CIRCLE_COLOR, ((WIDTH // 2 - play_board // 2) + (int((i * play_board//3) + (k * square_size)) + square_size // 2),
                                                                        (HEIGHT // 2 - play_board // 2) + (int((j * play_board/3) + (l * square_size)) + square_size // 2)), circle_radius, circle_width)
                    elif game[i][j].field[k][l].symbol == "x":
                        pygame.draw.line(screen, CROSS_COLOR, ((WIDTH // 2 - play_board // 2) + int((i * play_board//3) + (k * square_size)) + space, (HEIGHT // 2 - play_board // 2) + int((j * play_board/3)+(l * square_size)) + space), ((WIDTH // 2 - play_board // 2) + int((i * play_board/3) + (k * square_size)) + space * 4, (HEIGHT // 2 - play_board // 2) + int((j * play_board/3)+(l * square_size)) + space*4), cross_width)
                        pygame.draw.line(screen, CROSS_COLOR, ((WIDTH // 2 - play_board // 2) + int((i * play_board//3) + (k * square_size)) + space*4, (HEIGHT // 2 - play_board // 2) + int((j * play_board/3)+(l * square_size)) + space), ((WIDTH // 2 - play_board // 2) + int((i * play_board/3) + (k * square_size)) + space, (HEIGHT // 2 - play_board // 2) + int((j * play_board/3)+(l * square_size)) + space*4), cross_width)


def textsig(a):
    pygame.font.init()
    my_font = pygame.font.SysFont("Arial", int(play_board//10))
    text = my_font.render(a, False, LINE_COLOR)
    screen.blit(text, (WIDTH // 2 - play_board // 2, HEIGHT // 2 - play_board // 1.6))


def draw_lines():

    for i in range(BOARD_ROWS+1):
        if i % 3 == 0:
            pygame.draw.line(screen, LINE_COLOR, (round((WIDTH/2)-(play_board/2)), round((HEIGHT/2)-(play_board/2)) + i * square_size), (round((WIDTH/2)+(play_board/2)), round((HEIGHT/2)-(play_board/2)) + i * square_size), line_width*2)
        pygame.draw.line(screen, LINE_COLOR, (round((WIDTH/2)-(play_board/2)), round((HEIGHT/2)-(play_board/2)) + i * square_size), (round((WIDTH/2)+(play_board/2)), round((HEIGHT/2)-(play_board/2)) + i * square_size), line_width)

    for i in range(BOARD_ROWS+1):
        if i % 3 == 0:
            pygame.draw.line(screen, LINE_COLOR, (round((WIDTH/2)-(play_board/2)) + i * square_size, round((HEIGHT/2)-(play_board/2))), (round((WIDTH/2)-(play_board/2)) + i * square_size, round((HEIGHT/2)+(play_board/2))), line_width * 2)
        pygame.draw.line(screen, LINE_COLOR, (round((WIDTH/2)-(play_board/2)) + i * square_size, round((HEIGHT/2)-(play_board/2))), (round((WIDTH/2)-(play_board/2)) + i * square_size, round((HEIGHT/2)+(play_board/2))), line_width)


def draw_help_lines():
    for i in range(BOARD_ROWS+1):
        for j in range(BOARD_ROWS+1):
            if (i >= AvalaibleRowMin - 1 and i <= AvalaibleRowMax - 1) and (
                    j >= AvalaibleColMin - 1 and j <= AvalaibleColMax):
                if j % 3 == 0:
                    pygame.draw.line(screen, INVERSE_COLOR,
                                     (round((WIDTH / 2) - (play_board / 2)) + (i * square_size),
                                      round((HEIGHT / 2) - (play_board / 2)) + (j * square_size)),
                                     (round((WIDTH / 2) - (play_board / 2)) + square_size + (i * square_size),
                                      round((HEIGHT / 2) - (play_board / 2)) + (j * square_size)), line_width * 2)
                pygame.draw.line(screen, INVERSE_COLOR,
                                 (round((WIDTH / 2) - (play_board / 2)) + (i * square_size),
                                  round((HEIGHT / 2) - (play_board / 2)) + (j * square_size)),
                                 (round((WIDTH / 2) - (play_board / 2)) + square_size + (i * square_size),
                                  round((HEIGHT / 2) - (play_board / 2)) + (j * square_size)), line_width)

            if (i >= AvalaibleRowMin-1 and i <= AvalaibleRowMax) and (j >= AvalaibleColMin-1 and j <= AvalaibleColMax-1):
                if i % 3 == 0:
                    pygame.draw.line(screen, INVERSE_COLOR,
                    (round((WIDTH / 2) - (play_board / 2)) + (i * square_size),
                     round((HEIGHT / 2) - (play_board / 2)) + (j * square_size)),
                    (round((WIDTH / 2) - (play_board / 2)) + (i * square_size),
                     round((HEIGHT / 2) - (play_board / 2)) + square_size + (j * square_size)), line_width * 2)
                pygame.draw.line(screen, INVERSE_COLOR,
                                 (round((WIDTH / 2) - (play_board / 2)) + (i * square_size),
                                  round((HEIGHT / 2) - (play_board / 2)) + (j * square_size)),
                                 (round((WIDTH / 2) - (play_board / 2)) + (i * square_size),
                                  round((HEIGHT / 2) - (play_board / 2)) + square_size + (j * square_size)),
                                 line_width)


def CheckForSpaceAndSet(arr):
    global AvalaibleRowMin, AvalaibleRowMax, AvalaibleColMin, AvalaibleColMax, numOfTurns, SetSpot, gameNotOver, numOfTurns
    if(((arr[0] < AvalaibleRowMax) & (arr[0] >= AvalaibleRowMin-1)) & ((arr[1] < AvalaibleColMax) & (arr[1] >= AvalaibleColMin-1))):
        if numOfTurns % 2 == 0:
            player = "x"
        else:
            player = "o"
        i = (arr[0]) // 3
        j = (arr[1]) // 3
        k = (arr[0]) % 3
        l = (arr[1]) % 3
        if game[i][j].field[k][l].symbol == '.' and bigboard.field[i][j].symbol == '.':
            AvalaibleRowMin = k * 3 + 1
            AvalaibleRowMax = k * 3 + 2 + 1
            AvalaibleColMin = l * 3 + 1
            AvalaibleColMax = l * 3 + 2 + 1
            print(" - x = ", (i*3 + k+1), " y = ", (j*3 + l+1))
            game[i][j].field[k][l].symbol = player
            for m in range(3):
                for n in range(3):
                    if checkForWin(game[m][n]) and bigboard.field[m][n].symbol == '.':
                        bigboard.field[m][n].symbol = player
                        #fillField(m, n, player)
                        if checkForWin(bigboard):
                            print(player, 'has won')
                            textsig(player + " has won")
                            gameNotOver = False
            if bigboard.field[k][l].symbol != '.' or CheckForSpaceInField(k, l):
                AvalaibleRowMin = 1
                AvalaibleRowMax = 9
                AvalaibleColMin = 1
                AvalaibleColMax = 9
            else:
                numOfTurns += 1
                SetSpot = True
        else:
            textsig("spot taken")
            print("spot taken")


def CheckForSpaceInField(i, j):
    for k in range(len(game[i][j].field)):
        for l in range(len(game[i][j].field[k])):
            if game[i][j].field[k][l].symbol == ".":
                return False
    return True


def checkForWin(field):
    for i in range(3):
        if field.field[i][0].symbol == field.field[i][1].symbol and field.field[i][1].symbol == field.field[i][2].symbol and field.field[i][2].symbol != '.':
            return True
    for i in range(3):
        if field.field[0][i].symbol == field.field[1][i].symbol and field.field[1][i].symbol == field.field[2][i].symbol and field.field[2][i].symbol != '.':
            return True
    if field.field[0][0].symbol == field.field[1][1].symbol and field.field[1][1].symbol == field.field[2][2].symbol and field.field[2][2].symbol != '.':
        return True
    if field.field[0][2].symbol == field.field[1][1].symbol and field.field[1][1].symbol == field.field[2][0].symbol and field.field[2][0].symbol != '.':
        return True
    return False


def change_colors():
    global BG_COLOR, LINE_COLOR, background

    BG_COLOR = (secrets.randbelow(256), secrets.randbelow(256), secrets.randbelow(256))
    LINE_COLOR = (secrets.randbelow(256), secrets.randbelow(256), secrets.randbelow(256))
    background = (secrets.randbelow(256), secrets.randbelow(256), secrets.randbelow(256))
    print(BG_COLOR)
    print(LINE_COLOR)
    print(background)


def drawings():
    update_values()
    screen.fill(background)
    draw_sq()
    draw_lines()
    draw_figures()
    draw_help_lines()


def draw_sq():
    pygame.draw.rect(screen, BG_COLOR, pygame.Rect(round((WIDTH/2)-(play_board/2)), round((HEIGHT/2)-(play_board/2)), play_board, play_board))


def getRelativeCursorPosition():
    cursor_pos = pygame.mouse.get_pos()
    return [cursor_pos[0] - round((WIDTH/2)-(play_board/2)),cursor_pos[1] - round((HEIGHT/2)-(play_board/2))]


change_colors()
update_values()
running = True
screen.fill(background)
draw_sq()
draw_lines()
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                background = (00,255,00)
            elif event.key == pygame.K_w:
                background = (255,00,00)
            elif event.key == pygame.K_SPACE:
                change_colors()
                drawings()
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and  gameNotOver:
            mouseXY = getRelativeCursorPosition()

            clicked_row = int(mouseXY[0] // square_size) #// je celociselne deleni
            clicked_col = int(mouseXY[1] // square_size)

            CheckForSpaceAndSet([clicked_row, clicked_col])
            drawings()

            draw_figures()

        elif event.type == pygame.VIDEORESIZE:
            # Update object size based on window width and height
            WIDTH, HEIGHT = event.dict['size']
            play_board = min(WIDTH * 0.8, HEIGHT * 0.8)
            drawings()
            print("updated")
    pygame.display.update()


pygame.quit()
