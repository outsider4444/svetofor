import pygame

from Pedestrian import Pedestrian
from Car import Car, spawn_car, delete_car
from constants import WIDTH, HEIGHT
from init import traffic_light, crossing, screen, cars
from Road import Road

pygame.init()
# Создание флага для проверки состояния паузы
paused = False

# Устанавливаем название окна
pygame.display.set_caption("Светофор")

# Создаем объект дороги
road = Road(x=0, y=(HEIGHT - 300) // 2, width=WIDTH, height=250, strip_width=10, strip_count=20)

# Создание машину
delay = 500  # 1 секунды

# время, когда нужно создать следующую машину
next_circle_time = pygame.time.get_ticks() + delay

car = Car(x=WIDTH-1, y=(HEIGHT // 2) - 100, radius=25, speed=-4, id=0, direction="to_left")
cars.append(car)

# Создание пешехода
pedestrians = []

pedestrian1 = Pedestrian(WIDTH / 2 + 85, 50, speed=1, direction="to_down")
pedestrian2 = Pedestrian(WIDTH / 2 + 115, 650, speed=-1, direction="to_up")
pedestrians.append(
    pedestrian1
)
pedestrians.append(
    pedestrian2
)

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
        road.draw(screen)

        # Спавн и удаление машин
        current_time = pygame.time.get_ticks()
        if current_time >= next_circle_time:
            spawn_car(cars)
            next_circle_time = current_time + delay
        delete_car(cars)

        # Проверка чтобы люди не шли если машина на пешеходке
        for pedestrian in pedestrians:
            if pedestrian.direction == "to_down":
                # Машина на пешеходке
                if crossing.y - pedestrian.size <= pedestrian.y <= crossing.y:
                    for car in cars:
                        if (car.direction == "to_right" and crossing.x + crossing.width >= car.x >= crossing.x)\
                                or (car.direction == "to_left" and crossing.x <= car.x <= crossing.x + crossing.width) :
                            pedestrian.check_car = True
                            break
                        else:
                            pedestrian.check_car = False

        # движение человека
        for pedestrian in pedestrians:
            if pedestrian.direction == "to_up":
                speed = -1
            else:
                speed = 1
            pedestrian.move(speed)

        for pedestrian in pedestrians:
            # если человек на светофоре
            if pedestrian.check_crossing:
                # если машина возле пешеходки
                for car in cars:
                    print(car.id, car.direction, car.check_man)
                    if car.direction == "to_right":
                        if crossing.x - car.radius <= car.x <= crossing.x + car.radius:
                            car.check_man = True
                        else:
                            car.check_man = False
                    elif car.direction == "to_left":
                        if crossing.x + crossing.width + car.radius >= car.x >= crossing.x - car.radius:
                            car.check_man = True
                        else:
                            car.check_man = False

        # Отрисовываем машину на экране
        for car in cars:
            if 0 < car.x < WIDTH + 5:
                car.draw(screen)

        # Движение машины
        for car in cars:
            if car.direction == "to_left":
                speed = -4
            else:
                speed = 4
            car.move(speed=speed)
        # отрисовка перехода
        crossing.draw(screen)

        # отрисовка светофора
        traffic_light.update()
        traffic_light.draw(screen)

        for pedestrian in pedestrians:
            # Отрисовка пешехода
            pedestrian.draw(screen)

        pygame.display.update()

# Выходим из игры
pygame.quit()
