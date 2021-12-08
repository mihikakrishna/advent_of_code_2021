def sim():
    f = open("6.txt","r")
    states = list(map(int,list(f.readline().rstrip().split(","))))
    counts = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

    for s in states:
        counts[s] += 1

    for i in range(256):
        newFish = counts[0]
        for j in range(8):
            counts[j] = counts[j+1]
        counts[6] += newFish
        counts[8] = newFish 

    print(sum(counts.values()))
    

sim()