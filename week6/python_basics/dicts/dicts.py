def sum(numbers: dict):
    result = 0
    for num in numbers.values():
        result += num
    return result


def maximum(numbers: dict):
    largest = list(numbers.values())[0]
    string_return = list(numbers.keys())[0]
    for string, num in numbers.items():
        if largest < num:
            largest = num
            string_return = string
    return string_return


def count(string: str):
    result = {}
    for char in string:
        if char not in result:
            result.update({char: 1})
        else:
            result[char] += 1
    return result


def invert(dictionary: dict):
    return {value: key for key, value in dictionary.items()}


def merge(dict1: dict, dict2: dict):
    return dict1 | dict2


def filter_by_value(dictionary: dict[str, int], threshold: int):
    return {string: num for string, num in dictionary.items() if num > threshold}


def group_by_first_letter(words: list[str]):
    mapped_words: dict[str, list[str]] = {}
    for word in words:
        if word[0] not in mapped_words:
            mapped_words[word[0]] = [word]
        else:
            mapped_words[word[0]].append(word)
    return mapped_words


def frequency(string: str):
    result: dict[str, int] = {}
    word_list = string.split(" ")
    for word in word_list:
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1
    return result


def common(dict1: dict, dict2: dict):
    return sorted([key for key in dict1 if key in dict2])


def most_frequent(dictionary: dict):
    frequency = {}
    for val in dictionary.values():
        if val not in frequency:
            frequency[val] = 1
        else:
            frequency[val] += 1
    # most = max(list(frequency.items()), key = lambda x:x[1])
    # return most[0]
    highest_val = None
    highest_freq = 0
    for val, amount in frequency.items():
        if amount > highest_freq:
            highest_freq = amount
            highest_val = val
    return highest_val
