
# Цвета
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Класс светофора
class TrafficLight:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = RED
        self.next_change_time = pygame.time.get_ticks() + 5000  # Следующее изменение цвета через 5 секунд
        self.last_color = None

    def change_color(self):
        if self.color == RED:
            self.color = YELLOW
            self.next_change_time = pygame.time.get_ticks() + 2000  # Держим желтый 2 секунды
            self.last_color = "red"
        elif self.color == YELLOW:
            if self.last_color == "red":
                self.color = GREEN
            else:
                self.color = RED
            self.next_change_time = pygame.time.get_ticks() + 5000  # Держим цвет на 5 секунд
        elif self.color == GREEN:
            self.color = YELLOW
            self.next_change_time = pygame.time.get_ticks() + 2000  # Держим желтый 2 секунды
            self.last_color = "green"

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time >= self.next_change_time:
            self.change_color()

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
