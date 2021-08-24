import datetime
import time
from node import Node

MAX_SIZE = 4

def load_dictionary(dictionary_file):
    root = Node(None, False)
    t0 = time.clock()
    with open(dictionary_file, "r") as reader:
        line = reader.readline()
        while line != '':
            newRoot = root
            word = line.rstrip()
            for char in word[:-1]:
                curNode = newRoot.__add_child__(Node(char, False))
                newRoot = curNode
            newRoot.__add_child__(Node(word[-1], True))
            line = reader.readline()
    return root

def solve_helper(root, special_char, chars, cur_str, used_special_character, writer):
    # boundary condition hitting a leaf
    if not root.childset:
        if used_special_character and len(cur_str) > MAX_SIZE:
            writer.write(cur_str + "\n")
        return
    # another condition
    if root.is_word_end and used_special_character and len(cur_str) > MAX_SIZE:
        writer.write(cur_str + "\n")
    
    for child_value, child_node in root.childset.items():
        if child_value in chars:
            solve_helper(
                child_node,
                special_char,
                chars,
                cur_str + child_value,
                used_special_character or child_value == special_char,
                writer) 

def solve(special_char, chars):
    ct = datetime.datetime.now()

    t0 = time.clock()
    
    print("*** commencing dictionary loading")
    
    root = load_dictionary('/usr/share/dict/words')
    
    t1 = time.clock()
    delta = str(t1 - t0)
    
    print("*** dictionary loading completed in " + delta + "seconds")
    print("*** Starting Solver")
    
    writer = open(str(ct) + ".txt", "w")
    solve_helper(root, special_char, chars, '', False, writer)
    writer.close()
    
    t2 = time.clock()
    delta = str(t2 - t1)
    
    print("**** Solved in " + delta + "seconds")
