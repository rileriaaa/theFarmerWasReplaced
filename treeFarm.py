yo = get_world_size()
checkerFlag = True
yo2 = get_world_size() / 2


def harvs():

    flag = 0
    while flag <= yo:
        for i in range(yo):
            if can_harvest():
                harvest()
                move(East)
        move(North)
        flag += 1

    flag = 0


while True:
    flag = 0
    while flag <= yo:
        if checkerFlag == True:

            for i in range(yo):
                move(East)
                if get_pos_x() % 2 == 0:
                    if can_harvest():
                        harvest()
                    plant(Entities.Bush)
                else:
                    if can_harvest():
                        harvest()
                    plant(Entities.Tree)

            checkerFlag = False

        move(North)

        if checkerFlag == False:
            for i in range(yo):
                move(East)
                if get_pos_x() % 2 == 1:
                    if can_harvest():
                        harvest()
                    plant(Entities.Bush)
                else:
                    if can_harvest():
                        harvest()
                    plant(Entities.Tree)

            checkerFlag = True

        move(North)
