import random

def q28(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} uses {A} pads of paper a week for drawing. If there are {B} sheets of paper in a pad of paper, "
        "how many sheets of paper does {NAME} use every month?"
    )
    answer_text = (
        "{NAME} uses {B} x {A} = <<{B}*{A}={WEEKLY_SHEETS}>>{WEEKLY_SHEETS} sheets of paper every week.\n"
        "Therefore, {NAME} uses {WEEKLY_SHEETS} x 4 = <<{WEEKLY_SHEETS}*4={MONTHLY_SHEETS}>>{MONTHLY_SHEETS} sheets of paper every month.\n#### {MONTHLY_SHEETS}"
    )
    
    # Original values
    A, B = 2, 30  # Pads per week, sheets per pad
    original_name = "Miguel"

    # Name pools for name assignment
    common_names = ["Michael", "Sarah", "David", "Emily", "Daniel"]
    uncommon_names = ["Haruto", "Mei", "Akira", "Riko", "Sora"]
    random_strings = ["Tnqswrzx", "Bhlgkrvp", "Xclpsmqt", "Wflrjkxz", "Qzbmtrpk"]

    # Modify name based on name_level
    if name_level == 1:
        # Level 1: Use original name
        modified_name = original_name
    elif name_level == 2:
        # Level 2: Replace with common names
        modified_name = random.choice(common_names)
    elif name_level == 3:
        # Level 3: Replace with uncommon (Asian) names
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        # Level 4: Assign the symbol Z explicitly
        modified_name = "Z"
    elif name_level == 5:
        # Level 5: Replace with random strings
        modified_name = random.choice(random_strings)

    # Modify the values for num_level
    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B = A, B
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(2, 10) if num != A])  # Pads per week
        modified_B = random.choice([num for num in range(10, 91, 10) if num != B])  # Sheets per pad

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    weekly_sheets = modified_A * modified_B
    monthly_sheets = weekly_sheets * 4  # 4 is fixed for weeks in a month

    A = modified_A
    B = modified_B

    original_values = {"A": A, "B": B, "ans": (A * B) * 4}

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B = '\'A\'', '\'B\''
        weekly_sheets = f"{modified_B} * {modified_A}"
        monthly_sheets = f"({weekly_sheets}) * 4"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        WEEKLY_SHEETS=weekly_sheets,
        MONTHLY_SHEETS=monthly_sheets
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
