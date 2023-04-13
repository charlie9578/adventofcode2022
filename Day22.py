"""
--- Day 22: Monkey Map ---

The monkeys take you on a surprisingly easy trail through the jungle. They're even going in roughly the right direction according to your handheld device's Grove Positioning System.

As you walk, the monkeys explain that the grove is protected by a force field. To pass through the force field, you have to enter a password; doing so involves tracing a specific path on a strangely-shaped board.

At least, you're pretty sure that's what you have to do; the elephants aren't exactly fluent in monkey.

The monkeys give you notes that they took when they last saw the password entered (your puzzle input).

For example:

        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5

The first half of the monkeys' notes is a map of the board. It is comprised of a set of open tiles (on which you can move, drawn .) and solid walls (tiles which you cannot enter, drawn #).

The second half is a description of the path you must follow. It consists of alternating numbers and letters:

    A number indicates the number of tiles to move in the direction you are facing. If you run into a wall, you stop moving forward and continue with the next instruction.
    A letter indicates whether to turn 90 degrees clockwise (R) or counterclockwise (L). Turning happens in-place; it does not change your current tile.

So, a path like 10R5 means "go forward 10 tiles, then turn clockwise 90 degrees, then go forward 5 tiles".

You begin the path in the leftmost open tile of the top row of tiles. Initially, you are facing to the right (from the perspective of how the map is drawn).

If a movement instruction would take you off of the map, you wrap around to the other side of the board. In other words, if your next tile is off of the board, you should instead look in the direction opposite of your current facing as far as you can until you find the opposite edge of the board, then reappear there.

For example, if you are at A and facing to the right, the tile in front of you is marked B; if you are at C and facing down, the tile in front of you is marked D:

        ...#
        .#..
        #...
        ....
...#.D.....#
........#...
B.#....#...A
.....C....#.
        ...#....
        .....#..
        .#......
        ......#.

It is possible for the next tile (after wrapping around) to be a wall; this still counts as there being a wall in front of you, and so movement stops before you actually wrap to the other side of the board.

By drawing the last facing you had with an arrow on each tile you visit, the full path taken by the above example looks like this:

        >>v#    
        .#v.    
        #.v.    
        ..v.    
...#...v..v#    
>>>v...>#.>>    
..#v...#....    
...>>>>v..#.    
        ...#....
        .....#..
        .#......
        ......#.

To finish providing the password to this strange input device, you need to determine numbers for your final row, column, and facing as your final position appears from the perspective of the original map. Rows start from 1 at the top and count downward; columns start from 1 at the left and count rightward. (In the above example, row 1, column 1 refers to the empty space with no tile on it in the top-left corner.) Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^). The final password is the sum of 1000 times the row, 4 times the column, and the facing.

In the above example, the final row is 6, the final column is 8, and the final facing is 0. So, the final password is 1000 * 6 + 4 * 8 + 0: 6032.

Follow the path given in the monkeys' notes. What is the final password?
"""

import re
import numpy as np

# Read in the blueprints
file_name = r"day/22/input"
rows=[]
with open(file_name, "r") as file:

    for line in file:
        rows.append(line.strip("\n"))

def print_map(map):
    for row in map:
        print(row)

print(rows)

map = rows[:-2]
commands = rows[-1]
commands = re.split("(R|L)",str(commands))

print_map(map)
print(commands)

class player:
    def __init__(self,row,column,direction,max_row,max_column):
        self.row = row
        self.column = column
        self.direction = direction
        self.max_row = max_row
        self.max_column = max_column

    def step_forwards(self):
        self.direction = self.direction % 360
        
        if self.direction == 0:
            self.row = (self.row-1)%self.max_row
        elif self.direction == 90:
            self.column = (self.column+1)%self.max_column
        elif self.direction == 180:
            self.row = (self.row+1)%self.max_row
        elif self.direction == 270:
            self.column = (self.column-1)%self.max_column
        else:
            print("Error with next_loc")

    def step_backwards(self):
        self.direction = (180+self.direction) % 360
        self.step_forwards()
        self.direction = (180+self.direction) % 360

max_column = 0
for row in map:
    if max_column<len(row):
        max_column = len(row)

map_filled = []
for cnt,row in enumerate(map):
    columns = len(row)
    map_filled.append(list(row)+[" "]*(max_column-columns))

