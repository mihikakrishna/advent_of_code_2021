def fuel():
    f = open("7.txt","r")
    pos = list(map(int,list(f.readline().rstrip().split(","))))
    minFuel = float('inf')
    for p in range(min(pos),max(pos)+1):
        tot = 0
        for i in pos:
            tot += abs(i-p)
        if tot < minFuel : minFuel = tot
    print(minFuel)

fuel()