import json
from classes.spellingbee.node import Node

MAX_SIZE = 4
dicts = {'words.json' : '/usr/share/dict/words', 'words_alpha.json' : 'dicts/words_alpha.txt'}

def generate_dictionary(dictionary_file):
    root = Node(None, False)
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

def load_dictionary():
    with open('data/words_alpha.json', 'r') as openfile:
        data = json.load(openfile)
    
if __name__ == '__main__':
    for key,value in dicts.items():
        root = generate_dictionary(value)
        data = json.dumps(root.__encode__())
        with open(f'data/{key}', 'w') as outfile:
            outfile.write(data)
    