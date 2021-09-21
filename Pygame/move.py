import pygame
from pygame.locals import KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_a, K_d, K_w, K_s

from colors import WHITE

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Drawing")

speed = 2
clock = pygame.time.Clock()

x_cord = 0
y_cord = 0
carImg = pygame.image.load("car.bmp")
screen.fill(WHITE)
screen.blit(carImg, (x_cord, y_cord))


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYUP:
            if event.key in (K_LEFT, K_a):
                x_cord -= speed

                screen.fill(WHITE)
                screen.blit(carImg, (x_cord, y_cord))

            elif event.key in (K_RIGHT, K_d):
                x_cord += speed

                screen.fill(WHITE)
                screen.blit(carImg, (x_cord, y_cord))
            elif event.key in (K_UP, K_w):
                y_cord -= speed

                screen.fill(WHITE)
                screen.blit(carImg, (x_cord, y_cord))
            elif event.key in (K_DOWN, K_s):
                y_cord += speed

                screen.fill(WHITE)
                screen.blit(carImg, (x_cord, y_cord))

    pygame.display.update()

pygame.quit()
