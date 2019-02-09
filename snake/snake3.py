import pygame, randomS
from pygame.locals import *

GRID = 40

#Direção
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#TELA
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

#POSIÇÃO NO GRID
def posicaogrid():
    return (random.randint(0+GRID,560-GRID)//GRID*GRID, random.randint(0+GRID,560-GRID)//GRID*GRID)
#DETECTANDO A COLISÃO
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])
#DESENHANDO O SCORE
def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, (255,255,255))
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (600 - 120, 10)
    screen.blit(scoreSurf, scoreRect)

#MENSAGEM DE GAME OVER
def gameOver():
    scoreSurf = BASICFONT.render('Game Over', True, (255,255,255))
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (300 - 40, 300)
    screen.blit(scoreSurf, scoreRect)
    keyUpEvents = pygame.event.get(KEYUP)
    pygame.display.update()
    pygame.time.wait(500)
#SNAKE
snake = [(200, 200), (210,200), (220,200)]
snake_skin = pygame.Surface((GRID-4,GRID-4))
snake_skin.fill((255,255,255))

#APPLE
#gera posição aleatória no grid 10
apple_pos = posicaogrid()
apple = pygame.Surface((GRID,GRID))
apple.fill((255,0,0))

#DIREÇÃO INICIAL PARA A ESQUERDA
my_direction = LEFT

clock = pygame.time.Clock()
while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction!=DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction!=UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction!=RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction!=LEFT:
                my_direction = RIGHT  

    #COLISÃO
    if collision(snake[0], apple_pos):
        apple_pos = posicaogrid()
        snake.append((0,0))
        print(len(snake))
    if snake[0] in snake[2:]:
        snake = [(200, 200), (210,200), (220,200)]
        apple_pos = posicaogrid()
        gameOver()
        print(len(snake))
    if snake[0][0]==0 or snake[0][1]==0 or snake[0][0]==600 or snake[0][1]==600:
        snake = [(200, 200), (210,200), (220,200)]
        apple_pos = posicaogrid()
        gameOver()
    #

    if my_direction==UP:snake[0] = (snake[0][0], snake[0][1]-GRID)
    if my_direction==DOWN:snake[0] = (snake[0][0], snake[0][1]+GRID)
    if my_direction==LEFT:snake[0] = (snake[0][0] - GRID, snake[0][1])
    if my_direction==RIGHT:snake[0] = (snake[0][0] + GRID, snake[0][1])
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
    #desenha a maçã
    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    #desenha a snake
    for pos in snake:
        screen.blit(snake_skin,(pos[0]+2,pos[1]+2))
    drawScore(len(snake) - 3)
    pygame.display.update()
