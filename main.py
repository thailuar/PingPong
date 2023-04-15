import pygame

pygame.init()


window = pygame.display.set_mode([450, 700])
title = pygame.display.set_caption('Pinball')

#imagens
background = pygame.image.load("assets/background.jpg")

ball = pygame.image.load("assets/ball.png")
ball_x = 210
ball_y = 400
ball_dir = 1
ball_dir_x = 1

player = pygame.image.load("assets/bar.png")
player_x = 180
player_moveup = False
player_movedown = False


def move_player():
    global player_x

    if player_moveup:
        player_x -= 1
    else:
        player_x += 0

    if player_movedown:
        player_x += 1
    else:
        player_x += 0

    if player_x <= 0:
        player_x = 0
    elif player_x >= 350:
        player_x = 350


def move_ball():
    global ball_y
    global ball_x
    global player_x
    global ball_dir
    global ball_dir_x

    ball_y += ball_dir
    ball_x += ball_dir_x

    if ball_y > 580:
        if player_x < ball_x + 20:
            if player_x + 100 > ball_x:
                ball_dir *= -1

    if ball_y < 0:
        ball_dir *= -1

    if ball_y > 1:
        ball_dir_x *= -1
    elif ball_y >= 0:
        ball_dir_x *= -1


def draw():
    window.blit(background, (0, 0))
    window.blit(ball, (ball_x, ball_y))
    window.blit(player, (player_x, 600))


loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_a:
                player_moveup = True
            if events.key == pygame.K_d:
                player_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_a:
                player_moveup = False
            if events.key == pygame.K_d:
                player_movedown = False

    draw()
    move_player()
    move_ball()
    pygame.display.update()
