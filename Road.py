import pygame

from constants import WHITE, BLACK


class Road:
    def __init__(self, x, y, width, height, strip_width, strip_count):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.strip_width = strip_width
        self.strip_count = strip_count
        self.segment_width = (self.width - (self.strip_count + 1) * self.strip_width) // self.strip_count

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height))
        for i in range(self.strip_count):
            strip_x = self.x + (i + 1) * self.strip_width + i * self.segment_width
            strip_y = self.y + (self.height - self.strip_width) // 2
            pygame.draw.rect(surface, BLACK, (strip_x, strip_y, self.segment_width, self.strip_width))
