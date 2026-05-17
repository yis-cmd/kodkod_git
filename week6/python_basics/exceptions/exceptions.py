def safe_int(s):
    try:
        return int(s)
    except (ValueError, TypeError):
        return None


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "undefined"


def read_first_line(path):
    try:
        with open(path, "r") as file:
            return file.readline()
    except FileNotFoundError:
        return None


def get_value(d, key):
    try:
        return d[key]
    except KeyError:
        return "missing"


def parse_ints(values):
    int_values = []
    for val in values:
        try:
            int_values.append(int(val))
        except (TypeError, ValueError):
            pass
    return int_values


def set_age(age):
    if not 0 <= age <= 150:
        raise ValueError
    return age


class InsufficientFundsError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError
    return balance - amount


def retry(func, n):
    for time in range(n):
        try:
            return func()
        except Exception:
            if time == n - 1:
                raise


def count_errors(funcs):
    counter = 0
    for func in funcs:
        try:
            func()
        except Exception:
            counter += 1
    return counter


def load_config(path):
    try:
        with open(path, "r") as file:
            return int(file.readline())
    except Exception as e:
        raise RuntimeError("failed to load config") from e
