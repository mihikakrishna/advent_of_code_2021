from collections import deque

def valid_parentheses(str):
    open_parentheses = "([{<"
    close_parentheses = ")]}>"
    stack = deque()
    for c in str:
        if c in open_parentheses:
            stack.append(c)
        elif c in close_parentheses:
            p = stack.pop()
            if open_parentheses.index(p) != close_parentheses.index(c): return c
            else: continue

def parse():
    f = open("day10/10.txt","r")
    p_map = {None: 0, ")": 3, "]": 57, "}": 1197, ">": 25137}
    count = 0
    for line in f:
        count += p_map[valid_parentheses(line)]
    print(count)
parse()