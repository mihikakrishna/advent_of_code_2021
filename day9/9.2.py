def is_low_point(matrix,r,c):
    if r < len(matrix) - 1 and matrix[r][c] >= matrix[r+1][c] : return False
    if r > 0  and matrix[r][c] >= matrix[r-1][c] : return False
    if  c > 0 and matrix[r][c] >= matrix[r][c-1] : return False
    if  c < len(matrix[0]) - 1 and matrix[r][c] >= matrix[r][c+1] : return False
    return True

def dfs(matrix, r, c, visited):
    basin=1
    if int(matrix[r][c]) == 9:
        return 0
    if (r,c) in visited: return 0
    else: visited.add((r,c))
    
    if r < len(matrix) - 1 and int(matrix[r+1][c]) > int(matrix[r][c]) :
        basin += dfs(matrix,r+1,c,visited)
    if r > 0  and int(matrix[r-1][c]) > int(matrix[r][c]) :
        basin += dfs(matrix,r-1,c,visited)
    if  c > 0 and int(matrix[r][c-1]) > int(matrix[r][c]):
        basin += dfs(matrix,r,c-1,visited)
    if  c < len(matrix[0]) - 1 and int(matrix[r][c+1]) > int(matrix[r][c]) :
        basin += dfs(matrix,r,c+1,visited)
    return basin

def find_basins():
    f = open("day9/9.txt","r")
    matrix = []
    basins = []
    low_points = []

    for line in f:
        s = ''.join(x for x in line.rstrip() if x.isdigit())
        matrix.append(s)
    
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):  
            if is_low_point(matrix,r,c): low_points.append((r,c))
    
    for r,c in low_points:
        visited = set()
        basins.append(dfs(matrix,r,c,visited))
        
    basins.sort(reverse=True)
    print(basins[0]*basins[1]*basins[2])

find_basins()