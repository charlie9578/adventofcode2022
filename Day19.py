"""
--- Day 19: Not Enough Minerals ---

Your scans show that the lava did indeed form obsidian!

The wind has changed direction enough to stop sending lava droplets toward you, so you and the elephants exit the cave. As you do, you notice a collection of geodes around the pond. Perhaps you could use the obsidian to create some geode-cracking robots and break them open?

To collect the obsidian from the bottom of the pond, you'll need waterproof obsidian-collecting robots. Fortunately, there is an abundant amount of clay nearby that you can use to make them waterproof.

In order to harvest the clay, you'll need special-purpose clay-collecting robots. To make any type of robot, you'll need ore, which is also plentiful but in the opposite direction from the clay.

Collecting ore requires ore-collecting robots with big drills. Fortunately, you have exactly one ore-collecting robot in your pack that you can use to kickstart the whole operation.

Each robot can collect 1 of its resource type per minute. It also takes one minute for the robot factory (also conveniently from your pack) to construct any type of robot, although it consumes the necessary resources available when construction begins.

The robot factory has many blueprints (your puzzle input) you can choose from, but once you've configured it with a blueprint, you can't change it. You'll need to work out which blueprint is best.

For example:

Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian.

(Blueprints have been line-wrapped here for legibility. The robot factory's actual assortment of blueprints are provided one blueprint per line.)

The elephants are starting to look hungry, so you shouldn't take too long; you need to figure out which blueprint would maximize the number of opened geodes after 24 minutes by figuring out which robots to build and when to build them.

Using blueprint 1 in the example above, the largest number of geodes you could open in 24 minutes is 9. One way to achieve that is:

== Minute 1 ==
1 ore-collecting robot collects 1 ore; you now have 1 ore.

== Minute 2 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.

== Minute 3 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
The new clay-collecting robot is ready; you now have 1 of them.

== Minute 4 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
1 clay-collecting robot collects 1 clay; you now have 1 clay.

== Minute 5 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
1 clay-collecting robot collects 1 clay; you now have 2 clay.
The new clay-collecting robot is ready; you now have 2 of them.

== Minute 6 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
2 clay-collecting robots collect 2 clay; you now have 4 clay.

== Minute 7 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
2 clay-collecting robots collect 2 clay; you now have 6 clay.
The new clay-collecting robot is ready; you now have 3 of them.

== Minute 8 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
3 clay-collecting robots collect 3 clay; you now have 9 clay.

== Minute 9 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
3 clay-collecting robots collect 3 clay; you now have 12 clay.

== Minute 10 ==
1 ore-collecting robot collects 1 ore; you now have 4 ore.
3 clay-collecting robots collect 3 clay; you now have 15 clay.

== Minute 11 ==
Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 2 ore.
3 clay-collecting robots collect 3 clay; you now have 4 clay.
The new obsidian-collecting robot is ready; you now have 1 of them.

== Minute 12 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
3 clay-collecting robots collect 3 clay; you now have 7 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 1 obsidian.
The new clay-collecting robot is ready; you now have 4 of them.

== Minute 13 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
4 clay-collecting robots collect 4 clay; you now have 11 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 2 obsidian.

== Minute 14 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 15 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 3 obsidian.

== Minute 15 ==
Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
4 clay-collecting robots collect 4 clay; you now have 5 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 4 obsidian.
The new obsidian-collecting robot is ready; you now have 2 of them.

== Minute 16 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
4 clay-collecting robots collect 4 clay; you now have 9 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.

== Minute 17 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 13 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.

== Minute 18 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
1 ore-collecting robot collects 1 ore; you now have 2 ore.
4 clay-collecting robots collect 4 clay; you now have 17 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 3 obsidian.
The new geode-cracking robot is ready; you now have 1 of them.

== Minute 19 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 21 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 5 obsidian.
1 geode-cracking robot cracks 1 geode; you now have 1 open geode.

== Minute 20 ==
1 ore-collecting robot collects 1 ore; you now have 4 ore.
4 clay-collecting robots collect 4 clay; you now have 25 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 7 obsidian.
1 geode-cracking robot cracks 1 geode; you now have 2 open geodes.

== Minute 21 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 29 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 2 obsidian.
1 geode-cracking robot cracks 1 geode; you now have 3 open geodes.
The new geode-cracking robot is ready; you now have 2 of them.

== Minute 22 ==
1 ore-collecting robot collects 1 ore; you now have 4 ore.
4 clay-collecting robots collect 4 clay; you now have 33 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 4 obsidian.
2 geode-cracking robots crack 2 geodes; you now have 5 open geodes.

== Minute 23 ==
1 ore-collecting robot collects 1 ore; you now have 5 ore.
4 clay-collecting robots collect 4 clay; you now have 37 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.
2 geode-cracking robots crack 2 geodes; you now have 7 open geodes.

== Minute 24 ==
1 ore-collecting robot collects 1 ore; you now have 6 ore.
4 clay-collecting robots collect 4 clay; you now have 41 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.
2 geode-cracking robots crack 2 geodes; you now have 9 open geodes.

However, by using blueprint 2 in the example above, you could do even better: the largest number of geodes you could open in 24 minutes is 12.

Determine the quality level of each blueprint by multiplying that blueprint's ID number with the largest number of geodes that can be opened in 24 minutes using that blueprint. In this example, the first blueprint has ID 1 and can open 9 geodes, so its quality level is 9. The second blueprint has ID 2 and can open 12 geodes, so its quality level is 24. Finally, if you add up the quality levels of all of the blueprints in the list, you get 33.

Determine the quality level of each blueprint using the largest number of geodes it could produce in 24 minutes. What do you get if you add up the quality level of all of the blueprints in your list?
"""

