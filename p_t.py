def pascal_triangle(n):
    triangle = []  # make empty list

    for i in range(n):  # make cycle for pick elements from 0 to n
        row = [1]*(i+1)  # creates pyramyd through [1]
        for j in range(1, i):  # make double cycle for pick elements from 1 to i-1
            row[j] = triangle[i-1][j-1]+triangle[i-1][j]  # equals sum for 2 elements from prev row
        
        triangle.append(row)
    return triangle

def output_triangle(triangle):
    for row in triangle:
        print(''.join(map(str, row)).center(20))

n = 7
triangle = pascal_triangle(n)
print(triangle)
