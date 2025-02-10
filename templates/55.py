import random

def q55(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} grows grapes on their {A}-acre farm. Each acre produces {B} tons of grapes per year, "
        "and each ton of grapes makes {C} barrels of wine. How many barrels of wine does their farm produce per year?"
    )
    answer_text = (
        "If each acre produces {B} tons of grapes per year, then their {A}-acre farm produces {A} * {B} = "
        "<<{A}*{B}={TOTAL_TONS}>>{TOTAL_TONS} tons of grapes per year.\n"
        "If each ton of grapes makes {C} barrels of wine, then {TOTAL_TONS} tons makes {C} * {TOTAL_TONS} = "
        "<<{C}*{TOTAL_TONS}={TOTAL_BARRELS}>>{TOTAL_BARRELS} barrels of wine per year.\n#### {TOTAL_BARRELS}"
    )
    
    # Original values
    A, B, C = 10, 5, 2  # Acres, tons of grapes per acre, barrels of wine per ton

    # Dynamic name generation (excluding original names)
    common_names = ["Sam", "Emma", "Chris", "Alex", "Taylor"]
    uncommon_names = ["Hiro", "Aisha", "Mei", "Raj", "Lila"]
    random_strings = ["Xlyfrz", "Tmfqvs", "Prkltz", "Bgjwvs", "Lmzptq"]

    if name_level == 1:
        name = "Josie"
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
        modified_A = random.choice([num for num in range(10, 21, 5) if num != A])  # Acres
        modified_B = random.choice([num for num in range(2, 10) if num != B])  # Tons of grapes per acre
        modified_C = random.choice([num for num in range(2, 10) if num != C])  # Barrels per ton

        if num_level == 3:
            # Scale values for level 3
            modified_C *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_C = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    total_tons = modified_A * modified_B
    total_barrels = total_tons * modified_C

    # Prepare original values dictionary
    original_values = {
        "A": modified_A,
        "B": modified_B,
        "C": modified_C,
        "ans": modified_A * modified_B * modified_C
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        total_tons = f"{modified_A} * {modified_B}"
        total_barrels = f"{total_tons} * {modified_C}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        A=modified_A,
        B=modified_B,
        C=modified_C,
        TOTAL_TONS=total_tons,
        TOTAL_BARRELS=total_barrels
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
