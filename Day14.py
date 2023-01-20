"""
--- Day 14: Regolith Reservoir ---

The distress signal leads you to a giant waterfall! Actually, hang on - the signal seems like it's coming from the waterfall itself, and that doesn't make any sense. However, you do notice a little path that leads behind the waterfall.

Correction: the distress signal leads you behind a giant waterfall! There seems to be a large cave system here, and the signal definitely leads further inside.

As you begin to make your way deeper underground, you feel the ground rumble for a moment. Sand begins pouring into the cave! If you don't quickly figure out where the sand is going, you could quickly become trapped!

Fortunately, your familiarity with analyzing the path of falling material will come in handy here. You scan a two-dimensional vertical slice of the cave above you (your puzzle input) and discover that it is mostly air with structures made of rock.

Your scan traces the path of each solid rock structure and reports the x,y coordinates that form the shape of the path, where x represents distance to the right and y represents distance down. Each path appears as a single line of text in your scan. After the first point of each path, each point indicates the end of a straight horizontal or vertical line to be drawn from the previous point. For example:

498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9

This scan means that there are two paths of rock; the first path consists of two straight lines, and the second path consists of three straight lines. (Specifically, the first path consists of a line of rock from 498,4 through 498,6 and another line of rock from 498,6 through 496,6.)

The sand is pouring into the cave from point 500,0.

Drawing rock as #, air as ., and the source of the sand as +, this becomes:


  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.

Sand is produced one unit at a time, and the next unit of sand is not produced until the previous unit of sand comes to rest. A unit of sand is large enough to fill one tile of air in your scan.

A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left. If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right. Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves, at which point the next unit of sand is created back at the source.

So, drawing sand that has come to rest as o, the first unit of sand simply falls straight down and then stops:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
......o.#.
#########.

The second unit of sand then falls straight down, lands on the first one, and then comes to rest to its left:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
.....oo.#.
#########.

After a total of five units of sand have come to rest, they form this pattern:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
......o.#.
....oooo#.
#########.

After a total of 22 units of sand:

......+...
..........
......o...
.....ooo..
....#ooo##
....#ooo#.
..###ooo#.
....oooo#.
...ooooo#.
#########.

Finally, only two more units of sand can possibly come to rest:

......+...
..........
......o...
.....ooo..
....#ooo##
...o#ooo#.
..###ooo#.
....oooo#.
.o.ooooo#.
#########.

Once all 24 units of sand shown above have come to rest, all further sand flows out the bottom, falling into the endless void. Just for fun, the path any new sand takes before falling forever is shown here with ~:

.......+...
.......~...
......~o...
.....~ooo..
....~#ooo##
...~o#ooo#.
..~###ooo#.
..~..oooo#.
.~o.ooooo#.
~#########.
~..........
~..........
~..........

Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the abyss below?
"""

import numpy as np

def read_file():
  lines=[]
  min_x=500
  max_x=500
  min_y=0
  max_y=0
  with open(r"day/14/input", "r") as file:

      for line in file:
        line=line.strip()
        line=line.split("->")
        paths=[]

        for path in line:
          path=path.split(",")
          steps=[]

          for step in path:
            step=int(step)
            steps.append(step)

          if steps[0]>max_x:
            max_x=steps[0]
          if steps[1]>max_y:
            max_y=steps[1]
          if steps[0]<min_x:
            min_x=steps[0]
          if steps[1]<min_y:
            min_y=steps[1]
          
          paths.append(steps)
        
        lines.append(paths)

  return lines,min_x,min_y,max_x,max_y



