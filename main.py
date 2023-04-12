import pygame
from math import floor

# pygame setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
RECT_WIDTH, RECT_HEIGHT = 30, 200
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


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)  # limits FPS to 60

    screen.fill(BLACK)
    there_text = pygame.font.Font.render(standard_font, "There", True, WHITE)
    screen.blit(there_text, (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))

    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.display.update()


    # game logic here

pygame.quit()
