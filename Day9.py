"""
--- Day 9: Rope Bridge ---

This rope bridge creaks as you walk along it. You aren't sure how old it is, or whether it can even support your weight.

It seems to support the Elves just fine, though. The bridge spans a gorge which was carved out by the massive river far below you.

You step carefully; as you do, the ropes stretch and twist. You decide to distract yourself by modeling rope physics; maybe you can even figure out where not to step.

Consider a rope with a knot at each end; these knots mark the head and the tail of the rope. If the head moves far enough away from the tail, the tail is pulled toward the head.

Due to nebulous reasoning involving Planck lengths, you should be able to model the positions of the knots on a two-dimensional grid. Then, by following a hypothetical series of motions (your puzzle input) for the head, you can determine how the tail will move.

Due to the aforementioned Planck lengths, the rope must be quite short; in fact, the head (H) and tail (T) must always be touching (diagonally adjacent and even overlapping both count as touching):

....
.TH.
....

....
.H..
..T.
....

...
.H. (H covers T)
...

If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:

.....    .....    .....
.TH.. -> .T.H. -> ..TH.
.....    .....    .....

...    ...    ...
.T.    .T.    ...
.H. -> ... -> .T.
...    .H.    .H.
...    ...    ...

Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:

.....    .....    .....
.....    ..H..    ..H..
..H.. -> ..... -> ..T..
.T...    .T...    .....
.....    .....    .....

.....    .....    .....
.....    .....    .....
..H.. -> ...H. -> ..TH.
.T...    .T...    .....
.....    .....    .....

You just need to work out where the tail goes as the head follows a series of motions. Assume the head and the tail both start at the same position, overlapping.

For example:

R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2

This series of motions moves the head right four steps, then up four steps, then left three steps, then down one step, and so on. After each step, you'll need to update the position of the tail if the step means the head is no longer adjacent to the tail. Visually, these motions occur as follows (s marks the starting position as a reference point):

== Initial State ==

......
......
......
......
H.....  (H covers T, s)

== R 4 ==

......
......
......
......
TH....  (T covers s)

......
......
......
......
sTH...

......
......
......
......
s.TH..

......
......
......
......
s..TH.

== U 4 ==

......
......
......
....H.
s..T..

......
......
....H.
....T.
s.....

......
....H.
....T.
......
s.....

....H.
....T.
......
......
s.....

== L 3 ==

...H..
....T.
......
......
s.....

..HT..
......
......
......
s.....

.HT...
......
......
......
s.....

== D 1 ==

..T...
.H....
......
......
s.....

== R 4 ==

..T...
..H...
......
......
s.....

..T...
...H..
......
......
s.....

......
...TH.
......
......
s.....

......
....TH
......
......
s.....

== D 1 ==

......
....T.
.....H
......
s.....

== L 5 ==

......
....T.
....H.
......
s.....

......
....T.
...H..
......
s.....

......
......
..HT..
......
s.....

......
......
.HT...
......
s.....

......
......
HT....
......
s.....

== R 2 ==

......
......
.H....  (H covers T)
......
s.....

......
......
.TH...
......
s.....

After simulating the rope, you can count up all of the positions the tail visited at least once. In this diagram, s again marks the starting position (which the tail also visited) and # marks other positions the tail visited:

..##..
...##.
.####.
....#.
s###..

So, there are 13 positions the tail visited at least once.

Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?
"""

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Grid, LinearAxis, Patches, Plot


directions = []
movements = []
with open(r"day/9/input", "r") as file:

    for line in file:
        line = line.strip()
        # print(line)
        directions.append(line.split(" ")[0])
        movements.append(int(line.split(" ")[1]))

# print(direction)
# print(movement)

locations_x = []
locations_y = []
location_x = 0
location_y = 0
delta_x = 0
delta_y = 0
for direction,moves in zip(directions,movements):
    print(direction)
    print(moves)


    for move in range(moves):
        if direction == "U":
            delta_y = delta_y+1
        elif direction == "D":
            delta_y = delta_y-1
        elif direction == "R":
            delta_x = delta_x+1
        elif direction == "L":
            delta_x = delta_x-1
        else:
            print("No direction defined")

        # print(str(delta_x)+" "+str(delta_y))
        
        if (abs(delta_x)+abs(delta_y))>2:
            if delta_x>0:
                location_x = location_x+1
                delta_x = delta_x-1
            elif delta_x<0:
                location_x = location_x-1
                delta_x = delta_x+1
            if delta_y>0:
                location_y = location_y+1
                delta_y = delta_y-1
            elif delta_y<0:
                location_y = location_y-1
                delta_y = delta_y+1

        if delta_x>1:
            location_x = location_x+1
            delta_x = delta_x-1
        elif delta_x<-1:
            location_x = location_x-1
            delta_x = delta_x+1

        if delta_y>1:
            location_y = location_y+1
            delta_y = delta_y-1
        elif delta_y<-1:
            location_y = location_y-1
            delta_y = delta_y+1

        print(str(location_x)+" "+str(location_y))
        locations_x.append(location_x)
        locations_y.append(location_y)

print(locations_x)
print(locations_y)

locations = set(zip(locations_x,locations_y))

print(len(locations))

plot = figure(
    title="Tails",
    width=900, height=900,
    min_border=0,
    tools="hover,reset,pan,wheel_zoom,box_zoom", 
    tooltips="",
    match_aspect=True,
    )

plot.circle(x=locations_x,
            y=locations_y,
            fill_color="red", size=8)

show(plot)            



"""
"""


location_x = 0
location_y = 0
delta_x = 0
delta_y = 0

def delta_move(delta_x,delta_y,location_x,location_y):

            if (abs(delta_x)+abs(delta_y))>2:
                if delta_x>0:
                    location_x = location_x+1
                    delta_x = delta_x-1
                elif delta_x<0:
                    location_x = location_x-1
                    delta_x = delta_x+1
                if delta_y>0:
                    location_y = location_y+1
                    delta_y = delta_y-1
                elif delta_y<0:
                    location_y = location_y-1
                    delta_y = delta_y+1

            if delta_x>1:
                location_x = location_x+1
                delta_x = delta_x-1
            elif delta_x<-1:
                location_x = location_x-1
                delta_x = delta_x+1

            if delta_y>1:
                location_y = location_y+1
                delta_y = delta_y-1
            elif delta_y<-1:
                location_y = location_y-1
                delta_y = delta_y+1

            return location_x,location_y

def chain_move(head_locations_x,head_locations_y):

    tail_locations_x = []
    tail_locations_y = []
    
    tail_location_x = head_locations_x[0]
    tail_location_y = head_locations_y[0]

    for head_location in zip(head_locations_x,head_locations_y):
        
        delta_x = head_location[0]-tail_location_x
        delta_y = head_location[1]-tail_location_y
        
        tail_location_x,tail_location_y = delta_move(delta_x,delta_y,tail_location_x,tail_location_y)
        
        tail_locations_x.append(tail_location_x)
        tail_locations_y.append(tail_location_y)

    return tail_locations_x,tail_locations_y

for chain in range(8):
    locations_x,locations_y = chain_move(locations_x,locations_y)


plot = figure(
    title="Tails",
    width=900, height=900,
    min_border=0,
    tools="hover,reset,pan,wheel_zoom,box_zoom", 
    tooltips="",
    match_aspect=True,
    )

plot.circle(x=locations_x,
            y=locations_y,
            fill_color="red", size=8)

show(plot)                


locations = set(zip(locations_x,locations_y))

print(len(locations))