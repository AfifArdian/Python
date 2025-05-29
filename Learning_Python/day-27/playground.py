def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(1,2,3,4,5))

def calculate(n, **kwargs):
    print(kwargs)
    # for k, val in kwargs.items():
    #     print(k)
    #     print(val)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)


# calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Dodge", model="Hellcat")
print(my_car.color)