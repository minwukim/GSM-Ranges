import random

def q72(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original question and answer template
    question_text = (
        "{NAME} has {A} houses with {B} bedrooms each. Each bedroom has {C} windows each. "
        "There are an additional {D} windows in each house not connected to bedrooms. "
        "How many total windows are there between the houses?"
    )
    answer_text = (
        "Each house has {B}*{C}=<<{B}*{C}={WINDOWS_BEDROOMS}>>{WINDOWS_BEDROOMS} windows for the bedrooms\n"
        "So each house has {WINDOWS_BEDROOMS}+{D}=<<{WINDOWS_BEDROOMS}+{D}={WINDOWS_PER_HOUSE}>>{WINDOWS_PER_HOUSE} windows\n"
        "So the total number of windows is {WINDOWS_PER_HOUSE}*{A}=<<{WINDOWS_PER_HOUSE}*{A}={TOTAL_WINDOWS}>>{TOTAL_WINDOWS} windows\n#### {TOTAL_WINDOWS}"
    )
    
    # Original values
    A, B, C, D = 2, 3, 2, 4  # Houses, Bedrooms per house, Windows per bedroom, Additional windows per house
    original_name = "John"

    # Name modification levels
    common_names = ["Michael", "Emma", "Sophia", "Jack", "Olivia"]
    uncommon_asian_names = ["Haru", "Jiro", "Meilin", "Rina", "Akemi"]
    random_strings = ["Fjdlsaf", "Qpwoxnz", "Xytrplv", "Lmnqzrw", "Rvtpzxq"]

    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        modified_name = random.choice([name for name in common_names if name != original_name])
    elif name_level == 3:
        modified_name = random.choice(uncommon_asian_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = random.choice(random_strings)

    # Number modification levels
    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        modified_A = random.choice([num for num in range(1, 5) if num != A])
        modified_B = random.choice([num for num in range(2, 10) if num != B])
        modified_C = random.choice([num for num in range(1, 5) if num != C])
        modified_D = random.choice([num for num in range(3, 10) if num != D])

        if num_level == 3:
            modified_B *= multiplier
            modified_D *= multiplier
        elif num_level == 4:
            modified_B = random.randint(multiplier, multiplier * 10 - 1)
            modified_D = random.randint(multiplier, multiplier * 10 - 1)

    # Ensure positivity and relationships
    windows_bedrooms = modified_B * modified_C
    windows_per_house = windows_bedrooms + modified_D
    total_windows = windows_per_house * modified_A

    # Prepare original values dictionary
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "D": modified_D, "ans": total_windows
    }

    if is_symbolic:
        # Symbolic representation with ticks
        modified_A, modified_B, modified_C, modified_D = "'A'", "'B'", "'C'", "'D'"
        windows_bedrooms = f"({modified_B} * {modified_C})"
        windows_per_house = f"({windows_bedrooms} + {modified_D})"
        total_windows = f"({windows_per_house} * {modified_A})"

    # Replace placeholders in question and answer
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D)
    answer = answer_text.format(
        NAME=modified_name, 
        A=modified_A, B=modified_B, C=modified_C, D=modified_D,
        WINDOWS_BEDROOMS=windows_bedrooms, WINDOWS_PER_HOUSE=windows_per_house, TOTAL_WINDOWS=total_windows
    )

    # Return result
    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
