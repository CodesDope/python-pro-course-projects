import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Fonts")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

print(pygame.font.get_fonts())  # prints available fonts

font = pygame.font.SysFont("timesnewromanboldttf", 40)
font_roboto = pygame.font.Font("Roboto-Black.ttf", 40)  # From file

text_anti_alias_timesnewromanbold = font.render(
    "CodesDope", True, WHITE, RED  # White text on red background
)  # Anti-Aliasing
text_alias_timesnewromanbold = font.render("CodesDope", False, WHITE, RED)  # Aliasing
text_aliasing_roboto = font_roboto.render(
    "CodesDope", True, WHITE, RED
)  # Anti-Aliasing
text_anti_aliasing_roboto = font_roboto.render(
    "CodesDope", False, WHITE, RED
)  # Aliasing

text_anti_alias_timesnewromanbold_rect = text_anti_alias_timesnewromanbold.get_rect()
text_anti_alias_timesnewromanbold_rect.centerx = screen.get_rect().centerx
text_anti_alias_timesnewromanbold_rect.centery = screen.get_rect().centery

screen.blit(
    text_anti_alias_timesnewromanbold, text_anti_alias_timesnewromanbold_rect
)  # draws one surface on another
screen.blit(text_alias_timesnewromanbold, (0, 0))
screen.blit(text_aliasing_roboto, (0, 50))
screen.blit(text_anti_aliasing_roboto, (0, 110))
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
