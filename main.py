import pygame

from Pedestrian import Pedestrian
from Car import Car
from init import traffic_light, crossing
from Road import Road

pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

# Создаем окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Устанавливаем название окна
pygame.display.set_caption("Светофор")

# Создаем объект дороги
road = Road(x=0, y=(HEIGHT - 300) // 2, width=WIDTH, height=250, strip_width=10, strip_count=20)

# # Создаем светофор
# traffic_light = TrafficLight(WIDTH // 2 + 150, (HEIGHT // 2) + 150, 25)

# # рисуем границы для перехода
# crossing = PedestrianCrossing(WIDTH/2-50, HEIGHT/2-50)

# Создание машину
car1 = Car(x=11, y=(HEIGHT // 2) + 55, radius=25, speed=0, WIDTH=WIDTH)
car2 = Car(x=0, y=(HEIGHT // 2) - 140, radius=25, speed=0, WIDTH=WIDTH)

# Создание пешехода
pedestrian = Pedestrian(WIDTH/2 - 12, 0, speed=0)


# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # отрисовка дороги
    road.draw(screen)

    # Движение машины
    car1.move(2*0.2)
    car2.move(2*0.2)
    # движение человека
    pedestrian.move(2*0.2)

    # отрисовка перехода
    crossing.draw(screen)

    # отрисовка светофора
    traffic_light.update()
    traffic_light.draw(screen)

    # Отрисовываем машину на экране
    car1.draw(screen)
    car2.draw(screen)

    # Отрисовка пешехода
    pedestrian.draw(screen)


    pygame.display.update()
# Выходим из игры
pygame.quit()