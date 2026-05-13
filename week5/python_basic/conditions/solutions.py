#1
def one():
    age = int(input("Enter you age: "))
    if age < 0 or age > 120:
        print("Invalid")
    elif age <= 12:
        print("Child")
    elif age <= 17:
        print("Teen")
    else:
        print("Adult")

#2
def two():
    letter = input("Enter a letter: ")
    if not (letter.isupper() or letter.islower()):
        print("Invalid")
    elif letter in "aeiou":
        print("Vowel")
    else:
        print("Consonant")

#3
def three():
    age = int(input("Enter your age: "))
    if age < 16:
        print("rejected")
    else:
        VIP_card = ("yes" == input("Do you have a VIP card(yes/no): "))
        if (age > 18 and VIP_card) or (19 <= age <= 21):
            print("allowed")


#4
def four():
    PASSWORD = "some_password"
    user_pass = input("Enter password: ")
    if user_pass == PASSWORD:
        print("Access Granted")
    elif len(user_pass) < 8:
        print("Too short")
    else:
        print("Wrong password")

#5
def five():
    x = int(input("Enter the x: "))
    y = int(input("Enter the y: "))
    if 10<=x<=50 and 20<=y<=80:
        if x == 10 or x == 50 or y == 20 or y == 80:
            print("On the edge")
        else:
            print("Inside the rectangle")
    else:
        print("Outside the rectangle")

#6
def six():
    greeting = "hey {}"
    name = input("Enter your name")
    if not name:
        name = "Anonymous"
    print(greeting.format(name))

#7
def eight():
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))
    c = int(input("Enter the 3rd number: "))
    print((a > 0) + (b > 0) + (c > 0))


#8
def ten():
    score = int(input("Enter score: "))
    print(["F", "C", "B", "A"][(score >= 70) + (score >= 80) + (score >= 90)])