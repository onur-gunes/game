import pygame
pygame.init()
import time
import random

crash_sound = pygame.mixer.Sound('crash.wav')
pygame.mixer.music.load('8_bit_March.wav')

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
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')
(car_width,car_height) = carImg.get_rect().size

icon = pygame.image.load('racecar_icon.png')
pygame.display.set_icon(icon)

roadImg = pygame.image.load('46.png')

block_color = blue
high_score = 0
tol = 3
pause = False

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render('Dodged: {}'.format(str(count)), True, black)
    gameDisplay.blit(text,(5, 0))

def record(new_record):
    font = pygame.font.SysFont(None, 25)
    text = font.render('High Score: {}'.format(new_record), True, red)
    gameDisplay.blit(text,(675, 0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx,thingy, thingw,thingh])

def car(x,y):
    gameDisplay.blit( carImg, (x,y) )

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text,size,offset=0):
    largeText = pygame.font.SysFont('comicsansms', size)
    textSurf, textRect = text_objects(text, largeText)
    textRect.center = (display_width/2, display_height/2 + offset)
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    time.sleep(2)
    #game_loop()

def new_high_score(new_record):
    message_display('New High Score: {}'.format(str(new_record)), 50)

def crash(score, record):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    message_display('Wrecked', 115, -100)
    if score > record:
        global high_score
        high_score = score
        new_high_score(score)
    play_again()

def button(msg, x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    smallText = pygame.font.SysFont('comicsansms', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( x+w/2 , y+h/2)
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False
    pygame.mixer.music.unpause()
    
def paused():
    pygame.mixer.music.pause()

    largeText = pygame.font.SysFont('comicsansms', 115)
    textSurf, textRect = text_objects('Paused', largeText)
    textRect.center = (display_width/2, display_height/3)
    gameDisplay.blit(textSurf, textRect)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)

        button('Continue', 250,350,100,50,green,bright_green, unpause)
        button('Quit', 450,350,100,50,red,bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def play_again():
    again = True
    while again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont('comicsansms', 115)
        textSurf, textRect = text_objects('A bit Racey', largeText)
        textRect.center = (display_width/2, display_height/3)
        gameDisplay.blit(textSurf, textRect)

        button('Play Again', 250,350,100,50,green,bright_green, game_loop)
        button('Quit', 450,350,100,50,red,bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont('comicsansms', 115)
        textSurf, textRect = text_objects('A bit Racey', largeText)
        textRect.center = (display_width/2, display_height/3)
        gameDisplay.blit(textSurf, textRect)

        button('GO!', 250,350,100,50,green,bright_green, game_loop)
        button('Quit', 450,350,100,50,red,bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    dodged = 0
    final = 0
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.blit( roadImg, (0,0) )

        things(thing_startx,thing_starty, thing_width, thing_height, block_color)
        thing_starty +=thing_speed
        car(x,y)
        things_dodged(dodged)
        record(high_score)

        if x > display_width-car_width or x<0:
            final = dodged
            crash(final, high_score)
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width-100)
            dodged +=1
            if dodged % 10 == 0:
                thing_speed += 1
            thing_width += 5

        if y+tol < thing_starty + thing_height:
            if x-tol > thing_startx and x+tol < thing_startx+thing_width or x+car_width-tol > thing_startx and x+car_width+tol < thing_startx+thing_width:
                final = dodged
                crash(final, high_score)
        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()
