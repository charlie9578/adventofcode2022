"""
--- Day 18: Boiling Boulders ---

You and the elephants finally reach fresh air. You've emerged near the base of a large volcano that seems to be actively erupting! Fortunately, the lava seems to be flowing away from you and toward the ocean.

Bits of lava are still being ejected toward you, so you're sheltering in the cavern exit a little longer. Outside the cave, you can see the lava landing in a pond and hear it loudly hissing as it solidifies.

Depending on the specific compounds in the lava and speed at which it cools, it might be forming obsidian! The cooling rate should be based on the surface area of the lava droplets, so you take a quick scan of a droplet as it flies past you (your puzzle input).

Because of how quickly the lava is moving, the scan isn't very good; its resolution is quite low and, as a result, it approximates the shape of the lava droplet with 1x1x1 cubes on a 3D grid, each given as its x,y,z position.

To approximate the surface area, count the number of sides of each cube that are not immediately connected to another cube. So, if your scan were only two adjacent cubes like 1,1,1 and 2,1,1, each cube would have a single side covered and five sides exposed, a total surface area of 10 sides.

Here's a larger example:

2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5

In the above example, after counting up all the sides that aren't connected to another cube, the total surface area is 64.

What is the surface area of your scanned lava droplet?
"""

import pandas as pd

file_name = r"day/18/input"

df = pd.read_csv(file_name,names=["x","y","z"])

print(df)

neighbours=[]
for cnt,pixel in df.iterrows():
    # print(pixel)
    # print((df[["x","y"]]==pixel[["x","y"]]).sum(axis=1))
    df_delta = df-pixel
    neighbours.append((sum(df_delta.abs().sum(axis=1)==1)))

df['neighbours']=neighbours
df['exposed_sides']=6-df['neighbours']

print(df)

print(df.sum())


"""
What is the surface area of your scanned lava droplet?

Your puzzle answer was 4310.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

Something seems off about your calculation. The cooling rate depends on exterior surface area, but your calculation also included the surface area of air pockets trapped in the lava droplet.

Instead, consider only cube sides that could be reached by the water and steam as the lava droplet tumbles into the pond. The steam will expand to reach as much as possible, completely displacing any air on the outside of the lava droplet but never expanding diagonally.

In the larger example above, exactly one cube of air is trapped within the lava droplet (at 2,2,5), so the exterior surface area of the lava droplet is 58.

What is the exterior surface area of your scanned lava droplet?
"""

xs=[]
ys=[]
zs=[]
for x in range(df["x"].min()+1,df["x"].max()):
    for y in range(df["y"].min()+1,df["y"].max()):
        for z in range(df["z"].min()+1,df["z"].max()):
            xs.append(x)
            ys.append(y)
            zs.append(z)
df_empty=pd.DataFrame(zip(xs,ys,zs),columns=["x","y","z"])

print(df_empty)

neighbours=[]
for cnt,pixel in df_empty.iterrows():
    # print(pixel)
    # print((df[["x","y"]]==pixel[["x","y"]]).sum(axis=1))
    df_delta = df-pixel
    neighbours.append((sum(df_delta.abs().sum(axis=1)==1)))

df_empty['neighbours']=neighbours
df_empty['exposed_sides']=6-df_empty['neighbours']

print(df_empty)

internals=df_empty[df_empty['exposed_sides']==0]

print(internals)

df_new = pd.concat([df,internals],axis=0).drop_duplicates().reset_index(drop=True).drop(columns=["neighbours","exposed_sides"])

print(df_new)

neighbours=[]
for cnt,pixel in df_new.iterrows():
    # print(pixel)
    # print((df[["x","y"]]==pixel[["x","y"]]).sum(axis=1))
    df_delta = df_new-pixel
    neighbours.append((sum(df_delta.abs().sum(axis=1)==1)))

df_new['neighbours']=neighbours
df_new['exposed_sides']=6-df_new['neighbours']

print(df_new)
print(df_new.sum())

