def Binary_Diagnostic():
    d = {}
    
    f = open("3.txt", "r")
    for i in range(12): d[i] = ""
    for line in f:
        for i in range(12):
            d[i] += line[i]
    
    gammaRate = ""
    for i in range(len(d)):
        if d[i].count('1') > d[i].count('0'): gammaRate += '1'
        else: gammaRate += '0'
    gammaRate = int(gammaRate, 2)
    epsilonRate = gammaRate ^  int('1'*12, 2)
    print(gammaRate * epsilonRate)
    
Binary_Diagnostic()