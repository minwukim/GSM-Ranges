import random

def q14(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} teaches {A} dance classes every day on the weekdays and {B} classes on Saturday. "
        "If each class has {C} students and she charges ${D}.00 per student, how much money does she make in 1 week?"
    )
    answer_text = (
        "She teaches {A} dance classes {WEEKDAYS} days a week so that's {A}*{WEEKDAYS} = <<{A}*{WEEKDAYS}={WEEKLY_CLASSES}>>{WEEKLY_CLASSES} classes.\n"
        "She teaches {WEEKLY_CLASSES} classes during the week and {B} classes on Saturday for a total of {WEEKLY_CLASSES}+{B} = <<{WEEKLY_CLASSES}+{B}={TOTAL_CLASSES}>>{TOTAL_CLASSES} classes.\n"
        "There are {C} students in each of the {TOTAL_CLASSES} classes so there are {C}*{TOTAL_CLASSES} = <<{C}*{TOTAL_CLASSES}={TOTAL_STUDENTS}>>{TOTAL_STUDENTS} students.\n"
        "Each student pays ${D}.00 per class and there are {TOTAL_STUDENTS} students so {NAME} makes {D}*{TOTAL_STUDENTS} = $<<{D}*{TOTAL_STUDENTS}={TOTAL_EARNINGS}>>{TOTAL_EARNINGS}\n#### {TOTAL_EARNINGS}"
    )

    # Original values
    A, B, C, D = 5, 8, 15, 15  # Weekday classes per day, Saturday classes, students per class, dollars per student
    WEEKDAYS = 5  # Fixed constant for the number of weekdays
    original_name = "Judy"

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        common_names = ["Emma", "Sophia", "Olivia", "Isabella", "Ava"]
        modified_name = random.choice(common_names)
    elif name_level == 3:
        uncommon_names = ["Eulalia", "Calliope", "Zephyra", "Thalassa", "Rhiannon"]
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        symbols = ["Z", "Y", "X", "W", "V"]
        modified_name = symbols[0]
    elif name_level == 5:
        random_strings = ["Jdy", "Crlnk", "Fldpx", "Tmpln", "Blknx"]
        modified_name = random.choice(random_strings)

    # Modify the values for num_level
    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        modified_A = random.choice([num for num in range(2, 10) if num != A])
        modified_B = random.choice([num for num in range(2, 9) if num != B])
        modified_C = random.choice([num for num in range(10, 31, 5) if num != C])
        modified_D = random.choice([num for num in range(10, 31, 5) if num != D])

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier
        elif num_level == 4:
            modified_A = random.randint(multiplier, multiplier * 10)
            modified_B = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    weekly_classes = modified_A * WEEKDAYS
    total_classes = weekly_classes + modified_B
    total_students = total_classes * modified_C
    total_earnings = total_students * modified_D

    A = modified_A
    B = modified_B
    C = modified_C
    D = modified_D

    original_values = {
        "A": A, 
        "B": B, 
        "C": C, 
        "D": D, 
        "ans": (((A * WEEKDAYS) + B) * C) * D
    }

    if is_symbolic:
        modified_A, modified_B, modified_C, modified_D = '\'A\'', '\'B\'', '\'C\'', '\'D\''
        weekly_classes = f"{modified_A} * {WEEKDAYS}"
        total_classes = f"({weekly_classes}) + {modified_B}"
        total_students = f"({total_classes}) * {modified_C}"
        total_earnings = f"({total_students}) * {modified_D}"

    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        D=modified_D,
        WEEKDAYS=WEEKDAYS,
        WEEKLY_CLASSES=weekly_classes,
        TOTAL_CLASSES=total_classes,
        TOTAL_STUDENTS=total_students,
        TOTAL_EARNINGS=total_earnings
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
