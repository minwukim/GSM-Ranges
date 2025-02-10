import random

def q67(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} had {A} french fries, but {NAME2} took {B} of them. {NAME3} took twice as many as {NAME2}. "
        "{NAME4} gave {NAME1} a handful of her fries, and then {NAME5} took from {NAME1} {C} less than the number of fries that {NAME2} had taken. "
        "If in the end {NAME1} had {D} fries, how many fries did {NAME4} give {NAME1}?"
    )
    answer_text = (
        "{NAME1} had {A} french fries, but {NAME2} took {B} of them.\n"
        "{NAME3} took twice as many as {NAME2}, removing 2*{B}=<<2*{B}={BILLY_TAKES}>>{BILLY_TAKES} fries.\n"
        "{NAME5} took {C} less than the number of fries that {NAME2} had taken, removing {B}-{C}=<<{B}-{C}={COLBY_TAKES}>>{COLBY_TAKES} fries.\n"
        "If we let X be the number of fries given to {NAME1} by {NAME4}, then {A}-{B}-{BILLY_TAKES}-{COLBY_TAKES}+X={D}\n"
        "Thus, {NAME4} had given {NAME1} X={GINGER_GIVES} fries\n#### {GINGER_GIVES}"
    )

    # Names in the original question
    original_names = ["Griffin", "Kyle", "Billy", "Ginger", "Colby"]
    common_names = ["Alice", "Jack", "Sophia", "Michael", "Emma"]
    uncommon_names = ["Haruto", "Mei", "Aisha", "Raj", "Lila"]
    random_strings = ["Xlyfrzq", "Tmfnvps", "Prklzxc", "Bgjwsqv", "Lmzptkx"]

    # Dynamic name generation based on levels
    if name_level == 1:
        modified_names = original_names
    elif name_level == 2:
        modified_names = random.sample([name for name in common_names if name not in original_names], 5)
    elif name_level == 3:
        modified_names = random.sample(uncommon_names, 5)
    elif name_level == 4:
        modified_names = ["Z", "Y", "X", "W", "V"]
    elif name_level == 5:
        modified_names = random.sample(random_strings, 5)

    NAME1, NAME2, NAME3, NAME4, NAME5 = modified_names

    # Original values
    A, B, C, D = 24, 5, 3, 27

    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        # Level 2: Same digit, different value
        modified_B = random.choice([num for num in range(3, 6) if num != B])
        modified_A = random.choice([num for num in range(modified_B * 4, 30) if num != A])
        modified_C = random.choice([num for num in range(2, modified_B) if num != C])
        modified_D = random.choice([num for num in range(40, 100) if num != D])

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier
            modified_C *= multiplier
            modified_D *= multiplier
        elif num_level == 4:
            modified_B = random.randint(multiplier + 1, 2 * multiplier - 1)
            modified_A = random.randint(modified_B * 4,  10 * multiplier)
            modified_C = random.randint(multiplier, modified_B - 1)
            modified_D = random.randint(5 * multiplier, 10 * multiplier - 1)

    # Calculations
    billy_takes = 2 * modified_B
    colby_takes = modified_B - modified_C
    ginger_gives = modified_D - (modified_A - modified_B - billy_takes - colby_takes)

    # Original values for symbolic case
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "D": modified_D, "ans": ginger_gives
    }

    if is_symbolic:
        modified_A, modified_B, modified_C, modified_D = "'A'", "'B'", "'C'", "'D'"
        billy_takes = f"(2*{modified_B})"
        colby_takes = f"({modified_B}-{modified_C})"
        ginger_gives = f"({modified_D}-({modified_A}-{modified_B}-{billy_takes}-{colby_takes}))"

    # Generate question and answer
    question = question_text.format(NAME1=NAME1, NAME2=NAME2, NAME3=NAME3, NAME4=NAME4, NAME5=NAME5, A=modified_A, B=modified_B, C=modified_C, D=modified_D)
    answer = answer_text.format(
        NAME1=NAME1, NAME2=NAME2, NAME3=NAME3, NAME4=NAME4, NAME5=NAME5,
        A=modified_A, B=modified_B, C=modified_C, D=modified_D,
        BILLY_TAKES=billy_takes, COLBY_TAKES=colby_takes, GINGER_GIVES=ginger_gives
    )

    return {"question": question, "answer": answer, "original_values": original_values}
