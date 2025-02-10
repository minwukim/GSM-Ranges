import random

def q39(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} plays video games for {A} hours every day. {NAME1} also has a part-time job where they earn ${B} an hour. "
        "How much money would {NAME1} earn in one week if they spent their video game time working instead?"
    )
    answer_text = (
        "{NAME1} plays video games for {A} hours every day x 7 days in a week = <<{A}*7={WEEKLY_HOURS}>>{WEEKLY_HOURS} hours a week.\n"
        "If {NAME1} spent their {WEEKLY_HOURS} hours working instead, they would make {WEEKLY_HOURS} hours x ${B} = $<<{WEEKLY_HOURS}*{B}={TOTAL_EARNINGS}>>{TOTAL_EARNINGS}.\n#### {TOTAL_EARNINGS}"
    )
    
    # Original values
    A, B = 2, 10  # Hours spent gaming per day, hourly wage

    # Dynamic name generation
    common_names = ["Jordan", "Taylor", "Morgan", "Alex", "Sam"]
    uncommon_names = ["Kenji", "Amina", "Hiro", "Lila", "Ravi"]
    random_strings = ["Xlfpzk", "Brvjkl", "Njrwvp", "Plgtdz", "Tmrqsv"]

    if name_level == 1:
        name1 = "Jordan"
    elif name_level == 2:
        name1 = random.choice(common_names)
    elif name_level == 3:
        name1 = random.choice(uncommon_names)
    elif name_level == 4:
        name1 = "Z"
    elif name_level == 5:
        name1 = random.choice(random_strings)

    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B = A, B
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(2, 10) if num != A])  # Hours spent gaming per day
        modified_B = random.choice([num for num in range(10, 91, 10) if num != B])  # Hourly wage

        if num_level == 3:
            modified_B *= multiplier
        elif num_level == 4:
            modified_B = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    weekly_hours = modified_A * 7  # Fixed 7 days in a week
    total_earnings = weekly_hours * modified_B

    A = modified_A
    B = modified_B

    original_values = {"A": A, "B": B, "ans": A * 7 * B}

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B = '\'A\'', '\'B\''
        weekly_hours = f"{modified_A} * 7"
        total_earnings = f"{weekly_hours} * {modified_B}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=name1, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME1=name1,
        A=modified_A,
        B=modified_B,
        WEEKLY_HOURS=weekly_hours,
        TOTAL_EARNINGS=total_earnings
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}

