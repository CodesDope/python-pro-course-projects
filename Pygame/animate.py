import pygame
from colors import WHITE, RED

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Animate")

FPS = 30
clock = pygame.time.Clock()

rect = pygame.Rect(0, 0, 50, 30)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)  # without this previous red pixels won't become white
    pygame.draw.rect(screen, RED, rect)

    if rect.x < 250:
        rect.x += 1

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
