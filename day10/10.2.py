from collections import deque

def inc_parentheses(str):
    open_parentheses = "([{<"
    close_parentheses = ")]}>"
    stack = deque()
    for c in str:
        if c in open_parentheses:
            stack.append(c)
        elif c in close_parentheses:
            p = stack.pop()
            if open_parentheses.index(p) != close_parentheses.index(c): return '0'
    str = "".join(stack)[::-1]
    ret = ""
    for i in range(len(str)):
        ret += close_parentheses[open_parentheses.index(str[i])]
    return(ret)

def parse():
    f = open("day10/10.txt","r")
    p_map = {"0": 0, ")": 1, "]": 2, "}": 3, ">": 4}
    total = []
    for line in f:
        count = 0
        str = inc_parentheses(line)
        for c in str: count = 5*count + p_map[c]
        total.append(count)
        
    while 0 in total: total.remove(0)
    total.sort()
    print(total[len(total)//2])
parse()