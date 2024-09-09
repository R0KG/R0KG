import pygame 
import sys

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Basic Pygame Game')

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

# Character settings
character_color = (255, 0, 0)
character_x, character_y = screen_width // 2, screen_height // 2
character_width, character_height = 50, 50
character_speed = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed
    if keys[pygame.K_UP]:
        character_y -= character_speed
    if keys[pygame.K_DOWN]:
        character_y += character_speed
    
    screen.fill((0, 0, 0))  # Clear the screen
    pygame.draw.rect(screen, character_color, (character_x, character_y, character_width, character_height))
    pygame.display.flip()
    clock.tick(60)


# Quit Pygame
pygame.quit()
sys.exit()

