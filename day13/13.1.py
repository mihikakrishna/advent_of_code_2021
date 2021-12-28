
def parse_input():
    f = open("day13/13.txt","r")
    points = []
    folds = []
    for line in f:
        if "," in line:
            x,y = int(line.rstrip().split(",")[0]),int(line.rstrip().split(",")[1])
            points.append((x,y))

        elif "fold" in line:
            folds.append(line.split()[2])
    

    maxX = float("-inf")
    maxY = float("-inf")

    for p in points:
        if p[0] > maxX: maxX = p[0]
        if p[1] > maxY: maxY = p[1]
    
    matrix = [["."] * (maxX+1) for row in range(maxY+1)]
    
    
    for p in points:
        x,y = p
        matrix[y][x] = "#"

    return matrix,points,folds

def fold(fold_axis,fold_val):
    d = fold_val - fold_axis
    if d > 0:
        return fold_val - d * 2
    else: return -1

def solution():
    matrix,points,folds = parse_input()
    new_matrix = matrix
    fold_axis = folds[0][0]
    fold_val = int(folds[0][2])
    if fold_axis == "y":
        for point in points:
            x,y = point
            new_val = fold(y,fold_val)
            if new_val == -1:
                continue
            new_matrix[y][x] = "."
            new_matrix[new_val][x] = "#"
    elif fold_axis == "x":
        for point in points:
            x,y = point
            new_val = fold(x,fold_val)
            if new_val == -1:
                continue
            new_matrix[y][x] = "."
            new_matrix[y][new_val] = "#"
    count = 0
    for i in new_matrix: count += i.count("#")
    print(count)

solution()

   
