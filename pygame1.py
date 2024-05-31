import pygame, sys

pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("First Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

win.fill(WHITE)

# img = pygame.image.load("image/a.png")
# pygame.display.set_icon(img)
#
# bg = pygame.image.load("image/b.jpg")
# bg = pygame.transform.scale(bg, (800, 600))
# win.blit(bg, (0, 0))
#
# cat = pygame.image.load("image/cat.png")
# cat = pygame.transform.scale(cat, (100, 100))
# win.blit(cat, (500, 500))

# win.fill(WHITE)
# pygame.draw.circle(win, GREEN, (100, 100), 50, 0)
# pygame.draw.ellipse(win, YELLOW, (170, 50, 150, 50), 0)
# pygame.draw.polygon(win, BLUE, ((350, 50), (500, 50), (475, 100), (325, 100)), 0)
# pygame.draw.rect(win, RED, (550, 50, 200, 100), 0)
# pygame.draw.arc(win, BLUE, (100, 200, 50, 50), 1, 4, 1)
# pygame.draw.line(win, BLUE, (200, 200), (250, 250), 1)
# pygame.draw.aaline(win, BLUE, (270, 200), (350, 200), 1)
# pygame.draw.lines(win, GREEN, True, ((300, 300), (375, 375), (450, 200)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
