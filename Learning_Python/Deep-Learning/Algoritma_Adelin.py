import random

x1 = [1, 1, 0, 0]
x1_float = [float(i) for i in x1]
x2 = [1, 0, 1, 0]
x2_float = [float(i) for i in x2]
b = float(1)
t = [1, -1, -1, -1]
t_float = [float(i) for i in t]

# 1. Inisialisasi
# a. Semua bobot diberi harga Ɛ, dimana (Ɛ>0; bilangan positif kecil sebarang)
w1= 1
w2= 1
wb= 1

# b. Laju pembelajaran/learning rate (α)
# 0 < α <= 1 (untuk kemudahan, α dapat diberikan nilai 1)
alpha = 0.01

max_iteration = 1000
iteration = 0
treshold = 1e-5

delta_total = float('inf')

while iteration < max_iteration and delta_total > treshold:
    for i in range(4):
        # Hitung y_in
        y_in = x1_float[i] * w1 + x2_float[i] * w2 + b * wb

        # Hitung perubahan bobot (delta w)
        dw1 = alpha * (t[i] - y_in) * x1_float[i]
        dw2 = alpha * (t[i] - y_in) * x2_float[i]
        dwb = alpha * (t[i] - y_in) * b

        # Akumulasi perubahan bobot
        delta_total += abs(dw1) + abs(dw2) + abs(dwb)

        # Perbaharui nilai bobot (w)
        w1 += dw1
        w2 += dw2
        wb += dwb

    iteration += 1
    print(f"Iterasi {iteration}: w1={w1:.4f}, w2={w2:.4f}, wb={wb:.4f}, delta_total={delta_total:.6f}")

print("\nPelatihan selesai.")
print(f"Bobot akhir: w1={round(w1)}, w2={round(w2)}, wb={wb:.4f}")


# Proses Testing
print("\n\nTesting")
print("--------------------")
print("x1  x2  b  y_in  y")
print("--------------------")

y_in = 0
bias_int = []
y_in_int = []
for i in range(4):
    y_in = (x1_float[i] * w1) + (x2_float[i] * w2) + (b * wb)
    bias_int.append(int(b))
    y_in_int.append(int(y_in))

    if y_in >= 0:
        y = 1
    else:
        y = -1

    print(f"{x1[i]}\t{x2[i]}\t{bias_int[i]}\t{y_in_int[i]}\t{y}")
print("--------------------")