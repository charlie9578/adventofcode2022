"""
--- Day 23: Unstable Diffusion ---

You enter a large crater of gray dirt where the grove is supposed to be. All around you, plants you imagine were expected to be full of fruit are instead withered and broken. A large group of Elves has formed in the middle of the grove.

"...but this volcano has been dormant for months. Without ash, the fruit can't grow!"

You look up to see a massive, snow-capped mountain towering above you.

"It's not like there are other active volcanoes here; we've looked everywhere."

"But our scanners show active magma flows; clearly it's going somewhere."

They finally notice you at the edge of the grove, your pack almost overflowing from the random star fruit you've been collecting. Behind you, elephants and monkeys explore the grove, looking concerned. Then, the Elves recognize the ash cloud slowly spreading above your recent detour.

"Why do you--" "How is--" "Did you just--"

Before any of them can form a complete question, another Elf speaks up: "Okay, new plan. We have almost enough fruit already, and ash from the plume should spread here eventually. If we quickly plant new seedlings now, we can still make it to the extraction point. Spread out!"

The Elves each reach into their pack and pull out a tiny plant. The plants rely on important nutrients from the ash, so they can't be planted too close together.

There isn't enough time to let the Elves figure out where to plant the seedlings themselves; you quickly scan the grove (your puzzle input) and note their positions.

For example:

....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..

The scan shows Elves # and empty ground .; outside your scan, more empty ground extends a long way in every direction. The scan is oriented so that north is up; orthogonal directions are written N (north), S (south), W (west), and E (east), while diagonal directions are written NE, NW, SE, SW.

The Elves follow a time-consuming process to figure out where they should each go; you can speed up this process considerably. The process consists of some number of rounds during which Elves alternate between considering where to move and actually moving.

During the first half of each round, each Elf considers the eight positions adjacent to themself. If no other Elves are in one of those eight positions, the Elf does not do anything during this round. Otherwise, the Elf looks in each of four directions in the following order and proposes moving one step in the first valid direction:

    If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
    If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
    If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
    If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.

After each Elf has had a chance to propose a move, the second half of the round can begin. Simultaneously, each Elf moves to their proposed destination tile if they were the only Elf to propose moving to that position. If two or more Elves propose moving to the same position, none of those Elves move.

Finally, at the end of the round, the first direction the Elves considered is moved to the end of the list of directions. For example, during the second round, the Elves would try proposing a move to the south first, then west, then east, then north. On the third round, the Elves would first consider west, then east, then north, then south.

As a smaller example, consider just these five Elves:

.....
..##.
..#..
.....
..##.
.....

The northernmost two Elves and southernmost two Elves all propose moving north, while the middle Elf cannot move north and proposes moving south. The middle Elf proposes the same destination as the southwest Elf, so neither of them move, but the other three do:

..##.
.....
..#..
...#.
..#..
.....

Next, the northernmost two Elves and the southernmost Elf all propose moving south. Of the remaining middle two Elves, the west one cannot move south and proposes moving west, while the east one cannot move south or west and proposes moving east. All five Elves succeed in moving to their proposed positions:

.....
..##.
.#...
....#
.....
..#..

Finally, the southernmost two Elves choose not to move at all. Of the remaining three Elves, the west one proposes moving west, the east one proposes moving east, and the middle one proposes moving north; all three succeed in moving:

..#..
....#
#....
....#
.....
..#..

At this point, no Elves need to move, and so the process ends.

The larger example above proceeds as follows:

== Initial State ==
..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............

== End of Round 1 ==
..............
.......#......
.....#...#....
...#..#.#.....
.......#..#...
....#.#.##....
..#..#.#......
..#.#.#.##....
..............
....#..#......
..............
..............

== End of Round 2 ==
..............
.......#......
....#.....#...
...#..#.#.....
.......#...#..
...#..#.#.....
.#...#.#.#....
..............
..#.#.#.##....
....#..#......
..............
..............

== End of Round 3 ==
..............
.......#......
.....#....#...
..#..#...#....
.......#...#..
...#..#.#.....
.#..#.....#...
.......##.....
..##.#....#...
...#..........
.......#......
..............

== End of Round 4 ==
..............
.......#......
......#....#..
..#...##......
...#.....#.#..
.........#....
.#...###..#...
..#......#....
....##....#...
....#.........
.......#......
..............

== End of Round 5 ==
.......#......
..............
..#..#.....#..
.........#....
......##...#..
.#.#.####.....
...........#..
....##..#.....
..#...........
..........#...
....#..#......
..............

After a few more rounds...

== End of Round 10 ==
.......#......
...........#..
..#.#..#......
......#.......
...#.....#..#.
.#......##....
.....##.......
..#........#..
....#.#..#....
..............
....#..#..#...
..............

To make sure they're on the right track, the Elves like to check after round 10 that they're making good progress toward covering enough ground. To do this, count the number of empty ground tiles contained by the smallest rectangle that contains every Elf. (The edges of the rectangle should be aligned to the N/S/E/W directions; the Elves do not have the patience to calculate arbitrary rectangles.) In the above example, that rectangle is:

......#.....
..........#.
.#.#..#.....
.....#......
..#.....#..#
#......##...
....##......
.#........#.
...#.#..#...
............
...#..#..#..

In this region, the number of empty ground tiles is 110.

Simulate the Elves' process and find the smallest rectangle that contains the Elves after 10 rounds. How many empty ground tiles does that rectangle contain?

To begin, get your puzzle input.
"""

