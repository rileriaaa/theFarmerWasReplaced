yo = get_world_size()


while True:
    for i in range(yo):
        if get_ground_type() == Grounds.Grassland:
            till()
            plant(Entities.Pumpkin)
            move(East)
        else:
            move(East)

    for j in range(yo):
        if get_entity_type() == Entities.Dead_Pumpkin:
            harvest()
            plant(Entities.Pumpkin)
        else:
            move(East)

    move(North)

# fuckass puimpkin

# add harvest if it is a one big Pumpkin
