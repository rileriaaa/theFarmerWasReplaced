while True:
    for i in range(get_world_size()):
        if can_harvest():
            harvest()
            plant(Entities.Grass)
            move(East)
        else:
            move(East)

    move(North)
    for i in range(get_world_size()):
        if can_harvest():
            harvest()
            plant(Entities.Bush)
            move(East)
        else:
            move(East)

    move(North)

    for i in range(get_world_size()):
        if get_ground_type() == Grounds.Soil:
            break

        if get_ground_type() == Grounds.Grassland:
            till()
            plant(Entities.Carrot)
            move(East)
        else:
            move(East)

    for _ in range(get_world_size()):
        if num_items(Items.Hay) <= 5 and num_items(Items.Wood) <= 5:
            break
        else:
            if can_harvest():
                harvest()
                plant(Entities.Carrot)
                move(East)
            else:
                move(East)
    move(North)

    for i in range(get_world_size()):
        if can_harvest():
            harvest()
            plant(Entities.Grass)
            move(East)
        else:
            move(East)

    move(North)
