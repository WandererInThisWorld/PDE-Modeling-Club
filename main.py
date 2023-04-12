import pygame
from math import sqrt, floor
import random


# pygame setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
RECT_WIDTH, RECT_HEIGHT = 30, 200
BALL_RADIUS = 20
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Modeling Club")

clock = pygame.time.Clock()
running = True
time = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

standard_font = pygame.font.SysFont("helvetica", 20)
player1 = pygame.Rect(30,50,RECT_WIDTH,RECT_HEIGHT)
player2 = pygame.Rect(SCREEN_WIDTH-RECT_WIDTH-30,50,RECT_WIDTH,RECT_HEIGHT)
ball = pygame.Rect((SCREEN_WIDTH-BALL_RADIUS)/2, (SCREEN_HEIGHT-BALL_RADIUS)/2, BALL_RADIUS, BALL_RADIUS)

player_speed = 4
ball_speed = 8
ball_speed_x = random.randint(1,8)
ball_speed_y = floor(sqrt(ball_speed**2 - ball_speed_x**2)) + 1


ball_fuel = 1000
friction = 10

player1_score = 0
player2_score = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)  # limits FPS to 60

    screen.fill(BLACK)
    player1_scoreboard = pygame.font.Font.render(standard_font, str(player1_score), True, WHITE)
    screen.blit(player1_scoreboard, ((SCREEN_WIDTH/4)-60/2,10))
    
    player2_scoreboard = pygame.font.Font.render(standard_font, str(player2_score), True, WHITE)
    screen.blit(player2_scoreboard, (3*(SCREEN_WIDTH/4)-60/2,10))
    

    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.display.update()


    # game logic here
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w]:
        player1.y -= player_speed
    if keys_pressed[pygame.K_s]:
        player1.y += player_speed
    if keys_pressed[pygame.K_UP]:
        player2.y -= player_speed
    if keys_pressed[pygame.K_DOWN]:
        player2.y += player_speed
    
    if ball.y > SCREEN_HEIGHT - BALL_RADIUS:
        ball_speed_y *= -1
    elif ball.y < 0:
        ball_speed_y *= -1

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if player1.colliderect(ball):
        
        '''
        # calculate center of rectangle
        center_rect_x = player1.x + RECT_WIDTH/2
        center_rect_y = player1.y + RECT_HEIGHT/2
        
        center_ball_x = ball.x + BALL_RADIUS
        center_ball_y = ball.y + BALL_RADIUS

        vect_x = center_ball_x - center_rect_x
        vect_y = center_ball_y - center_rect_y

        floor()
        '''


        ball_speed_x *= -1
    elif player2.colliderect(ball):
        '''
        # calculate center of rectangle
        center_rect_x = player2.x + RECT_WIDTH/2
        center_rect_y = player2.y + RECT_HEIGHT/2

        center_ball_x = ball.x + BALL_RADIUS
        center_ball_y = ball.y + BALL_RADIUS
        
        vect_x = center_ball_x - center_rect_x
        vect_y = center_ball_y - center_rect_y

        '''
        ball_speed_x *= -1
        
    if ball.x + BALL_RADIUS< 0:
        print("player 2 scores")
        player2_score += player2_score
        ball.x, ball.y = (SCREEN_WIDTH-BALL_RADIUS)/2, (SCREEN_HEIGHT-BALL_RADIUS)/2
    elif ball.x > SCREEN_WIDTH + BALL_RADIUS:
        print("player 1 scores")
        player1_score += player1_score
        ball.x, ball.y = (SCREEN_WIDTH-BALL_RADIUS)/2, (SCREEN_HEIGHT-BALL_RADIUS)/2

pygame.quit()
