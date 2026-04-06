import pygame
import random

pygame.init()
screen=pygame.display.set_mode((600,600))

class Circle:
    def __init__(self, color, pos, width, radius):
        self.color=color
        self.pos=pos
        self.width=width
        self.radius=radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius, self.width)

    def shrink(self, r):
        if self.radius>0:
            self.radius-=r

    def random_color(self):
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

circle=Circle(("purple"), (300,300), 0, 300)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            circle.draw(screen)
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            circle.shrink(20)
            screen.fill((255,255,255))
            circle.draw(screen)
            pygame.display.update()

pygame.quit()