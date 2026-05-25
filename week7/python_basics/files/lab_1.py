filename_1 = "diary.txt"


def diary_create():
    try:
        with open(filename_1, "w", encoding="utf-8") as file:
            file.write(
                "2024-01-1 5 היה יום עמוס בפרויקט\n"
                "P-Pyth-ב Fil Handlin על למדתי 6 2024-01-1\n"
                "1 7 השלמתי את התרגיל הראשון\n"
            )
    except Exception:
        return


def add_entry():
    try:
        with open(filename_1, "a", encoding="utf-8") as file:
            file.write(":2024-01-18 יום נפלא — סיימתי תרגיל 1")
    except Exception:
        return


def search_diary(filename, keyword):
    result = []
    with open(filename, "r") as file:
        for line in file:
            if keyword in line:
                result.append(line)
    return result


import os


def safe_read_diary(filename):
    if not os.path.exists(filename):
        print("file does not exist")
        return
    with open(filename, "r") as file:
        return file.read()