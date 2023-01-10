"""
--- Day 8: Treetop Tree House ---

The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

30373
25512
65332
33549
35390

Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

    The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
    The top-middle 5 is visible from the top and right.
    The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
    The left-middle 5 is visible, but only from the right.
    The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
    The right-middle 3 is visible from the right.
    In the bottom row, the middle 5 is visible, but the 3 and 4 are not.

With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?
"""

import numpy as np
import pandas as pd

data = []
with open(r"day/8/input", "r") as file:

    for line in file:
        line = line.strip()
        x = [int(x) for x in line]
        data.append(x)

print(data)



def determine_line_visibility(line):
    max_value = -1
    line_visiblity = []
    for value in line:
        if value <= max_value:
            line_visiblity.append(0)
        else:
            max_value = value
            line_visiblity.append(1)
    return line_visiblity

data_left_visibility = []
data_right_visibility = []
for row in data:
    data_left_visibility.append(determine_line_visibility(row))
    data_right_visibility.append(list(reversed(determine_line_visibility(reversed(row)))))

print(data_left_visibility)
print(data_right_visibility)

def transpose(data):
    data_T = [list(x) for x in zip(*data)]
    return data_T

# print(data)

# print(transpose(data))

data_top_visibility=[]
data_bottom_visibility=[]
for row in transpose(data):
    data_top_visibility.append(determine_line_visibility(row))
    data_bottom_visibility.append(list(reversed(determine_line_visibility(reversed(row)))))

data_top_visibility=transpose(data_top_visibility) 
data_bottom_visibility=transpose(data_bottom_visibility)

print(data_top_visibility)
print(data_bottom_visibility)

mask=np.array([data_left_visibility,data_right_visibility,data_top_visibility,data_bottom_visibility]).sum(axis=0)

print(mask)
print((mask>0).sum())



"""
Your puzzle answer was 1843.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.

To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

In the example above, consider the middle 5 in the second row:

30373
25512
65332
33549
35390

    Looking up, its view is not blocked; it can see 1 tree (of height 3).
    Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
    Looking right, its view is not blocked; it can see 2 trees.
    Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).

A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

However, you can do even better: consider the tree of height 5 in the middle of the fourth row:

30373
25512
65332
33549
35390

    Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
    Looking left, its view is not blocked; it can see 2 trees.
    Looking down, its view is also not blocked; it can see 1 tree.
    Looking right, its view is blocked at 2 trees (by a massive tree of height 9).

This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

Consider each tree on your map. What is the highest scenic score possible for any tree?
"""

array = np.array(data)

print(array)
print(array[:,0])
print(array[0,:])

def trees_visible(row, cnt_element, element):
    tree_count=0
    for tree in row[cnt_element+1:]:
        # print("\n")
        # print(element)
        # print(tree)

        if tree<element:
            tree_count = tree_count+1
        else:
            return tree_count+1
    return tree_count

def tree_counter(data):
    right_trees = []
    left_trees = []
    for row in data:
        
        line_right = []
        for cnt_element,element in enumerate(row):
            line_right.append(trees_visible(row, cnt_element, element))
        right_trees.append(line_right)

        line_left = []
        for cnt_element,element in enumerate(reversed(row)):
            line_left.append(trees_visible(list(reversed(row)), cnt_element, element))
        left_trees.append(list(reversed(line_left)))
    
    return right_trees,left_trees

right_trees,left_trees=tree_counter(data)
top_trees,bottom_trees=tree_counter(transpose(data))
top_trees = transpose(top_trees)
bottom_trees = transpose(bottom_trees)

print(right_trees)
print(left_trees)
print(top_trees)
print(bottom_trees)

mask=np.array([right_trees,left_trees,top_trees,bottom_trees]).prod(axis=0)

print(mask)

print(mask.max())
