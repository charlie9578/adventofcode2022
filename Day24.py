"""
--- Day 24: Blizzard Basin ---

With everything replanted for next year (and with elephants and monkeys to tend the grove), you and the Elves leave for the extraction point.

Partway up the mountain that shields the grove is a flat, open area that serves as the extraction point. It's a bit of a climb, but nothing the expedition can't handle.

At least, that would normally be true; now that the mountain is covered in snow, things have become more difficult than the Elves are used to.

As the expedition reaches a valley that must be traversed to reach the extraction site, you find that strong, turbulent winds are pushing small blizzards of snow and sharp ice around the valley. It's a good thing everyone packed warm clothes! To make it across safely, you'll need to find a way to avoid them.

Fortunately, it's easy to see all of this from the entrance to the valley, so you make a map of the valley and the blizzards (your puzzle input). For example:

#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#

The walls of the valley are drawn as #; everything else is ground. Clear ground - where there is currently no blizzard - is drawn as .. Otherwise, blizzards are drawn with an arrow indicating their direction of motion: up (^), down (v), left (<), or right (>).

The above map includes two blizzards, one moving right (>) and one moving down (v). In one minute, each blizzard moves one position in the direction it is pointing:

#.#####
#.....#
#.>...#
#.....#
#.....#
#...v.#
#####.#

Due to conservation of blizzard energy, as a blizzard reaches the wall of the valley, a new blizzard forms on the opposite side of the valley moving in the same direction. After another minute, the bottom downward-moving blizzard has been replaced with a new downward-moving blizzard at the top of the valley instead:

#.#####
#...v.#
#..>..#
#.....#
#.....#
#.....#
#####.#

Because blizzards are made of tiny snowflakes, they pass right through each other. After another minute, both blizzards temporarily occupy the same position, marked 2:

#.#####
#.....#
#...2.#
#.....#
#.....#
#.....#
#####.#

After another minute, the situation resolves itself, giving each blizzard back its personal space:

#.#####
#.....#
#....>#
#...v.#
#.....#
#.....#
#####.#

Finally, after yet another minute, the rightward-facing blizzard on the right is replaced with a new one on the left facing the same direction:

#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#

This process repeats at least as long as you are observing it, but probably forever.

Here is a more complex example:

#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#

Your expedition begins in the only non-wall position in the top row and needs to reach the only non-wall position in the bottom row. On each minute, you can move up, down, left, or right, or you can wait in place. You and the blizzards act simultaneously, and you cannot share a position with a blizzard.

In the above example, the fastest way to reach your goal requires 18 steps. Drawing the position of the expedition as E, one way to achieve this is:

Initial state:
#E######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#

Minute 1, move down:
#.######
#E>3.<.#
#<..<<.#
#>2.22.#
#>v..^<#
######.#

Minute 2, move down:
#.######
#.2>2..#
#E^22^<#
#.>2.^>#
#.>..<.#
######.#

Minute 3, wait:
#.######
#<^<22.#
#E2<.2.#
#><2>..#
#..><..#
######.#

Minute 4, move up:
#.######
#E<..22#
#<<.<..#
#<2.>>.#
#.^22^.#
######.#

Minute 5, move right:
#.######
#2Ev.<>#
#<.<..<#
#.^>^22#
#.2..2.#
######.#

Minute 6, move right:
#.######
#>2E<.<#
#.2v^2<#
#>..>2>#
#<....>#
######.#

Minute 7, move down:
#.######
#.22^2.#
#<vE<2.#
#>>v<>.#
#>....<#
######.#

Minute 8, move left:
#.######
#.<>2^.#
#.E<<.<#
#.22..>#
#.2v^2.#
######.#

Minute 9, move up:
#.######
#<E2>>.#
#.<<.<.#
#>2>2^.#
#.v><^.#
######.#

Minute 10, move right:
#.######
#.2E.>2#
#<2v2^.#
#<>.>2.#
#..<>..#
######.#

Minute 11, wait:
#.######
#2^E^2>#
#<v<.^<#
#..2.>2#
#.<..>.#
######.#

Minute 12, move down:
#.######
#>>.<^<#
#.<E.<<#
#>v.><>#
#<^v^^>#
######.#

Minute 13, move down:
#.######
#.>3.<.#
#<..<<.#
#>2E22.#
#>v..^<#
######.#

Minute 14, move right:
#.######
#.2>2..#
#.^22^<#
#.>2E^>#
#.>..<.#
######.#

Minute 15, move right:
#.######
#<^<22.#
#.2<.2.#
#><2>E.#
#..><..#
######.#

Minute 16, move right:
#.######
#.<..22#
#<<.<..#
#<2.>>E#
#.^22^.#
######.#

Minute 17, move down:
#.######
#2.v.<>#
#<.<..<#
#.^>^22#
#.2..2E#
######.#

Minute 18, move down:
#.######
#>2.<.<#
#.2v^2<#
#>..>2>#
#<....>#
######E#

What is the fewest number of minutes required to avoid the blizzards and reach the goal?

"""

