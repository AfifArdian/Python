import random
import math

x = [
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0]
]
t = [0, 1, 1, 0]
b = 1

# Inisialisasi bobot secara acak antara -1 dan 1
v = [[random.uniform(-1, 1) for _ in range(3)] for _ in range(3)]
w = [random.uniform(-1, 1) for _ in range(4)]

dv = [[0] * 3 for _ in range(3)]
dw = [0] * 4
z = [0] * 3
teta_in = [0] * 3
teta_h = [0] * 3

alpha = 0.8
max_iter = 1000
threshold_mse = 0.01
k = 0
ulang = True

print("Bobot Awal/inisialisasi\n")
for i in range(3):
    for j in range(3):
        print(f"v[{i}][{j}] = {v[i][j]:.3f}")
for j in range(4):
    print(f"w[{j}] = {w[j]:.3f}")

# Training
while k < max_iter and ulang:
    t_error = 0

    for d in range(4):
        for j in range(3):
            z_in = b * v[j][0]
            for i in range(2):
                z_in += x[d][i] * v[j][i + 1]
            z[j] = 1 / (1 + math.exp(-z_in))

        y_in = b * w[0]
        for j in range(3):
            y_in += z[j] * w[j + 1]
        y = 1 / (1 + math.exp(-y_in))

        error = t[d] - y
        t_error += error ** 2

        teta = error * y * (1 - y)

        dw[0] = alpha * teta * b
        for j in range(3):
            dw[j + 1] = alpha * teta * z[j]

        for j in range(3):
            teta_in[j] = teta * w[j + 1]
            teta_h[j] = teta_in[j] * z[j] * (1 - z[j])
            dv[j][0] = alpha * teta_h[j] * b
            for i in range(2):
                dv[j][i + 1] = alpha * teta_h[j] * x[d][i]

        for j in range(4):
            w[j] += dw[j]
        for j in range(3):
            for i in range(3):
                v[j][i] += dv[j][i]

    mse = t_error / 4
    if mse < threshold_mse:
        ulang = False
    k += 1

print(f"\n\nBobot setelah proses training sebanyak {k} iterasi\n")
for i in range(3):
    for j in range(3):
        print(f"v[{i}][{j}] = {v[i][j]:.3f}")
for j in range(4):
    print(f"w[{j}] = {w[j]:.3f}")

# Testing
print("\n\nProses Testing\n")
print("x1  x2   b   y")
print("--------------------")
for d in range(4):
    for j in range(3):
        z_in = b * v[j][0]
        for i in range(2):
            z_in += x[d][i] * v[j][i + 1]
        z[j] = 1 / (1 + math.exp(-z_in))

    y_in = b * w[0]
    for j in range(3):
        y_in += z[j] * w[j + 1]
    y = 1 / (1 + math.exp(-y_in))

    print(f"{x[d][0]:2.0f} {x[d][1]:2.0f}   {b:2.0f}   {round(y):.0f}")
print("--------------------")