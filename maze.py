def next2(current_dir):
    if current_dir >= 1:
        next_dir = current_dir - 1
    else:
        next_dir = 3
    return next_dir


def next1(current_dir):
    if current_dir <= 2:
        next_dir = current_dir + 1
    else:
        next_dir = 0
    return next_dir


def backwards(current_dir):
    if current_dir == 0:
        return 2
    elif current_dir == 1:
        return 3
    elif current_dir == 2:
        return 0
    elif current_dir == 3:
        return 1


dir = [North, East, South, West]
current_dir = 0
catched = False


while True:
    if get_ground_type() == Grounds.Soil:
        till()
    plant(Entities.Bush)
    substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

    while get_entity_type() != Entities.Treasure:
        if move(dir[next1(current_dir)]):
            current_dir = next1(current_dir)
        elif move(dir[current_dir]):
            current_dir = current_dir
        elif move(dir[next2(current_dir)]):
            current_dir = next2(current_dir)
        elif move(dir[backwards(current_dir)]):
            current_dir = backwards(current_dir)

    if get_entity_type() == Entities.Treasure:
        harvest()
