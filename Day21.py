"""
--- Day 21: Monkey Math ---

The monkeys are back! You're worried they're going to try to steal your stuff again, but it seems like they're just holding their ground and making various monkey noises at you.

Eventually, one of the elephants realizes you don't speak monkey and comes over to interpret. As it turns out, they overheard you talking about trying to find the grove; they can show you a shortcut if you answer their riddle.

Each monkey is given a job: either to yell a specific number or to yell the result of a math operation. All of the number-yelling monkeys know their number from the start; however, the math operation monkeys need to wait for two other monkeys to yell a number, and those two other monkeys might also be waiting on other monkeys.

Your job is to work out the number the monkey named root will yell before the monkeys figure it out themselves.

For example:

root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32

Each line contains the name of a monkey, a colon, and then the job of that monkey:

    A lone number means the monkey's job is simply to yell that number.
    A job like aaaa + bbbb means the monkey waits for monkeys aaaa and bbbb to yell each of their numbers; the monkey then yells the sum of those two numbers.
    aaaa - bbbb means the monkey yells aaaa's number minus bbbb's number.
    Job aaaa * bbbb will yell aaaa's number multiplied by bbbb's number.
    Job aaaa / bbbb will yell aaaa's number divided by bbbb's number.

So, in the above example, monkey drzm has to wait for monkeys hmdt and zczc to yell their numbers. Fortunately, both hmdt and zczc have jobs that involve simply yelling a single number, so they do this immediately: 32 and 2. Monkey drzm can then yell its number by finding 32 minus 2: 30.

Then, monkey sjmn has one of its numbers (30, from monkey drzm), and already has its other number, 5, from dbpl. This allows it to yell its own number by finding 30 multiplied by 5: 150.

This process continues until root yells a number: 152.

However, your actual situation involves considerably more monkeys. What number will the monkey named root yell?
"""

# get the monkeys
file_name = r"day/21/input_example"
monkey_dict={}
with open(file_name, "r") as file:

    for line in file:
        monkey = line.split(":")[0]
        calc = line.split(":")[1].strip()
        monkey_dict[monkey] = calc

print(monkey_dict)

while not(monkey_dict["root"].isnumeric()):
    print(monkey_dict)

    for monkey in monkey_dict:
        #print(f"{monkey} : {monkey_dict[monkey]}")
        #print(monkey_dict)

        if not(monkey_dict[monkey].isnumeric()):
            #print(monkey_dict[monkey])
            part_1 = monkey_dict[monkey].split(" ")[0]
            operator = monkey_dict[monkey].split(" ")[1]
            part_2 = monkey_dict[monkey].split(" ")[2]

            if not(part_1.isnumeric()) and monkey_dict[part_1].isnumeric():
                part_1 = monkey_dict[part_1]

            if not(part_2.isnumeric()) and monkey_dict[part_2].isnumeric():
                part_2 = monkey_dict[part_2]

            if part_1.isnumeric() and part_2.isnumeric():
                if operator == "+":
                    monkey_dict[monkey] = str(int(int(part_1)+int(part_2)))
                elif operator == "-":
                    monkey_dict[monkey] = str(int(int(part_1)-int(part_2)))
                elif operator == "*":
                    monkey_dict[monkey] = str(int(int(part_1)*int(part_2)))
                elif operator == "/":
                    monkey_dict[monkey] = str(int(int(part_1)/int(part_2)))
                else:
                    print("operator error")
            else:
                monkey_dict[monkey] = f"{part_1} {operator} {part_2}"

print(monkey_dict)

print(monkey_dict["root"])


"""
Your puzzle answer was 268597611536314.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

Due to some kind of monkey-elephant-human mistranslation, you seem to have misunderstood a few key details about the riddle.

First, you got the wrong job for the monkey named root; specifically, you got the wrong math operation. The correct operation for monkey root should be =, which means that it still listens for two numbers (from the same two monkeys as before), but now checks that the two numbers match.

Second, you got the wrong monkey for the job starting with humn:. It isn't a monkey - it's you. Actually, you got the job wrong, too: you need to figure out what number you need to yell so that root's equality check passes. (The number that appears after humn: in your input is now irrelevant.)

In the above example, the number you need to yell to pass root's equality test is 301. (This causes root to get the same number, 150, from both of its monkeys.)

What number do you yell to pass root's equality test?
"""

import re

print("=======PART2========")
file_name = r"day/21/input"
monkey_dict={}
with open(file_name, "r") as file:

    for line in file:
        monkey = line.split(":")[0]
        calc = line.split(":")[1].strip()
        monkey_dict[monkey] = calc

monkey_dict["humn"] = "humn"
monkey_dict["root"] = monkey_dict["root"].replace("+","=")

print(monkey_dict)

