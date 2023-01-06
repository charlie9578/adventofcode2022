"""
--- Day 15: Beacon Exclusion Zone ---

You feel the ground rumble again as the distress signal leads you to a large network of subterranean tunnels. You don't have time to search them all, but you don't need to: your pack contains a set of deployable sensors that you imagine were originally built to locate lost Elves.

The sensors aren't very powerful, but that's okay; your handheld device indicates that you're close enough to the source of the distress signal to use them. You pull the emergency sensor system out of your pack, hit the big button on top, and the sensors zoom off down the tunnels.

Once a sensor finds a spot it thinks will give it a good reading, it attaches itself to a hard surface and begins monitoring for the nearest signal source beacon. Sensors and beacons always exist at integer coordinates. Each sensor knows its own position and can determine the position of a beacon precisely; however, sensors can only lock on to the one beacon closest to the sensor as measured by the Manhattan distance. (There is never a tie where two beacons are the same distance to a sensor.)

It doesn't take long for the sensors to report back their positions and closest beacons (your puzzle input). For example:

Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3

So, consider the sensor at 2,18; the closest beacon to it is at -2,15. For the sensor at 9,16, the closest beacon to it is at 10,16.

Drawing sensors as S and beacons as B, the above arrangement of sensors and beacons looks like this:

               1    1    2    2
     0    5    0    5    0    5
 0 ....S.......................
 1 ......................S.....
 2 ...............S............
 3 ................SB..........
 4 ............................
 5 ............................
 6 ............................
 7 ..........S.......S.........
 8 ............................
 9 ............................
10 ....B.......................
11 ..S.........................
12 ............................
13 ............................
14 ..............S.......S.....
15 B...........................
16 ...........SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....

This isn't necessarily a comprehensive map of all beacons in the area, though. Because each sensor only identifies its closest beacon, if a sensor detects a beacon, you know there are no other beacons that close or closer to that sensor. There could still be beacons that just happen to not be the closest beacon to any sensor. Consider the sensor at 8,7:

               1    1    2    2
     0    5    0    5    0    5
-2 ..........#.................
-1 .........###................
 0 ....S...#####...............
 1 .......#######........S.....
 2 ......#########S............
 3 .....###########SB..........
 4 ....#############...........
 5 ...###############..........
 6 ..#################.........
 7 .#########S#######S#........
 8 ..#################.........
 9 ...###############..........
10 ....B############...........
11 ..S..###########............
12 ......#########.............
13 .......#######..............
14 ........#####.S.......S.....
15 B........###................
16 ..........#SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....

This sensor's closest beacon is at 2,10, and so you know there are no beacons that close or closer (in any positions marked #).

None of the detected beacons seem to be producing the distress signal, so you'll need to work out where the distress beacon is by working out where it isn't. For now, keep things simple by counting the positions where a beacon cannot possibly be along just a single row.

So, suppose you have an arrangement of beacons and sensors like in the example above and, just in the row where y=10, you'd like to count the number of positions a beacon cannot possibly exist. The coverage from all sensors near that row looks like this:

                 1    1    2    2
       0    5    0    5    0    5
 9 ...#########################...
10 ..####B######################..
11 .###S#############.###########.

In this example, in the row where y=10, there are 26 positions where a beacon cannot be present.

Consult the report from the sensors you just deployed. In the row where y=2000000, how many positions cannot contain a beacon?

"""


import pandas as pd

row_number = 2000000
file_name = r"day/15/input"
boundary_min = 0
boundary_max = 4000000

sensor_xx=[]
sensor_yy=[]
beacon_xx=[]
beacon_yy=[]
with open(file_name, "r") as file:

    for line in file:
        sensor = line.split("at ")[1].split(":")[0]
        sensor_x = sensor.split(",")[0].split("=")[1]
        sensor_y = sensor.split(",")[1].split("=")[1]

        beacon = line.split("at ")[-1].split(":")[0]
        beacon_x = beacon.split(",")[0].split("=")[1]
        beacon_y = beacon.split(",")[1].split("=")[1]

        sensor_xx.append(int(sensor_x))
        sensor_yy.append(int(sensor_y))
        beacon_xx.append(int(beacon_x))
        beacon_yy.append(int(beacon_y))
        
        
print(sensor_xx[-1])
print(sensor_yy[-1])
print(beacon_xx[-1])
print(beacon_yy[-1])

data_dict = {"sensor_x":sensor_xx,"sensor_y":sensor_yy,"beacon_x":beacon_xx,"beacon_y":beacon_yy}

df = pd.DataFrame(data_dict)

df["beacon_dx"]=df["beacon_x"]-df["sensor_x"]
df["beacon_dy"]=df["beacon_y"]-df["sensor_y"]

