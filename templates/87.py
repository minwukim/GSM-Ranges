import random

def q87(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "After {NAME} saved some money, she then spent the rest of her money on an ${A} sweater and gave her brother ${B}. "
        "If she had ${C} in the beginning, how much did {NAME} save?"
    )
    answer_text = (
        "{NAME} spent and gave her brother a total of {A} + {B} = $<<{A}+{B}={TOTAL_SPENT}>>{TOTAL_SPENT}.\n"
        "So, she saved {C} - {TOTAL_SPENT} = $<<{C}-{TOTAL_SPENT}={SAVED_AMOUNT}>>{SAVED_AMOUNT}.\n#### {SAVED_AMOUNT}"
    )

    # Extract original values
    original_name = "Andrea"
    A, B, C = 11, 4, 36  # Sweater cost, money given to brother, initial money

    # Name adjustments based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        common_names = ["Emma", "Sophia", "Olivia", "Mia", "Charlotte"]
        modified_name = random.choice(common_names)
    elif name_level == 3:
        uncommon_names = ["Haruka", "Meilin", "Kaede", "Rinako", "Takeshi"]
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=7))

    # Number adjustments based on num_level
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    elif num_level == 2:
        modified_A = random.choice([num for num in range(10, 30) if num != A])
        modified_B = random.choice([num for num in range(1, 10) if num != B])
        modified_C = random.choice([num for num in range(40, 100) if num != C])
    elif num_level == 3:
        modified_A = random.choice([num for num in range(10, 30) if num != A]) * multiplier
        modified_B = random.choice([num for num in range(1, 10) if num != B]) * multiplier
        modified_C = random.choice([num for num in range(40, 100) if num != C]) * multiplier
    elif num_level == 4:
        modified_A = random.randint(multiplier, multiplier * 3)
        modified_B = random.randint(multiplier, multiplier * 3)
        modified_C = random.randint(multiplier * 7, multiplier * 10 - 1)

    # Ensure positivity in calculations
    total_spent = modified_A + modified_B
    saved_amount = modified_C - total_spent

    # Adjust if is_symbolic is True
    original_values = {
        "A": modified_A,
        "B": modified_B,
        "C": modified_C,
        "ans": saved_amount
    }

    if is_symbolic:
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        total_spent = f"({modified_A} + {modified_B})"
        saved_amount = f"({modified_C} - {total_spent})"

    # Replace placeholders in question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        TOTAL_SPENT=total_spent,
        SAVED_AMOUNT=saved_amount
    )

    return {"question": question, "answer": answer, "original_values": original_values if is_symbolic else None}
