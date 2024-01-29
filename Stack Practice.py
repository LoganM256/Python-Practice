from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
def reverse_string(string):
    stack = Stack()

    for letter in string:
        stack.push(letter)
    
    r_string = ''

    while len(stack) != 0:
        r_string += stack.pop()

    return r_string

def valid_parentheses(s):

    mapping = {'(':')', '[':']','{':'}'}
    stack = Stack()

    for item in s:
        if item in mapping:
            stack.push(item)
        elif item not in mapping.values():
            continue
        elif mapping[stack.pop()] != item:
            return False

    return stack.size() == 0

print(valid_parentheses("({a+b})"))