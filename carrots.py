yo = get_world_size()

while True:
    for i in range(yo):

        if get_ground_type() == Grounds.Grassland:
            till()
            plant(Entities.Carrot)
            move(East)
        else:
            plant(Entities.Carrot)
            move(East)
            if can_harvest():
                harvest()
                plant(Entities.Carrot)

    move(North)
