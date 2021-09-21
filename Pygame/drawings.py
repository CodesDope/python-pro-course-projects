import pygame
from colors import WHITE, BLUE, RED, GREEN, LIME, YELLOW

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Drawing")

screen.fill(WHITE)

pygame.draw.polygon(screen, BLUE, ((0, 0), (50, 0), (50, 50), (0, 50)))
pygame.draw.polygon(screen, RED, ((60, 0), (120, 50), (170, 70), (100, 100)))
pygame.draw.line(screen, GREEN, (0, 90), (90, 90))

pygame.draw.line(screen, GREEN, (10, 100), (100, 100), 4)
pygame.draw.line(screen, GREEN, (100, 100), (100, 110), 4)
pygame.draw.line(screen, GREEN, (100, 110), (10, 110), 4)
pygame.draw.line(screen, GREEN, (10, 110), (10, 100), 4)

pygame.draw.circle(screen, LIME, (150, 150), 20, 0)  # Filled
pygame.draw.circle(screen, LIME, (190, 190), 20)
pygame.draw.circle(screen, LIME, (230, 230), 20, 5)  # Outlined with border 5 pixels

pygame.draw.ellipse(screen, YELLOW, (150, 0, 20, 40), 0)

pygame.draw.rect(
    screen,
    RED,
    (200, 0, 50, 30),
)  # left, top, width, height

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
