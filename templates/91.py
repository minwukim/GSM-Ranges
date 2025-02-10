import random

def q91(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "After scoring {A} points, {NAME1} now has {B} times more points than {NAME2}, who scored {C}. How many points did {NAME1} have before?"
    )
    answer_text = (
        "{NAME1} now has {B} times more points than {NAME2}, which is {B}*{C}= <<{B}*{C}={TRIPLE_POINTS}>>{TRIPLE_POINTS} more points than {NAME2}.\n"
        "This means {NAME1} has a total of {C}+{TRIPLE_POINTS} = <<{C}+{TRIPLE_POINTS}={CURRENT_POINTS}>>{CURRENT_POINTS} points now.\n"
        "Before, {NAME1} had {CURRENT_POINTS}-{A}= <<{CURRENT_POINTS}-{A}={BEFORE_POINTS}>>{BEFORE_POINTS} points\n#### {BEFORE_POINTS}"
    )

    # Original values
    A, B, C = 14, 3, 8  # Points scored by NAME1, times more points than NAME2, points scored by NAME2
    default_name1, default_name2 = "Erin", "Sara"

    # Handle name levels
    common_names = ["Alice", "Emma", "Sophia", "Michael", "Chris"]
    uncommon_names = ["Haruto", "Aisha", "Rinako", "Mingyu", "Takeshi"]
    random_strings = ["Xlyfrzq", "Tmfvbsk", "Pqrltzw", "Bgjwvsz", "Lmztpqv"]

    if name_level == 1:
        name1, name2 = default_name1, default_name2
    elif name_level == 2:
        names = random.sample([name for name in common_names if name not in [default_name1, default_name2]], 2)
        name1, name2 = names[0], names[1]
    elif name_level == 3:
        names = random.sample(uncommon_names, 2)
        name1, name2 = names[0], names[1]
    elif name_level == 4:
        name1, name2 = "Z", "Y"
    elif name_level == 5:
        names = random.sample(random_strings, 2)
        name1, name2 = names[0], names[1]

    # Handle number levels
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    else:
        modified_A = random.choice([num for num in range(10, 20) if num != A])  # Same digit, different
        modified_B = random.choice([num for num in range(3, 10) if num != B])  # Reasonable multiplier range
        modified_C = random.choice([num for num in range(7, 10) if num != C])  # Same digit, different

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier
        elif num_level == 4:
            modified_A = random.randint(multiplier, 2 * multiplier - 1)
            modified_B = random.randint(3 * multiplier, 10 * multiplier - 1)

    # Ensure positivity of calculations
    triple_points = modified_B * modified_C
    current_points = modified_C + triple_points
    before_points = current_points - modified_A

    # Save original values
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "ans": before_points
    }

    if is_symbolic:
        # Use symbolic variables
        modified_A, modified_B, modified_C = "'A'", "'B'", "'C'"
        triple_points = f"({modified_B}*{modified_C})"
        current_points = f"({modified_C}+{triple_points})"
        before_points = f"({current_points}-{modified_A})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=name1, NAME2=name2, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME1=name1, NAME2=name2, A=modified_A, B=modified_B, C=modified_C,
        TRIPLE_POINTS=triple_points, CURRENT_POINTS=current_points, BEFORE_POINTS=before_points
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
