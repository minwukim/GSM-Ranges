import random

def q52(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} wants to buy new crayons. They need them in {A} different colors and prepared ${B} for this purchase. "
        "One crayon costs ${C}. How much change will they get?"
    )
    answer_text = (
        "{NAME} is going to pay {A} * {C} = $<<{A}*{C}={TOTAL_COST}>>{TOTAL_COST} for the crayons they want.\n"
        "If they pay ${B}, they will get {B} - {TOTAL_COST} = $<<{B}-{TOTAL_COST}={CHANGE}>>{CHANGE} of change.\n#### {CHANGE}"
    )
    
    # Original values
    A, B, C = 5, 20, 2  # Number of crayons, prepared amount, cost per crayon
    
    # Dynamic name assignment (excluding original names)
    common_names = ["Sam", "Emma", "Chris", "Alex", "Taylor"]
    uncommon_names = ["Hiro", "Aisha", "Mei", "Raj", "Lila"]
    random_strings = ["Xlyfrz", "Tmfqvs", "Prkltz", "Bgjwvs", "Lmzptq"]

    if name_level == 1:
        name = "Violetta"
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
        modified_A = random.choice([num for num in range(2, 6) if num != A])  # Number of crayons
        modified_B = random.choice([num for num in range(20, 91, 10) if num != B])  # Prepared amount
        modified_C = random.choice([num for num in range(1, 4) if num != C])  # Cost per crayon

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_B *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier, multiplier * 2)
            modified_B = random.randint(multiplier * 9, multiplier * 10 - 1)

    # Calculate totals
    total_cost = modified_A * modified_C
    change = modified_B - total_cost

    # Prepare original values dictionary
    original_values = {
        "A": modified_A,
        "B": modified_B,
        "C": modified_C,
        "ans": modified_B - (modified_A * modified_C)
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = "'A'", "'B'", "'C'"
        total_cost = f"{modified_A} * {modified_C}"
        change = f"{modified_B} - {total_cost}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        TOTAL_COST=total_cost,
        CHANGE=change
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer, "original_values": original_values}
