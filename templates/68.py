import random

def q68(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} had {A} apps on his tablet. He deleted {B} apps he didn't use anymore and downloaded {C} more. "
        "How many apps are on his tablet now?"
    )
    answer_text = (
        "{NAME} had {A} - {B} = <<{A}-{B}={REMAINING_APPS}>>{REMAINING_APPS} apps after deleting the ones he didn't use.\n"
        "After downloading some more he now has {REMAINING_APPS} + {C} = <<{REMAINING_APPS}+{C}={TOTAL_APPS}>>{TOTAL_APPS} apps on his tablet.\n#### {TOTAL_APPS}"
    )

    # Name options
    common_names = ["Emma", "Sophia", "Liam", "Mason", "Olivia"]
    uncommon_names = ["Haruto", "Mei", "Aarav", "Yumi", "Zhi"]
    random_strings = ["Vxzkqpl", "Trmjzsd", "Fkqpwvl", "Qnxlptz", "Bsrwdcf"]

    # Dynamic name generation
    if name_level == 1:
        name = "Travis"
    elif name_level == 2:
        name = random.choice([n for n in common_names if n != "Travis"])
    elif name_level == 3:
        name = random.choice(uncommon_names)
    elif name_level == 4:
        name = "Z"
    elif name_level == 5:
        name = random.choice(random_strings)

    # Original values
    A, B, C = 61, 9, 18  # A = original apps, B = deleted apps, C = downloaded apps

    # Ensure positivity: A > B
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    else:
        # Level 2: Same digit values, ensure A > B
        modified_A = random.choice([num for num in range(10, 100) if num != A])
        modified_B = random.choice([num for num in range(5, 10) if num != B])
        modified_C = random.choice([num for num in range(10, 100) if num != C])

        if num_level == 3:
            # Level 3: Multiply level 2 numbers by multiplier
            modified_A, modified_B, modified_C = modified_A * multiplier, modified_B * multiplier, modified_C * multiplier
        elif num_level == 4:
            # Level 4: Random values in range (multiplier, 10 * multiplier - 1)
            modified_A = random.randint(multiplier + 1, multiplier * 10 - 1)
            modified_B = random.randint(multiplier, modified_A - 1)
            modified_C = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate final apps
    remaining_apps = modified_A - modified_B
    total_apps = remaining_apps + modified_C

    # Save original values before modifying for symbolic mode
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "ans": total_apps
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = "'A'", "'B'", "'C'"
        remaining_apps = f"({modified_A} - {modified_B})"
        total_apps = f"({remaining_apps} + {modified_C})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=name, A=modified_A, B=modified_B, C=modified_C,
        REMAINING_APPS=remaining_apps, TOTAL_APPS=total_apps
    )

    return {"question": question, "answer": answer, "original_values": original_values}
