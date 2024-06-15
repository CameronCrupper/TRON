# Example file showing a circle moving on screen
import pygame
from pygame.locals import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

blue = (0, 0, 255)
red = (255, 0, 0)


#(location x, location y, width, height)
rect1 = Rect(400, 180, 30, 15)
rect2 = Rect(800, 180, 30, 15)

x = 100
y = 100
velocity = 12


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # stores keys pressed  
    keys = pygame.key.get_pressed() 
      
    if keys[pygame.K_w]:
        rect1.y -= 300 * dt
    if keys[pygame.K_s]:
        rect1.y += 300 * dt
    if keys[pygame.K_a]:
        rect1.x -= 300 * dt
    if keys[pygame.K_d]:
        rect1.x += 300 * dt

    if keys[pygame.K_UP]:
        rect2.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        rect2.y += 300 * dt
    if keys[pygame.K_LEFT]:
        rect2.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        rect2.x += 300 * dt


    background = pygame.image.load('Background.jpg')
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, blue, rect1)
    pygame.draw.rect(screen, red, rect2)

    pygame.display.update()
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
    dt = clock.tick(60) / 1000
pygame.quit()