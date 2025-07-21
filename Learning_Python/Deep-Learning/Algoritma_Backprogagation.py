import random
# Menggunakan library math, jika ingin menggunakan fungsi math.exp dari pada menggunakan pow()
import math

# PROSES PEMBELAJARAN (MENGHITUNG BOBOT)
# DALAM NEURAL NETWORK DISEBUT DENGAN ISTILAH TRAINING (PELATIHAN)
# ----------------------------------------------------------------
# Deklarasi neuron masukkan x1 dan neuron masukkan x2: [ x1, x2]
EKSPONESIAL = 2.7182

x = [
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0]
]

t = [0, 1, 1, 0] # neuron target t, studi kasus: AND, OR, AND NOT, XOR
b = 1

# inisilisasi bobot (weight) dan hidden - menggunakan fungsi random (boleh negatif)
v = [[random.uniform(-1, 1) for _ in range(3)] for _ in range(3)] # kolom pertama untuk bias, kolom kedua dan ketiga untuk x1 dan x2
w = [random.uniform(-1, 1) for _ in range(4)]

# Membuat array/list untuk menyimpan nilai delta_v, delta_w, teta_in, z, dan teta_hidden
delta_v: list[list[float]] = [[0] * 3 for _ in range(3)]
delta_w = [0] * 4
z = [0] * 3
teta_in = [0] * 3
teta_hidden = [0] * 3

print("\n----------------------------------------------------")
print("Bobot Awal/inisialisasi")
print("----------------------------------------------------")
for i in range(3):
    for j in range(3):
        print(f"v[{i}][{j}] = {v[i][j]:.3f}")
for j in range(4):
    print(f"w[{j}] = {w[j]:.3f}")

print("----------------------------------------------------")

# Langkah 1: Jika kondisi penghentian belum terpenuhi, lakukan langkah 2 sampai dengan 8
alpha = 0.8
max_iter = 10000
threshold_mse = 0.01
epoch = 0
loop = True

# Training
while epoch < max_iter and loop:
    t_error = 0
    # Langkah 2: Untuk setiap pasang data pelatihan, lakukan langkah 3 sampai dengan 8
    for d in range(4):
        # Langkah 3: Tiap unit masukkan menerima sinyal dan meneruskan ke unit tersembunyi
        # Langkah 4: Hitung keluaran unit tersembunyi (zj)
        for j in range(3):
            z_in = b * v[j][0]
            for i in range(2):
                z_in += x[d][i] * v[j][i + 1]
            # z[j] = 1 / (1 + math.exp(-z_in))
            z[j] = 1 / (1 + pow(EKSPONESIAL, -z_in))

        # Langkah 5: Hitung keluaran unit yk
        y_in = b * w[0]
        for j in range(3):
            y_in += z[j] * w[j + 1]
        # y = 1 / (1 + math.exp(-y_in))
        y = 1 / (1 + pow(EKSPONESIAL, -y_in))

        # *************************************************
        # hitung total error
        error = t[d] - y
        t_error += error ** 2
        # *************************************************

        # Langkah 6: Hitung faktor teta di unit keluaran yk
        teta = error * y * (1 - y)

        # Hitung perubahan bobot wkj (dengan alpha=0.2):
        delta_w[0] = alpha * teta * b
        for j in range(3):
            delta_w[j + 1] = alpha * teta * z[j]

        # Langkah 7: Hitung penjumlahan kesalahan dari unit tersembunyi (=teta)
        for j in range(3):
            teta_in[j] = teta * w[j + 1]

            # Faktor kesalahan d di unit tersembunyi:
            teta_hidden[j] = teta_in[j] * z[j] * (1 - z[j])

            # Hitung perubahan bobot ke unit tersembunyi (dengan alpha=0.2):
            delta_v[j][0] = alpha * teta_hidden[j] * b
            for i in range(2):
                delta_v[j][i + 1] = alpha * teta_hidden[j] * x[d][i]

        # Langkah 8: Hitung semua perubahan bobot

        # Perubahan bobot unit keluaran:
        for j in range(4):
            w[j] += delta_w[j]

        # Perubahan bobot unit tersembunyi:
        for j in range(3):
            for i in range(3):
                v[j][i] += delta_v[j][i]

    # ******************************
    # hitung Mean Square Errod (MSE)
    mse = t_error / 4
    if mse < threshold_mse:
        loop = False
    # ******************************
    epoch += 1

print("\n----------------------------------------------------")
print(f"Bobot setelah proses training sebanyak {epoch} iterasi")
print("----------------------------------------------------")
for i in range(3):
    for j in range(3):
        print(f"v[{i}][{j}] = {v[i][j]:.3f}")
for j in range(4):
    print(f"w[{j}] = {w[j]:.3f}")
print("----------------------------------------------------")

# Testing
# PROSES PENGUJIAN (MENGUJI APAKAH BOBOT SUDAH BENAR)
# DALAM NEURAL NETWORK DISEBUT DENGAN ISTILAH TESTING (PENGUJIAN)
# ---------------------------------------------------------------
print("\n\n---------------")
print("Proses Testing")
print("---------------")
print(" x1  x2   b   y")
print("---------------")
for d in range(4):
    for j in range(3):
        z_in = b * v[j][0]
        for i in range(2):
            z_in += x[d][i] * v[j][i + 1]
        # z[j] = 1 / (1 + math.exp(-z_in))
        z[j] = 1 / (1 + pow(EKSPONESIAL, -z_in))

    y_in = b * w[0]
    for j in range(3):
        y_in += z[j] * w[j + 1]
    # y = 1 / (1 + math.exp(-y_in))
    y = 1 / (1 + pow(EKSPONESIAL, -y_in))

    print(f"{x[d][0]:2.0f}  {x[d][1]:2.0f}   {b:2.0f}   {round(y):.0f}")
print("---------------")