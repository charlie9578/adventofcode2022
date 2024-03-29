"""
--- Day 16: Proboscidea Volcanium ---

The sensors have led you to the origin of the distress signal: yet another handheld device, just like the one the Elves gave you. However, you don't see any Elves around; instead, the device is surrounded by elephants! They must have gotten lost in these tunnels, and one of the elephants apparently figured out how to turn on the distress signal.

The ground rumbles again, much stronger this time. What kind of cave is this, exactly? You scan the cave with your handheld device; it reports mostly igneous rock, some ash, pockets of pressurized gas, magma... this isn't just a cave, it's a volcano!

You need to get the elephants out of here, quickly. Your device estimates that you have 30 minutes before the volcano erupts, so you don't have time to go back out the way you came in.

You scan the cave for other options and discover a network of pipes and pressure-release valves. You aren't sure how such a system got into a volcano, but you don't have time to complain; your device produces a report (your puzzle input) of each valve's flow rate if it were opened (in pressure per minute) and the tunnels you could use to move between the valves.

There's even a valve in the room you and the elephants are currently standing in labeled AA. You estimate it will take you one minute to open a single valve and one minute to follow any tunnel from one valve to another. What is the most pressure you could release?

For example, suppose you had the following scan output:

Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II

All of the valves begin closed. You start at valve AA, but it must be damaged or jammed or something: its flow rate is 0, so there's no point in opening it. However, you could spend one minute moving to valve BB and another minute opening it; doing so would release pressure during the remaining 28 minutes at a flow rate of 13, a total eventual pressure release of 28 * 13 = 364. Then, you could spend your third minute moving to valve CC and your fourth minute opening it, providing an additional 26 minutes of eventual pressure release at a flow rate of 2, or 52 total pressure released by valve CC.

Making your way through the tunnels like this, you could probably open many or all of the valves by the time 30 minutes have elapsed. However, you need to release as much pressure as possible, so you'll need to be methodical. Instead, consider this approach:

== Minute 1 ==
No valves are open.
You move to valve DD.

== Minute 2 ==
No valves are open.
You open valve DD.

== Minute 3 ==
Valve DD is open, releasing 20 pressure.
You move to valve CC.

== Minute 4 ==
Valve DD is open, releasing 20 pressure.
You move to valve BB.

== Minute 5 ==
Valve DD is open, releasing 20 pressure.
You open valve BB.

== Minute 6 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve AA.

== Minute 7 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve II.

== Minute 8 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve JJ.

== Minute 9 ==
Valves BB and DD are open, releasing 33 pressure.
You open valve JJ.

== Minute 10 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve II.

== Minute 11 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve AA.

== Minute 12 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve DD.

== Minute 13 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve EE.

== Minute 14 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve FF.

== Minute 15 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve GG.

== Minute 16 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve HH.

== Minute 17 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You open valve HH.

== Minute 18 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve GG.

== Minute 19 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve FF.

== Minute 20 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve EE.

== Minute 21 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You open valve EE.

== Minute 22 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve DD.

== Minute 23 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve CC.

== Minute 24 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You open valve CC.

== Minute 25 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 26 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 27 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 28 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 29 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 30 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

This approach lets you release the most pressure possible in 30 minutes with this valve layout, 1651.

Work out the steps to release the most pressure in 30 minutes. What is the most pressure you can release?
"""

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import time

timer = time.time()

file_name = r"day/16/input"
valve=[]
flow=[]
target=[]
with open(file_name, "r") as file:

    for line in file:
        parts = line.strip().split(" ")
        for target_valve in parts[9:]:
            valve.append(parts[1])
            flow.append(int(parts[4].split("=")[-1].strip(";")))
            target.append(target_valve.strip(","))


print(valve)
print(flow)
print(target)

df = pd.DataFrame(list(zip(valve,target,flow)),
               columns =['Source','Target','Flow'])

print(df)

G = nx.from_pandas_edgelist(df, source="Source", target="Target")

nx.draw(G, with_labels=True, font_weight='bold')

# plt.show()

df_useful = df[["Source","Flow"]].drop_duplicates()
df_useful = df_useful[df_useful["Flow"]>0]
df_useful = df_useful.set_index("Source")

print(df_useful)

shortest_paths = dict(nx.shortest_path_length(G))
# print(shortest_paths)

flows = dict(zip(valve,flow))
print(flows)


def check_routes(path,time_remaining,discharge,max_discharge):
    current_node = path[-1]
    potential_nodes = set(df_useful.index)

    for node in potential_nodes-set(path):
        new_path = path.copy()
        distance = shortest_paths[current_node][node]
        new_time_remaining = time_remaining - distance - 1

        if new_time_remaining>=0:
            new_path.append(node)
            flow = flows[node]
            new_discharge = discharge + flow*new_time_remaining

            if new_discharge>max_discharge:
                max_discharge=new_discharge
                print(f"Route {path} produced a discharge of {new_discharge} with {new_time_remaining} time remaining")

            max_discharge=check_routes(new_path,new_time_remaining,discharge=new_discharge,max_discharge=max_discharge)

    return max_discharge


