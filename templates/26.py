import random

def q26(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} plants {A} flowers a day in their garden. After {B} days, how many flowers do they have if {C} did not grow?"
    )
    answer_text = (
        "{NAME} plants {A}*{B}=<<{A}*{B}={TOTAL_FLOWERS}>>{TOTAL_FLOWERS} flowers in total.\n"
        "Given {C} plants did not grow, they have {TOTAL_FLOWERS}-{C}=<<{TOTAL_FLOWERS}-{C}={FINAL_FLOWERS}>>{FINAL_FLOWERS} flowers in their garden.\n#### {FINAL_FLOWERS}"
    )

    # Original values
    A, B, C = 2, 15, 5  # Flowers planted per day, days planting, flowers that did not grow
    original_name = "Ryan"

    # Name pools for name assignment
    common_names = ["Alex", "Taylor", "Jordan", "Morgan", "Casey"]
    uncommon_names = ["Haruto", "Mei", "Akira", "Riko", "Sora"]
    random_strings = ["Pqlzmkrt", "Lwxsnbrq", "Kdrmntpq", "Btxwvzlq", "Jmpqkzln"]

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
        modified_A, modified_B, modified_C = A, B, C
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(1, 10) if num != A])
        modified_B = random.choice([num for num in range(10, 21, 5) if num != B])
        modified_C = random.choice([num for num in range(2, 10) if num != C])

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_C *= multiplier

    if num_level == 4:
        # Use values within a scaled range for level 4
        modified_A = random.randint(multiplier, multiplier * 10)
        modified_C = random.randint(multiplier, multiplier * 9)

    # Calculate totals
    total_flowers = modified_A * modified_B
    final_flowers = total_flowers - modified_C

    A = modified_A
    B = modified_B
    C = modified_C

    original_values = {
        "A": A, "B": B, "C": C, "ans": (A * B) - C
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        total_flowers = f"{modified_A} * {modified_B}"
        final_flowers = f"{total_flowers} - {modified_C}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        TOTAL_FLOWERS=total_flowers,
        FINAL_FLOWERS=final_flowers
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
