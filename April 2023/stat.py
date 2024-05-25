x = [1,4,9,12,23]
y = [1,2,3,4,5]

x_mean = sum(x for x in x)/len(x)
print(x_mean)

y_mean = sum(y for y in y)/len(y)

print(y_mean)

x_diff = []
for x in x:
    x_diff.append(round(x-x_mean,2))

y_diff = []
for y in y:
    y_diff.append(round(y-y_mean,2))



print(x_diff,y_diff)

product = []
for x in x_diff:
    for y in y_diff:
        product.append(round(x*y,2))
        break
print(product)

s = 0
for i in product:
    s += round(i,2)
    print(s/4)
