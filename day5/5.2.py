def readInput():
    f = open("day5/5.txt","r")
    lines = []
    for line in f:
        lines.append(line.rstrip().split(" -> "))
        # x1, y1, x2, y2 = int(input[0][0]), int(input[0][2]), int(input[1][0]), int(input[1][2])
        # return (x1,y1), (x2,y2)
    return lines

def drawLines():
    input = readInput()
    lines = []
    cross = {}
    for inputLine in input:
 
        t1,t2 = eval(inputLine[0]), eval(inputLine[1])
  
        x1 = int(t1[0])
        x2 = int(t2[0])
        y1 = int(t1[1])
        y2 = int(t2[1])

        if (x1,y1) > (x2,y2):
            temp = (x2,y2)
            x2,y2 = x1,y1
            x1,y1 = temp

        points = []
        if x1 == x2: 
            for i in range(y1,y2+1): points.append((x1,i))
        elif y1 == y2: 
            for i in range(x1,x2+1): points.append((i,y1))
        elif (x2 - x1) == (y2 - y1):
            i,j = x1,y1
            while((i,j) != (x2,y2)):
                points.append((i,j))
                i+=1
                j+=1
            points.append((x2,y2))
        elif (x2 - x1) == -(y2 - y1):
            i,j = x1,y1
            while((i,j) != (x2,y2)):
                points.append((i,j))
                i+=1
                j-=1
            points.append((x2,y2))
        lines.append(points)
    for l in lines: 
        for p in l:
            if p in cross: cross[p] += 1
            else: cross[p] = 1  
    count = 0
    for p in cross: 
        if cross[p] >= 2: count += 1
    print(count)
drawLines()