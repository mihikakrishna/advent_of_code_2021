def findInc():
    prev = float('inf')
    count = 0
    f = open("day1/temp.txt", "r")
    for line in f:
        count += (prev < int(line)) 
        prev = int(line)
    print(count)

def slidingWindowSums():
    inputLines = []
    prevSums = {}
    total = 0
    with open("day1/1.txt") as file:
        inputLines = file.read().split()
    f = open("day1/temp.txt", "w")
    i = 1
    prevSums[0] = int(inputLines[0]) + int(inputLines[1])  + int(inputLines[2])
    f.write(str(prevSums[0])+'\n')
    while(i < len(inputLines)-2):
        prevSums[i] = prevSums[i-1] - int(inputLines[i-1]) + int(inputLines[i+2])
        f.write(str(prevSums[i])+'\n')
        i+=1

slidingWindowSums()
findInc()