import numpy as np

# Read in the map
file_name = r"day/24/input"
blizzard_map=[]
with open(file_name, "r") as file:
    for line in file:
        blizzard_map.append(list(line.strip()))

def print_map(map):
    for row in map:
        print(f"{''.join(row)}")

print_map(blizzard_map)

blizzard_array = np.zeros(shape=[len(blizzard_map)-2,len(blizzard_map[0])-2],dtype=int)

print(blizzard_array)

for row in range(blizzard_array.shape[0]):
    for column in range(blizzard_array.shape[1]):
        value = blizzard_map[row+1][column+1]
        if value==">":
            blizzard_array[row,column] = 1
        elif value=="<":
            blizzard_array[row,column] = 2
        elif value=="v":
            blizzard_array[row,column] = 4
        elif value=="^":
            blizzard_array[row,column] = 8

print(blizzard_array)

def is_set(x, n):
    # bitwise checking
    return x & 1 << n != 0

def update_blizzard(blizzard_array):
    new_blizzard_array = np.zeros(blizzard_array.shape,dtype=int)

    rows = blizzard_array.shape[0]
    columns = blizzard_array.shape[1]

    for row in range(rows):
        for column in range(columns):
            value = 0
            if is_set(blizzard_array[row][(column-1)%columns],0):
                value = value+1
            if is_set(blizzard_array[row][(column+1)%columns],1):
                value = value+2
            if is_set(blizzard_array[(row-1)%rows][column],2):
                value = value+4
            if is_set(blizzard_array[(row+1)%rows][column],3):
                value = value+8
            
            new_blizzard_array[row][column] = value

    return new_blizzard_array


def get_me_out(blizzard_array,start_x=0,start_y=0,end_x=-1,end_y=-1):
    blizzard_visited = np.zeros(blizzard_array.shape,dtype=bool)
    for a in range(5000):
        blizzard_array = update_blizzard(blizzard_array)

        if blizzard_array[start_x,start_y]==0:
            blizzard_visited[start_x,start_y]=True
        
        blizzard_visited_new = blizzard_visited.copy()
        blizzard_visited_new[1:,:] = blizzard_visited_new[1:,:] + blizzard_visited[:-1,:]
        blizzard_visited_new[:-1,:] = blizzard_visited_new[:-1,:] + blizzard_visited[1:,:]
        blizzard_visited_new[:,1:] = blizzard_visited_new[:,1:] + blizzard_visited[:,:-1]
        blizzard_visited_new[:,:-1] = blizzard_visited_new[:,:-1] + blizzard_visited[:,1:]

        blizzard_visited = ((blizzard_array==0) & (blizzard_visited_new==True))
        
        # print(f"Minute: {a+1}")
        # print(blizzard_visited)

        if blizzard_visited[end_x,end_y]==True:
            blizzard_array = update_blizzard(blizzard_array)
            print(f"Escaped after {a+2} minutes")
            break

    return a+2,blizzard_array

print(blizzard_array)

"""
What is the fewest number of minutes required to avoid the blizzards and reach the goal?

Your puzzle answer was 334.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

As the expedition reaches the far side of the valley, one of the Elves looks especially dismayed:

He forgot his snacks at the entrance to the valley!

Since you're so good at dodging blizzards, the Elves humbly request that you go back for his snacks. From the same initial conditions, how quickly can you make it from the start to the goal, then back to the start, then back to the goal?

In the above example, the first trip to the goal takes 18 minutes, the trip back to the start takes 23 minutes, and the trip back to the goal again takes 13 minutes, for a total time of 54 minutes.

What is the fewest number of minutes required to reach the goal, go back to the start, then reach the goal again?

"""
    
time_taken1,blizzard_array = get_me_out(blizzard_array,start_x=0,start_y=0,end_x=-1,end_y=-1)
# print(f"Time taken 1: {time_taken1} minutes")
# print(blizzard_array)

time_taken2,blizzard_array = get_me_out(blizzard_array,start_x=-1,start_y=-1,end_x=0,end_y=0)
# print(f"Time taken 2: {time_taken2} minutes")
# print(blizzard_array)

time_taken3,blizzard_array = get_me_out(blizzard_array,start_x=0,start_y=0,end_x=-1,end_y=-1)
# print(f"Time taken 3: {time_taken3} minutes")
# print(blizzard_array)

print(f"Total time taken: {time_taken1+time_taken2+time_taken3}")