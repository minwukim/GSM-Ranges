import random

def q56(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} ate a sandwich every day this week for lunch and used {B} slice(s) of cheese on each sandwich. "
        "They ate cheese and egg omelets for breakfast {A} days in the week, using {C} more slice(s) per omelet than they did per sandwich. "
        "They made a big dish of macaroni and cheese to last several dinners for the week and used {D} slice(s) of cheese in it. "
        "How many slices of cheese did {NAME} use in total?"
    )
    answer_text = (
        "The sandwiches used {B} * 7 = <<{B}*7={SANDWICH_CHEESE}>>{SANDWICH_CHEESE} slices of cheese for all 7 days.\n"
        "The omelets used {B} + {C} = <<{B}+{C}={OMELET_CHEESE_PER_DAY}>>{OMELET_CHEESE_PER_DAY} slices per day.\n"
        "They made {A} omelets, so they used {OMELET_CHEESE_PER_DAY} * {A} = <<{OMELET_CHEESE_PER_DAY}*{A}={TOTAL_OMELET_CHEESE}>>{TOTAL_OMELET_CHEESE} slices for breakfast.\n"
        "Finally, the macaroni and cheese used {D} slices.\n"
        "In total, they used {SANDWICH_CHEESE} + {TOTAL_OMELET_CHEESE} + {D} = <<{SANDWICH_CHEESE}+{TOTAL_OMELET_CHEESE}+{D}={TOTAL_CHEESE}>>{TOTAL_CHEESE} slices of cheese.\n#### {TOTAL_CHEESE}"
    )
    
    # Original values
    A, B, C, D = 3, 2, 1, 8  # Omelet days, slices per sandwich, extra slices per omelet, slices for macaroni

    # Name assignment logic
    common_names = ["Alex", "Jordan", "Taylor", "Chris", "Morgan"]
    uncommon_names = ["Hiro", "Aisha", "Mei", "Raj", "Lila"]
    random_strings = ["Xlyfrz", "Tmfqvs", "Prkltz", "Bgjwvs", "Lmzptq"]

    if name_level == 1:
        name = "Carl"
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
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(2, 8) if num != A])  # Omelet days
        modified_B = random.choice([num for num in range(2, 10) if num != B])  # Slices per sandwich
        modified_C = random.choice([num for num in range(2, 10) if num != C])  # Extra slices per omelet
        modified_D = random.choice([num for num in range(2, 10) if num != D])  # Slices for macaroni

        if num_level == 3:
            # Scale values for level 3
            modified_B *= multiplier
            modified_C *= multiplier
            modified_D *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_B = random.randint(multiplier, multiplier * 10 - 1)
            modified_C = random.randint(multiplier, multiplier * 10 - 1)
            modified_D = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    sandwich_cheese = 7 * modified_B
    omelet_cheese_per_day = modified_B + modified_C
    total_omelet_cheese = omelet_cheese_per_day * modified_A
    total_cheese = sandwich_cheese + total_omelet_cheese + modified_D

    # Prepare original values output
    original_values = {
        "A": modified_A,
        "B": modified_B,
        "C": modified_C,
        "D": modified_D,
        "ans": total_cheese
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D = '\'A\'', '\'B\'', '\'C\'', '\'D\''
        sandwich_cheese = f"{modified_B} * 7"
        omelet_cheese_per_day = f"{modified_B} + {modified_C}"
        total_omelet_cheese = f"{omelet_cheese_per_day} * {modified_A}"
        total_cheese = f"{sandwich_cheese} + {total_omelet_cheese} + {modified_D}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=name, A=modified_A, B=modified_B, C=modified_C, D=modified_D)
    answer = answer_text.format(
        NAME=name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        D=modified_D,
        SANDWICH_CHEESE=sandwich_cheese,
        OMELET_CHEESE_PER_DAY=omelet_cheese_per_day,
        TOTAL_OMELET_CHEESE=total_omelet_cheese,
        TOTAL_CHEESE=total_cheese
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer, "original_values": original_values}