import re
import itertools
import time

# Read in the blueprints
file_name = r"day/19/input"
blueprints=[]
with open(file_name, "r") as file:

    for line in file:
        blueprint = []
        parts = line.strip().split(".")[:-1]
        print(parts)

        for part in parts:
            
            name=part.split(" robot")[-2].split(" ")[-1]
            
            try:
                ore=int(part.split(" ore")[-2].split(" ")[-1])
            except:
                ore=0

            try:
                clay=int(part.split(" clay")[-2].split(" ")[-1])
            except:
                clay=0

            try:
                obsidian=int(part.split(" obsidian")[-2].split(" ")[-1])
            except:
                obsidian=0
            
            blueprint.append([ore,clay,obsidian])

        blueprints.append(blueprint)

print(blueprints)

# minutes = 24
# blueprint = blueprints[0]
# targets = [0,1]+[1,1,2,1,2,3,3]
# robots = [1,0,0,0]
# minerals = [0,0,0,0]
# most_geodes = 0
# for minute in range(minutes):

#     print(f"\n== Minute {minute+1} ==")
#     print(f"Robots: {robots}")

#     # build robots with available resources
#     if sum(robots) < len(targets):
#         target_robot = targets[sum(robots)]
#         robot_cost = blueprint[target_robot]

#         if minerals[0]>=robot_cost[0] and minerals[1]>=robot_cost[1] and minerals[2]>=robot_cost[2]:
#             robots[target_robot] = robots[target_robot] + 1
#             for cnt,mineral in enumerate(robot_cost):
#                 minerals[cnt]=minerals[cnt]-mineral
#             minerals[target_robot] = minerals[target_robot] - 1
#             print(f"Robot {target_robot} built")

#     # mine minerals
#     for cnt,robot in enumerate(robots):
#         minerals[cnt]=minerals[cnt]+robot

#     print(f"Minerals: {minerals}")

# total_geodes = minerals[3]

# print(f"\nTotal geodes: {minerals[3]}\n")

# if minerals[3]>=most_geodes:
#     most_geodes = minerals[3]


# def calculate_geodes(targets,blueprint):
    
#     targets = targets.copy()
#     minutes = 24
#     robots = [1,0,0,0]
#     minerals = [0,0,0,0]
#     previous_minerals = [0,0,0,0]
#     wait = 0
#     shortages = [0,0,0]

#     for minute in range(minutes):

#         # print(f"\n== Minute {minute+1} ==")
#         # print(f"Robots: {robots}")

#         # build robots with available resources
#         if sum(robots) < len(targets):
#             target_robot = targets[sum(robots)]
#             robot_cost = blueprint[target_robot]

#             if minerals[0]>=robot_cost[0] and minerals[1]>=robot_cost[1] and minerals[2]>=robot_cost[2]:
#                 robots[target_robot] = robots[target_robot] + 1
#                 for cnt,mineral in enumerate(robot_cost):
#                     minerals[cnt]=minerals[cnt]-mineral
#                 minerals[target_robot] = minerals[target_robot] - 1
#                 # print(f"Robot {target_robot} built")

#                 for cnt in range(3):
#                     if previous_minerals[cnt]<robot_cost[cnt]:
#                         # print(f"Minute {minute}. Robot built {target_robot}. More {cnt} would speed things up. {wait} minute wait")
#                         shortages[cnt] = shortages[cnt] + wait
#                         wait = 0

