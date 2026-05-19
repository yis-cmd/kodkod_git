def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


from datetime import datetime as dt

import geometry.circle
import geometry.rectangle

print(dt.now())


def public_names(m):
    return sorted([name for name in dir(m) if not name.startswith("_")])


# the bag list will always be the same list along multiple runs
def add_item(item, bag=None):
    bag = []
    bag.append(item)
    return bag

import geometry
print(geometry.circle.area(5))
print(geometry.rectangle.area(4,6))