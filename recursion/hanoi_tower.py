def move_dish(level, start, inter, dest):
    if level == 1:
        print('from %s move the disk %d to %s' % (start, level, dest))
    else:
        move_dish(level-1, start, dest, inter)
        print('from %s move the disk %d to %s' % (start, level, dest))
        move_dish(level-1, inter, start, dest)

n_disk = 5
move_dish(n_disk, 'A', 'B', 'C')



