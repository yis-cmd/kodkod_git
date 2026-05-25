def create_grades_file(filename):
    students = [
        ("Dan", [85, 90, 78]),
        ("MOMO", [92, 88, 95]),
        ("Yoni", [70, 65, 80]),
        ("Avi", [100, 95, 98]),
        ("Sara", [60, 72, 68]),
    ]
    with open(filename, "w") as file:
        for name, scores in students:
            grades = ",".join([str(score) for score in scores])
            file.write(f"{name},{grades}\n")


def calculate_averages(filename):
    averages = {}
    with open(filename, "r") as file:
        for line in file:
            student = line.strip().split(",")
            name = student.pop(0)
            avg = sum(int(grade) for grade in student) / (len(student))
            averages[name] = avg
    return averages


def save_results(averages: dict[str, int], output_filename):
    results = sorted(averages.items(), key=lambda x: x[1])
    overall_avg = sum(result[1] for result in results) / len(results)
    lowest = min(result[1] for result in results)
    highest = max((result[1] for result in results))
    passers = len([result for result in results if result[1] >= 60])
    with open(output_filename, "w") as file:
        file.write("=== Student Results ===")
        for i, (name, avg) in enumerate(results, start=1):
            file.write(f"{i}. {name}: {avg}\n")
        file.write(f"\noverall avg: {overall_avg}\n"\
                    f"lowest score: {lowest}\n"
                    f"highest score: {highest}\n"
                    f"passers: {passers}\n")


averages = calculate_averages("grades.txt")
save_results(averages, "results.txt")
