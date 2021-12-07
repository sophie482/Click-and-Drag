import pygame

width = 500
height = 400

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

FPS = 30

pygame.init()

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Click and Drag")

mainRect = pygame.rect.Rect(100, 100, 20, 20)
mainCircle = pygame.draw.circle(screen, GREEN, (200, 200), 10)
rectDragging = False
circleDragging = False

clock = pygame.time.Clock()

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:        
            if mainRect.collidepoint(event.pos):
                rectDragging = True
                rXMousePos, rYMousePos = event.pos
                rOffsetX = mainRect.x - rXMousePos
                rOffsetY = mainRect.y - rYMousePos
            elif mainCircle.collidepoint(event.pos):
                circleDragging = True
                cXMousePos, cYMousePos = event.pos
                cOffsetX = mainCircle.x - cXMousePos
                cOffsetY = mainCircle.y - cYMousePos

        if event.type == pygame.MOUSEBUTTONUP:          
            rectDragging = False
            circleDragging = False

        if event.type == pygame.MOUSEMOTION:
            if rectDragging:
                rXMousePos, rYMousePos = event.pos
                mainRect.x = rXMousePos + rOffsetX
                mainRect.y = rYMousePos + rOffsetY
            elif circleDragging: 
                cXMousePos, cYMousePos = event.pos
                mainCircle.x = cXMousePos + cOffsetX
                mainCircle.y = cYMousePos + cOffsetY

    screen.fill(WHITE)

    pygame.draw.rect(screen, GREEN, mainRect)
    pygame.draw.circle(screen, GREEN, (mainCircle.x, mainCircle.y), 10)

    pygame.display.flip()
