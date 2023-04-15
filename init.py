# Создаем светофор
import random

import pygame

from Crossing import PedestrianCrossing
from constants import WIDTH, HEIGHT
from TrafficLight import TrafficLight

# Создаем окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# рисуем светофор
traffic_light = TrafficLight(WIDTH // 2 + 200, (HEIGHT // 2) + 150, 25)

# рисуем границы для перехода
crossing1 = PedestrianCrossing(WIDTH / 2 - 100, HEIGHT / 2 - 50,100,200,2, 0)
crossing2 = PedestrianCrossing(WIDTH / 2 + 275, HEIGHT / 2 - 50,100,200,2, 1)

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
for i in range(len(cars)):
    if cars[i].y == (HEIGHT // 2) + 55:
        cars_to_right.append(cars[i])
    else:
        cars_to_left.append(cars[i])
for i in range(len(cars_to_right)):
    for j in range(len(cars_to_right)):
        if cars_to_right[i].x < cars_to_right[j].x:
            cars_to_right[i], cars_to_right[j] = cars_to_right[j], cars_to_right[i]
for i in range(len(cars_to_left)):
    for j in range(len(cars_to_left)):
        if cars_to_left[i].x < cars_to_left[j].x:
            cars_to_left[i], cars_to_left[j] = cars_to_left[j], cars_to_left[i]
cars = cars_to_right + cars_to_left

# Создание пешехода
pedestrians = []
