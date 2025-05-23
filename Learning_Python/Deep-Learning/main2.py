x = [
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0]
]

# initialization bobot/weight
v = [[2, -1], [-1, 2]]
w = [2, 2]
# z1 = [[]]
# z2 = [[]]

z = []

print("x1 x2 z1 z2 y")
print("-------------")

for i in range(4):
    z1_in = 0
    z2_in = 0
    # y_in = 0
    for j in range(2):
        z1_in += x[i][j] * v[0][j]
        z2_in += x[i][j] * v[1][j]
        print(f"{x[i][j]} ", end=" ")

    if z1_in >= 2:
        z1 = 1
    else:
        z1 = 0

    if z2_in >= 2:
        z2 = 1
    else:
        z2 = 0

    z.append([z1,z2])

    print(f"{z1} ", end=" ")
    print(z2)

for a in range(4):
    y_in = 0
    for b in range(2):
        y_in += z[a][b] * w[b]

    if y_in >= 2:
        y = 1
    else:
        y = 0

    print(y)


print("-------------")
