import pygame
import random

width = 500
height = 400

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

FPS = 30

pygame.init()

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Click and Drag")

clock = pygame.time.Clock()

rectangles = []

class Rectangle: 
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def makeRectangles():
        for i in range(0, 10):
            rectangles.append(Rectangle(random.randint(0, width), random.randint(0, height), 20, 20))

    def draw():
        for i in range(len(rectangles)):
            pygame.draw.rect(screen, GREEN, pygame.Rect(rectangles[i].x, rectangles[i].y, rectangles[i].w, rectangles[i].h))

def main():
    done = False
    Rectangle.makeRectangles()
    rectDragging = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN: 
                for i in range(len(rectangles)):       
                    if rectangles[i].collidepoint(event.pos):
                        rectDragging = True
                        rXMousePos, rYMousePos = event.pos
                        rOffsetX = rectangles[i].x - rXMousePos
                        rOffsetY = rectangles[i].y - rYMousePos

            if event.type == pygame.MOUSEBUTTONUP:          
                rectDragging = False

            if event.type == pygame.MOUSEMOTION:
                if rectDragging:
                    rXMousePos, rYMousePos = event.pos
                    rectangles[i].x = rXMousePos + rOffsetX
                    rectangles[i].y = rYMousePos + rOffsetY

        screen.fill(WHITE)

        Rectangle.draw()

        pygame.display.flip()

main()
