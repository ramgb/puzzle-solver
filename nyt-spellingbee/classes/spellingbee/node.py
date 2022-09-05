class Node:
    
    def __init__(self, value, is_word_end):
        self.value = value
        self.childset = {}
        self.is_word_end = is_word_end
        
    def __add_child__(self, child):
        if child.value not in self.childset:
            self.childset[child.value] = child
        self.childset[child.value].__update_word_end__(child.is_word_end)
        return self.childset[child.value]
    
    def __update_word_end__(self, child_word_end):
        self.is_word_end = self.is_word_end or child_word_end