#             wait = wait + 1
#             previous_minerals = minerals.copy()
                

#         # mine minerals
#         for cnt,robot in enumerate(robots):
#             minerals[cnt]=minerals[cnt]+robot

#         # print(f"Minerals: {minerals}")

#     total_geodes = minerals[3]

#     # print(f"\nTotal geodes: {total_geodes}\n")   

#     suggested_build = shortages.index(max(shortages))
#     # print(f"Shortages: {shortages}")
#     # print(f"Suggested build: {suggested_build}")

#     return total_geodes,robots,suggested_build



# blueprint = blueprints[1]
# targets = [0,1]+[1,1,2,1,2,3,3]
# targets = [0,1,1,1,1,2,2,3,3,3,3,3,3,3]
# targets = [0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3]

# targets = [0,1,2,3,3,3,3,3,3,3,3,3,3,3]
# max_geodes = 0
# best_targets = []
# for a in range(20):

#     for b in range(20):
#         total_geodes,robots,suggested_build = calculate_geodes(targets,blueprint)
#         print(total_geodes)

#         if total_geodes>= max_geodes:
#             max_geodes = total_geodes
#             best_targets = targets.copy()
        
#         targets.insert(targets.index(suggested_build),suggested_build)

#     if total_geodes>= max_geodes:
#         max_geodes = total_geodes
#         best_targets = targets.copy()
       
#     targets = best_targets.copy()
#     suggested_build = 0
#     targets.insert(targets.index(suggested_build),suggested_build)
#     total_geodes,robots,suggested_build = calculate_geodes(targets,blueprint)

#     if total_geodes>= max_geodes:
#         max_geodes = total_geodes
#         best_targets = targets.copy()

#     targets = best_targets.copy()
#     suggested_build = 1
#     targets.insert(targets.index(suggested_build),suggested_build)
#     total_geodes,robots,suggested_build = calculate_geodes(targets,blueprint)

#     if total_geodes>= max_geodes:
#         max_geodes = total_geodes
#         best_targets = targets.copy()

#     targets = best_targets.copy()
#     suggested_build = 2
#     targets.insert(targets.index(suggested_build),suggested_build)
#     total_geodes,robots,suggested_build = calculate_geodes(targets,blueprint)

#     if total_geodes>= max_geodes:
#         max_geodes = total_geodes
#         best_targets = targets.copy()

#     targets = best_targets.copy()
#     shift_value = 1
#     shift_index = targets.index(shift_value)
#     shifted_value = targets[shift_index-1]
#     targets[shift_index-1] = shift_value
#     targets[shift_index] = shifted_value
#     total_geodes,robots,suggested_build = calculate_geodes(targets,blueprint)

#     if total_geodes>= max_geodes:
#         max_geodes = total_geodes
#         best_targets = targets.copy()

#     targets = best_targets.copy()
#     shift_value = 2
#     shift_index = targets.index(shift_value)
#     shifted_value = targets[shift_index-1]
#     targets[shift_index-1] = shift_value
#     targets[shift_index] = shifted_value
#     total_geodes,robots,suggested_build = calculate_geodes(targets,blueprint)

#     if total_geodes>= max_geodes:
#         max_geodes = total_geodes
#         best_targets = targets.copy()

#     targets = best_targets.copy()
#     shift_value = 3
#     shift_index = targets.index(shift_value)
#     shifted_value = targets[shift_index-1]
#     targets[shift_index-1] = shift_value
#     targets[shift_index] = shifted_value
#     total_geodes,robots,suggested_build = calculate_geodes(targets,blueprint)

#     print(f"Best result: {max_geodes},{best_targets}")

# print(f"Best result: {max_geodes},{best_targets}")


# target_list = []
# for a in range(1,5):
#     for b in range(1,11):
#         for c in range(1,11):
#             d = 8

#             # no switching
#             target_list.append([0]*a+[1]*b+[2]*c+[3]*d)

#             # one switch
#             target_list.append([0]*(a-1)+[1]+[0]+[1]*(b-1)+[2]*c+[3]*d)
#             target_list.append([0]*a+[1]*(b-1)+[2]+[1]+[2]*(c-1)+[3]*d)
#             target_list.append([0]*a+[1]*b+[2]*(c-1)+[3]+[2]+[3]*(d-1))
                
