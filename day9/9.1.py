def is_low_point(matrix,r,c):
    if r < len(matrix) - 1 and matrix[r][c] >= matrix[r+1][c] : return False
    if r > 0  and matrix[r][c] >= matrix[r-1][c] : return False
    if  c > 0 and matrix[r][c] >= matrix[r][c-1] : return False
    if  c < len(matrix[0]) - 1 and matrix[r][c] >= matrix[r][c+1] : return False
    return True

def smoke_basin():
    f = open("day9/9.txt","r")
    matrix = []
    for line in f:
        s = ''.join(x for x in line.rstrip() if x.isdigit())
        matrix.append(s)
    low_points = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):  
            if is_low_point(matrix,r,c):low_points.append(matrix[r][c])
    for i in range(len(low_points)): 
        num = int(low_points[i])
        low_points[i] = num + 1
    print(sum(low_points))
smoke_basin()