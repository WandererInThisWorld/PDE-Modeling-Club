import pygame
from math import floor

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
time = 0
current_screen = 0
white = (230, 230, 230)

# title screen (screen value of 0)
def title_screen():
    screen.fill("black")
    pygame.font.Font.render(pygame.font.SysFont("brushscript",20), "Hello", True, white)

# game screen (screen value of 1)
def game_screen():
    screen.fill("purple")
    pygame.font.Font.render(pygame.font.SysFont("brushscript",20), "There", True, white)

# end screen (screen value of 2)
def end_screen():
    pygame.font.Font.render(pygame.font.SysFont("brushscript",20), "General", True, white)


    

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    '''
    player1 = pygame.draw.rect(surface=)
    pygame.Surface
    player2 = 
    
    pygame.key.get_pressed(accel)
    '''
    time = time+1
    if (event.type == pygame.KEYDOWN):
        game_screen()
    elif (event.type == pygame.KEYUP):
        end_screen()
    else:
        title_screen()
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 60

pygame.quit()
