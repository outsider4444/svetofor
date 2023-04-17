
# Цвета
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Класс светофора
class TrafficLight:
    def __init__(self, x, y, radius, red_time=5, yellow_time=2, green_time=5):
        self.x = x
        self.y = y
        self.radius = radius

        self.red_time = red_time
        self.yellow_time = yellow_time
        self.green_time = green_time

        self.color = RED
        self.next_change_time = pygame.time.get_ticks() + 3000  # Следующее изменение цвета через 3 секунд
        self.new_color = "red"

    def change_color(self,next_color=None, duration=None):
        if self.color == RED:
            self.color = YELLOW
            self.next_change_time = pygame.time.get_ticks() + 1200  # Держим желтый 1.2 секунды
        elif self.color == YELLOW:
            if self.new_color == "red":
                self.color = GREEN
                self.new_color = "green"
                self.next_change_time = pygame.time.get_ticks() + 3000  # Держим зеленый на 2 секунд
            else:
                self.color = RED
                self.new_color = "red"
                self.next_change_time = pygame.time.get_ticks() + 6000  # Держим красный на 6 секунд
        elif self.color == GREEN:
            self.color = YELLOW
            self.next_change_time = pygame.time.get_ticks() + 1200  # Держим желтый 1.2 секунды

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time >= self.next_change_time:
            self.change_color()

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
