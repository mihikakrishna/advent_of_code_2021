
def check_flash(matrix,r,c,flashed):
    if (r,c) not in flashed: 
        matrix[r][c] += 0 if (matrix[r][c] + 1 > 9)  else 1


def run_flashes(matrix):
    count = 0
    flashed = set()

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] += 1
            if matrix[r][c] > 9:
                count += 1
                matrix[r][c] = 0
                flashed.add((r,c))

                if r+1 < len(matrix):
                     check_flash(matrix,r+1,c,flashed)
                if r-1 >= 0:
                     check_flash(matrix,r-1,c,flashed) 
                if c+1 < len(matrix[0]):
                     check_flash(matrix,r,c+1,flashed)
                if c-1 >= 0:
                     check_flash(matrix,r,c-1,flashed)
                if r+1 < len(matrix) and c+1 < len(matrix[0]):
                     check_flash(matrix,r+1,c+1,flashed)
                if r-1 >= 0 and c+1 < len(matrix[0]):
                    check_flash(matrix,r-1,c+1,flashed)
                if r+1 < len(matrix) and c-1 >= 0:
                     check_flash(matrix,r+1,c-1,flashed)
                if r-1 >= 0 and c-1 >= 0:
                    check_flash(matrix,r-1,c-1,flashed)

    return count
    
def solution():
    f = open("day11/11.txt","r")
    f2 = open("day11/tmp.txt","w")
    matrix = []
    for line in f: 
        matrix.append(list(map(int, line.rstrip())))
    count = 0
    for i in range(10):
        count += run_flashes(matrix)
        for i in matrix: 
            f2.write(str(i))
            f2.write('\n')
        f2.write('\n')
    print(count)
    
solution()