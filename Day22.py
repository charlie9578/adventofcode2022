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

## create routing for cubes shape
# 1. expand the space
# 2. create the routing signals
# 3. create the route command
# 4. redefine end position


def print_map2(map):
    print('-'*(len(map)+2))
    for row in map:
        print(f"|{''.join(row)}|")
    print('-'*(len(map)+2))


class player2:
    def __init__(self,row,column,direction):
        self.row = row
        self.column = column
        self.direction = direction

    def step_forwards(self):
        self.direction = self.direction % 360
        
        if self.direction == 0:
            self.row = (self.row-1)
        elif self.direction == 90:
            self.column = (self.column+1)
        elif self.direction == 180:
            self.row = (self.row+1)
        elif self.direction == 270:
            self.column = (self.column-1)
        else:
            print("Error with next_loc")

    def step_backwards(self):
        self.direction = (180+self.direction) % 360
        self.step_forwards()
        self.direction = (180+self.direction) % 360


if file_name == "day/22/input_example":
    box_size = 4
    map_expanded_size = 6*box_size
    displace_rows = box_size
    displace_columns = box_size
    mark = player2(1*box_size,3*box_size,90)
else:
    box_size = 50
    map_expanded_size = 7*box_size
    displace_rows = 2*box_size
    displace_columns = 3*box_size
    mark = player2(2*box_size,4*box_size,90)


map_expanded = []
for row in range(map_expanded_size):
    map_expanded.append([" "]*map_expanded_size)

map_filled_tmp = []
for cnt,row in enumerate(map):
    columns = len(row)
    map_filled_tmp.append(list(row)+[" "]*(max_column-columns))

print_map2(map_filled_tmp)

for row in range(len(map_filled_tmp)):
    for column in range(len(map_filled_tmp[0])):
        map_expanded[row+displace_rows][column+displace_columns] = map_filled_tmp[row][column]

print_map2(map_expanded)

if file_name == "day/22/input_example":
    start_point_row = box_size-1
    start_point_column = 3*box_size
    length = box_size
    for point in range(length):
        map_expanded[start_point_row-point][start_point_column+point]="c"

    start_point_row = 3*box_size-1
    start_point_column = 4*box_size
    length = 2*box_size
    for point in range(length):
        map_expanded[start_point_row-point][start_point_column+point]="c"

    start_point_row = 3*box_size
    start_point_column = 3*box_size-1
    length = 3*box_size
    for point in range(length):
        map_expanded[start_point_row+point][start_point_column-point]="c"

    start_point_row = 2*box_size-1
    start_point_column = 3*box_size-1
    length = 2*box_size
    for point in range(length):
        map_expanded[start_point_row-point][start_point_column-point]="a"

    start_point_row = 3*box_size-1
    start_point_column = 1*box_size-1
    length = 1*box_size
    for point in range(length):
        map_expanded[start_point_row-point][start_point_column-point]="a"

    start_point_row = 3*box_size
    start_point_column = 5*box_size
    length = 1*box_size
    for point in range(length):
        map_expanded[start_point_row+point][start_point_column+point]="a"

    start_point_row = 4*box_size
    start_point_column = 3*box_size
    length = 2*box_size
    for point in range(length):
        map_expanded[start_point_row+point][start_point_column+point]="a"

else:
    start_point_row = 2*box_size-1
    start_point_column = 4*box_size
    length = 2*box_size
    for point in range(length):
        map_expanded[start_point_row-point][start_point_column+point]="c"

    start_point_row = 3*box_size
    start_point_column = 6*box_size
    length = box_size
    for point in range(length):
        map_expanded[start_point_row-point-1][start_point_column+point]="c"

    start_point_row = 3*box_size
    start_point_column = 5*box_size
    length = 2*box_size
    for point in range(length):
        map_expanded[start_point_row+point][start_point_column+point]="a"

    start_point_row = 4*box_size-1
    start_point_column = 4*box_size-1
    length = 4*box_size
    for point in range(length):
        map_expanded[start_point_row-point][start_point_column-point]="a"

    start_point_row = 4*box_size
    start_point_column = 3*box_size-1
    length = 3*box_size
    for point in range(length):
        map_expanded[start_point_row+point][start_point_column-point]="c"

    start_point_row = 5*box_size
    start_point_column = 4*box_size
    length = 1*box_size
    for point in range(length):
        map_expanded[start_point_row+point][start_point_column+point]="a"

    start_point_row = 6*box_size
    start_point_column = 3*box_size
    length = 1*box_size
    for point in range(length):
        map_expanded[start_point_row+point][start_point_column+point]="a"


print_map2(map_expanded)

map_filled = map_expanded

with open("day/22/output_map_expanded", "w") as f:
    for row in map_filled:
        for item in row:
            f.write(item)
        f.write("\n")

for command in commands:
    
    # print_map2(map_expanded)
    
    # print(f"\n Command: {command}")
    
    start_r = mark.row
    start_c = mark.column

    if command=="R":
        mark.direction = (mark.direction+90)%360

    elif command=="L":
        mark.direction = (mark.direction-90)%360

    elif command.isnumeric():
        
        movements = int(command)
        
        print(f"Movements {movements} due {mark.direction} degrees from location: {mark.row},{mark.column}")
        # print(f"Current location: {mark.row},{mark.column}")
        for move in range(movements):
            
            start_row = mark.row
            start_column = mark.column
            start_direction = mark.direction

            # step forwards
            mark.step_forwards()

            # continue to move forward if the cell is empty
            while (map_filled[mark.row][mark.column]==" ") or (map_filled[mark.row][mark.column]=="a") or (map_filled[mark.row][mark.column]=="c"):
            
                if map_filled[mark.row][mark.column]=="c":
                    if mark.direction==0:
                        mark.direction = 270
                    elif mark.direction==90:
                        mark.direction = 180
                    elif mark.direction==180:
                        mark.direction = 90
                    elif mark.direction==270:
                        mark.direction = 0
                    else:
                        "Error with mark's direction"

                if map_filled[mark.row][mark.column]=="a":
                    if mark.direction==0:
                        mark.direction = 90
                    elif mark.direction==90:
                        mark.direction = 0
                    elif mark.direction==180:
                        mark.direction = 270
                    elif mark.direction==270:
                        mark.direction = 180
                    else:
                        "Error with mark's direction"

                mark.step_forwards()

                if map_filled[mark.row][mark.column]=="#":
                    mark.row = start_row
                    mark.column = start_column
                    mark.direction = start_direction

            # step back again if a wall is hit
            if map_filled[mark.row][mark.column]=="#":
                mark.row = start_row
                mark.column = start_column
                mark.direction = start_direction

            # print(f"New location: {mark.row},{mark.column}")
            if (map_filled[mark.row][mark.column]!="c") and (map_filled[mark.row][mark.column]!="a"):
                if mark.direction == 0:
                    map_filled[mark.row][mark.column] = "^"
                elif mark.direction == 90:
                    map_filled[mark.row][mark.column] = ">"
                elif mark.direction == 180:
                    map_filled[mark.row][mark.column] = "v"
                elif mark.direction == 270:
                    map_filled[mark.row][mark.column] = "<"


    else:
        print(f"Error with command {command}")  


print_map2(map_expanded)

with open("day/22/output_map_expanded_complete", "w") as f:
    for row in map_filled:
        for item in row:
            f.write(item)
        f.write("\n")

password = 1000*(mark.row+1-displace_rows) + 4*(mark.column+1-displace_columns) + int(((mark.direction-90)%360)/90)
print(password)