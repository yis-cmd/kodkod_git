# Q1
def reverse(tpl:tuple) -> tuple:
    new_tpl = tuple()
    for idx in range(1,len(tuple) + 1):
	new_tpl += tpl[-idx]
    return new_tpl


# ========================================
# Q2
def secondary(lst:list[int]) -> int:
    if not lst:
        return None
    maximum = lst[0]
    second = None
    for num in lst:
        if num > maximum:
            second = maximum
	    maximum = num
        elif num == maximum:
	    continue
        elif not second or second < num:
	    second = num
    return second

# ========================================
# Q3
def rotate(k:int, numbers:list[int]):
    for i in range(k):
        num = numbers.pop(0)
	numbers.append(num)
    return numbers


# ========================================
# Q4
def count(tpl:tuple):
    counter = {}
    for item in tpl:
        if item not in counter:
	    counter[item] + 1
	else:
	    counter[item] += 1
    as_list = [(item, number) for item, number in counter.items()]
    return tuple(as_list)


# ========================================
# Q5
def bigger_than(dictionary:dict[str,int], threshold:int):
    return {letter:num for letter, num in dictionary.items() if num > threshold}


# ========================================
# Q6
def symmetric_difference(lst1:list, lst2:list):
    new_lst1 = [item for item in lst1 if item not in lst2]
    new_lat2 = [item for item in lst2 if item not in lst1]
    result = new_lst1 + new_lst2
    return sorted(result)


# ========================================
# Q7
def set_age(age:int) -> int:
    if 150 >= age >= 0:
        return age
    raise ValueError


# ========================================
# Q8
def replace(dictionary:dict):
    return {value: key for key, value in dictionary.items()}


# ========================================
# Q9
def unionate(dct1:dict, dct2:dict) -> dict:
    return dct1 | dct2


# ========================================
# Q10
def mapping(words:list[str]) -> dict:
    mapper = {}
    for word in words:
	if word[0] not in mapper:
	    mapper[word[0]] = [word]
	else:
	    mapper[word[0]].append(word)
    return mapper