time_remaining = 30
discharge = 0
max_discharge = 0
path = ["AA"]
max_discharge=check_routes(path=path,time_remaining=time_remaining,discharge=discharge,max_discharge=max_discharge)
print(max_discharge)

print(f"Time elapsed: {time.time()-timer}s")


"""
Your puzzle answer was 1673.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

You're worried that even with an optimal approach, the pressure released won't be enough. What if you got one of the elephants to help you?

It would take you 4 minutes to teach an elephant how to open the right valves in the right order, leaving you with only 26 minutes to actually execute your plan. Would having two of you working together be better, even if it means having less time? (Assume that you teach the elephant before opening any valves yourself, giving you both the same full 26 minutes.)

In the example above, you could teach the elephant to help you as follows:

== Minute 1 ==
No valves are open.
You move to valve II.
The elephant moves to valve DD.

== Minute 2 ==
No valves are open.
You move to valve JJ.
The elephant opens valve DD.

== Minute 3 ==
Valve DD is open, releasing 20 pressure.
You open valve JJ.
The elephant moves to valve EE.

== Minute 4 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve II.
The elephant moves to valve FF.

== Minute 5 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve AA.
The elephant moves to valve GG.

== Minute 6 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve BB.
The elephant moves to valve HH.

== Minute 7 ==
Valves DD and JJ are open, releasing 41 pressure.
You open valve BB.
The elephant opens valve HH.

== Minute 8 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve CC.
The elephant moves to valve GG.

== Minute 9 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You open valve CC.
The elephant moves to valve FF.

== Minute 10 ==
Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
The elephant moves to valve EE.

== Minute 11 ==
Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
The elephant opens valve EE.

(At this point, all valves are open.)

== Minute 12 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

...

== Minute 20 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

...

== Minute 26 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

With the elephant helping, after 26 minutes, the best you could do would release a total of 1707 pressure.

With you and an elephant working together for 26 minutes, what is the most pressure you could release?
"""

max_discharge_possible = check_routes(path=["AA"],time_remaining=26,discharge=0,max_discharge=0)

def check_routes1(path,time_remaining,discharge,max_discharge):
    current_node = path[-1]
    potential_nodes = set(df_useful.index)

    for node in potential_nodes-set(path):
        new_path = path.copy()
        distance = shortest_paths[current_node][node]
        new_time_remaining = time_remaining - distance - 1

        if new_time_remaining>=0:
            new_path.append(node)
            flow = flows[node]
            new_discharge = discharge + flow*new_time_remaining

            if new_discharge + max_discharge_possible >= max_discharge:
                second_discharge,best_path,best_remaining_time = check_routes2(path1=new_path,path=["AA"],time_remaining=26,discharge=0,max_discharge=0,best_path=[],best_remaining_time=0)
            else:
                best_path=[]
                best_remaining_time = 0
                second_discharge = 0

            if new_discharge + second_discharge > max_discharge:
                max_discharge = new_discharge + second_discharge
                print(f"Max discharge {max_discharge}")
                print(f"Route1 {new_path} produced a discharge of {new_discharge} with {new_time_remaining} time remaining")
                print(f"Route2 {best_path} produced a discharge of {second_discharge} with {best_remaining_time} time remaining")

            max_discharge=check_routes1(new_path,new_time_remaining,discharge=new_discharge,max_discharge=max_discharge)

    return max_discharge


def check_routes2(path1,path,time_remaining,discharge,max_discharge,best_path,best_remaining_time):
    current_node = path[-1]
    potential_nodes = set(df_useful.index)-set(path1)


    for node in potential_nodes-set(path):
        new_path = path.copy()
        distance = shortest_paths[current_node][node]
        new_time_remaining = time_remaining - distance - 1

        if new_time_remaining>=0:
            new_path.append(node)
            flow = flows[node]
            new_discharge = discharge + flow*new_time_remaining

            if new_discharge>max_discharge:
                max_discharge=new_discharge
                best_path = new_path
                best_remaining_time = new_time_remaining
                # print(f"Route2 {path} produced a discharge of {new_discharge} with {new_time_remaining} time remaining")

            max_discharge,best_path,best_remaining_time=check_routes2(path1,new_path,new_time_remaining,discharge=new_discharge,max_discharge=max_discharge,best_path=best_path,best_remaining_time=best_remaining_time)

    return max_discharge,best_path,best_remaining_time

max_discharge=check_routes1(path=["AA"],time_remaining=26,discharge=0,max_discharge=0)
print(max_discharge)

print(f"Time elapsed: {time.time()-timer}s")