import numpy as np

# Read in the map
file_name = r"day/23/input"
elf_map=[]
with open(file_name, "r") as file:

    for line in file:
        elf_map.append(list(line.strip("\n")))

def print_map(map):
    print('-'*(len(map)+2))
    for row in map:
        print(f"|{''.join(row)}|")
    print('-'*(len(map)+2))

print_map(elf_map)


elf_cnt = 0
for row in range(len(elf_map)):
    for column in range(len(elf_map[0])):
        if elf_map[row][column]=="#":
            elf_cnt = elf_cnt+1
            elf_map[row][column] = elf_cnt
        else:
            elf_map[row][column] = 0

elf_array = np.array(elf_map)

elf_array = np.insert(elf_array, [0,elf_array.shape[0]], values=0, axis=0)
elf_array = np.insert(elf_array, [0,elf_array.shape[1]], values=0, axis=1)

print(elf_array)


class elf_class:
    def __init__(self,name,row,column):
        self.name = name
        self.row = row
        self.column = column
        self.directions = ["N","S","W","E"]
        self.direction = "N"
        self.row_proposed = row
        self.column_proposed = column

    def new_location(self,surroundings):
        self.row_proposed = self.row
        self.column_proposed = self.column
        
        if (surroundings.sum()-self.name)==0:
            self.direction = "0"
        else:
            for direction in self.directions:
                if direction == "N":
                    north_neighbours = surroundings[0,:]
                    # print(f"Direction {direction} and check values {north_neighbours}")
                    if north_neighbours.sum()==0:
                        self.row_proposed = self.row-1
                        self.column_proposed = self.column
                        break
                    else:
                        self.direction = "0"
                elif direction == "S":
                    south_neighbours = surroundings[2,:]
                    # print(f"Direction {direction} and check values {south_neighbours}")
                    if south_neighbours.sum()==0:
                        self.row_proposed = self.row+1
                        self.column_proposed = self.column
                        break
                    else:
                        self.direction = "0"
                elif direction == "W":
                    west_neighbours = surroundings[:,0]
                    # print(f"Direction {direction} and check values {west_neighbours}")
                    if west_neighbours.sum()==0:
                        self.row_proposed = self.row
                        self.column_proposed = self.column-1
                        break
                    else:
                        self.direction = "0"
                elif direction == "E":
                    east_neighbours = surroundings[:,2]
                    # print(f"Direction {direction} and check values {east_neighbours}")
                    if east_neighbours.sum()==0:
                        self.row_proposed = self.row
                        self.column_proposed = self.column+1
                        break
                    else:
                        self.direction = "0"
                else:
                    print("Error with directions")
            self.direction = direction
        
        # print(f"Moved from ({self.row},{self.column}) {self.direction} to ({self.row_proposed},{self.column_proposed})")
        
        # self.directions = self.directions[1:] + [self.directions[0]]

    def blocked(self):
        # print(f"Elf blocked from ({self.row},{self.column}) {self.direction} moving to ({self.row_proposed},{self.column_proposed})")
        self.row_proposed = self.row
        self.column_proposed = self.column
        
        

