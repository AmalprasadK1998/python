

x = [[0]*3] * 4

print(x)
x[0][0] = 2
print(x)

x = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

print(x)
x[0][0] = 2
print(x)

l = [[0,0,0],
     [0,0,0],
     [0,0,0]]

size = 3
l = [[0 for i in range(size)] for j in range(size)]
print(f'l = {l}')

l = [[1 if i == j else l[i][j] for j in range(len(l))] for i in range(len(l))]
print(f"comprehended l = {l}")


"The other way of doing the above list comprehension of creating an identity matrix from null matrix"

"""for i in range(len(l)):
    for j in range(len(l)):
        if i == j:
            l[i][j] = 1"""


l = [[3*l[i][j]  for i in range(size)] for j in range(size)]

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

sum = [[l[i][j] + x[i][j] for j in range(len(l[0]))]for i in range(len(x))]

print(f'sum : {sum}')

print(f'x[0]:{x[0]}')
print(l)
