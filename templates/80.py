import random

def q80(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "On Tuesday, {NAME} wants to exercise for {A} times the amount of time he did on Monday and Sunday combined. "
        "On Sunday he exercised for {SUNDAY} minutes. On Monday he exercised for {MONDAY} minutes. "
        "How many minutes does he have to exercise on Tuesday to reach his goal?"
    )
    answer_text = (
        "On Sunday and Monday he exercised a total of {SUNDAY} + {MONDAY} = <<{SUNDAY}+{MONDAY}={TOTAL_WEEKDAYS}>>{TOTAL_WEEKDAYS} minutes.\n"
        "On Tuesday he has to exercise for ({TOTAL_WEEKDAYS} * {A}) = <<{TOTAL_WEEKDAYS}*{A}={TUESDAY_EXERCISE}>>{TUESDAY_EXERCISE} minutes.\n#### {TUESDAY_EXERCISE}"
    )

    # Original values
    SUNDAY, MONDAY, A = 23, 16, 2  # Exercise minutes for Sunday, Monday, and multiplier A
    default_name = "Peter"

    # Dynamic name generation
    common_names = ["Alice", "Jack", "Sophia", "Michael", "Emma"]
    uncommon_names = ["Hiro", "Mei", "Aisha", "Raj", "Lila"]
    random_strings = ["Xlyfrz", "Tmfqvs", "Prkltz", "Bgjwvs", "Lmzptq"]

    if name_level == 1:
        modified_name = default_name
    elif name_level == 2:
        modified_name = random.choice([name for name in common_names if name != default_name])
    elif name_level == 3:
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = random.choice(random_strings)

    # Modify numbers based on num_level
    if num_level == 1:
        modified_sunday, modified_monday, modified_a = SUNDAY, MONDAY, A
    else:
        modified_sunday = random.choice([num for num in range(10, 100) if num != SUNDAY])
        modified_monday = random.choice([num for num in range(10, 100) if num != MONDAY])
        modified_a = random.choice([num for num in range(2, 10) if num != A])

        if num_level == 3:
            modified_sunday *= multiplier
            modified_monday *= multiplier
        elif num_level == 4:
            modified_sunday = random.randint(multiplier, 10 * multiplier - 1)
            modified_monday = random.randint(multiplier, 10 * multiplier - 1)

    # Calculate totals
    total_weekdays = modified_sunday + modified_monday
    tuesday_exercise = total_weekdays * modified_a

    # Save original values in modified format
    original_values = {
        "A": modified_sunday, "B": modified_monday, "C": modified_a,
        "ans": tuesday_exercise
    }

    if is_symbolic:
        # Represent numbers symbolically with quotes
        modified_sunday, modified_monday, modified_a = '\'B\'', '\'C\'', '\'A\''
        total_weekdays = f"({modified_sunday} + {modified_monday})"
        tuesday_exercise = f"({total_weekdays} * {modified_a})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_a, SUNDAY=modified_sunday, MONDAY=modified_monday)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_a,
        SUNDAY=modified_sunday,
        MONDAY=modified_monday,
        TOTAL_WEEKDAYS=total_weekdays,
        TUESDAY_EXERCISE=tuesday_exercise
    )

    return {"question": question, "answer": answer, "original_values": original_values}
