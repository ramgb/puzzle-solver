import time
from node import Node

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

def solve_helper(root, special_char, chars, cur_str, used_special_character):
    # boundary condition hitting a leaf
    if not root.childset:
        if used_special_character:
            print(cur_str)
        return
    # another condition
    if root.is_word_end and used_special_character:
        print(cur_str)
    
    for child_value, child_node in root.childset.items():
        if child_value in chars:
            solve_helper(child_node, special_char, chars, cur_str + child_value, used_special_character or child_value == special_char) 

def solve(special_char, chars):
    t0 = time.clock()
    #print("commencing dictionary loading")
    
    root = load_dictionary('/usr/share/dict/words')
    
    t1 = time.clock()
    delta = str(t1 - t0)
    #print("dictionary loading completed in " + delta + "seconds")
    #print("Starting Solver")
    
    solve_helper(root, special_char, chars, '', False)
    
    t2 = time.clock()
    delta = str(t2 - t1)
    #print("Solved in " + delta + "seconds")
