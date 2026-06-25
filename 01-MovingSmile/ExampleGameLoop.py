
import pygame
import sys
pygame.display.set_caption("Joshua Lee")
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(pygame.Color("Gray"))
    pygame.draw.circle(screen, pygame.Color("Cyan"), (50,50), 25)
    pygame.draw.circle(screen, (128, 0, 0), (screen.get_width() / 2, screen.get_height() / 2), 100)
    pygame.draw.circle(screen, (255, 255, 0), (0, 480), 10)
    pygame.display.update()
