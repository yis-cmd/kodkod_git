def uniq(numbers: list) -> list:
    return list(set(numbers))


def len_uniq(numbers: list):
    uniq_numbers = set(numbers)
    length = 0
    for _ in uniq_numbers:
        length += 1
    return length


def common_elements(lst1, lst2):
    common = set(lst1).intersection(set(lst2))
    return sorted(list(common))


def differ_elements(lst1, lst2):
    common = set(lst1).symmetric_difference(set(lst2))
    return sorted(list(common))


def is_subset(lst1, lst2):
    return set(lst1).issubset(set(lst2))


def uniq_chars(string: str):
    chars = list(string)
    return len(chars) == len(set(chars))


def repeated(item_list):
    singles = set()
    for item in item_list:
        if item in singles:
            return item
        else:
            singles.add(item)


def uniq_words(string: str):
    word_list = string.lower().split(" ")
    return len(set(word_list))


def sum_exist(numbers: list[int], target: int):
    seen = set()
    for num in numbers:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False


def symmetric_diff(lst1, lst2):
    common = set(lst1).intersection(set(lst2))
    both = set(lst1 + lst2)
    for i in common:
        both.remove(i)
    return both
