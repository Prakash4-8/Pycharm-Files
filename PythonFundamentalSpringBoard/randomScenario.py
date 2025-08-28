import random


# print(help(random))

def petrol_vals():
    possiblePrice = []
    price = 1.10
    output = []
    while price <= 1.45:
        price += 0.01
        possiblePrice.append(round(price, 2))
    # return random.sample(possiblePrice, 30)  # sample can't be more than to it's population
    for _ in range(30):
        output.append(random.choice(possiblePrice))  # choice used to choose one value from the list
    return output


def petrol_val2():
    output = []
    for _ in range(30):
        output.append(random.randint(110, 145) / 100)
    return output


print(petrol_val2())
