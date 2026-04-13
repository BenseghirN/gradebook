# reports.py
# Developer C — Reporting & summaries
# Branch: feature/reports

from grades import get_average

def get_top_students(students:dict, grades: dict, n: int = 3) -> list:

    result = []

    for student_id, student_info in students.items():
        name = student_info["name"]
        student_grades = grades.get(student_id, {})

        if student_grades:
            average = sum(student_grades.values()) / len(student_grades)
        else:
            average = 0.0

        result.append((student_id, name, average))

    result.sort(key=lambda x: x[2], reverse=True)

    return result[:n]

    """
    Return the top n students with the highest average scores.

    - Returns a list of (student_id, name, average) tuples.
    - Sorted by average in descending order (highest first).
    - If n is greater than the number of students, return all of them.
    - Students with no grades have an average of 0.0.

    Args:
        students (dict): the students database
        grades (dict): the grades database
        n (int): number of top students to return (default 3)

    Returns:
        list[tuple]: list of (student_id, name, average) sorted descending

    Example:
        >>> students = {
        ...   "S001": {"name": "Alice", "id": "S001"},
        ...   "S002": {"name": "Bob",   "id": "S002"},
        ... }
        >>> grades = {"S001": {"Math": 90}, "S002": {"Math": 70}}
        >>> get_top_students(students, grades, n=1)
        [("S001", "Alice", 90.0)]
    """


def summarize_class(students: dict, grades: dict) -> tuple:

    if not students:
        return (0, 0.0, 0.0, 0.0)

    averages = []

    for student_id in students:
        student_grades = grades.get(student_id, {})

        if student_grades:
            average = sum(student_grades.values()) / len(student_grades)
        else:
            average = 0.0

        averages.append(average)

    total_students = len(students)
    class_average = round(sum(averages) / total_students, 2)
    highest_average = max(averages)
    lowest_average = min(averages)

    return (total_students, class_average, highest_average, lowest_average)

    # """
    # Return a summary of the whole class as a single tuple.
    #
    # The tuple must contain exactly 4 values in this order:
    #     (total_students, class_average, highest_average, lowest_average)
    #
    # - total_students (int): number of students in the database
    # - class_average (float): average of all students' averages, rounded to 2 decimals
    # - highest_average (float): the best individual average in the class
    # - lowest_average (float): the worst individual average in the class
    #
    # - If there are no students, return (0, 0.0, 0.0, 0.0).
    #
    # Args:
    #     students (dict): the students database
    #     grades (dict): the grades database
    #
    # Returns:
    #     tuple: (total_students, class_average, highest_average, lowest_average)
    #
    # Example:
    #     >>> students = {
    #     ...   "S001": {"name": "Alice", "id": "S001"},
    #     ...   "S002": {"name": "Bob",   "id": "S002"},
    #     ... }
    #     >>> grades = {"S001": {"Math": 80}, "S002": {"Math": 60}}
    #     >>> summarize_class(students, grades)
    #     (2, 70.0, 80.0, 60.0)
    # """
    # TODO: implement this function
    #raise NotImplementedError("summarize_class is not implemented yet.")


def export_report(students: dict, grades: dict) -> str:

    total_students, class_average, _, _ = summarize_class(students, grades)

    separator = "─" * 33

    lines = []
    lines.append(separator)
    lines.append("GRADEBOOK REPORT")
    lines.append(f"Total students: {total_students}")
    lines.append(f"Class average:  {class_average:.2f}")
    lines.append("")
    lines.append("STUDENT DETAILS")

    sorted_students = sorted(students.values(), key=lambda s: s["name"])

    for student in sorted_students:
        student_id = student["id"]
        name = student["name"]
        student_grades = grades.get(student_id, {})

        if student_grades:
            average = sum(student_grades.values()) / len(student_grades)
            subjects = ", ".join(sorted(student_grades.keys()))
        else:
            average = 0.0
            subjects = "none"

        lines.append(f"{student_id} | {name:<16} | Avg: {average:>6.2f} | Subjects: {subjects}")

    lines.append(separator)

    return "\n".join(lines)
    # """
    # Generate and return a formatted text report as a single string.
    #
    # The report must follow this exact format:
    # ─────────────────────────────────
    # GRADEBOOK REPORT
    # Total students: 3
    # Class average:  75.33
    #
    # STUDENT DETAILS
    # S001 | Alice Smith     | Avg:  85.00 | Subjects: English, Math, Science
    # S002 | Bob Martin      | Avg:  62.50 | Subjects: Math, Science
    # S003 | Carol White     | Avg:   0.00 | Subjects: none
    # ─────────────────────────────────
    #
    # Rules:
    # - Student names are left-aligned in a field of 16 characters.
    # - Averages are right-aligned with 2 decimal places.
    # - Subjects are listed in alphabetical order, comma-separated.
    # - If a student has no grades, show "none" for subjects.
    # - Use summarize_class() to get total_students and class_average.
    # - Students are listed in alphabetical order by name.
    #
    # Args:
    #     students (dict): the students database
    #     grades (dict): the grades database
    #
    # Returns:
    #     str: the complete formatted report
    # """
    # TODO: implement this function
    #raise NotImplementedError("export_report is not implemented yet.")

