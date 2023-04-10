import pygame
from init import traffic_light, crossing, YELLOW

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Car:
    def __init__(self, x, y, radius, speed, WIDTH):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.WIDTH = WIDTH
        self.finish_line = 500  # примерная координата X, до которой нужно доехать
        self.left_to_right = True

    def move(self, speed):
        self.x += self.speed
        self.speed = speed
        if self.x >= crossing.x - self.radius and self.x <= self.WIDTH - crossing.x:
            if traffic_light.color == RED or traffic_light.color == YELLOW:
                self.speed = 0

        if self.x > self.WIDTH:
            self.x = 0

    def draw(self, surface):
        pygame.draw.circle(surface, BLACK, (int(self.x), int(self.y)), self.radius)