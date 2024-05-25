my_dict = {'one':[1,2,3],
           'two':[4,5,6]
}

for value in my_dict.values():
    print(max(value))

l = ['amal','akhil','basil','jerin','akshay']
lc = [l[i] for i in range(len(l)) if l[i][0]=='a']
print(lc)

# multiplication of two matrices

n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

m = [[1,4,7],
     [2,5,8],
     [3,6,9]]

product = []
for i in range(len(m)):
    z = []
    for j in range(len(n[0])):
        result = 0
        for k in range(len(n)):
            result += m[i][k]*n[k][j]
        z.append(result)
        print(f'{result}',end='\t')

    product.append(z)
    print()


print(f'product(m*n):{product}')


sum = []
for i in range(len(m)):
    z = []
    for j in range(len(n)):
        x = n[i][j] + m[i][j]
        print(x,end='\t')
        z.append(x)
    sum.append(z)
    print()

print(f'sum(m+n):{sum}')


a = [[1,2],[3,4]]

def Minor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def det(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c) * m[0][c] * det(Minor(m, 0, c))
    return determinant


i = [[1,2,5],[2,4,10],[3,23,1]]
print(det(i))
print(det(m))

# dot product
m = [1,2,3]
n = [5,6,7]
l = []
for i in range(len(m)):
    for j in range(len(n)):
        if i == j:
            l.append(m[i]*n[j])

print(l)

