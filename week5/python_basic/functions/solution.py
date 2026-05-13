def is_even(n):
    return n % 2 == 0


def factorial(n):
    factorial_n = 0
    for num in range(1, n + 1):
        factorial_n *= num
    return factorial_n


# def count_vowels(s):
#     vowels = 0
#     for char in s:
#         if char in "aeiou":
#             vowels += 1
#     return vowels


def sum_digits(number: int):
    summ = 0
    while number > 0:
        summ += number % 10
        number //= 10
    return summ  # c meir silberman


def digital_root(n):
    while n >= 10:
        n = sum_digits(n)
    return n


# def reverse_string(s):
#     return s[::-1]


# def find_max(lst):
#     highest = lst[0]
#     for num in lst:
#         if num > highest:
#             num = highest
#     return highest


# def celsius_to_fahrenheit(c):
#     return c * 9/5 + 32


def is_palindrome(s: str):
    return s.lower() == s[::-1].lower()


def count_digits(number):
    digits_num = 0
    while number > 0:
        digits += 1
        number //= 10
    return digits_num


def reverse_int(number):
    is_minus = False
    if number < 0:
        is_minus = True
        number *= -1
    reversed_number = int(str(reversed(str(number))))
    if is_minus:
        return -reversed_number
    else:
        return reversed_number


# def only_even(numbers):
#     return [number for number in numbers if number % 2 == 0]


# def is_anagram(phrase_a:str, phrase_b:str):
#     return sorted(phrase_a.lower()) == sorted(phrase_b.lower())

# def word_amount(text):
#     word_count = {}
#     for word in text:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return word_count


# def  intercept_length(packet):
#     return len(packet)
# def verify_transmission(packet):
#     packet_length = intercept_length(packet)
# print(f"Intercepted packet contains {packet_length} bytes of data.")


def move_zeroes(numbers: list):
    zeroes = 0
    for num in numbers:
        if num == 0:
            zeroes += 1
    for _ in range(zeroes):
        numbers.remove(0)
        numbers.append(0)
    return numbers


def numbers_stats(numbers):
    if numbers:
        sum = minimum = maximum = numbers[0]
        for num in numbers[1:]:
            sum += num
            if minimum > num:
                minimum = num
            if maximum < num:
                maximum = num
        print(f"{sum}, {sum/len(numbers)}, {minimum}, {maximum}")


def reverse(a_list: list):
    new_list = []
    for i in range(len(a_list), 0, -1):
        new_list.append(i)
    return new_list


def uniq(a_list: list):
    new_list = []
    for thing in a_list:
        if thing not in new_list:
            new_list.append(thing)
    return new_list

print(move_zeroes([0,0,1,0,2,3,0]))