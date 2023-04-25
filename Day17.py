"""
--- Day 17: Pyroclastic Flow ---

Your handheld device has located an alternative exit from the cave for you and the elephants. The ground is rumbling almost continuously now, but the strange valves bought you some time. It's definitely getting warmer in here, though.

The tunnels eventually open into a very tall, narrow chamber. Large, oddly-shaped rocks are falling into the chamber from above, presumably due to all the rumbling. If you can't work out where the rocks will fall next, you might be crushed!

The five types of rocks have the following peculiar shapes, where # is rock and . is empty space:

####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##

The rocks fall in the order shown above: first the - shape, then the + shape, and so on. Once the end of the list is reached, the same order repeats: the - shape falls first, sixth, 11th, 16th, etc.

The rocks don't spin, but they do get pushed around by jets of hot gas coming out of the walls themselves. A quick scan reveals the effect the jets of hot gas will have on the rocks as they fall (your puzzle input).

For example, suppose this was the jet pattern in your cave:

>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>

In jet patterns, < means a push to the left, while > means a push to the right. The pattern above means that the jets will push a falling rock right, then right, then right, then left, then left, then right, and so on. If the end of the list is reached, it repeats.

The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).

After a rock appears, it alternates between being pushed by a jet of hot gas one unit (in the direction indicated by the next symbol in the jet pattern) and then falling one unit down. If any movement would cause any part of the rock to move into the walls, floor, or a stopped rock, the movement instead does not occur. If a downward movement would have caused a falling rock to move into the floor or an already-fallen rock, the falling rock stops where it is (having landed on something) and a new rock immediately begins falling.

Drawing falling rocks with @ and stopped rocks with #, the jet pattern in the example above manifests as follows:

The first rock begins falling:
|..@@@@.|
|.......|
|.......|
|.......|
+-------+

Jet of gas pushes rock right:
|...@@@@|
|.......|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
+-------+

Jet of gas pushes rock left:
|..@@@@.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|..####.|
+-------+

A new rock begins falling:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|...@...|
|..@@@..|
|...@...|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|..####.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|...#...|
|..###..|
|...#...|
|..####.|
+-------+

A new rock begins falling:
|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|...#...|
|..###..|
|...#...|
|..####.|
+-------+

The moment each of the next few rocks begins falling, you would see this:

|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|..#....|
|..#....|
|####...|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|..#....|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|.....#.|
|.....#.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|....##.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|##..##.|
|######.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

To prove to the elephants your simulation is accurate, they want to know how tall the tower will get after 2022 rocks have stopped (but before the 2023rd rock begins falling). In this example, the tower of rocks will be 3068 units tall.

How many units tall will the tower of rocks be after 2022 rocks have stopped falling?
"""

import numpy as np
import math

# get the jet order
file_name = r"day/17/input"
jets=[]
with open(file_name, "r") as file:

    for line in file:
        for item in line:
            jets.append(item)

print(jets)

# create the shapes
horizontal_line = np.array([[1,1,1,1]])
cross = np.array([[0,1,0],[1,1,1],[0,1,0]])
corner = np.array([[0,0,1],[0,0,1],[1,1,1]])
vertical_line = np.array([[1],[1],[1],[1]])
square = np.array([[1,1],[1,1]])

shapes = [horizontal_line,cross,corner,vertical_line,square]
print(shapes)

# create the initial tunnel
tunnel = np.array([[1]+[0]*7+[1]]*50000+[[9]*9])
print(tunnel)


