# Если человек на светофоре
def man_on_crossing(cars, pedestrians, crossings):
    for car in cars:
        for pedestrian in pedestrians:
            if car.direction == "to_right":
                if crossings[0].x - 5 <= car.x + car.radius <= crossings[0].x:
                    if crossings[0].x <= pedestrian.x <= crossings[0].x + crossings[0].width:
                        if crossings[0].y <= pedestrian.y <= crossings[0].y + crossings[0].height:
                            car.check_man = True
                        else:
                            car.check_man = False
                if crossings[1].x - 5 <= car.x + car.radius <= crossings[1].x:
                    if crossings[1].x <= pedestrian.x <= crossings[1].x + crossings[1].width:
                        if crossings[1].y <= pedestrian.y <= crossings[1].y + crossings[1].height:
                            car.check_man = True
                        else:
                            car.check_man = False
            elif car.direction == "to_left":
                if crossings[1].x + crossings[1].width <= car.x - car.radius <= crossings[1].x + crossings[1].width + 5:
                    if crossings[1].x <= pedestrian.x <= crossings[1].x + crossings[1].width:
                        if crossings[1].y <= pedestrian.y + pedestrian.size <= crossings[1].y + crossings[1].height:
                            car.check_man = True
                        else:
                            car.check_man = False
                if crossings[0].x + crossings[0].width <= car.x - car.radius <= crossings[0].x + crossings[0].width + 5:
                    if crossings[0].x <= pedestrian.x <= crossings[0].x + crossings[0].width:
                        if crossings[0].y <= pedestrian.y + pedestrian.size <= crossings[0].y + crossings[0].height:
                            car.check_man = True
                        else:
                            car.check_man = False
