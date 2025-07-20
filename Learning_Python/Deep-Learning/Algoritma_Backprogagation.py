# Data XOR
x1 = [1, 1, 0, 0]
x2 = [1, 0, 1, 0]
t = [0, 1, 1, 0]  # XOR target

# Konversi ke float
x1 = [float(i) for i in x1]
x2 = [float(i) for i in x2]
t = [float(i) for i in t]
b = 1.0
alpha = 0.2
EXPONENTIAL = 2.7182
threshold = 0.01

# Inisialisasi bobot (input to hidden)
# Format: v[input][neuron_hidden]
v = [
    [-0.3, 0.3, 0.3],  # bias to z1, z2, z3
    [0.2, 0.3, -0.1],  # x1 to z1, z2, z3
    [0.3, 0.1, -0.1]  # x2 to z1, z2, z3
]

# Inisialisasi bobot (hidden to output)
# Format: w[neuron_hidden + bias]
w = [-0.1, 0.5, -0.3, -0.4]  # bias, z1, z2, z3

# Training
max_iter = 200
epoch = 0

while epoch < max_iter:
    total_error = 0
    print(f"\nEpoch {epoch + 1}")
    print("Forward Propagation")
    print("---------------------------------------")
    print("x1  x2  b   y_in    y")

    for i in range(4):
        # --- FORWARD PASS ---
        # Hitung z_in dan z
        z_in = []
        z = []
        for j in range(3):  # untuk z1, z2, z3
            zin = b * v[0][j] + x1[i] * v[1][j] + x2[i] * v[2][j]
            z_in.append(zin)
            z.append(1 / (1 + pow(EXPONENTIAL, -zin)))

        # Hitung y_in dan y (output)
        y_in = b * w[0] + sum(z[j] * w[j + 1] for j in range(3))
        y = 1 / (1 + pow(EXPONENTIAL, -y_in))

        print(f"{round(x1[i])}   {round(x2[i])}   {round(b)}   {round(y_in, 2)}   {round(y, 2)}")

        # --- BACKWARD PASS ---
        # Output layer delta
        teta = (t[i] - y) * y * (1 - y)

        # Update bobot output layer
        w[0] += alpha * teta * b
        for j in range(3):
            w[j + 1] += alpha * teta * z[j]

        # Hidden layer delta dan update bobot
        for j in range(3):
            teta_in = teta * w[j + 1]
            teta_hidden = teta_in * z[j] * (1 - z[j])

            # Update bobot v[input][j]
            v[0][j] += alpha * teta_hidden * b  # bias
            v[1][j] += alpha * teta_hidden * x1[i]  # x1
            v[2][j] += alpha * teta_hidden * x2[i]  # x2


    epoch += 1
    print("---------------------------------------\n")



