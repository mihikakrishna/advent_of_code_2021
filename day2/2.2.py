def findDepth():
    f = open("day2/2.txt", "r")
    x,y,aim = 0,0,0
    
    for line in f:
        arr = line.split()
        dir,dist = arr[0], int(arr[1])
        if dir == "forward" : 
            x += dist
            y += aim * dist
        elif dir == "up" : aim -= dist
        elif dir == "down": aim += dist
    print(x*y)

findDepth()