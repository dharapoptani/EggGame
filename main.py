import pygame
import random
from pygame import mixer

#initializing pygame module
pygame.init()

#creating background
bg = pygame.image.load("bg.jpg")

#creating screen
screen = pygame.display.set_mode((1100, 630))

#creating music
sound = mixer.music.load("sucess.wav")

pygame.display.set_caption("Duck game")
icon = pygame.image.load("duck.png")
pygame.display.set_icon(icon)


#score creation
score = 0
score_font = pygame.font.Font("freesansbold.ttf", 24)
egg_drop = 0
max_egg_drop_allowed = 20
egg_font = pygame.font.Font("freesansbold.ttf", 24)
over_font = pygame.font.Font("freesansbold.ttf", 36)
restart_font = pygame.font.Font("freesansbold.ttf", 24)
over = False

def game_over():
    value3 = over_font.render("GAME OVER!!!!  ", True, (20, 15, 60))
    screen.blit(value3, (300, 300))

def restart():
    value2 = restart_font.render("Press escape to restart", True, (20, 15, 60))
    screen.blit(value2, (300, 350))

def show_score():
    value = score_font.render("SCORE : "+str(score), True, (20, 8, 60))
    screen.blit(value, (20, 10))

def show_drop():
    value = egg_font.render("DROP : "+str(egg_drop), True, (20, 8, 60))
    screen.blit(value, (20, 40))

#creating basket
basket = pygame.image.load("basket (1).png")
basketX = 485
basketY = 500
bmove = 0

def show_basket():
    screen.blit(basket, (basketX, basketY))

#creating egg
egg = pygame.image.load("egg (3).png")
no_of_eggs = 5
eggX = []
eggY = []
emove = 0.2
for i in range(no_of_eggs):
    eggX.append(random.randint(0, 1036))
    eggY.append(random.randint(-900, 150))

def show_egg():
    for i in range(no_of_eggs):
        screen.blit(egg, (eggX[i], eggY[i]))

#collision method
def isCollision(ex, ey, bx, by):
    if ex>=bx and ex<bx+128 and by-ey<45 and by-ey>30:
        global score
        score += 1
        return True
    return False



running = True
while running:

    # screen.fill((123, 135, 154))
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bmove = -1
            elif event.key == pygame.K_RIGHT:
                bmove = 1
            elif event.key == pygame.K_ESCAPE and over:
                over = False
                emove = 0.2
                score = 0
                egg_drop = 0
                for i in range(no_of_eggs):
                    eggX[i] = random.randint(0, 1036)
                    eggY[i] = random.randint(-900, 150)

        if event.type == pygame.KEYUP:
            bmove = 0

    for i in range(no_of_eggs):
        eggY[i] += emove
        if eggY[i] >= 630:
            egg_drop += 1
            eggX[i] = random.randint(0, 1036)
            eggY[i] = random.randint(-900, 150)
            if egg_drop > max_egg_drop_allowed:
                emove = 0
                over = True
                for j in range(no_of_eggs):
                    eggX[j] = 1500

        elif isCollision(eggX[i], eggY[i], basketX, basketY):
            eggX[i] = random.randint(0, 1036)
            eggY[i] = random.randint(-900, 150)
            mixer.music.play()
    if over:
        game_over()
        restart()



    show_egg()

    basketX += bmove
    if basketX < 0:
        basketX = 0
    elif basketX >= 972:
        basketX = 972

    show_basket()
    show_score()
    show_drop()
    pygame.display.update()