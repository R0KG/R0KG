import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Animating a Circle")

# Initial position
x, y = 100, 300
speed_x, speed_y = 2, 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update position
    x += speed_x
    y += speed_y

    # Bounce the circle when it hits the edge of the screen
    if x > 800 or x < 0:
        speed_x = -speed_x
    if y > 600 or y < 0:
        speed_y = -speed_y

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the moving circle
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 50)

    pygame.display.flip()

pygame.quit()
sys.exit()
