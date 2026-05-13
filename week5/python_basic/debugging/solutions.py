def calc_price(cost: int, discount: int):
    print(f"DEBUG: {cost}")
    breakpoint()
    final_cost = cost - discount


def add_a(a: int):
    a += 1

    def add_b(a):
        a += 1

        def add_c(a):
            a += 1
            return a

        return add_c(a)

    return add_b(a)


def error():
    print(f"{2/0}")

