import random

def q54(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} gets water from a well. They get {A} pails of water every morning and {B} pails of water every afternoon. "
        "If each pail contains {C} liters of water, how many liters of water do they get every day?"
    )
    answer_text = (
        "{NAME} gets {A} x {C} = <<{A}*{C}={MORNING_LITERS}>>{MORNING_LITERS} liters of water in the morning.\n"
        "They get {B} x {C} = <<{B}*{C}={AFTERNOON_LITERS}>>{AFTERNOON_LITERS} liters of water in the afternoon.\n"
        "Therefore, the total liters of water they get every day is {MORNING_LITERS} + {AFTERNOON_LITERS} = "
        "<<{MORNING_LITERS}+{AFTERNOON_LITERS}={TOTAL_LITERS}>>{TOTAL_LITERS}.\n#### {TOTAL_LITERS}"
    )
    
    # Original values
    A, B, C = 5, 6, 5  # Morning pails, afternoon pails, liters per pail

    # Dynamic name generation (excluding original names)
    common_names = ["Sam", "Emma", "Chris", "Alex", "Taylor"]
    uncommon_names = ["Hiro", "Aisha", "Mei", "Raj", "Lila"]
    random_strings = ["Xlyfrz", "Tmfqvs", "Prkltz", "Bgjwvs", "Lmzptq"]

    if name_level == 1:
        name = "Baldur"
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
        modified_A = random.choice([num for num in range(2, 10) if num != A])  # Morning pails
        modified_B = random.choice([num for num in range(2, 10) if num != B])  # Afternoon pails
        modified_C = random.choice([num for num in range(2, 10) if num != C])  # Liters per pail

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_B *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_B = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    morning_liters = modified_A * modified_C
    afternoon_liters = modified_B * modified_C
    total_liters = morning_liters + afternoon_liters

    original_values = {
        "A": modified_A,
        "B": modified_B,
        "C": modified_C,
        "ans": total_liters
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        morning_liters = f"{modified_A} * {modified_C}"
        afternoon_liters = f"{modified_B} * {modified_C}"
        total_liters = f"({morning_liters}) + ({afternoon_liters})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        MORNING_LITERS=morning_liters,
        AFTERNOON_LITERS=afternoon_liters,
        TOTAL_LITERS=total_liters
    )

    return {"question": question, "answer": answer, "original_values": original_values}
