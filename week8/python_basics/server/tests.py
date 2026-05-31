import requests


def test_1():
    res = requests.get("http://localhost:6543/ping")
    print(f"test status: {res.status_code}")
    print(f"test response: {res.json()}")

    res_2 = requests.get("http://localhost:6543/greet/yis")
    print(f"test status: {res_2.status_code}")
    print(f"test response: {res_2.json()}")


def test_2():
    res = requests.get("http://localhost:6543/")
    print(f"test status: {res.status_code}")
    print(f"test response: {res.json()}")

    res_2 = requests.get("http://localhost:6543/users/2345")
    print(f"test status: {res_2.status_code}")
    print(f"test response: {res_2.json()}")


def test_3():
    a, b = 1, 2
    op = "sub"
    res = requests.get(f"http://localhost:6543/calc/{a}/{op}/{b}")
    print(f"test status: {res.status_code}")
    print(f"test response: {res.json()}")

    assert res.json()["result"] == -1


def test_4():
    res = requests.get(f"http://localhost:6543/status")
    print(f"test status: {res.status_code}")
    print(f"test response: {res.json()}")


def test_5():
    all_students = requests.get(f"http://localhost:6543/students")
    print(f"test status: {all_students.status_code}")
    print(f"test response: {all_students.json()}")

    assert all_students.json() == {
        "1": {"name": "Moshe", "grade": 88},
        "2": {"name": "Yaakov", "grade": 75},
        "3": {"name": "David", "grade": 92},
    }

    top_score = requests.get(f"http://localhost:6543/students/top")
    print(f"test status: {top_score.status_code}")
    print(f"test response: {top_score.json()}")

    assert top_score.json() == {"3": {"name": "David", "grade": 92}}

    average_score = requests.get(f"http://localhost:6543/students/average")
    print(f"test status: {average_score.status_code}")
    print(f"test response: {average_score.json()}")

    assert average_score.json() == 85

    student_count = requests.get(f"http://localhost:6543/students/count")
    print(f"test status: {student_count.status_code}")
    print(f"test response: {student_count.json()}")

    assert student_count.json() == 3

    student = requests.get(f"http://localhost:6543/students/1")
    print(f"test status: {student.status_code}")
    print(f"test response: {student.json()}")

    assert student.json() == {"name": "Moshe", "grade": 88}