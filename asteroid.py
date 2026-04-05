import pygame
import random
from circleshape import *
from constants import *
from logger import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

    # 2. If it's already small, stop
        if self.radius <= ASTEROID_MIN_RADIUS:
             return

    # 3. Log the split
        log_event("asteroid_split")

    # 4. Random angle
        angle = random.uniform(20, 50)

    # 5. Create two new directions
        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-angle)

    # 6. New smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

    # 7. Create two new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

    # 8. Set their velocities (slightly faster)
        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2
