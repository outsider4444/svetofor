import pygame

from Pedestrian import Pedestrian
from Car import Car, spawn_car, delete_car
from constants import WIDTH, HEIGHT, BLACK, GREEN, RED
from init import traffic_light, screen, cars, pedestrians, crossings
from Road import Road

pygame.init()
# Создание флага для проверки состояния паузы
paused = False

# Устанавливаем название окна
pygame.display.set_caption("Светофор")

# Создаем объект дороги
road = Road(x=0, y=(HEIGHT - 300) // 2, width=WIDTH, height=200, strip_width=10, strip_count=20)
# road_v = Road(x=WIDTH // 2, y=0, width=250, height=HEIGHT, strip_width=10, strip_count=20)

# Создание машину
delay = 700  # 1 секунды

# время, когда нужно создать следующую машину
next_circle_time = pygame.time.get_ticks() + delay

# Машины
# todo Убрать случайное появление машин. Нужно 12 вправо и 6 влево
car = Car(x=WIDTH - 1, y=(HEIGHT // 2) - 100, radius=25, speed=-4, id=0, direction="to_left")
cars.append(car)

# Пешеходы
pedestrian1 = Pedestrian(WIDTH / 2 - 50, 0, speed=1, direction="to_down")
# pedestrian2 = Pedestrian(WIDTH / 2 + 315, 650, speed=-1, direction="to_up")
pedestrians.append(
    pedestrian1
)
# pedestrians.append(
#     pedestrian2
# )

# Создаем объект для отслеживания времени
clock = pygame.time.Clock()

# Основной цикл игры
running = True
while running:
    # Ограничиваем частоту обновления кадров
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Обработка нажатий клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused  # Изменение значения флага при нажатии на пробел
    if not paused:
        # отрисовка дороги
        screen.fill(BLACK)
        road.draw(screen)
        # road_v.draw(screen)

        # Спавн и удаление машин
        current_time = pygame.time.get_ticks()
        if current_time >= next_circle_time:
            spawn_car(cars)
            next_circle_time = current_time + delay
        delete_car(cars)

        # todo Проверка чтобы люди не шли если машина на пешеходке


        # todo если человек на светофоре

        # Движение машины
        for car in cars:
            # Отрисовываем машину на экране
            if -1 < car.x < WIDTH + 5:
                car.draw(screen)
            if car.direction == "to_left":
                speed = -4
            else:
                speed = 4
            # car.accelerate()  # ускоряем круг
            car.move(speed=speed)

        # отрисовка перехода
        for crossing in crossings:
            crossing.draw(screen)

        # отрисовка светофора
        traffic_light.update()
        traffic_light.draw(screen)

        for pedestrian in pedestrians:
            # Отрисовка пешехода
            if pedestrian.direction == "to_up":
                speed = -1
            else:
                speed = 0.5
            pedestrian.move(speed)
            pedestrian.draw(screen)

        pygame.display.update()

# Выходим из игры
pygame.quit()
