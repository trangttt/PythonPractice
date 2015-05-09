for start_x, start_y in routes:
# Now loop through all possible starting positions
    # and all possible directions
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        # Initialise x and y to the starting position
        x = start_x
        y = start_y
        # Now apply each instruction sequentially
        for instruction in path:
            x, y, dx, dy = instruction(x, y, dx, dy)
            # if the new position is not possible then stop
            # as the route is invalid
            if (x, y) not in routes:
                break
        else:
            # if you make it through all the instructions then the route is
            # valid so print the solution
            print('From ({}, {}) to ({}, {})'.format(start_x, start_y,
                                                     x, y))
