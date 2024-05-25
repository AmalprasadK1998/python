
"1.Matrix creation!"



r = int(input("Enter the number of rows:"))

c = int(input("Enter the number of columns:"))




y = []

for i in range(r):
    z = []
    for j in range(c):
        x = int(input("Enter the element:"))
        z.append(x)
    y.append(z)


print(f"Row vector:{y}")





m = []

for i in range(c):
    z = []
    for j in range(r):
        z.append(y[j][i])

    m.append(z)

print(f"Transpose of row vector(column vector):{m}")

# List comprehension of transpose

transpose = [[y[j][i] for j in range(r)]for i in range(c)]
print(f'transpose:{transpose}')



"Little bit optimal way for a square matrix!"

"""if r == c:
    for i in range(r):
        for j in range(i + 1):
            if y[i] != y[j]:
                y[i][j], y[j][i] = y[j][i], y[i][j]

    print(f"Transpose of row vector(column vector):{y}")"""




# sum of matrices

sum = []
for i in range(len(m)):
    z = []
    for j in range(len(y)):
        x = y[i][j] + m[i][j]
        print(x,end='\t')
        z.append(x)
    sum.append(z)
    print()

print(f'sum:{sum}')

# multiplication of two matrices


c = []
for i in range(len(m)):
    z = []
    for j in range(len(y[0])):
        result = 0
        for k in range(len(y)):
            result += m[i][k] * y[k][j]
        z.append(result)
        print(result, end='\t')

    c.append(z)
    print()

print(f'product (m*y):{c}')
