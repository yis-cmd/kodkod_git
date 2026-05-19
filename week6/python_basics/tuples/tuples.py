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
    reversed = tuple()
    for i in range(1, len(numbers) + 1):
        reversed += (numbers[-i],)
    return reversed


def swap(numbers):
    swapped = []
    for i in range(0, len(numbers), 2):
        swapped.append(numbers[i + 1])
        swapped.append(numbers[i])
    return tuple(swapped)


# def extract_swapped_pairs(numbers: tuple):
#     i = 0
#     while i < len(numbers) - 1:
#         pair = (numbers[i + 1], numbers[i])
#         yield pair
#         i += 2


# def fun_swap(numbers: tuple):
#     swapped = tuple()
#     for i in extract_swapped_pairs(numbers):
#         swapped += i
#     return swapped


def minimum(numbers: tuple):
    lowest = numbers[0]
    for num in numbers:
        if num < lowest:
            lowest = num
    return lowest


def maximum(numbers: tuple):
    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
    return highest


def min_max(numbers: tuple):
    return (minimum(numbers), maximum(numbers))


def euclidean_dist(coords1: tuple, coords2: tuple):
    x = coords1[0] - coords2[0]
    y = coords1[1] - coords2[1]
    x **= 2
    y **= 2
    return (x + y) ** (1 / 2)


def merge(numbers1, numbers2):
    merged: tuple = tuple()
    x = 0
    y = 0
    for _ in range(len(numbers1) + len(numbers2)):
        if len(numbers1) == x:
            merged += numbers2[y:]
            break
        elif len(numbers2) == y:
            merged += numbers1[x:]
            break
        elif numbers1[x] < numbers2[y]:
            merged += (numbers1[x],)
            x += 1
        else:
            merged += (numbers2[y],)
            y += 1
    return merged


def active_merge_sort(numbers):
    if len(numbers) == 1:
        return numbers
    numbers1 = active_merge_sort(numbers[: len(numbers) // 2])
    numbers2 = active_merge_sort(numbers[len(numbers) // 2 :])
    return merge(numbers1, numbers2)


def merge_sort(numbers1, numbers2):
    return active_merge_sort(numbers1 + numbers2)


def frequency_table(items):
    table = {}
    for item in items:
        if item not in table:
            table.update({item: 1})
        else:
            table[item] += 1
    result = tuple()
    for item in table.items():
        result += ((item[0], item[1]),)
    return result


def rotate(numbers, k):
    rotation = k % len(numbers)
    numbers = list(numbers)
    for _ in range(rotation):
        a = numbers.pop(0)
        numbers.append(a)
    return tuple(numbers)
