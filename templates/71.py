import random

def q71(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original question and answer template
    question_text = (
        "{NAME} has {A} boxes with {B} marbles in each box. Then she gets {C} marbles from her friend. "
        "How many marbles does she have now?"
    )
    answer_text = (
        "{NAME} has {A} * {B} = <<({A})*({B})={BOX_MARBLES}>>{BOX_MARBLES} marbles from her boxes.\n"
        "So she has a total of ({BOX_MARBLES}) + ({C}) = <<({BOX_MARBLES})+({C})={TOTAL_MARBLES}>>{TOTAL_MARBLES} marbles now.\n#### {TOTAL_MARBLES}"
    )

    # Name levels
    original_name = "Maddison"
    common_names = ["Emma", "Olivia", "Sophia", "Ava", "Isabella"]
    uncommon_asian_names = ["Haruka", "Rinako", "Meiyu", "Kaede", "Jinhai"]
    random_strings = ["Xfjlspr", "Qwvbntz", "Klpfrwe", "Vmdzxup", "Tyrbfql"]

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

    # Original values
    A, B, C = 5, 50, 20  # Boxes, marbles per box, marbles from friend

    # Modify numbers based on num_level
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    else:
        # Level 2: Same digits, non-overlapping
        modified_A = random.choice([num for num in range(2, 10) if num != A])
        modified_B = random.choice([num for num in range(10, 100, 10) if num != B])
        modified_C = random.choice([num for num in range(10, 100) if num != C])

        if num_level == 3:
            # Multiply Level 2 values by multiplier
            modified_A *= multiplier
            # modified_B *= multiplier
            modified_C *= multiplier
        elif num_level == 4:
            # Random numbers in range (multiplier, 10 * multiplier - 1)
            modified_A = random.randint(multiplier, 10 * multiplier - 1)
            # modified_B = random.randint(multiplier, 10 * multiplier - 1)
            modified_C = random.randint(multiplier, 10 * multiplier - 1)

    # Ensure positivity
    total_marbles = modified_A * modified_B + modified_C

    # Save original values for symbolic mode
    original_values = {
        "A": modified_A,
        "B": modified_B,
        "C": modified_C,
        "ans": total_marbles
    }

    if is_symbolic:
        # Symbolic representation
        modified_A, modified_B, modified_C = "'A'", "'B'", "'C'"
        box_marbles = f"({modified_A}) * ({modified_B})"
        total_marbles = f"({box_marbles}) + ({modified_C})"
    else:
        box_marbles = modified_A * modified_B
        total_marbles = box_marbles + modified_C

    # Generate question and answer
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A, B=modified_B, C=modified_C,
        BOX_MARBLES=box_marbles,
        TOTAL_MARBLES=total_marbles
    )

    # Return values
    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