#             # one switch 2 places
#             if a>1:
#                 target_list.append([0]*(a-2)+[1]+2*[0]+[1]*(b-1)+[2]*c+[3]*d)
#             if b>1:
#                 target_list.append([0]*a+[1]*(b-2)+[2]+2*[1]+[2]*(c-1)+[3]*d)
#             if c>1:
#                 target_list.append([0]*a+[1]*b+[2]*(c-2)+[3]+2*[2]+[3]*(d-1))

#             # one switch 3 places
#             if a>2:
#                 target_list.append([0]*(a-3)+[1]+3*[0]+[1]*(b-1)+[2]*c+[3]*d)
#             if b>2:
#                 target_list.append([0]*a+[1]*(b-3)+[2]+3*[1]+[2]*(c-1)+[3]*d)
#             if c>2:
#                 target_list.append([0]*a+[1]*b+[2]*(c-3)+[3]+3*[2]+[3]*(d-1))

#             # two different switches
#             # 1 & 2
#             if b>1:
#                 target_list.append([0]*(a-1)+[1]+[0]+[1]*(b-2)+[2]+[1]+[2]*(c-1)+[3]*d)
#             # 2 & 3
#             if c>1:
#                 target_list.append([0]*a+[1]*(b-1)+[2]+[1]+[2]*(c-2)+[3]+[2]+[3]*d)
#             # 1 & 3
#             target_list.append([0]*(a-1)+[1]+[0]+[1]*(b-1)+[2]*(c-1)+[3]+[2]+[3]*(d-1))

#             # two different switches both two places
#             # 1 & 2
#             if a>1 and b>2:
#                 target_list.append([0]*(a-2)+[1]+2*[0]+[1]*(b-3)+[2]+2*[1]+[2]*(c-1)+[3]*d)
#             # 2 & 3
#             if b>1 and c>2:
#                 target_list.append([0]*a+[1]*(b-2)+[2]+2*[1]+[2]*(c-3)+[3]+2*[2]+[3]*d)
#             # 1 & 3
#             if a>1 and c>1:
#                 target_list.append([0]*(a-2)+[1]+2*[0]+[1]*(b-1)+[2]*(c-2)+[3]+2*[2]+[3]*(d-1))

#             # three different switches
#             if b>1 and c>1:
#                 target_list.append([0]*(a-1)+[1]+[0]+[1]*(b-2)+[2]+[1]+[2]*(c-2)+[3]+[2]+[3]*(d-1))


# print(len(target_list))

# ids = []
# blueprint_cnt = 0

# for blueprint in blueprints:
#     blueprint_cnt = blueprint_cnt+1

#     max_geodes = 0
#     for targets in target_list:
#         total_geodes,robots,suggested_build = calculate_geodes(targets,blueprint)

#         if total_geodes>0 and total_geodes>= max_geodes:
#             max_geodes = total_geodes
#             best_targets = targets.copy()

#     print(f"Best result from target_list for blueprint {blueprint_cnt}. Geodes: {max_geodes}, Robots produced: {best_targets}, ID: {max_geodes*blueprint_cnt}")

#     ids.append(max_geodes*blueprint_cnt)

# print(f"Total ids: {sum(ids)}")



# def dodgy_optimizer(blueprint):
#     targets = [0,1,2,3,3,3,3,3,3,3,3,3,3,3]
#     max_geodes = 0
#     best_targets = targets.copy()
#     for a in range(20):

#         for b in range(20):
#             total_geodes,robots,suggested_build = calculate_geodes(targets,blueprint)
#             # print(total_geodes)

#             if total_geodes>0 and total_geodes>= max_geodes:
#                 max_geodes = total_geodes
#                 best_targets = targets.copy()
            
#             targets.insert(targets.index(suggested_build),suggested_build)

#         if total_geodes>0 and total_geodes>= max_geodes:
#             max_geodes = total_geodes
#             best_targets = targets.copy()
        
#         targets = best_targets.copy()
#         suggested_build = 0
#         targets.insert(targets.index(suggested_build),suggested_build)
#         total_geodes,robots,suggested_build = calculate_geodes(targets,blueprint)

#         if total_geodes>= max_geodes:
#             max_geodes = total_geodes
#             best_targets = targets.copy()

#         targets = best_targets.copy()
#         suggested_build = 1
#         targets.insert(targets.index(suggested_build),suggested_build)
#         total_geodes,robots,suggested_build = calculate_geodes(targets,blueprint)

#         if total_geodes>= max_geodes:
#             max_geodes = total_geodes
#             best_targets = targets.copy()

