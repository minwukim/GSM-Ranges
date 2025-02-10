import random

def q59(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} went to the store on Monday and bought {A} cakes. Tuesday she went to a different store and bought {B} times that number of cakes. "
        "On Wednesday she went to another store and bought {C} times the number of cakes she did on Tuesday. "
        "How many cakes did she buy after all three days?"
    )
    answer_text = (
        "On Monday she bought {A} cakes\n"
        "On Tuesday she bought {A} * {B} = <<{A}*{B}={TUESDAY_CAKES}>>{TUESDAY_CAKES} cakes\n"
        "On Wednesday she bought {TUESDAY_CAKES} * {C} = <<{TUESDAY_CAKES}*{C}={WEDNESDAY_CAKES}>>{WEDNESDAY_CAKES} cakes\n"
        "{NAME} bought a total of {A} + {TUESDAY_CAKES} + {WEDNESDAY_CAKES} = <<{A}+{TUESDAY_CAKES}+{WEDNESDAY_CAKES}={TOTAL_CAKES}>>{TOTAL_CAKES} cakes during the three days\n#### {TOTAL_CAKES}"
    )

    # Name levels
    original_name = "Rose"
    common_names = ["Emma", "Sophia", "Liam", "Noah", "Ava"]
    uncommon_names = ["Haruto", "Mei", "Rinako", "Yara", "Aisha"]
    random_strings = ["Xksjeow", "Tnspeqa", "Lkqpzvn", "Rmglqwe", "Fjqwksd"]

    if name_level == 1:
        name = original_name
    elif name_level == 2:
        name = random.choice([n for n in common_names if n != original_name])
    elif name_level == 3:
        name = random.choice(uncommon_names)
    elif name_level == 4:
        name = "Z"
    elif name_level == 5:
        name = random.choice(random_strings)

    # Original values
    A, B, C = 4, 3, 5  # Monday cakes, times on Tuesday, times on Wednesday

    # Number levels
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    else:
        # Level 2: Change numbers to same-digit alternatives
        modified_A = random.choice([num for num in range(2, 10) if num != A])
        modified_B = random.choice([num for num in range(2, 10) if num != B])
        modified_C = random.choice([num for num in range(2, 10) if num != C])
        
        # Level 3: Multiply by the multiplier
        if num_level == 3:
            modified_B *= multiplier

        # Level 4: Use a random range based on the multiplier
        elif num_level == 4:
            modified_B = random.randint(multiplier, multiplier * 10 - 1)

    # Ensure positivity
    tuesday_cakes = modified_A * modified_B
    wednesday_cakes = tuesday_cakes * modified_C
    total_cakes = modified_A + tuesday_cakes + wednesday_cakes

    # Symbolic mode
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "ans": total_cakes
    }

    if is_symbolic:
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        tuesday_cakes = f"{modified_A} * {modified_B}"
        wednesday_cakes = f"{tuesday_cakes} * {modified_C}"
        total_cakes = f"{modified_A} + {tuesday_cakes} + {wednesday_cakes}"

    # Format question and answer
    question = question_text.format(NAME=name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=name, A=modified_A, B=modified_B, C=modified_C,
        TUESDAY_CAKES=tuesday_cakes, WEDNESDAY_CAKES=wednesday_cakes, TOTAL_CAKES=total_cakes
    )

    return {"question": question, "answer": answer, "original_values": original_values}
