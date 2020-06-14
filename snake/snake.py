import pygame
pygame.init()
import time
import random

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)

bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')
clock = pygame.time.Clock()



font = pygame.font.SysFont(None, 25)

block_size = 10
FPS = 20

def snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size,block_size])

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

def game_loop():
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - block_size)/10.0)*10.0

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen('c to play, q to quit', red)
            pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if lead_x_change == block_size:
                        pass
                    else:
                        lead_x_change = -block_size
                        lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    if lead_x_change == -block_size:
                        pass
                    else:
                        lead_x_change = block_size
                        lead_y_change = 0
                elif event.key == pygame.K_UP:
                    if lead_y_change == block_size:
                        pass
                    else:
                        lead_y_change = -block_size
                        lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    if lead_y_change == -block_size:
                        pass
                    else:
                        lead_y_change = block_size
                        lead_x_change = 0

        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0 :
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY, block_size,block_size])


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)
        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
            randAppleY = round(random.randrange(0, display_height - block_size)/10.0)*10.0
            snakeLength +=1

        clock.tick(FPS)

    pygame.quit()
    quit()

game_loop()
