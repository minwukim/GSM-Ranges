import random

def q90(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "To be promoted to the next school year, {NAME} takes {A} tests that together must total at least {B} points. "
        "On {NAME}'s first test, {NAME} scored {C} points, on the second test {NAME} scored {D} points. "
        "What is the minimum number of points {NAME} must score on the third test to pass?"
    )
    answer_text = (
        "Adding the points obtained in the first two tests, {NAME} scored {C} + {D} = <<{C}+{D}={TOTAL_FIRST_TWO}>>{TOTAL_FIRST_TWO} points.\n"
        "To pass, {NAME} must score {B} - {TOTAL_FIRST_TWO} = <<{B}-{TOTAL_FIRST_TWO}={MINIMUM_POINTS}>>{MINIMUM_POINTS} points.\n#### {MINIMUM_POINTS}"
    )

    # Names
    original_name = "Jane"
    common_names = ["Alice", "Sophia", "Emma", "Olivia", "Mia"]
    uncommon_names = ["Haruka", "Mei", "Aisha", "Rin", "Kaede"]
    random_strings = ["Fjskdfl", "Qwpertz", "Xmplsht", "Nkydfgh", "Zplmcqr"]

    # Name modification based on level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        modified_name = random.choice([name for name in common_names if name != original_name])
    elif name_level == 3:
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = random.choice(random_strings)

    # Original values
    A, B, C, D = 3, 42, 15, 18

    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        # Level 2: Numbers of the same digit
        modified_A = random.choice([num for num in range(2, 10) if num != A])  
        modified_B = random.choice([num for num in range(40, 50) if num != B])
        modified_C = random.choice([num for num in range(10, 20) if num != C])
        modified_D = random.choice([num for num in range(10, 20) if num != D])

        if num_level == 3:
            # Multiply Level 2 numbers by the multiplier
            modified_A = modified_A * multiplier
            modified_B = modified_B * multiplier
            modified_C = modified_C * multiplier
            modified_D = modified_D * multiplier

        elif num_level == 4:
            # Random numbers in range (multiplier, 10 * multiplier - 1)
            modified_A = random.randint(multiplier, 10 * multiplier - 1)
            modified_B = random.randint(5 * multiplier, 10 * multiplier - 1)
            modified_C = random.randint(multiplier, 2 * multiplier)
            modified_D = random.randint(multiplier, 2 * multiplier)

    # Ensure positivity of the remaining score
    total_first_two = modified_C + modified_D
    minimum_points = max(modified_B - total_first_two, 0)

    # Save original values
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "D": modified_D,
        "ans": minimum_points
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D = '\'A\'', '\'B\'', '\'C\'', '\'D\''
        total_first_two = f"({modified_C} + {modified_D})"
        minimum_points = f"({modified_B} - {total_first_two})"

    # Replace placeholders in question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D)
    answer = answer_text.format(
        NAME=modified_name,
        C=modified_C, D=modified_D,
        B=modified_B, TOTAL_FIRST_TWO=total_first_two,
        MINIMUM_POINTS=minimum_points
    )

    return {"question": question, "answer": answer, "original_values": original_values}
