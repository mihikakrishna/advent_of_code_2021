def fold(fold_axis,fold_val):
    d = fold_val - fold_axis
    if d > 0:
        return fold_val - d * 2
    else: return -1

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

def solution():
    matrix,points,folds = parse_input()
    new_matrix = matrix
    for point in points:
        x,y = point
        new_x,new_y = x,y
        for fold_instruction in folds:
            axis, pos = fold_instruction[0],int(fold_instruction[2:])
            if axis == "y":
                new_matrix = new_matrix[:pos]

                temp_new_y = fold(pos, new_y)
                if temp_new_y == -1:
                    continue
                else:
                    new_y = temp_new_y
            elif axis == "x":
                for i, row in enumerate(new_matrix):
                    new_matrix[i] = row[:pos]

            temp_new_x = fold(pos, new_x)
            if temp_new_x == -1:
                continue
            else:
                new_x = temp_new_x
    new_matrix[new_y][new_x] = "#"

    for i in new_matrix: print("".join(i))

solution()