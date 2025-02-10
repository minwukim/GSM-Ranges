import random

def q30(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} can run {A} miles per hour for {B} hours. After that, {NAME} runs {C} miles per hour. "
        "How many miles can {NAME} run in {D} hours?"
    )
    answer_text = (
        "For the first {B} hours, {NAME} runs {A} miles per hour, so {NAME} runs {A}*{B}=<<{A}*{B}={FIRST_PART_MILES}>>{FIRST_PART_MILES} miles.\n"
        "However, {NAME} still has {D}-{B}=<<{D}-{B}={REMAINING_HOURS}>>{REMAINING_HOURS} hours left to run.\n"
        "For the next {REMAINING_HOURS} hours, {NAME} runs {C} miles per hour, so {NAME} runs {C}*{REMAINING_HOURS}=<<{C}*{REMAINING_HOURS}={SECOND_PART_MILES}>>{SECOND_PART_MILES} miles.\n"
        "In total, {NAME} runs {FIRST_PART_MILES}+{SECOND_PART_MILES}=<<{FIRST_PART_MILES}+{SECOND_PART_MILES}={TOTAL_MILES}>>{TOTAL_MILES} miles.\n#### {TOTAL_MILES}"
    )

    # Original values
    A, B, C, D = 10, 3, 5, 7  # Speed for first part, duration at speed, reduced speed, total duration
    original_name = "Rosie"

    # Name pools
    common_names = ["Alice", "Ethan", "Sophia", "Liam", "Isabella"]
    uncommon_names = ["Aiko", "Haruto", "Meera", "Saanvi", "Tenzing"]
    random_strings = ["Zkjptrm", "Wlyzgnk", "Fqxrbmt", "Trwvslm", "Ypltnrc"]

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        modified_name = random.choice(common_names)
    elif name_level == 3:
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"  # Explicit symbol assignment
    elif name_level == 5:
        modified_name = random.choice(random_strings)

    # Modify the values for num_level
    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        modified_A = random.choice([num for num in range(8, 12) if num != A])  # Speed for first part
        modified_B = random.choice([num for num in range(2, 5) if num != B])  # Duration at first speed
        modified_C = random.choice([num for num in range(4, 7) if num != C])  # Reduced speed
        modified_D = random.choice([num for num in range(modified_B + 2, 10) if num != D])  # Total duration

        if num_level == 3:
            modified_A *= multiplier
            modified_C *= multiplier
        elif num_level == 4:
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_C = random.randint(multiplier, multiplier * 3)

    # Calculate totals
    first_part_miles = modified_A * modified_B
    remaining_hours = modified_D - modified_B
    second_part_miles = modified_C * remaining_hours
    total_miles = first_part_miles + second_part_miles

    A = modified_A
    B = modified_B
    C = modified_C
    D = modified_D

    original_values = {
        "A": A, "B": B, "C": C, "D": D,
        "ans": (A * B) + (C * (D - B))
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D = '\'A\'', '\'B\'', '\'C\'', '\'D\''
        first_part_miles = f"{modified_A} * {modified_B}"
        remaining_hours = f"{modified_D} - {modified_B}"
        second_part_miles = f"{modified_C} * ({remaining_hours})"
        total_miles = f"{first_part_miles} + {second_part_miles}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        D=modified_D,
        FIRST_PART_MILES=first_part_miles,
        REMAINING_HOURS=remaining_hours,
        SECOND_PART_MILES=second_part_miles,
        TOTAL_MILES=total_miles
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
