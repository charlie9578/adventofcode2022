"""
--- Day 12: Hill Climbing Algorithm ---

You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^

In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the location that should get the best signal?
"""

import numpy as np

max_steps = 500
data = []
with open(r"day/12/input", "r") as file:

    for line in file:
        row = []
        line = line.strip()
        for letter in line:
            if letter == "S":
                row.append(0)
            elif letter == "E":
                row.append(27)
            else:
                row.append(ord(letter)-96)
        data.append(row)

data = np.array(data)


def check_neighbours(start,steps,data):
    # print("check neighbours")
    neighbours=[(start[0]+1,start[1]),(start[0]-1,start[1]),(start[0],start[1]+1),(start[0],start[1]-1)]
    
    for neighbour in neighbours:
        
        if not(neighbour[0] < 0 or neighbour[1] < 0 or neighbour[0] >= data.shape[0] or neighbour[1] >= data.shape[1]):
            
            if data[neighbour]-data[start]<=1:
                # print(neighbour)
                if steps[neighbour]==-1 or steps[neighbour]>steps[start]+1:
                    
                    steps[neighbour]=steps[start]+1

    return steps

def create_path(steps,data):
    for value in range(max_steps):
        starts = np.argwhere(steps == value)
        # print(starts)
        for start in starts:
            start = tuple(start)
            steps = check_neighbours(start,steps,data)

    return steps


def path_length(start_coord,end_coord,data):
    
    steps = np.ones(data.shape)*max_steps

    steps[start_coord]=0

    steps=create_path(steps,data)

    return steps[end_coord]


start_coord=tuple(np.argwhere(data == 0)[0])
end_coord=tuple(np.argwhere(data == 27)[0])

print(path_length(start_coord,end_coord,data))

potential_starts = np.argwhere(data == 1)
print(potential_starts)

lengths=[]
for potential_start in potential_starts:

    lengths.append(path_length(tuple(potential_start),end_coord,data))

print(np.array(lengths).min())