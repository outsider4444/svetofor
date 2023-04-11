# Создаем светофор
import pygame

from PedestrianCrossing import PedestrianCrossing
from constants import WIDTH, HEIGHT
from traffic_light import TrafficLight


# Создаем окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# рисуем светофор
traffic_light = TrafficLight(WIDTH // 2 + 150, (HEIGHT // 2) + 150, 25)

# рисуем границы для перехода
crossing = PedestrianCrossing(WIDTH / 2 + 50, HEIGHT / 2 - 50)
