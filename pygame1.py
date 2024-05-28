import pygame, sys

pygame.init()

win = pygame.display.set_mode((800, 600), )
pygame.display.set_caption("first game")

# colo
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (125, 125, 125)

pygame.draw.rect(win, BLUE, ((50, 20), (200, 100)), 0)
pygame.draw.circle(win, RED, (350, 70), 50, 0)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
