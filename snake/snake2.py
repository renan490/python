import pygame, random
from pygame.locals import *

def posicaogrid():
    return (random.randint(0,590)//10*10, random.randint(0,590)//10*10)
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

#SNAKE
snake = [(200, 200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))
#</SNAKE>

#APPLE
#gera posição aleatória no grid 10
apple_pos = posicaogrid()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))
#</APLE>
my_direction = LEFT

clock = pygame.time.Clock()
while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    #COLISÃO
    if collision(snake[0], apple_pos):
        apple_pos = posicaogrid()
        snake.append((0,0))
    #</COLISÃO>
    if event.type == KEYDOWN:
        if event.key == K_UP:
            my_direction = UP
        if event.key == K_DOWN:
            my_direction = DOWN
        if event.key == K_LEFT:
            my_direction = LEFT
        if event.key == K_RIGHT:
            my_direction = RIGHT

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1]-10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1]+10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
    #desenha a maçã
    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    #desenha a snake
    for pos in snake:
        screen.blit(snake_skin,pos)
    pygame.display.update()