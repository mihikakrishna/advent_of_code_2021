def findInc():
    prev = float('inf')
    count = 0
    f = open("1.txt", "r")
    for line in f:
        count += (prev < int(line)) 
        prev = int(line)
    print(count)

findInc()