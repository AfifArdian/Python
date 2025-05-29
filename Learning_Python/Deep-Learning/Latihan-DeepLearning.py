# logical and
#
# x1 = 1
# x2 = 1
# w1 = 1
# w2 = 1
#
# y_in = (x1 * w1) + (x2 * w2)
#
# if y_in >= 2 :
#     y = 1
# else:
#     y = 0
#
# print(f"x1 = {x1} x2 = {x2} y = {y}")

# looping array 1 dimensional
#
# x1 = [1,1,0,0]
# x2 = [1,0,1,0]
#
# initialization bobot/weight
# w1 = 2
# w2 = -1
#
# print("x1 x2 y")
# print("--------")
#
# for i in range(0,4) :
#
#     y_in = (x1[i] * w1) + (x2[i] * w2)
#
#     if y_in >= 2:
#         y = 1
#     else:
#         y = 0
#
#     print(f"{x1[i]}  {x2[i]}  {y}")
#
# print("--------")

# looping array 2 dimensional

array2d = [
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0]
]

# initialization bobot/weight
w = [2, -1]


print("x1 x2 y")
print("--------")

for i in range(0,4):
    y_in = 0
    for j in range(0,2):
        y_in += array2d[i][j] * w[j]
        print(f"{array2d[i][j]} ", end=" ")

    if y_in >= 2:
        y = 1
    else:
        y = 0

    print(y)

print("--------")