#         targets = best_targets.copy()
#         suggested_build = 2
#         targets.insert(targets.index(suggested_build),suggested_build)
#         total_geodes,robots,suggested_build = calculate_geodes(targets,blueprint)

#         if total_geodes>= max_geodes:
#             max_geodes = total_geodes
#             best_targets = targets.copy()

#         targets = best_targets.copy()
#         shift_value = 1
#         shift_index = targets.index(shift_value)
#         shifted_value = targets[shift_index-1]
#         targets[shift_index-1] = shift_value
#         targets[shift_index] = shifted_value
#         total_geodes,robots,suggested_build = calculate_geodes(targets,blueprint)

#         if total_geodes>= max_geodes:
#             max_geodes = total_geodes
#             best_targets = targets.copy()

#         targets = best_targets.copy()
#         shift_value = 2
#         shift_index = targets.index(shift_value)
#         shifted_value = targets[shift_index-1]
#         targets[shift_index-1] = shift_value
#         targets[shift_index] = shifted_value
#         total_geodes,robots,suggested_build = calculate_geodes(targets,blueprint)

#         if total_geodes>= max_geodes:
#             max_geodes = total_geodes
#             best_targets = targets.copy()

#         targets = best_targets.copy()
#         shift_value = 3
#         shift_index = targets.index(shift_value)
#         shifted_value = targets[shift_index-1]
#         targets[shift_index-1] = shift_value
#         targets[shift_index] = shifted_value
#         total_geodes,robots,suggested_build = calculate_geodes(targets,blueprint)

#         # print(f"Best result: {max_geodes},{best_targets}")

#     # print(f"Best result: {max_geodes},{best_targets}")

#     return (max_geodes,best_targets,robots)

# blueprint_cnt = 0
# final_geodes = 0
# best_result = []
# ids = []
# for blueprint in blueprints:
#     blueprint_cnt = blueprint_cnt+1
#     max_geodes,best_targets,robots = dodgy_optimizer(blueprint)
#     print(f"Best result from optimizer for blueprint {blueprint_cnt}. Geodes: {max_geodes}, Robots produced: {robots}, ID: {max_geodes*blueprint_cnt}")
#     ids.append(max_geodes*blueprint_cnt)

# print(f"Total ids: {sum(ids)}")

# shift_value = 0
# targets = best_targets.copy()
# for a in range(15):

#     total_geodes,robots,suggested_build = calculate_geodes(targets,blueprint)
#     print(total_geodes)

#     if total_geodes>= max_geodes:
#         max_geodes = total_geodes
#         best_targets = targets.copy()

#     shift_value = (shift_value + 1)%3
#     targets = best_targets.copy()
#     shift_index = targets.index(shift_value)
#     shifted_value = targets[shift_index-1]
#     print(targets)
#     targets[shift_index-1] = shift_value
#     targets[shift_index] = shifted_value
#     print(targets)

# print(f"Shifting nodes best result: {max_geodes},{best_targets}")

# blueprint = blueprints[1]

# combos = itertools.product(range(12),repeat=10)
# print(len(list(combos)))

# combos = [[1,1,2,1,2,3,3]] # solution to blueprint 0
# robots_used = []
# old_targets = []
# most_geodes = 0
# for combo in combos:
    
#     combo = list(combo)

#     combo_clean = []
#     for cnt,item in enumerate(combo):
#         combo_clean.append(item%4)
#         run = True
#         if cnt>0 and (item%4)>max(combo_clean[0:cnt])+1:
#             run = False
#             break

#     if combo_clean[0]>2: 
#         run = False

#     if 3 not in combo_clean:
#         run = False

#     targets = [0,1]+list(combo_clean)  

#     if robots_used:
#         if targets[0:sum(robots_used)] == old_targets[0:sum(robots_used)]:
#             run = False

#     if run:
#             geodes,robots_used = calculate_geodes(targets,blueprint)

#             print(f"Targets: {targets}, Old targets: {old_targets}, Robots: {robots_used}, Geodes: {geodes}")

#             if geodes>=most_geodes:
#                 most_geodes = geodes
#                 print(most_geodes)

#             old_targets=targets.copy()

# print(most_geodes)


