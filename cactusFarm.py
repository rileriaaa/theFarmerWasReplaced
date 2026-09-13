yo = get_world_size()
yo2 = yo * yo


def checkSoil():
    while True:
        if get_ground_type() == Grounds.Soil:
            break
        if get_ground_type() == Grounds.Grassland:
            tilled = 0
            while tilled != yo2:
                for i in range(yo):
                    till()
                    tilled += 1
                    move(East)
                move(North)


def plantFlow():
    planted = 0
    while planted != yo2:
        for i in range(yo):
            plant(Entities.Cactus)
            planted += 1
            move(North)
        move(East)
        print(planted)


def mainFlow():
    while True:
        edge = get_world_size() - 1
        columns_sorted = yo
        rows_sorted = yo
        while True:
            if columns_sorted == yo:
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
            if rows_sorted == yo:
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

        if columns_sorted == yo and rows_sorted == yo:
            harvest()
            columns_sorted = 0
            rows_sorted = 0
            break


def main():
    while True:
        checkSoil()
        plantFlow()
        mainFlow()


main()
