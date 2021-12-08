def o2(d, o2_rate, cols, lines):
    for i in range(cols):
        if d.count('1') >= d.count('0'): 
            o2_rate += '1'
            for idx,j in enumerate(lines):
                if len(j) ==  0: continue 
                if j[i] == '0' : lines[idx] = ""
        else: 
            o2_rate += '0'
            for idx,j in enumerate(lines):
                if len(j) ==  0: continue 
                if j[i] == '1' : lines[idx] = ""
        
        d = ""
        for line in lines:
            if i+1 < cols-1 and line != "" : d += line[i+1]
    return o2_rate

def co2(d, co2_rate, cols, lines):
    for i in range(cols):
        if d.count('1') >= d.count('0'):
            co2_rate += '0'
            for idx,j in enumerate(lines):
                if len(j) ==  0: continue 
                if j[i] == '1' : lines[idx] = "" 
        else:
            co2_rate += '1'
            for idx,j in enumerate(lines):
                if len(j) ==  0: continue 
                if j[i] == '0' : lines[idx] = ""
        if lines.count("") == len(lines)-1 : 
            for i in lines: 
                if i != "" : return i
        d = ""
        for line in lines:
            if i+1 < cols-1 and line != "" : d += line[i+1]

def inputParser():
    file = open("day3/3.txt", "r")

    lines = []
    for line in file:
        stripped_line = line.strip()
        lines.append(stripped_line)
    file.close()

    d = ""
    for line in lines:
        d += line[0]
    return lines, d

def Binary_Diagnostic2():
    lines, d = inputParser()
    cols = len(lines[0])
    o2_rate = o2(d,"",cols,lines)
    lines, d = inputParser()
    file = open("3.txt", "r")
    co2_rate = co2(d,"", cols, lines)

    o2_rate = int(o2_rate, 2)
    print("O2_rate",o2_rate)
    co2_rate = int(co2_rate, 2)
    print("CO2_rate",co2_rate)
    print("Result", o2_rate * co2_rate)

Binary_Diagnostic2()

