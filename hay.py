yo = get_world_size()

while True:
    for i in range(yo):
        harvest()
        move(East)
    move(North)
