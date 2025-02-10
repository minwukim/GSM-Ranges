import random

def q44(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} is trying to decide whether to do {POSSESSIVE} taxes herself or hire an accountant. "
        "If she does the taxes herself, she'll be able to do {A} fewer hours of freelance work, losing ${B}/hour in missed income. "
        "The accountant charges ${C}. How much more money will she have if she hires the accountant?"
    )
    answer_text = (
        "First, calculate the total lost revenue if {NAME} does her taxes herself: ${B}/hour * {A} hours = $<<{B}*{A}={LOST_INCOME}>>{LOST_INCOME}.\n"
        "Next, subtract the accountant's charge to find the savings: ${LOST_INCOME} - ${C} = $<<{LOST_INCOME}-{C}={SAVINGS}>>{SAVINGS}.\n#### {SAVINGS}"
    )
    
    # Name variations
    common_names = ["Jackie", "Sophia", "Emily", "Olivia", "Lily"]
    uncommon_names = ["Ariana", "Maeve", "Isla", "Leilani", "Evangeline"]
    random_names = ["Xyra", "Pluto", "Zyvia", "Wynora", "Klyne"]

    # Select name and possessive variation
    if name_level == 1:
        name = "Jackie"
    elif name_level == 2:
        name = random.choice(common_names)
    elif name_level == 3:
        name = random.choice(uncommon_names)
    elif name_level == 4:
        name = "Z"
    elif name_level == 5:
        name = random.choice(random_names)
    possessive = f"{name}'s" if not name.endswith("s") else f"{name}'"

    # Original values
    A, B, C = 3, 35, 90  # Hours of missed work, hourly income, accountant's fee

    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B, modified_C = A, B, C
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(3, 6) if num != A])
        modified_B = random.choice([num for num in range(40, 61, 5) if num != B])
        modified_C = random.choice([num for num in range(60, 100, 10) if num != C])

        if num_level == 3:
            # Scale values for level 3
            modified_B *= multiplier
            modified_C *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_B = random.randint(multiplier, multiplier * 10 - 1)
            modified_C = random.randint(multiplier, modified_A * modified_B)

    # Calculate totals
    lost_income = modified_B * modified_A
    savings = lost_income - modified_C

    # Prepare original and modified values
    original_values = {
        "A": modified_A, 
        "B": modified_B, 
        "C": modified_C, 
        "ans": savings
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        lost_income = f"{modified_B} * {modified_A}"
        savings = f"{lost_income} - {modified_C}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=name, POSSESSIVE=possessive, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        LOST_INCOME=lost_income,
        SAVINGS=savings
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
