def segment_search():
    f = open("day8/8.txt","r")
    count = 0
    for line in f:
        input = line.rstrip().split("|")[1].split()
        for str in input:
            if len(str) == 2 or len(str) == 4 or len(str) == 3 or len(str) == 7:
                count += 1
    print(count)

segment_search()