descent = -1
height_tower_only = 1
height_repetitions = 0
repeat_descent = None
repeat_shape = None
start_repeat_check = 10000
end_seq_height = None
rock_cnt = 0
total_rocks = 1000000000000
while rock_cnt < (total_rocks):
    
    rock_cnt = rock_cnt+1

    active_shape = shapes[(rock_cnt-1)%len(shapes)]

    # print(active_shape)

    x_loc = 3
    y_loc = tunnel.shape[0]-height_tower_only-active_shape.shape[0]-3

    falling = True
    while falling:

        # determine jet movement
        descent = (descent + 1)%len(jets)
        jet = jets[descent]
        

        # jet push
        if jet == ">":
            x_loc = x_loc+1
            tunnel_section = tunnel[y_loc:y_loc+active_shape.shape[0],x_loc:x_loc+active_shape.shape[1]]
            if np.multiply(active_shape,tunnel_section).sum()>=1:
                x_loc = x_loc-1

        elif jet == "<":
            x_loc = x_loc-1
            tunnel_section = tunnel[y_loc:y_loc+active_shape.shape[0],x_loc:x_loc+active_shape.shape[1]]
            if np.multiply(active_shape,tunnel_section).sum()>=1:
                x_loc = x_loc+1

        if rock_cnt==42:
            print(f"Jet moved: {jet}")
            tunnel_tmp = tunnel.copy()
            tunnel_tmp[y_loc:y_loc+active_shape.shape[0],x_loc:x_loc+active_shape.shape[1]] = tunnel_tmp[y_loc:y_loc+active_shape.shape[0],x_loc:x_loc+active_shape.shape[1]]+active_shape*(rock_cnt%len(shapes)+2)
            print(tunnel_tmp)

        # rock descent
        y_loc = y_loc + 1
        tunnel_section = tunnel[y_loc:y_loc+active_shape.shape[0],x_loc:x_loc+active_shape.shape[1]]

        # stop falling if hits the bottom or another shape
        if np.multiply(active_shape,tunnel_section).sum()>1:
            y_loc = y_loc - 1
            if height_tower_only<tunnel.shape[0]-y_loc:
                height_tower_only = tunnel.shape[0]-y_loc
            tunnel[y_loc:y_loc+active_shape.shape[0],x_loc:x_loc+active_shape.shape[1]] = tunnel[y_loc:y_loc+active_shape.shape[0],x_loc:x_loc+active_shape.shape[1]]+active_shape*(rock_cnt%len(shapes)+2)
            # print(tunnel)
            falling = False

    print(f"{rock_cnt} rocks have fallen, with tower height: {(height_tower_only-1)+height_repetitions}, descent: {descent}, shape: {(rock_cnt-1)%len(shapes)}")

    if rock_cnt==start_repeat_check:
        # print(f"{rock_cnt} rocks have fallen, with tower height: {(height_tower_only-1)+height_repetitions}, descent: {descent}, shape: {(rock_cnt-1)%len(shapes)}")
        repeat_descent = descent
        repeat_shape = (rock_cnt-1)%len(shapes)
        start_seq_repeat = rock_cnt
        start_seq_height = height_tower_only-1
        top = (tunnel>0).argmax(axis=0)[1:-1] - min((tunnel>0).argmax(axis=0)[1:-1])
        
    if rock_cnt>start_repeat_check and end_seq_height==None:
        if descent==repeat_descent and (rock_cnt-1)%len(shapes)==repeat_shape:
            if np.array_equal((tunnel>0).argmax(axis=0)[1:-1] - min((tunnel>0).argmax(axis=0)[1:-1]),top):
                # print(f"{rock_cnt} rocks have fallen, with tower height: {(height_tower_only-1)+height_repetitions}, descent: {descent}, shape: {(rock_cnt-1)%len(shapes)}")
                end_seq_repeat = rock_cnt
                end_seq_height = height_tower_only-1
                repetitions = math.floor((1000000000000-rock_cnt)/(end_seq_repeat-start_seq_repeat))-1
                rock_cnt = rock_cnt + repetitions*(end_seq_repeat-start_seq_repeat)
                height_repetitions = repetitions*(end_seq_height-start_seq_height)
                print(f"Descent: {descent}, shape: {repeat_shape}, start seq: {start_seq_repeat}, start height: {start_seq_height}, end seq: {end_seq_repeat}, end height: {end_seq_height}")
                print(top,(tunnel>0).argmax(axis=0)[1:-1] - min((tunnel>0).argmax(axis=0)[1:-1]))
                
print(f"{rock_cnt} rocks have fallen, with tower height: {(height_tower_only-1)+height_repetitions}, descent: {descent}, shape: {(rock_cnt-1)%len(shapes)}")


"""
Your puzzle answer was 3184.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

The elephants are not impressed by your simulation. They demand to know how tall the tower will be after 1000000000000 rocks have stopped! Only then will they feel confident enough to proceed through the cave.

In the example above, the tower would be 1514285714288 units tall!

How tall will the tower be after 1000000000000 rocks have stopped?

Puzzle answer: 1577077363915
"""    

