import datetime
import time
from classes.spellingbee.dict_loader import load_dictionary, MAX_SIZE

def solve_helper(root, special_char, chars, cur_str, used_special_character, writer):
    # boundary condition hitting a leaf
    if not root.childset:
        if used_special_character and len(cur_str) >= MAX_SIZE:
            writer.write(cur_str + "\n")
        return
    # another condition
    if root.is_word_end and used_special_character and len(cur_str) >= MAX_SIZE:
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

def solve(chars):
    ct = datetime.datetime.now()

    t0 = time.perf_counter()
    
    print("*** commencing dictionary loading")
    root = load_dictionary()
    
    t1 = time.perf_counter()
    delta = str(t1 - t0)
    
    print("*** dictionary loading completed in " + delta + "seconds")
    print("*** Starting Solver")
    
    writer = open("solutions/" + str(ct) + "_" + chars +".txt", "w")
    special_char = chars[0]
    solve_helper(root, special_char, chars, '', False, writer)
    writer.close()
    
    t2 = time.perf_counter()
    delta = str(t2 - t1)
    
    print("**** Solved in " + delta + "seconds")
