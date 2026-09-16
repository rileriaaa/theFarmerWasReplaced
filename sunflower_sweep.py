def go_to(x, y):
    while get_pos_x() != x:
        if get_pos_x() < x:
            move(East)
        else:
            move(West)
    while get_pos_y() != y:
        if get_pos_y() < y:
            move(North)
        else:
            move(South)


def plantSunflower():
    yo = get_world_size()
    for y in range(yo):
        for x in range(yo):
            go_to(x, y)
            if get_ground_type() != Grounds.Soil:
                till()
            if can_harvest():
                harvest()
            if get_entity_type() != Entities.Sunflower:
                plant(Entities.Sunflower)


def harvestSunflower():
    yo = get_world_size()
    for y in range(yo):
        for x in range(yo):
            go_to(x, y)
            if get_entity_type() == Entities.Sunflower and can_harvest():
                harvest()


clear()
while True:
    plantSunflower()
    while harvestSunflower():
        pass