def create_cave(lines,min_x,min_y,max_x,max_y):
  
  cave = np.zeros((max_y-min_y+1,max_x-min_x+1))

  for path in lines:
    # print(path)
    step_old=None
    for step in path:
      step[0]=step[0]-min_x
      step[1]=step[1]-min_y
      
      if not(step_old==None):
        
        # print("step")
        # print(step)
        # print(step_old)

        if step[0]==step_old[0]:
          # print("step1 used")
          if step[1]<step_old[1]:
            # print("here")
            cave[step[1]:step_old[1]+1,step[0]:step[0]+1]=1
          else:
            cave[step_old[1]:step[1]+1,step[0]:step[0]+1]=1
        else:
          # print("step0 used")
          if step[0]<step_old[0]:
            # print("here")
            cave[step[1]:step[1]+1,step[0]:step_old[0]+1]=1
          else:
            cave[step[1]:step[1]+1,step_old[0]:step[0]+1]=1
        
        # print(cave)
          
      step_old=step

  return cave

def falling_sand(cave,min_y,min_x):
  cnt_sand = 0
  more_sand = True
  while more_sand==True:

    cnt_sand=cnt_sand+1
    if cnt_sand%100==0:
      print(cnt_sand)

    falling=True

    if cave[0-min_y,500-min_x]==8:
      falling=False
      more_sand=False
    else:
      cave[0-min_y,500-min_x]=5
    
    while falling==True:
      y,x=(np.where(cave == 5))
      x=x[0]
      y=y[0]

      
      if y+1>cave.shape[0]-1:
        falling=False
        more_sand=False

      elif cave[y+1,x]==0:
        cave[y+1,x]=5
        cave[y,x]=0

      elif x-1<0:
        falling=False
        more_sand=False

      elif cave[y+1,x-1]==0:
        cave[y+1,x-1]=5
        cave[y,x]=0

      elif (x+1)>cave.shape[1]-1:
        falling=False
        more_sand=False

      elif cave[y+1,x+1]==0:
        cave[y+1,x+1]=5
        cave[y,x]=0

      else:
        cave[y,x]=8
        falling=False

  return cave

lines,min_x,min_y,max_x,max_y = read_file()

print(lines)

print(min_x)
print(max_x)
print(min_y)
print(max_y)

cave = create_cave(lines,min_x,min_y,max_x,max_y)

print(cave)

cave = falling_sand(cave,min_y,min_x)

print(cave)
print(sum(sum(cave == 8)))

np.savetxt("foo.csv", cave, delimiter=" ", fmt="%i")

    
    
"""
--- Part Two ---

You realize you misread the scan. There isn't an endless void at the bottom of the scan - there's floor, and you're standing on it!

You don't have time to scan the floor, so assume the floor is an infinite horizontal line with a y coordinate equal to two plus the highest y coordinate of any point in your scan.

In the example above, the highest y coordinate of any point is 9, and so the floor is at y=11. (This is as if your scan contained one extra rock path like -infinity,11 -> infinity,11.) With the added floor, the example above now looks like this:

        ...........+........
        ....................
        ....................
        ....................
        .........#...##.....
        .........#...#......
        .......###...#......
        .............#......
        .............#......
        .....#########......
        ....................
<-- etc #################### etc -->

To find somewhere safe to stand, you'll need to simulate falling sand until a unit of sand comes to rest at 500,0, blocking the source entirely and stopping the flow of sand into the cave. In the example above, the situation finally looks like this after 93 units of sand come to rest:

............o............
...........ooo...........
..........ooooo..........
.........ooooooo.........
........oo#ooo##o........
.......ooo#ooo#ooo.......
......oo###ooo#oooo......
.....oooo.oooo#ooooo.....
....oooooooooo#oooooo....
...ooo#########ooooooo...
..ooooo.......ooooooooo..
#########################

Using your scan, simulate the falling sand until the source of the sand becomes blocked. How many units of sand come to rest?
"""

lines,min_x,min_y,max_x,max_y = read_file()

print(str([[min_x,max_y+2],[max_x,max_y+2]]))

max_y=max_y+2
min_x=min_x-max_y
max_x=max_x+max_y

lines.append([[min_x,max_y],[max_x,max_y]])

cave2 = create_cave(lines,min_x,min_y,max_x,max_y)

print(cave2)

cave2 = falling_sand(cave2,min_y,min_x)

np.savetxt("foot.csv", cave2, delimiter=" ", fmt="%i")

print(cave2)
print(sum(sum(cave2 == 8)))

