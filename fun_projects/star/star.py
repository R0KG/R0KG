import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Starfield Simulation")

# Define Star class
class Star:
    def __init__(self):
        self.x = random.uniform(-width, width)
        self.y = random.uniform(-height, height)
        self.z = random.uniform(0, width)
        self.pz = self.z

    def update(self, speed):
        self.z -= speed
        if self.z < 1:
            self.z = width
            self.x = random.uniform(-width, width)
            self.y = random.uniform(-height, height)
            self.pz = self.z

    def show(self, surface):
        sx = self.map_to_screen(self.x / self.z, 0, 1, 0, width)
        sy = self.map_to_screen(self.y / self.z, 0, 1, 0, height)

        r = self.map_to_screen(self.z, 0, width, 16, 0)
        pygame.draw.circle(surface, (255, 255, 255), (int(sx), int(sy)), int(r))
        
        pygame.draw.circle(surface, (255, 255, 255), (int(sx), int(sy)), int(r))
        
        line_length = random.uniform(1,1.1)
        px = self.map_to_screen(self.x / self.pz, 0, line_length, 0, width)
        py = self.map_to_screen(self.y / self.pz, 0, line_length, 0, height)

        self.pz = self.z

        pygame.draw.line(surface, (255, 255, 255), (int(px), int(py)), (int(sx), int(sy)))

    @staticmethod
    def map_to_screen(value, start1, stop1, start2, stop2):
        return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))

# Initialize stars
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
        star.show(win)

    pygame.display.update()  # Update the display

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