df["distance to beacon"]=abs(df["beacon_dx"])+abs(df["beacon_dy"])

min_x = df[["sensor_x","beacon_x"]].min().min()
max_x = df[["sensor_x","beacon_x"]].max().max()

df["distance to row"] = abs(row_number - df["sensor_y"])

df["row reach"] = df["distance to beacon"] - df["distance to row"]

def row_values(sensor_y,row_reach):
    if row_reach>=0:
        return list(range(sensor_y-row_reach,sensor_y+row_reach+1,1))
    else:
        return list()


df["row values"] = df.apply(lambda row : row_values(row["sensor_x"],row["row reach"]), axis = 1)

print(df)

# print(df["row values"].values)

def upack(lsts):
    output=set()
    for lst in lsts:
        output=output.union(set(lst))
    return list(output)

excluded_locs = upack(df["row values"].values)

print(set(range(0,20))-set(excluded_locs))
print(len(excluded_locs))


"""
Your puzzle answer was 4424278.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

Your handheld device indicates that the distress signal is coming from a beacon nearby. The distress beacon is not detected by any sensor, but the distress beacon must have x and y coordinates each no lower than 0 and no larger than 4000000.

To isolate the distress beacon's signal, you need to determine its tuning frequency, which can be found by multiplying its x coordinate by 4000000 and then adding its y coordinate.

In the example above, the search space is smaller: instead, the x and y coordinates can each be at most 20. With this reduced search area, there is only a single position that could have a beacon: x=14, y=11. The tuning frequency for this distress beacon is 56000011.

Find the only possible position for the distress beacon. What is its tuning frequency?
"""

import numpy as np

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Grid, LinearAxis, Patches, Plot

from bokeh.models import NumeralTickFormatter

from bokeh.palettes import Category20

from shapely.geometry import Polygon
from shapely.ops import unary_union


df["x_top"] = df["sensor_x"]+df["distance to beacon"]
df["x_bot"] = df["sensor_x"]-df["distance to beacon"]
df["y_top"] = df["sensor_y"]+df["distance to beacon"]
df["y_bot"] = df["sensor_y"]-df["distance to beacon"]

print(df)

xs = []
ys = []
polygons=[]
for i,row in df.iterrows():
    
    #print(row)
    xpts = [row["x_top"]+0.5, row["sensor_x"], row["x_bot"]-0.5, row["sensor_x"]]
    ypts = [row["sensor_y"], row["y_bot"]-0.5, row["sensor_y"], row["y_top"]+0.5]

    poly = Polygon(zip(xpts,ypts))

    xs.append(xpts)
    ys.append(ypts)
    polygons.append(poly)

boundary = Polygon(zip([boundary_min,boundary_min,boundary_max,boundary_max],
                    [boundary_min,boundary_max,boundary_max,boundary_min]))  
# print(xs)
# print(ys)
# print(polygons)

all_exclusions = unary_union(polygons)
exclusions_in_boundary = all_exclusions.intersection(boundary)
possible_locations = boundary.symmetric_difference(exclusions_in_boundary)

print(possible_locations)

TOOLTIPS = [
    ("index", "$index"),
    ("(x,y)", "($x{int}, $y{int})"),
]


source = ColumnDataSource(dict(
        xs=xs,
        ys=ys,
        color=list(Category20[20])+['#1f77b4','#1f77b4','#1f77b4']    
    )
)

source_boundary = ColumnDataSource(dict(
        xs=[[boundary_min,boundary_min,boundary_max,boundary_max]],
        ys=[[boundary_min,boundary_max,boundary_max,boundary_min]],
    )
)

print(len(list(Category20[20])+['#1f77b4','#1f77b4','#1f77b4']))

plot = figure(
    title="Beacon Exclusion Zone",
    width=900, height=900,
    min_border=0,
    tools="hover,reset,pan,wheel_zoom,box_zoom", 
    tooltips=TOOLTIPS,
    match_aspect=True,
    )

glyph1 = Patches(xs="xs", ys="ys", fill_color="#000000", line_color="#ff0000")
plot.add_glyph(source_boundary, glyph1)

glyph2 = Patches(xs="xs", ys="ys", fill_color="color", line_color = "color", fill_alpha = 0.7)
plot.add_glyph(source, glyph2)

plot.circle(x=possible_locations.centroid.x,
            y=possible_locations.centroid.y,
            fill_color="white", size=8)

plot.xaxis.formatter = NumeralTickFormatter(format='0')
plot.yaxis.formatter = NumeralTickFormatter(format='0')

show(plot)

print(possible_locations.centroid.x*4000000+possible_locations.centroid.y)