# Translation

y = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

z = [[5 if i == j else 0 for j in range(len(y[0]))] for i in range(len(y))]

print(f'y:{y}')
print(f'z:{z}')

x = [[5 if j == 0 else 0 for j in range(len(y[0]))] for i in range(len(y))]
print(f'x:{x}')
trans_matrix = [[y[i][j] + x[i][j] for j in range(len(x[0]))] for i in range(len(x))]
print(f'Translated matrix(x+y):{trans_matrix}')

trans_matrix = [[y[i][j] + z[i][j] for j in range(len(z[0]))] for i in range(len(z))]
print(f'translated matrix(y+z):{trans_matrix}')

a = [[2, -1],
     [4, 3],
     [-3, -2]]
b = [[-5 if j == 0 else 2 for j in range(len(a[0]))] for i in range(len(a))]

print(f'a:{a}')
print(f'b:{b}')

Translated_matrix = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

print(f'Translated matrix(a+b):{Translated_matrix}')

# rotation

# 90 degree rotation of vectors in m using vectors in l
# Here l is the matrix of transformation i.e, l gets applied on m (l*m)
# row vectors
m = [[1, 2],
     [0, 0]]

l = [[0,-1],
     [1,0]]


# printing in  Matrix format
for i in range(len(l)):
    for j in range(len(l[0])):
        print(l[i][j], end='  ')
    print()


def rotation(l,m):
    rotate = [[sum(l[i][k] * m[k][j] for k in range(len(m))) for j in range(len(m[0]))] for i in range(len(l))]
    return rotate



print(f'l:{l}')
print(f'm:{m}')
times = 0

# 90 degree rotation
rotation_1 = rotation(l,m)

# 180 degree rotation(90 + 90)
rotation_2 = rotation(l,rotation_1)

print(f'rotation_1:{rotation_1}')
print(f'rotation_2:{rotation_2}')



l_transpose = [[l[j][i] for j in range(len(l[0]))]for i in range(len(l))]
m_transpose = [[m[j][i] for j in range(len(m[0]))]for i in range(len(m))]
rotation_1_transpose = [[rotation_1[j][i] for j in range(len(rotation_1[0]))]for i in range(len(rotation_1))]

rotation_2_transpose = [[rotation_2[j][i] for j in range(len(rotation_2[0]))]for i in range(len(rotation_2))]

print()

print(f'l_transpose:{l_transpose}')
print(f'm_transpose:{m_transpose}')
print(f'rotation_1_transpose:{rotation_1_transpose}')

print(f'rotation_2_transpose:{rotation_2_transpose}')



m = [[1,2,3],[4,5,6],[7,8,9]]
m[0],m[2] = m[2],m[0]
print(m)

m = [[m[j][i] for j in range(len(m[0]))]for i in range(len(m))]
print(m)
