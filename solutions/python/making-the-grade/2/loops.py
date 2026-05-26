"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores."""
    rounded = []

    while student_scores:
        value = student_scores.pop()
        rounded.append(round(value))

    return rounded


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided."""
    count = 0

    for score in student_scores:
        if score <= 40:
            count += 1

    return count


def above_threshold(student_scores, threshold):
    """Determine which scores are above or equal to threshold."""
    best = []

    for score in student_scores:
        if score >= threshold:
            best.append(score)

    return best


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade."""
    increment = round((highest - 41) / 4)
    thresholds = []

    for grade_position in range(1, 4):  # D, C, B
        thresholds.append(round(41 + grade_position * increment))
    thresholds.insert(0,41)

    return thresholds


def student_ranking(student_scores, student_names):
    """Organize rank, name, and score."""
    scores_names = []

    for index, score in enumerate(student_scores):
        result = f"{index + 1}. {student_names[index]}: {score}"
        scores_names.append(result)

    return scores_names


def perfect_score(student_info):
    """Return first student with score 100."""
    for student in student_info:
        if student[1] == 100:
            return student

    return []