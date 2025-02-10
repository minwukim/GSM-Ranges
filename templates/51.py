import random

def q51(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} collects peaches for {A} hours. {NAME} can collect {B} peaches a minute. How many peaches does {NAME} collect?"
    )
    answer_text = (
        "{NAME} is collecting peaches for {A} * 60 = <<{A}*60={TOTAL_MINUTES}>>{TOTAL_MINUTES} minutes.\n"
        "So {NAME} can collect {TOTAL_MINUTES} * {B} = <<{TOTAL_MINUTES}*{B}={TOTAL_PEACHES}>>{TOTAL_PEACHES} peaches.\n#### {TOTAL_PEACHES}"
    )
    
    # Original values
    A, B = 3, 2  # Hours collecting peaches, peaches per minute
    
    # Dynamic name generation (excluding "John")
    common_names = ["Emma", "Chris", "Taylor", "Alex", "Sam"]
    uncommon_names = ["Hiro", "Aisha", "Mei", "Raj", "Lila"]
    random_strings = ["Zjfplx", "Tkmqsr", "Xrvywb", "Plzqtw", "Msnjvq"]

    if name_level == 1:
        name = "John"
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
        modified_A, modified_B = A, B
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(2, 10) if num != A])  # Hours
        modified_B = random.choice([num for num in range(2, 10) if num != B])  # Peaches per minute

        if num_level == 3:
            # Scale values for level 3
            modified_B *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_B = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    total_minutes = modified_A * 60
    total_peaches = total_minutes * modified_B

    # Prepare original and modified values
    original_values = {
        "A": modified_A, 
        "B": modified_B, 
        "ans": total_peaches
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B = "\'A\'", "\'B\'"
        total_minutes = f"{modified_A} * 60"
        total_peaches = f"{total_minutes} * {modified_B}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=name, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME=name,
        A=modified_A,
        B=modified_B,
        TOTAL_MINUTES=total_minutes,
        TOTAL_PEACHES=total_peaches
    )

    return {"question": question, "answer": answer, "original_values": original_values}
