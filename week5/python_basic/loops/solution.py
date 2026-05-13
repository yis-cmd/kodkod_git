# 1
def one():
    for i in range(10):
        if i % 2 == 0:
            continue
        if i >= 7:
            break
        print(i)


"""**********"""


# 2
def two():
    while True:
        password = input("Enter a password: ")
        if password == "1234":
            print("Welcome")
            break
        else:
            print("Try again")


"""*********"""


# 3
def three():
    products = []
    while True:
        product = input("enter a product name: ")
        if product == "done":
            break
        products.append(product)
    print(products)


"""**********"""


# 3.5
def three_and_a_half():
    for row in range(3):
        for col in range(3):
            print(row, col)
            if col == 2:
                break


"""**********"""


# 4
def four():
    vowels = "aeiouAEIOU"
    how_many = 0
    string = input("enter a string: ")
    for i in string:
        if i in vowels:
            how_many += 1
    print(how_many)


"""**********"""


# 5
def five():
    for i in range(1, 6):
        for j in range(1, 6):
            print(f"{i} * {j} = {i * j}")


"""**********"""


# 6
def six():
    string = input("Enter a string: ")
    for i in range(len(string)):
        print(string[-(i + 1)])


"""**********"""


# 7
def seven():
    evens = 0
    positive_integer = 65374695243652374562378569
    while positive_integer > 0:
        remainder = positive_integer % 10
        positive_integer //= 10
        if remainder % 2 == 0:
            evens += 1


"""**********"""


# 8
def eight():
    given_string = "long long string"
    new_string = ""
    for i in given_string:
        new_string += i * 2
    print(new_string)


"""**********"""


# 9
def nine():
    highest = 0
    while True:
        num = int(input("Enter a positive number: "))
        if num == 0:
            break
        if num > highest:
            highest = num
    print(highest)


"""**********"""


# 10
def ten():
    contains_only_letters_or_numbers = True
    a_string = "a lot of words / here"
    for i in a_string:
        if not i.isalnum():
            contains_only_letters_or_numbers = False
            break
    print(contains_only_letters_or_numbers)


"""**********"""


# 11
def eleven():
    number = 143514541
    new_number = 0
    while number > 0:
        number, remainder = divmod(number, 10)
        new_number *= 10
        new_number += remainder
    print(new_number)
