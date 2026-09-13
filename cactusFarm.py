yo = get_world_size()


def tillSoil():
    till()


def checkSoil():
    if get_ground_type() == Grounds.Grassland:
        tillSoil()


def sdasdadasdsada():
    planted = 0
    while True:
        for _ in range(yo):
            checkSoil()
            plant(Entities.Cactus)
            planted += 1
            move(East)
        move(North)
        if planted == 256:
            break


def plantFlow():
    planted = 0
    while planted != 256:
        for _ in range(yo):
            plant(Entities.Cactus)
            planted += 1
            move(North)
        move(East)
        print(planted)


def mainFlow():
    while True:

        edge = get_world_size() - 1
        columns_sorted = 0
        rows_sorted = 0
        while True:

            if columns_sorted == 15:
                break
            sorted = True
            while sorted:
                sorted = False
                for i in range(yo):
                    current = measure()
                    if edge == get_pos_y():
                        pass
                    else:
                        if current > measure(North):
                            swap(North)
                            sorted = True
                    move(North)

            move(East)
            columns_sorted += 1
            print(columns_sorted)

        while True:

            if rows_sorted == 15:
                break
            sorted = True
            while sorted:
                sorted = False
                for i in range(yo):
                    current = measure()
                    if edge == get_pos_x():
                        pass
                    else:
                        if current > measure(East):
                            swap(East)
                            sorted = True
                    move(East)
            move(South)
            rows_sorted += 1
            print(rows_sorted)

        if columns_sorted == 15 and rows_sorted == 15:
            harvest()
            columns_sorted = 0
            rows_sorted = 0


def main():
    while True:
        plantFlow()
        mainFlow()


main()

# di pa tapos aslkjaslkdjklajdasdjalkjd