def calculate_geodes_recursive(minerals,robots,blueprint,step,max_geodes,target_robots):
    minerals=minerals.copy()
    robots=robots.copy()
    step = int(step)

    step = step + 1

    if step<=24:        

        # try and create robots
        step_pre_loop = step
        minerals_pre_loop = minerals.copy()
        robots_pre_loop = robots.copy()

        for target_robot in target_robots:
            
            step_old = step_pre_loop
            minerals_old = minerals_pre_loop.copy()
            robots_old = robots_pre_loop.copy()

            robot_cost = blueprint[target_robot]

            # create the target robot if possible
            if minerals_old[0]>=robot_cost[0] and minerals_old[1]>=robot_cost[1] and minerals_old[2]>=robot_cost[2]:
                robots_old[target_robot] = robots_old[target_robot] + 1
                for cnt,mineral in enumerate(robot_cost):
                    minerals_old[cnt]=minerals_old[cnt]-mineral
                minerals_old[target_robot] = minerals_old[target_robot] - 1

                # mine minerals
                for cnt,robot in enumerate(robots_old):
                    minerals_old[cnt]=minerals_old[cnt]+robot


                # continue to next round
                new_target_robots = []
                if robots_old[0]<5:
                    new_target_robots.append(0)
                if robots_old[1]<10:
                    new_target_robots.append(1)
                if robots_old[2]<10 and robots_old[1]>=1:
                    new_target_robots.append(2)
                if robots_old[2]>=1:
                    new_target_robots.append(3)

                if (minerals[3]+(25-step_old)*robots[3]+(25-step_old)*(25-step_old))<max_geodes:
                    step = 99
                    return step,minerals,robots,max_geodes

                step,minerals,robots,max_geodes = calculate_geodes_recursive(minerals_old.copy(),robots_old.copy(),blueprint,step_old,max_geodes,target_robots=new_target_robots)

            else:
                # mine minerals
                for cnt,robot in enumerate(robots_old):
                    minerals_old[cnt]=minerals_old[cnt]+robot

                # try to build the same robot next time round if failed to build it
                step,minerals,robots,max_geodes = calculate_geodes_recursive(minerals_old.copy(),robots_old.copy(),blueprint,step_old,max_geodes,target_robots=[target_robot])
        
        # print(step,minerals,robots)

    # print(step,minerals,robots)
    
    if minerals[3]>max_geodes:
        max_geodes = minerals[3]

    return step,minerals,robots,max_geodes
    
    


    
        

print(f"\n==== RECURSIVE ====\n")
blueprint = blueprints[0]
minerals=[0,0,0,0] #[4,15,0,0] #[4, 25, 7, 2] # [0,0,0,0]
robots=[1,0,0,0] # [1, 3, 0, 0] # [1,0,0,0]
target_robots=[0,1,2,3]
step=0 #10 #20

start_time = time.time()
print(time.strftime("%H:%M:%S", time.localtime(start_time)))

ids = []
blueprint_cnt = 0

for blueprint in blueprints:
    
    blueprint_cnt = blueprint_cnt+1

    minerals=[0,0,0,0]
    robots=[1,0,0,0]
    target_robots=[0,1]
    step=0

    step,minerals,robots,max_geodes = calculate_geodes_recursive(minerals=minerals.copy(),robots=robots.copy(),target_robots=target_robots,blueprint=blueprint,step=step,max_geodes=0)

    print(f"Best result from target_list for blueprint {blueprint_cnt}. Geodes: {max_geodes}, ID: {max_geodes*blueprint_cnt}. Time taken: {time.time()-start_time:0.2f}s.")

    ids.append(max_geodes*blueprint_cnt)

print(f"Total ids: {sum(ids)}")

# def simple_recursion(step,target_robot,minerals):
#     step = step+1
    
#     for cnt,robot in enumerate(robots):
#                 minerals[cnt]=minerals[cnt]+robot

#     if step<=10:
#         print(f"Minute: {step}, Target robot: {target_robot}, Minerals: {minerals}")
#         if step>=8:
#             for target_robot in range(3):
#                 simple_recursion(step,target_robot,minerals)
#         else:
#             simple_recursion(step,target_robot,minerals)
    
#     return step

# simple_recursion(step=step,target_robot=target_robot,minerals=minerals)


# def geode_recursion(step,target_robot,minerals):
#     step = step+1
    
#     for cnt,robot in enumerate(robots):
#                 minerals[cnt]=minerals[cnt]+robot

#     if step<=5:
#         print(f"Minute: {step}, Target robot: {target_robot}, Minerals: {minerals}")

#         if step>=2:

#             for target_robot in range(3):
#                 geode_recursion(step,target_robot,minerals.copy())
        
#         else:
#             geode_recursion(step,target_robot,minerals.copy())
    
#     return step

# print("===Recursion===")
# geode_recursion(step=0,target_robot=0,minerals=[0,0,0,0])