for x in range(5):
    print(monkey_dict)

    for monkey in monkey_dict:
        print(f"{monkey} : {monkey_dict[monkey]}")
        #print(monkey_dict)
        # monkey_dict[monkey] = monkey_dict[monkey].replace(" ","")

        if not(monkey=='humn'):
            print(monkey_dict[monkey])
            # parts = re.split("\+|\-|\*|\/|=|\(|\)", monkey_dict[monkey])
            parts = monkey_dict[monkey].split(" ")
            print(parts)
            combo = ""
            for part in parts:
                if not(part.isnumeric()) and (part not in ["+","-","*","/","=","(",")"]):
                    part = "( "+monkey_dict[part]+" )"
                combo = combo+" "+part
                

            monkey_dict[monkey] = combo[1:]


print(monkey_dict["root"])

LHS = monkey_dict["root"].split("=")[0].strip()#.split(" ")
RHS = monkey_dict["root"].split("=")[1]
RHS = eval(RHS)

print(RHS)

def numeric_solver(LHS,RHS,guess,order):

    humn = guess
    calculated_LHS = eval(LHS)
    print(guess,calculated_LHS)
    
    if calculated_LHS==RHS:
        return guess,calculated_LHS

    if calculated_LHS<RHS:
        guess,calculated_LHS = numeric_solver(LHS, RHS,guess=int(guess-order),order=int(order/10))
    else:
        guess,calculated_LHS = numeric_solver(LHS, RHS,guess=int(guess+order),order=order)

    if calculated_LHS==RHS:
        return guess,calculated_LHS

humn = numeric_solver(LHS,RHS,0,100000000000000)[0]

print(eval(LHS),RHS)

print(f"Part 2 answer: {humn}")

"Your puzzle answer was 3451534022348."


## Failed Analytic Approach!

# print(humn)
# first_right_bracket = humn.index(")")
# corresponding_left_bracket = first_right_bracket-humn[first_right_bracket::-1].index("(")
# print(humn[first_right_bracket::-1])
# print(corresponding_left_bracket, first_right_bracket)
# print(humn[corresponding_left_bracket+1: first_right_bracket])
# print("".join(humn[corresponding_left_bracket+1: first_right_bracket]))
# str_inside_brackets= "".join(humn[corresponding_left_bracket+1: first_right_bracket])
# inside_brackets = eval(str_inside_brackets)
# print(inside_brackets)
# del humn[first_right_bracket]
# del humn[corresponding_left_bracket]
# humn.insert(inside_brackets,corresponding_left_bracket)
# print(humn)

# def evaluator(equation):
#     first_right_bracket = equation.index(")")
#     # print(first_right_bracket)
#     corresponding_left_bracket = first_right_bracket-equation[first_right_bracket::-1].index("(")
#     # print(corresponding_left_bracket)
#     str_inside_brackets= "".join(equation[corresponding_left_bracket+1: first_right_bracket])
#     # print(str_inside_brackets)
#     if str_inside_brackets=="humn":
#         inside_brackets="humn"
#     else:
#         inside_brackets = str(eval(str_inside_brackets))
#     # print(inside_brackets)
#     # print(equation)
#     # print("del")
#     del equation[corresponding_left_bracket:first_right_bracket+1]
#     # print(equation)
#     equation.insert(corresponding_left_bracket,inside_brackets)
#     # print(equation)
#     return equation


# def solver(LHS,RHS):
#     if LHS[0].isnumeric():
#         if LHS[1] == "+":
#             RHS = eval(str(RHS)+"-"+LHS[0])
#         elif LHS[1] == "-":
#             RHS = eval(str(RHS)+"+"+LHS[0])
#         elif LHS[1] == "*":
#             RHS = eval(str(RHS)+"/"+LHS[0])
            
#         del LHS[:2]
#         return LHS,RHS

#     elif LHS[-1].isnumeric():
#         if LHS[-2] == "+":
#             RHS = eval(str(RHS)+"-"+LHS[-1])            
#         elif LHS[-2] == "-":
#             RHS = eval(str(RHS)+"+"+LHS[-1])
#         elif LHS[-2] == "*":
#             RHS = eval(str(RHS)+"/"+LHS[-1])
#         elif LHS[-2] == "/":
#             RHS = eval(str(RHS)+"*"+LHS[-1])
            
#         del LHS[-2:]
#         return LHS,RHS


#     right_bracket = len(LHS)-LHS[::-1].index(")")-1

#     cnt_bracket=0
#     for bracket_index,bracket in enumerate(LHS[right_bracket::-1]):
#         if bracket=="(":
#             cnt_bracket = cnt_bracket+1
#         elif bracket==")":
#             cnt_bracket = cnt_bracket-1
        
#         if cnt_bracket==0:
#             break

#     left_bracket = len(LHS[right_bracket::-1])-bracket_index-1
    
#     print(left_bracket,right_bracket)

#     del LHS[right_bracket]
#     del LHS[left_bracket]
    
#     return LHS,RHS

# print("Fn")
# print(LHS)

# for a in range(9):
#     LHS = evaluator(LHS)
#     print(LHS)

# for a in range(20):
#     LHS,RHS = solver(LHS,RHS)
#     print(LHS,RHS)