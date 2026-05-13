# 1
from typing import TypedDict

ADULT_AGE: int = 18


class Person(TypedDict):
    name: str
    age: int
    is_active: bool


def get_active_adults(people_details: list[Person]):
    active_adults_names: list[str] = []
    for person in people_details:
        if person["age"] >= ADULT_AGE and person["is_active"]:
            active_adults_names.append(person["name"])
    return active_adults_names


people_details: list[Person] = [
    {"name": "Dan", "age": 25, "is_active": True},
    {"name": "Noa", "age": 16, "is_active": True},
    {"name": "Yael", "age": 30, "is_active": False},
]

print(get_active_adults(people_details))


# 2
from dataclasses import dataclass

FIRST_AMOUNT_FOR_DISCOUNT = 10
FIRST_QUANTITY_DISCOUNT = 0.9
SECOND_AMOUNT_FOR_DISCOUNT = 50
SECOND_QUANTITY_DISCOUNT = 0.85


@dataclass
class PurchaseDetails:
    user_email: str
    product_name: str
    product_price: float
    stock: int
    quantity: int


@dataclass
class OrderDetails:
    order_user: str
    order_product: str
    order_quantity: int
    order_total: float
    order_status: str

    def __str__(self) -> str:
        return (
            f"Order {self.order_status}: {self.order_user}"
            f"bought {self.order_quantity}x"
            f"{self.order_product} for ${self.order_total}"
        )


def handle_purchase(purchase_details: PurchaseDetails):
    if not is_valid_purchase(
        purchase_details.user_email, purchase_details.quantity, purchase_details.stock
    ):
        return None

    price: float = calculate_price_with_discount(
        purchase_details.product_price, purchase_details.quantity
    )

    purchase_details.stock -= purchase_details.quantity
    order_details = OrderDetails(
        purchase_details.user_email,
        purchase_details.product_name,
        purchase_details.quantity,
        price,
        "confirmed",
    )
    print(str(order_details))
    return order_details


def is_valid_purchase(user_email, quantity, stock):
    if not user_email:
        print("Invalid user")
        return False
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
        return False
    return True


def calculate_price_with_discount(product_price, quantity) -> float:
    price = product_price * quantity
    if quantity >= FIRST_AMOUNT_FOR_DISCOUNT:
        price *= FIRST_QUANTITY_DISCOUNT
    if quantity >= SECOND_AMOUNT_FOR_DISCOUNT:
        price *= SECOND_QUANTITY_DISCOUNT
    return price


# 3
TOP_GRADE = 90
PASSING_GRADE = 56


def manage_students(students: list[str], grades: list, new_name: str, new_grade):
    # validation
    if not validate_students_grades(new_name, new_grade):
        return students
    # add student
    students.append(new_name)
    grades.append(new_grade)

    average, top_count, failing_count = calculate_stats(grades)

    print_students_report(students, grades, average, top_count, failing_count)

    save_students_grades_file(students, grades)

    return students, grades


def validate_students_grades(new_name: str, new_grade):
    if not new_name or len(new_name) < 2:
        print("Error: invalid name")
        return False
    if new_grade < 0 or new_grade > 100:
        print("Error: grade must be 0-100")
        return False
    return True


def calculate_stats(grades: list):
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for g in grades if g >= TOP_GRADE)
    failing_count = sum(1 for g in grades if g < PASSING_GRADE)
    return average, top_count, failing_count


def print_students_report(students: list[str], grades: list, average, top_count, failing_count):
    print("=== Student Report ===")
    for i in range(len(students)):
        print(f"  {students[i]}: {grades[i]}")
    print(f"Average: {average:.1f}")
    print(f"Top students: {top_count}")
    print(f"Failing: {failing_count}")


def save_students_grades_file(students: list[str], grades: list):
    with open("students.txt", "w") as f:
        for i in range(len(students)):
            f.write(f"{students[i]},{grades[i]}\n")


# 4
def create_user(kind, name, email):
    validate_user_details(name, email)
    return name, email, kind, "2024-01-01", True


def validate_user_details(name, email):
    if not name or len(name) < 2:
        raise ValueError("Invalid name")
    if "@" not in email:
        raise ValueError("Invalid email")


# 5
def get_status(score):
    if score >= 90:
        return "excellent"
    elif score >= 70:
        return "good"
    elif score >= 55:
        return "average"
    elif score < 55:
        return "fail"
    else:
        return "unknown"


def is_valid_age(age):
    if not isinstance(age, int):
        return False
    if age <= 0 or age > 120:
        return False
    return True


def get_greeting(hour):
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Good night"


# 6

PASSING_GRADE = 56


def process_grades(names, all_grades):
    result_names = []
    result_averages = []
    result_statuses = []
    result_highs = []
    result_lows = []
    for i in range(len(names)):
        name = names[i]
        grades = all_grades[i]

        if not validate_student(name, grades):
            continue

        average, status, highest, lowest = calculate_student_stats(grades)

        result_names.append(name)
        result_averages.append(round(average, 1))
        result_statuses.append(status)
        result_highs.append(highest)
        result_lows.append(lowest)

    print_report(
        result_names, result_averages, result_statuses, result_lows, result_highs
    )

    passing_count = sum(1 for s in result_statuses if s == "pass")
    print(f"Total passing: {passing_count}/{len(result_names)}")
    return result_names, result_averages, result_statuses


def validate_student(name, grades):
    if not name:
        print(f"Error: missing name")
        return False
    if not grades:
        print(f"Error: {name} has no grades")
        return False
    return True


def calculate_student_stats(grades):
    total = sum(grades)
    average = total / len(grades)
    status = "pass" if average >= PASSING_GRADE else "fail"
    highest = max(grades)
    lowest = min(grades)
    return average, status, highest, lowest


def print_report(
    result_names, result_averages, result_statuses, result_lows, result_highs
):
    print("=" * 40)
    print("Student Grade Report")
    print("=" * 40)
    for i in range(len(result_names)):
        print(f"Name: {result_names[i]}")
        print(f"  Average: {result_averages[i]}")
        print(f"  Status: {result_statuses[i]}")
        print(f"  Range: {result_lows[i]} - {result_highs[i]}")
        print()


# 7
TAX = 0.17
PREMIUM_DISCOUNT = 0.9
VIP_DISCOUNT = 0.8
SHIPPING_AMOUNT_FOR_FREE = 500
SHIPPING_AMOUNT_FOR_DISCOUNT = 200
SHIPPING_COST_WITH_DISCOUNT = 25
SHIPPING_COST_WITH_NO_DISCOUNT = 50


def ProcessCart(prices, quantities, user_type):
    total_price = 0

    for item in range(len(prices)):
        price = prices[item]
        quantity = quantities[item]
        # adding current item's cost to the total
        total_price = total_price + (price * quantity)

    # add tax
    total_price = total_price + (total_price * TAX)

    total_price = calc_membership_discount(user_type, total_price)

    shipping = calc_shipping_price(total_price)
    total_price += shipping
    return total_price

def calc_membership_discount(user_type, total_price):
    if user_type == "premium":
        return total_price * PREMIUM_DISCOUNT
    elif user_type == "vip":
        return total_price * VIP_DISCOUNT
    return total_price


def calc_shipping_price(total_price) -> int:
    if total_price > SHIPPING_AMOUNT_FOR_FREE:
        return 0
    elif total_price > SHIPPING_AMOUNT_FOR_DISCOUNT:
        return SHIPPING_COST_WITH_DISCOUNT
    else:
        return SHIPPING_COST_WITH_NO_DISCOUNT
