def sim():
    f = open("6.txt","r")
    states = list(map(int,list(f.readline().rstrip().split(","))))

    i = 0
    while(i<80):
        j = 0
        while(j<len(states)):
            if states[j] == 0: 
                states[j] = 6
                states.append(9)
            else: states[j] -= 1
            j += 1
        i += 1

    print(len(states))
    

sim()