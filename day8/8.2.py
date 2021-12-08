import string

def decode_pattern(str):
    input = "".join(str)
    signals = dict(zip(string.ascii_lowercase, [0]*8))

    #  segment layout:

    # 1111   
    # 2  3
    # 2  3
    # 4444   
    # 5  6      
    # 5  6
    # 7777

# a: 8, b: 6, c: 8, d: 7, e: 4, f: 9, g: 7


    # decode each segment individually
    
    for c in input:
        if input.count(c) == 4: 
            signals['e'] = c
        elif input.count(c) == 6:
            signals['b'] = c
        elif input.count(c) == 9:
            signals['f'] = c

    for s in sorted(str, key=len):
        if len(s) == 2:
            signals['c'] = s.replace(signals['f'],"")
            
        elif len(s) == 3:
            signals['a'] = s.replace(signals['f'],"").replace(signals['c'],"")
        
        elif len(s) == 4:
            signals['d'] = s.replace(signals['b'],"").replace(signals['c'],"").replace(signals['f'],"")
            
        elif len(s) == 7:
            signals['g'] = s.replace(signals['a'],"").replace(signals['b'],"").replace(signals['c'],"").replace(signals['d'],"").replace(signals['e'],"").replace(signals['f'],"")

    
    return signals

def map_displays(str):
    signals = decode_pattern(str)

    # default encoding
    displays = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
    
    for i,s in enumerate(displays):
        res = ""
        for c in s:
            res += signals.get(c,c)
        res = ''.join(sorted(res))   
        displays[i] = res
    return displays
    
def decode_nums(str,displays):
    count = []
    for s in str:
        temp = ''.join(sorted(s)) 
        for i in range(len(displays)):
            if displays[i] == temp: count.append(i)
    return count
        

def segment_search():
    f = open("day8/8.txt","r")
    count = 0
    for line in f:
        in1,in2 = line.rstrip().split("|")
        res = decode_nums(in2.split(),map_displays(in1.split()))
        count += int("".join([str(i) for i in res]))
    print(count)
        

segment_search()
