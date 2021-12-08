def findDepth():
    f = open("2.txt", "r")
    x,y = 0,0
    for line in f:
        arr = line.split()
        dir,dist = arr[0], int(arr[1])
        if dir == "forward" : x += dist
        elif dir == "up" : y -= dist
        elif dir == "down": y += dist
    print(x*y)

findDepth()