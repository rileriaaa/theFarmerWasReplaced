while True:
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            harvest()
            if get_ground_type() == Grounds.Grassland:
                till()
            plant(Entities.Bush)
            use_item(Items.Fertilizer)
            move(East)
        move(North)
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            harvest()
            plant(Entities.Bush)
            use_item(Items.Fertilizer)
            move(East)
        move(North)
