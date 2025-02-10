import random

def q73(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Question and answer templates
    question_text = (
        "It's April, and {NAME} has been busy on her farm planting different types of vegetables for the season. "
        "She has bought {A} packets of tomato seeds and {B} packets of celery seeds to plant. "
        "If a packet of tomato seeds costs ${C} and a packet of celery seeds costs ${D}, "
        "how much money did she use to buy the seeds?"
    )

    answer_text = (
        "The total amount of money she used to buy the tomato seeds is {A} * {C} = $<<{A}*{C}={TOTAL_TOMATO}>>{TOTAL_TOMATO}\n"
        "The celery seeds cost her {B} * {D} = $<<{B}*{D}={TOTAL_CELERY}>>{TOTAL_CELERY}\n"
        "For the seeds, {NAME} paid {TOTAL_CELERY} + {TOTAL_TOMATO} = $<<{TOTAL_CELERY}+{TOTAL_TOMATO}={TOTAL_COST}>>{TOTAL_COST}\n#### {TOTAL_COST}"
    )

    # Name handling
    original_name = "Mrs. Rylan"
    common_names = ["Alice", "Emma", "Sophia", "Olivia", "Mia"]
    uncommon_names = ["Haruka", "Mei", "Aisha", "Yara", "Rinako"]
    random_strings = ["Trqjvbn", "Xplwzke", "Bgfstun", "Qwerplm", "Tzksjdn"]

    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        modified_name = random.choice(common_names)
    elif name_level == 3:
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = random.choice(random_strings)

    # Original values
    A, B, C, D = 20, 80, 40, 30  # Packets of tomato seeds, celery seeds, and their costs

    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        # Level 2: Same digit, but different numbers
        modified_A = random.choice([num for num in range(10, 100) if num != A and num % 10 == 0])
        modified_B = random.choice([num for num in range(10, 100) if num != B and num % 10 == 0])
        modified_C = random.choice([num for num in range(10, 100, 10) if num != C])
        modified_D = random.choice([num for num in range(10, 100, 10) if num != D])

        if num_level == 3:
            # Multiply Level 2 numbers by multiplier
            modified_B *= multiplier
            modified_C *= multiplier
        elif num_level == 4:
            # Random values in a range (multiplier, 10 * multiplier - 1)
            modified_B = random.randint(multiplier, 10 * multiplier - 1)
            modified_C = random.randint(multiplier, 10 * multiplier - 1)

    # Calculate totals
    total_tomato = modified_A * modified_C
    total_celery = modified_B * modified_D
    total_cost = total_tomato + total_celery

    # Prepare original values before modifying symbolic placeholders
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "D": modified_D, "ans": total_cost
    }

    if is_symbolic:
        # Replace numbers with symbolic representations
        modified_A, modified_B, modified_C, modified_D = "'A'", "'B'", "'C'", "'D'"
        total_tomato = f"({modified_A} * {modified_C})"
        total_celery = f"({modified_B} * {modified_D})"
        total_cost = f"({total_celery} + {total_tomato})"

    # Generate question and answer
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A, B=modified_B, C=modified_C, D=modified_D,
        TOTAL_TOMATO=total_tomato, TOTAL_CELERY=total_celery, TOTAL_COST=total_cost
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