# create a list of all the elves
elves = []
for elf in range(1,elf_array.max()+1):
    row, column = np.where(elf_array == elf)
    column = column[0]
    row = row[0]
    elves.append(elf_class(elf,row,column))


def propose_moves(elf_array,elves):
    # find the proposed moves
    elf_array_proposed = np.zeros(elf_array.shape,dtype=int)
    for elf in elves:
        # print(f"Elf: {elf.name}, located at row {elf.row} and column {elf.column} with directions {elf.directions}")
        
        elf_surroundings = elf_array[elf.row-1:elf.row+2,elf.column-1:elf.column+2]

        elf.new_location(elf_surroundings)

        elf_array_proposed[elf.row_proposed,elf.column_proposed]=elf_array_proposed[elf.row_proposed,elf.column_proposed]+1

    # print(elf_array_proposed)
    return elf_array_proposed


def make_moves(elf_array_proposed,elves):
    elf_array = np.zeros(elf_array_proposed.shape,dtype=int)
    for elf in elves:
        # check if any blockers otherwise move them
        if elf_array_proposed[elf.row_proposed,elf.column_proposed]>1:
            elf.blocked()

        # move elves
        # print(f"Elf: {elf.name}, located at ({elf.row}, {elf.column}) moved {elf.direction} to ({elf.row_proposed},{elf.column_proposed}) with directions {elf.directions}")
        elf.column = elf.column_proposed
        elf.row = elf.row_proposed

        elf_array[elf.row,elf.column] = elf.name

        # shift the directions along
        elf.directions = elf.directions[1:] + [elf.directions[0]]

    
    # if elves are at the edges, expand them
    if elf_array[0,:].sum()>0:
        elf_array = np.insert(elf_array, 0, values=0, axis=0)
        for elf in elves:
            elf.row = elf.row+1

    if elf_array[elf_array.shape[0]-1,:].sum()>0:
        elf_array = np.insert(elf_array, elf_array.shape[0], values=0, axis=0)

    if elf_array[:,0].sum()>0:
        elf_array = np.insert(elf_array, 0, values=0, axis=1)
        for elf in elves:
            elf.column = elf.column+1

    if elf_array[:,elf_array.shape[1]-1].sum()>0:
        elf_array = np.insert(elf_array, elf_array.shape[1], values=0, axis=1)



    print(elf_array)
    return elf_array


# select if for part one or two of the challenge
part = 2 #1 or 2

if part==1:
    rounds = 10
else:
    rounds = 50000


for round in range(rounds):
    print(round+1)

    old_elf_array = elf_array.copy()
    elf_array_proposed = propose_moves(elf_array,elves)
    elf_array = make_moves(elf_array_proposed,elves)

    if np.array_equal(old_elf_array,elf_array):
        print(f"Part 2 answer: {round+1}")
        break    
    

print(f"Part 1 answer: {(elf_array.shape[0]-2)*(elf_array.shape[1]-2)-len(elves)}")


"""
Your puzzle answer was 3871.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

It seems you're on the right track. Finish simulating the process and figure out where the Elves need to go. How many rounds did you save them?

In the example above, the first round where no Elf moved was round 20:

.......#......
....#......#..
..#.....#.....
......#.......
...#....#.#..#
#.............
....#.....#...
..#.....#.....
....#.#....#..
.........#....
....#......#..
.......#......

Figure out where the Elves need to go. What is the number of the first round where no Elf moves?
"""