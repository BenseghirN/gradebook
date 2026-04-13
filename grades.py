#machin
# grades.py
# Developer B — Grade calculations
# Branch: feature/grades

# The grades database is a nested dictionary with this structure:
# {
#   "S001": {"Math": 85, "English": 90, "Science": 78},
#   "S002": {"Math": 60, "English": 55},
# }

mock_grade = {
   "S001": {"Math": 85, "English": 90, "Science": 78},
   "S002": {"Math": 60, "English": 55},
}

def add_grade(grades: dict, student_id: str, subject: str, score: int) -> dict|None:
    """
    Add or update a grade for a student in a given subject.

    - Score must be between 0 and 100 (inclusive).
      If not, print a warning and do NOT add the grade:
      "Invalid score: 110. Score must be between 0 and 100."
    - If student_id does not exist in grades yet, create their entry.
    - Overwrite the score if the subject already exists for that student.

    Args:
        grades (dict): the current grades database
        student_id (str): the student's ID
        subject (str): the subject name (e.g. "Math")
        score (int): the score between 0 and 100

    Returns:
        dict: the updated grades dictionary

    Example:
        >>> db = {}
        >>> _ = add_grade(db, "S001", "Math", 85)
        >>> db
        {'S001': {'Math': 85}}
    """
    # Return nothing if grade is empty
    if grades == {}:
        pass
        # return None
    # Check is student exist
    if student_id not in grades:
        grades[student_id] = {}

    # Check score validity
    if 0 <= score <= 100:
        pass
    else:
        print(f"Invalid score: {score}. Score must be between 0 and 100.")
        return grades

    # Update student entry
    grades[student_id].update({subject: score})

    return grades


def get_average(grades: dict, student_id: str) -> float:
    """
    Calculate the average score of a student across all their subjects.

    - Returns 0.0 if the student has no grades or does not exist.
    - Round the result to 2 decimal places.

    Args:
        grades (dict): the current grades database
        student_id (str): the student's ID

    Returns:
        float: the average score, rounded to 2 decimal places

    Example:
        >>> db = {"S001": {"Math": 80, "English": 90}}
        >>> get_average(db, "S001")
        85.0
        >>> get_average(db, "S999")
        0.0
    """
    if student_id not in grades:
        return 0.0

    if grades[student_id] == {}:
        return 0.0

    sum = 0
    for subject,score in grades[student_id].items():
        sum += score
    average = round(sum / len(grades[student_id]),2)

    return average

def get_subjects(grades: dict) -> set:
    """
    Return the set of ALL unique subjects that appear across all students.

    - Uses a set to avoid duplicates.
    - Returns an empty set if grades is empty.

    Args:
        grades (dict): the current grades database

    Returns:
        set: a set of subject name strings

    Example:
        >>> db = {
        ...   "S001": {"Math": 80, "English": 90},
        ...   "S002": {"Math": 70, "Science": 65},
        ... }
        >>> get_subjects(db)
        {"Math", "English", "Science"}
    """
    subjects = set()

    for student_id in grades:
        for subject in grades[student_id]:
            subjects.add(subject)

    return subjects

def get_failing_students(students: dict, grades: dict, threshold: int = 50) -> list:
    """
    Return a list of (student_id, name, average) tuples for students
    whose average score is strictly below the threshold.

    - Tuples must be sorted by average score in ascending order (lowest first).
    - Students with no grades at all should be included with average 0.0.
    - Use get_average() to compute each student's average.

    Args:
        students (dict): the students database
        grades (dict): the grades database
        threshold (int): the minimum passing average (default 50)

    Returns:
        list[tuple]: list of (student_id, name, average) sorted by average

    Example:
        >>> students = {"S001": {"name": "Alice", "id": "S001"},
        ...             "S002": {"name": "Bob",   "id": "S002"}}
        >>> grades   = {"S001": {"Math": 40}, "S002": {"Math": 80}}
        >>> get_failing_students(students, grades)
        [("S001", "Alice", 40.0)]
    """

    students_failing = []

    for student_id in students:
        student_average_score = get_average(grades, student_id)
        if student_average_score < 50:
            student_name = students[student_id]["name"]
            students_failing.append(tuple([student_id, student_name,student_average_score]))

    students_failing.sort(key=lambda tup: tup[1])
    return students_failing