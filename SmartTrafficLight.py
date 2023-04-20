import time

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

class SmartTrafficLight(pygame.sprite.Sprite):
    def __init__(self, x, y, red_time, green_time):
        super().__init__()
        self.colors = ['red', 'yellow', 'green']
        self.color = RED
        self.image = pygame.Surface((30, 90))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.red_time = red_time
        self.green_time = green_time
        self.last_color_change = time.time()
        self.cars = 0
        self.pedestrians = 0
        self.new_color = "red"

    def change_color(self):
        if time.time() - self.last_color_change >= self.red_time and self.color == RED:
            self.color = YELLOW
            self.last_color_change = time.time()
            self.new_color = "red"
            self.red_time = 3
        elif time.time() - self.last_color_change >= 1 and self.color == YELLOW and self.new_color == "red":
            self.color = GREEN
            self.last_color_change = time.time()
            self.new_color = "green"
            self.red_time = 3
        elif time.time() - self.last_color_change >= self.green_time and self.color == GREEN:
            self.color = YELLOW
            self.last_color_change = time.time()
        elif time.time() - self.last_color_change >= 1 and self.color == YELLOW and self.new_color == "green":
            self.color = RED
            self.last_color_change = time.time()
            self.new_color = "red"
        print(time.time() - self.last_color_change, self.green_time, self.red_time)

    def adjust_times(self):
        # Определяем, насколько должен быть уменьшен или увеличен таймер для каждого цвета светофора
        car_multiplier = (10 - self.cars) / 10 if self.cars <= 10 else 0
        ped_multiplier = (5 - self.pedestrians) / 5 if self.pedestrians <= 5 else 0
        red_adjustment = 3 * ped_multiplier
        green_adjustment = 10 * car_multiplier
        print(green_adjustment)

        # Обновляем таймеры для каждого цвета светофора
        self.red_time = max(2, red_adjustment)
        self.green_time = max(2, green_adjustment)

    def update(self, cars, pedestrians):
        self.cars = cars
        self.pedestrians = pedestrians
        self.adjust_times()
        self.change_color()

    def draw(self, screen):
        if self.color == RED:
            pygame.draw.circle(screen, RED, self.rect.center, 25)
        elif self.color == YELLOW:
            pygame.draw.circle(screen, YELLOW, self.rect.center, 25)
        elif self.color == GREEN:
            pygame.draw.circle(screen, GREEN, self.rect.center, 25)