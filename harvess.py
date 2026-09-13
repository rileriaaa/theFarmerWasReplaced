def harvs():
    yo = get_world_size()
    flag = 0
    while flag <= 5:
        for i in range(yo):
            if can_harvest():
                harvest()
                move(East)
        move(North)
        flag += 1

    flag = 0
