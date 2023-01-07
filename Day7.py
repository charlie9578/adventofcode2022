"""
--- Day 7: No Space Left On Device ---

You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device

Perhaps you can delete some files to make space for the update?

You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:

$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k

The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

    cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
        cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
        cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
        cd / switches the current directory to the outermost directory, /.
    ls means list. It prints out all of the files and directories immediately contained by the current directory:
        123 abc means that the current directory contains a file named abc with size 123.
        dir xyz means that the current directory contains a directory named xyz.

Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)

Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a). These directories also contain files of various sizes.

Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the total size of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

The total sizes of the directories above can be found as follows:

    The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
    The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
    Directory d has total size 24933642.
    As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.

To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)

Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
"""

from typing import NamedTuple

class directory(NamedTuple):
    # name:str
    # directories:list
    # files:list
    pass

class file(NamedTuple):
    name:str
    size:int
    

filesystem = dict()

print(filesystem)
call = ["root","a"]
filesystem["root"] = {}
filesystem["root"]["c"] = {"size":99}

def nested_get(dic, keys):    
    for key in keys:
        dic = dic[key]
    return dic

def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value    

def nested_add(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]][value[0]] = value[1]

filesystem = {}
current_dir = []
with open(r"day/7/input", "r") as file:

    for line in file:
        
        line = line.strip()

        print(current_dir)
        print("\nCurrent line: "+line)

        split_line = line.split(" ")

        if split_line[0]=="$":
            #print("command")
            #print(split_line)
            if split_line[1]=="ls":
                print("list directory")
            elif split_line[1]=="cd":
                if split_line[2]=="/":
                    print("cd root")
                    current_dir = ["root"]
                elif split_line[2]=="..":
                    print("move out one directory")
                    current_dir = current_dir[0:-1]
                else:
                    print("move into directory "+split_line[2])
                    current_dir.append(split_line[2])
            else:
                print("command ERROR")
        
        elif split_line[0]=="dir":
            print("directory "+split_line[1])
        
        else:
            print("size = "+split_line[0])
            print("filename = "+split_line[1])
            nested_set(filesystem,current_dir+[split_line[1]],int(split_line[0]))


print(filesystem)

total_size = 0
def sum_sizes(dic,total_size):
    for key in dic:
        # print(dic[key])
        if isinstance(dic[key], int):
            total_size = total_size + dic[key]
        else:
            total_size = sum_sizes(dic[key],total_size)
    return total_size

print(sum_sizes(filesystem,total_size=0))

limit = 100000

keys=[]
values=[]
def small_dirs(dic,total_size):
    
    for key in dic:
        if isinstance(dic[key], dict):
            print(key)
            print(dic[key])
            print(sum_sizes(dic[key],total_size=0))
            if sum_sizes(dic[key],total_size=0)<=limit:
                print("key added: "+key)
                keys.append(key)
                values.append(sum_sizes(dic[key],total_size=0))
                total_size = total_size+sum_sizes(dic[key],total_size=0)+small_dirs(dic[key],total_size)
            else:
                total_size = small_dirs(dic[key],total_size)
        else:
            total_size = total_size

    return total_size

print(small_dirs(filesystem,total_size=0))
print(keys)
print(values)

total=0
for value in values:
    total=total+value

print(total)    