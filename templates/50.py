import random

def q50(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} earns ${A} an hour on Math tutoring. He tutored {B} hours for the first week and {C} hours for the second week. "
        "How much did he earn for the first two weeks?"
    )
    answer_text = (
        "{NAME} tutored {B} + {C} = <<{B}+{C}={TOTAL_HOURS}>>{TOTAL_HOURS} hours for the first two weeks.\n"
        "Therefore, he earned {TOTAL_HOURS} x ${A} = $<<{TOTAL_HOURS}*{A}={TOTAL_EARNINGS}>>{TOTAL_EARNINGS} for the first two weeks.\n#### {TOTAL_EARNINGS}"
    )
    
    # Original values
    A, B, C = 10, 5, 8  # Hourly rate, hours tutored in week 1 and week 2

    # Dynamic name generation (excluding original name "Lloyd")
    common_names = ["Sam", "Emma", "Chris", "Alex", "Taylor"]
    uncommon_names = ["Hiro", "Aisha", "Mei", "Raj", "Lila"]
    random_strings = ["Xlyfrz", "Tmfqvs", "Prkltz", "Bgjwvs", "Lmzptq"]

    if name_level == 1:
        name = "Lloyd"
    elif name_level == 2:
        name = random.choice(common_names)
    elif name_level == 3:
        name = random.choice(uncommon_names)
    elif name_level == 4:
        name = "Z"
    elif name_level == 5:
        name = random.choice(random_strings)

    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B, modified_C = A, B, C
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(10, 91, 10) if num != A])  # Hourly rate
        modified_B = random.choice([num for num in range(2, 10) if num != B])  # Hours week 1
        modified_C = random.choice([num for num in range(2, 10) if num != C and num != modified_B])  # Hours week 2

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    total_hours = modified_B + modified_C
    total_earnings = total_hours * modified_A

    # Prepare original values dictionary
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "ans": (modified_B + modified_C) * modified_A
    }

    if is_symbolic:
        # Represent numbers symbolically with '\'' marks
        modified_A, modified_B, modified_C = "'A'", "'B'", "'C'"
        total_hours = f"{modified_B} + {modified_C}"
        total_earnings = f"{total_hours} * {modified_A}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        TOTAL_HOURS=total_hours,
        TOTAL_EARNINGS=total_earnings
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer, "original_values": original_values}
