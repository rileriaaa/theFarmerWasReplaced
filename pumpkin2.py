def back(x=0, y=0):
    while x != get_pos_x() or y != get_pos_y():
        while get_pos_x() != x:
            if get_pos_x() < x:
                moveEx(East)
            else:
                moveEx(West)
        while get_pos_y() != y:
            if get_pos_y() < y:
                moveEx(North)
            else:
                moveEx(South)


def moveEx(dir):
    dirs = [East, South, West, North]
    dirs.remove(dir)
    if not move(dir):
        if not move(dirs[0]):
            if not move(dirs[1]):
                if not move(dirs[2]):
                    return False


def do(x, worldsize=0):
    if worldsize == 0:
        worldsize = get_world_size()
    dir = East
    for i in range(worldsize):
        for j in range(worldsize - 1):
            x()
            move(dir)
        x()
        move(North)
        if dir == East:
            dir = West
        else:
            dir = East


def plantpumpkin():
    plant(Entities.Pumpkin)


def doPumpkin():
    back()
    success = []

    def adddie():
        if not can_harvest():
            success.append({"x": get_pos_x(), "y": get_pos_y()})
            plantpumpkin()

    def removedie():
        if can_harvest():
            success.remove({"x": get_pos_x(), "y": get_pos_y()})
        else:
            plantpumpkin()

    def plantonce(x):
        dir = East
        for _ in range(get_world_size()):
            for _ in range(get_world_size() - 1):
                x()
                move(dir)
            x()
            move(North)
            if dir == East:
                dir = West
            else:
                dir = East

    plantonce(plantpumpkin)
    back()
    plantonce(adddie)

    while len(success) != 0:
        for pos in success:
            back(pos["x"], pos["y"])
            removedie()

    return len(success) == 0


def pumpProject():
    def tillx():
        if get_ground_type() == Grounds.Grassland:
            till()

    back()
    do(tillx)

    while True:
        while doPumpkin():
            back()
            harvest()


clear()
pumpProject()
