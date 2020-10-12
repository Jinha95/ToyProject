import pygame
import sys
from time import sleep
import random


padWidth = 1500
padHeight = 750
BLACK = (0, 0, 0)
rockImage = ['rock01.jpg', 'rock02.jpg', 'rock03.jpg', 'rock04.jpg',
             'rock05.jpg', 'rock06.jpg', 'rock07.jpg', 'rock08.jpg',
             'rock09.jpg', 'rock10.jpg', 'rock11.jpg', 'rock12.jpg',
             'rock13.jpg', 'rock14.jpg', 'rock15.jpg', 'rock16.jpg',
             'rock17.jpg', 'rock18.jpg', 'rock19.jpg', 'rock20.jpg',
             'rock21.jpg', 'rock22.jpg', 'rock23.jpg', 'rock24.jpg',
             'rock25.jpg', 'rock26.jpg', 'rock27.jpg'
             ]

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))

def initGame():
    global gamePad, clock, background, fighter, missile, explosion
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('Pyshooting')
    # background = pygame.image.load('background.png')
    fighter = pygame.image.load('fighter.jpg')
    missile = pygame.image.load('missile.jpg')
    explosion = pygame.image.load('explosion.png')
    clock = pygame.time.Clock()

def runGame():
    global gapdPad, clock, background, fighter, missile, explosion

    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    x = padWidth * 0.45
    y = padHeight * 0.8
    fighterX = 0

    missileXY = []

    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]


    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    rockSpeed = 2

    isShot = False
    shotCount = 0

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    fighterX -= 10
                elif event.key == pygame.K_RIGHT:
                    fighterX += 10
                elif event.key == pygame.K_SPACE:
                    missileX = x + fighterWidth/2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])
            
            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0

        gamePad.fill(BLACK)
        
        x += fighterX        
        if x < 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth
        drawObject(fighter, x, y)
        
        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -= 10
                missileXY[i][1] = bxy[1]

                if bxy[1] < rockY:
                    if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
                        missileXY.remove(bxy)
                        isShot = True
                        shotCount += 1

                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass
        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        rockY += rockSpeed
        if rockY > padHeight:
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0

        if isShot:
            drawObject(explosion, rockX, rockY)
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
            isShot = False

        drawObject(rock, rockX, rockY)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

initGame()
runGame()