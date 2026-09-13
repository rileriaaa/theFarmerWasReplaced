import harvess

yo = get_world_size()
checkerFlag = True

while True:
    flag = 0
    while flag <= 3:
        if checkerFlag == True:
            for i in range(yo):
                move(East)
                if get_pos_x() % 2 == 0:
                    if can_harvest():
                        harvest()
                    else:
                        harvest()
                else:
                    plant(Entities.Tree)
                    use_item(Items.Water)

            checkerFlag = False

        move(North)

        if checkerFlag == False:
            for i in range(yo):
                move(East)
                if get_pos_x() % 2 == 1:
                    if can_harvest():
                        harvest()
                    else:
                        harvest()
                else:
                    plant(Entities.Tree)
                    use_item(Items.Water)
                    move(East)

            checkerFlag = True

        move(North)
        flag += 1

        if flag == 3:
            harvess.harvs()
            flag = 0
