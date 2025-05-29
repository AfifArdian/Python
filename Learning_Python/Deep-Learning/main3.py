x = [[1, 1],
     [1, 0],
     [0, 1],
     [0, 0]]

v = [[2, -1],
     [-1, 2]]

w = [2, 2]

for i in range(4):
    y_in = 0
    for j in range(2):
        z_in = 0
        for k in range(2):
            z_in += x[i][k] * v[k][j]
        if z_in >= 2:
            z = 1
        else:
            z = 0

        y_in += z * w[j]

    if y_in >= 2:
        y = 1
    else:
        y = 0

    print(y)