with open("day/22/output", "w") as f:
    for row in map_filled:
        for item in row:
            f.write(item)
        f.write("\n")

print(map_filled)

print(len(map_filled),len(map_filled[0]))

charlie = player(0,map_filled[0].index("."),90,len(map_filled),len(map_filled[0]))

print(charlie.max_row)
print(charlie.max_column)

print(map_filled[charlie.row][charlie.column])

print(charlie.row,charlie.column)


for command in commands:
    
    # print(f"\n Command: {command}")
    start_r = charlie.row
    start_c = charlie.column

    if command=="R":
        charlie.direction = (charlie.direction+90)%360

    elif command=="L":
        charlie.direction = (charlie.direction-90)%360

    elif command.isnumeric():
        
        movements = int(command)
        
        print(f"Movements {movements} due {charlie.direction} degrees from location: {charlie.row},{charlie.column}")
        # print(f"Current location: {charlie.row},{charlie.column}")
        for move in range(movements):
            
            start_row = charlie.row
            start_column = charlie.column
            
            # step forwards
            charlie.step_forwards()

            # step back again if a wall is hit
            if map_filled[charlie.row][charlie.column]=="#":
                charlie.row = start_row
                charlie.column = start_column

            # continue to move forward if the cell is empty
            while map_filled[charlie.row][charlie.column]==" ":
                charlie.step_forwards()
                if map_filled[charlie.row][charlie.column]=="#":
                    charlie.row = start_row
                    charlie.column = start_column
            
            # print(f"New location: {charlie.row},{charlie.column}")
            if charlie.direction == 0:
                map_filled[charlie.row][charlie.column] = "^"
            elif charlie.direction == 90:
                map_filled[charlie.row][charlie.column] = ">"
            elif charlie.direction == 180:
                map_filled[charlie.row][charlie.column] = "v"
            elif charlie.direction == 270:
                map_filled[charlie.row][charlie.column] = "<"


    else:
        print(f"Error with command {command}")  



password = 1000*(charlie.row+1) + 4*(charlie.column+1) + int(((charlie.direction-90)%360)/90)
print(password)

with open("day/22/output2", "w") as f:
    for row in map_filled:
        for item in row:
            f.write(item)
        f.write("\n")


"""
Your puzzle answer was 60362.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

As you reach the force field, you think you hear some Elves in the distance. Perhaps they've already arrived?

You approach the strange input device, but it isn't quite what the monkeys drew in their notes. Instead, you are met with a large cube; each of its six faces is a square of 50x50 tiles.

To be fair, the monkeys' map does have six 50x50 regions on it. If you were to carefully fold the map, you should be able to shape it into a cube!

In the example above, the six (smaller, 4x4) faces of the cube are:

        1111
        1111
        1111
        1111
222233334444
222233334444
222233334444
222233334444
        55556666
        55556666
        55556666
        55556666

You still start in the same position and with the same facing as before, but the wrapping rules are different. Now, if you would walk off the board, you instead proceed around the cube. From the perspective of the map, this can look a little strange. In the above example, if you are at A and move to the right, you would arrive at B facing down; if you are at C and move down, you would arrive at D facing up:

        ...#
        .#..
        #...
        ....
...#.......#
........#..A
..#....#....
.D........#.
        ...#..B.
        .....#..
        .#......
        ..C...#.

Walls still block your path, even if they are on a different face of the cube. If you are at E facing up, your movement is blocked by the wall marked by the arrow:

        ...#
        .#..
     -->#...
        ....
...#..E....#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

Using the same method of drawing the last facing you had with an arrow on each tile you visit, the full path taken by the above example now looks like this:

        >>v#    
        .#v.    
        #.v.    
        ..v.    
...#..^...v#    
.>>>>>^.#.>>    
.^#....#....    
.^........#.    
        ...#..v.
        .....#v.
        .#v<<<<.
        ..v...#.

The final password is still calculated from your final position and facing from the perspective of the map. In this example, the final row is 5, the final column is 7, and the final facing is 3, so the final password is 1000 * 5 + 4 * 7 + 3 = 5031.

Fold the map into a cube, then follow the path given in the monkeys' notes. What is the final password?
"""