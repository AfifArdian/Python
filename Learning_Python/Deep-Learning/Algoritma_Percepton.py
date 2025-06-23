# Proses Training
x1 = [1, 1, 0, 0]
x1_float = [float(i) for i in x1]
x2 = [1, 0, 1, 0]
x2_float = [float(i) for i in x2]
b = float(1)
t = [1, -1, -1, -1]
t_float = [float(i) for i in t]

# 1. Inisialisasi
# a. Semua bobot diberi harga 0.
w1=0
w2=0
wb=0
# b. Laju pembelajaran/learning rate (alpha)
# 0 < α <= 1 (untuk kemudahan, α dapat diberikan nilai 1)
alpha = 1
treshold = float(0.2)

looping = True
# 2. Diulang/loop, selama semua perubahan bobot tidak nol – perulangan luar
while looping:
# for j in range(11):
    change = False
    for i in range(4):
        y_in=x1_float[i]*w1+x2_float[i]*w2+b*wb
        if y_in > treshold:
            y = 1
        elif y_in >= -treshold and y_in <= treshold:
            y = 0
        else:
            y = -1

        if y != t_float[i]:
            dw1 = alpha * x1_float[i] * t_float[i]
            dw2 = alpha * x2_float[i] * t_float[i]
            dwb = alpha * b * t_float[i]
            change = True
        else:
            dw1 = 0
            dw2 = 0
            dwb = 0

        w1 += dw1
        w2 += dw2
        wb += dwb

        if not change:
            looping = False

print("Hasil Training")
print(f"w1 = {w1}\nw2 = {w2}\nwb = {wb}")

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