import random

def q84(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original question and answer templates
    question_text = (
        "{NAME} needs {A} ounces of sugar to make a batch of suckers and {B} ounces of sugar to make a batch of fudge. "
        "How much sugar does he need to make {C} batches of suckers and 1 batch of fudge?"
    )
    answer_text = (
        "First find the total sugar needed for the suckers: {A} ounces/batch * {C} batches = "
        "<<{A}*{C}={TOTAL_SUGAR_SUCKERS}>>{TOTAL_SUGAR_SUCKERS} ounces\n"
        "Then add the amount he needs to make the fudge to find the total amount of sugar needed: "
        "{TOTAL_SUGAR_SUCKERS} ounces + {B} ounces = <<{TOTAL_SUGAR_SUCKERS}+{B}={TOTAL_SUGAR}>>{TOTAL_SUGAR} ounces\n#### {TOTAL_SUGAR}"
    )

    # Extracted original values
    original_name = "Mason"
    A, B, C, D = 30, 70, 8, 1  # Suckers sugar/batch, Fudge sugar/batch, Batches of suckers, Batches of fudge

    # Handle name levels
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        common_names = ["Oliver", "Liam", "Sophia", "Emma", "Noah"]
        modified_name = random.choice([name for name in common_names if name != original_name])
    elif name_level == 3:
        uncommon_asian_names = ["Haruto", "Mei", "Aiko", "Raj", "Chen"]
        modified_name = random.choice(uncommon_asian_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=7))

    # Handle number levels
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    else:
        modified_A = random.choice([num for num in range(10, 100, 10) if num != A])
        modified_B = random.choice([num for num in range(10, 100, 10) if num != B])
        modified_C = random.choice([num for num in range(2, 10) if num != C])

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier
            # modified_C *= multiplier
        elif num_level == 4:
            modified_A = random.randint(multiplier, 10 * multiplier - 1)
            modified_B = random.randint(multiplier, 10 * multiplier - 1)
            # modified_C = random.randint(multiplier, 10 * multiplier - 1)

    # Calculate totals
    total_sugar_suckers = modified_A * modified_C
    total_sugar = total_sugar_suckers + modified_B

    # Save original values before modification for symbolic mode
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "ans": total_sugar
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = "'A'", "'B'", "'C'"
        total_sugar_suckers = f"({modified_A} * {modified_C})"
        total_sugar = f"({total_sugar_suckers} + {modified_B})"

    # Format the question and answer with modified values
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        TOTAL_SUGAR_SUCKERS=total_sugar_suckers,
        TOTAL_SUGAR=total_sugar
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
