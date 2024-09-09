import pygame
import random
import math

pygame.init()

width, height = 800,800
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Hello Stars")

class Star:
    def __init__(self):
        self.x = random.uniform(-width,width)
        self.y = random.uniform(-height,height)
        self.z = random.uniform(0,width)
        self.pz = self.z
    
    def update(self,speed):
        self.z -= speed
        if self.z < 1:
            self.x = random.uniform(-width,width)
            self.y = random.uniform(-height,height)
            self.z = random.uniform(0,width)
            self.pz = self.z
            
            

        
        
        
        
num_stars = 800
stars = [Star() for _ in range(num_stars)]
speed = 5

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # Limit to 60 FPS
    win.fill((0, 0, 0))  # Black background

    for star in stars:
        star.update(speed)
        

    pygame.display.update()  # Update the display

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
