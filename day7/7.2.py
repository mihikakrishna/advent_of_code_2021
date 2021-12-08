def fuel():
    f = open("day7/7.txt","r")
    pos = list(map(int,list(f.readline().rstrip().split(","))))
    minFuel = float('inf')
    for p in range(min(pos),max(pos)+1):
        tot = 0
        for i in pos:
            tot += int((abs(i-p)*(abs(i-p)+1))/2)
        if tot < minFuel : minFuel = tot
    print(minFuel)

fuel()