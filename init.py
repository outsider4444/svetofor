import pygame

from SmartTrafficLight import SmartTrafficLight
from Crossing import PedestrianCrossing
from constants import WIDTH, HEIGHT
from TrafficLight import TrafficLight

# Создаем окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Светофор
# traffic_light = TrafficLight(WIDTH // 2, (HEIGHT // 2) + 125, 25)
traffic_light_p = TrafficLight(WIDTH // 2 + 50, (HEIGHT // 2) + 150, 15)
# Умный светофор
smart_traffic_light = SmartTrafficLight((WIDTH // 2) + 50, (HEIGHT // 2) + 150, 0, 0)
traffic_light = smart_traffic_light

# рисуем границы для перехода
crossing1 = PedestrianCrossing((WIDTH / 2) - 220, (HEIGHT / 2)-20, 100, 240, 2, 0)
crossing2 = PedestrianCrossing((WIDTH / 2) + 119, (HEIGHT / 2)-20, 100, 240, 2, 1)

crossing3 = PedestrianCrossing(WIDTH / 2, (HEIGHT / 2) - 150, direction="horizontal")
crossing4 = PedestrianCrossing(WIDTH / 2, (HEIGHT / 2) + 200, direction="horizontal")

crossings = [
    crossing1,
    crossing2,
    # crossing3, crossing4
]

cars = []
cars_to_right, cars_to_left = [], []

# сортировка машин
# for i in range(len(cars)):
#     if cars[i].y == (HEIGHT // 2) + 55:
#         cars_to_right.append(cars[i])
#     else:
#         cars_to_left.append(cars[i])
# for i in range(len(cars_to_right)):
#     for j in range(len(cars_to_right)):
#         if cars_to_right[i].x < cars_to_right[j].x:
#             cars_to_right[i], cars_to_right[j] = cars_to_right[j], cars_to_right[i]
# for i in range(len(cars_to_left)):
#     for j in range(len(cars_to_left)):
#         if cars_to_left[i].x < cars_to_left[j].x:
#             cars_to_left[i], cars_to_left[j] = cars_to_left[j], cars_to_left[i]
# cars = cars_to_right + cars_to_left

# Создание пешехода
pedestrians = []
all_sprites = pygame.sprite.Group()