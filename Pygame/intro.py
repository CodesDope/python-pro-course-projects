import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("First Pygame Program")

BLUE = (0, 0, 255)
screen.fill(BLUE)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
