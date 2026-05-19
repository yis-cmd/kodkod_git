def sum(numbers):
    result = 0
    for num in numbers:
        result += num
    return result


def max(numbers):
    largest = numbers[0]
    for num in numbers:
        if largest < num:
            largest = num
    return largest


def count(numbers, item):
    overall = 0
    for num in numbers:
        if num == item:
            overall += 1
    return overall


def reverse(numbers):
    reversed = []
    for i in range(1, len(numbers) + 1):
        reversed.append(numbers[-i])
    return reversed


# def fun_reverse(numbers):
#     if not numbers:
#         return []
#     num = numbers.pop(0)
#     reversed = fun_reverse(numbers)
#     reversed.append(num)
#     return reversed


def uniq(numbers):
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique


# def fun_uniq(numbers:list[int]) -> list[int]:
#     if not numbers:
#         return []
#     num = numbers.pop()
#     unique = fun_uniq(numbers)
#     if num not in unique:
#         unique.append(num)
#     return unique


def second_largest(numbers):
    if len(numbers) < 2:
        return None
    largest = numbers[0]
    second = None
    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num < largest and (second is None or num > second):
            second = num
    return second


def merge(numbers1, numbers2):
    merged: list = []
    x = 0
    y = 0
    for _ in range(len(numbers1) + len(numbers2)):
        if len(numbers1) == x:
            merged.extend(numbers2[y:])
            break
        elif len(numbers2) == y:
            merged.extend(numbers1[x:])
            break
        elif numbers1[x] < numbers2[y]:
            merged.append(numbers1[x])
            x += 1
        else:
            merged.append(numbers2[y])
            y += 1
    return merged


def rotate(numbers, k):
    rotation = k % len(numbers)
    for _ in range(rotation):
        a = numbers.pop(0)
        numbers.append(a)
    return numbers
