# Создаем светофор
from PedestrianCrossing import PedestrianCrossing
from traffic_light import TrafficLight

# Размеры экрана
WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

# рисуем светофор
traffic_light = TrafficLight(WIDTH // 2 + 150, (HEIGHT // 2) + 150, 25)

# рисуем границы для перехода
crossing = PedestrianCrossing(WIDTH/2-50, HEIGHT/2-50)
