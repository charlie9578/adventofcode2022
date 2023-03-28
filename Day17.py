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

# TODO: functionise things, speed up things by cropping the bottom when the full row is covered


import numpy as np

import shapely
import shapely.affinity
import shapely.ops

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show

# get the jet order
file_name = r"day/17/input"
jets=[]
with open(file_name, "r") as file:

    for line in file:
        for item in line:
            jets.append(item)

print(jets)

# create the shapes
horizontal_line = shapely.Polygon([(0, 0), (4, 0), (4, 1),(0,1)])
cross = shapely.Polygon([(0, 1), (1, 1), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (1, 3), (1, 2), (0,2)])
corner = shapely.Polygon([(0, 0), (3, 0), (3, 3), (2, 3), (2, 1), (0, 1)])
vertical_line = shapely.Polygon([(0, 0), (0, 4), (1, 4),(1,0)])
square = shapely.Polygon([(0, 0), (2, 0), (2, 2),(0,2)])

shapes = [horizontal_line,cross,corner,vertical_line,square]

xs, ys = [], []

cnt = 0
for shape in shapes:
    cnt = cnt + 1
    xs = xs + [np.array(shape.boundary.coords.xy[1])+cnt*5]
    ys = ys + [np.array(shape.boundary.coords.xy[0])]

# xs = [list(polygon.boundary.coords.xy[0]) for polygon in shapes]
# ys = [list(polygon.boundary.coords.xy[1]) for polygon in shapes]
print(corner.boundary.coords.xy[0])
print(corner.boundary.coords.xy[1])

print(xs)
print(ys)

source = ColumnDataSource(dict(xs = xs, ys = ys))

p = figure(title = 'Shapes', tools = 'pan, wheel_zoom, box_zoom, reset, hover, save',
           width = int(700/4),
           height = int(3000/4),
           x_range = (0,7),
           y_range = (0,30),
           aspect_scale=1)

p.patches(xs='ys', ys='xs', fill_alpha = 0.7, fill_color = 'green', line_color = 'black', line_width = 0.5, source = source)
show(p)



total_shapes = 5
shape_cnt = 1
start_height = 3
start_height_delta = 3
start_location = 2
dead_shapes = []
active_shape = shapes[0]
active_shape = shapely.affinity.translate(active_shape, xoff=start_location, yoff=start_height)
rock_cnt = 1
descend = 0
while rock_cnt < 2023:
    
    # determine jet movement
    jet = jets[descend%len(jets)]

    descend = descend + 1

    if jet == ">":
        if max(active_shape.boundary.coords.xy[0])<7:
            xoff = 1
        else:
            xoff = 0
    elif jet == "<":
        if min(active_shape.boundary.coords.xy[0])>0:
            xoff = -1
        else:
            xoff = 0
    else:
        print("jet error")


    # jet movement
    active_shape = shapely.affinity.translate(active_shape, xoff=xoff, yoff=0)
    
    # check if jet cause the shape to hit another one
    if len(dead_shapes) > 0:
        if active_shape.intersection(dead_shape).area>0:
            active_shape = shapely.affinity.translate(active_shape, xoff=-xoff, yoff=0)

    # fall movement
    active_shape = shapely.affinity.translate(active_shape, xoff=0, yoff=-1)
    
    # check if fall brings shape to rest on another shape
    if len(dead_shapes) > 0:
        if active_shape.intersection(dead_shape).area>0:
            active_shape = shapely.affinity.translate(active_shape, xoff=0, yoff=+1)
            dead_shapes = dead_shapes + [active_shape]
            dead_shape = shapely.ops.unary_union(dead_shapes)
            start_height = max(dead_shape.exterior.coords.xy[1])+start_height_delta
            active_shape = shapes[shape_cnt%total_shapes]
            shape_cnt = shape_cnt+1
            active_shape = shapely.affinity.translate(active_shape, xoff=start_location, yoff=start_height)

            rock_cnt = rock_cnt+1

            print(f"rocks: {rock_cnt} height: +{start_height-start_height_delta}")


    # check if fall brings shape to rest on the bottom
    if min(active_shape.exterior.coords.xy[1])<0:
        active_shape = shapely.affinity.translate(active_shape, xoff=0, yoff=+1)
        dead_shapes = dead_shapes + [active_shape]
        dead_shape = shapely.ops.unary_union(dead_shapes)
        start_height = max(dead_shape.exterior.coords.xy[1])+start_height_delta
        active_shape = shapes[shape_cnt%total_shapes]
        shape_cnt = shape_cnt+1
        active_shape = shapely.affinity.translate(active_shape, xoff=start_location, yoff=start_height)

    
    


    