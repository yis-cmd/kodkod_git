counter_for_exc_1 = 0


def bump():
    global counter_for_exc_1
    counter_for_exc_1 += 1


def value():
    return counter_for_exc_1


# i was expecting to get "local" "enclosing" "global"
# and that's what happened

# the variable list shadows the function list
# 1
numbers = [1, 2, 3]
print(list(range(5)))

# 2 xd
import builtins

list = [1, 2, 3]
print(builtins.list(range(5)))
