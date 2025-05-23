x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]
b = 1
t = [1, -1, -1, -1] # You can change to AND, OR, AND NOT

# 1. Initialize weights, all weights are assigned a value of 0.

w1= 0
w2= 0
wb= 0


print("Training")
print("-------------------------------------")
print("x1  x2  b   t  dw1  dw2 dwb w1  w2 wb")
print("-------------------------------------")

# 2. For each pair of input vectors and output targets (repeated/looped as many times as
# number of pairs of input and target data

for i in range(4):

    # a. Calculate the change in weight (delta w)
    dw1 = x1[i] * t[i]
    dw2 = x2[i] * t[i]
    dwb = b * t[i]

    # b. Update the weight value (w)
    w1 += dw1
    w2 += dw2
    wb += dwb

    # print details
    print(f"{x1[i]}\t{x2[i]}\t{b}\t{t[i]}\t{dw1}\t{dw2}\t{dwb}\t{w1}\t{w2}  {wb}")

print("-------------------------------------")

print("\n\nTesting")
print("----------------")
print("x1  x2  b  y_in y")
print("------------------")

y_in = 0
for i in range(4):
    y_in = x1[i] * w1 + x2[i] * w2 + b * wb

    if y_in >= 0:
        y = 1
    else:
        y = -1

    print(f"{x1[i]}\t{x2[i]}\t{b}\t{y_in}\t{y}")

print("------------------")
