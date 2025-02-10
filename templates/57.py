import random

def q57(num_level=1, multiplier=10000, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} had {A} green pens and {B} yellow pens. Then {NAME1} bought {C} bags of blue pens and {D} bags of red pens. "
        "There were {E} pens in each bag of blue and {F} pens in each bag of red. "
        "How many pens does {NAME1} have now?"
    )
    answer_text = (
        "{NAME1} previously had {A} + {B} = <<{A}+{B}={INITIAL_PENS}>>{INITIAL_PENS} pens.\n"
        "The number of blue pens is {C} x {E} = <<{C}*{E}={BLUE_PENS}>>{BLUE_PENS}.\n"
        "The number of red pens is {D} x {F} = <<{D}*{F}={RED_PENS}>>{RED_PENS}.\n"
        "{NAME1} has {INITIAL_PENS} + {BLUE_PENS} + {RED_PENS} = <<{INITIAL_PENS}+{BLUE_PENS}+{RED_PENS}={TOTAL_PENS}>>{TOTAL_PENS} pens now.\n#### {TOTAL_PENS}"
    )
    
    # Original values
    A, B, C, D, E, F = 22, 10, 6, 2, 9, 6  # Green pens, yellow pens, blue bag count, red bag count, pens per blue bag, pens per red bag

    # Dynamic naming
    common_names = ["Sam", "Emma", "Chris", "Alex", "Taylor"]
    uncommon_names = ["Hiro", "Aisha", "Mei", "Raj", "Lila"]
    random_strings = ["Xlyfrz", "Tmfqvs", "Prkltz", "Bgjwvs", "Lmzptq"]

    if name_level == 1:
        name1 = "Janet"
    elif name_level == 2:
        name1 = random.choice(common_names)
    elif name_level == 3:
        name1 = random.choice(uncommon_names)
    elif name_level == 4:
        name1 = "Z"
    elif name_level == 5:
        name1 = random.choice(random_strings)

    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B, modified_C, modified_D, modified_E, modified_F = A, B, C, D, E, F
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(10, 25) if num != A])  # Green pens
        modified_B = random.choice([num for num in range(10, 20) if num != B])  # Yellow pens
        modified_C = random.choice([num for num in range(2, 10) if num != C])  # Blue bags
        modified_D = random.choice([num for num in range(2, 10) if num != D])  # Red bags
        modified_E = random.choice([num for num in range(2, 10) if num != E])  # Pens per blue bag
        modified_F = random.choice([num for num in range(2, 10) if num != F])  # Pens per red bag

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_B *= multiplier
            modified_C *= multiplier
            modified_D *= multiplier
        
        elif num_level == 4:
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_B = random.randint(multiplier, multiplier * 10 - 1)
            modified_C = random.randint(multiplier, multiplier * 10 - 1)
            modified_D = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    initial_pens = modified_A + modified_B
    blue_pens = modified_C * modified_E
    red_pens = modified_D * modified_F
    total_pens = initial_pens + blue_pens + red_pens

    # Original values with modifications
    original_values = {
        "A": modified_A,
        "B": modified_B,
        "C": modified_C,
        "D": modified_D,
        "E": modified_E,
        "F": modified_F,
        "ans": total_pens
    }

    if is_symbolic:
        # Represent numbers symbolically with escaped quotes
        modified_A, modified_B, modified_C, modified_D, modified_E, modified_F = '\'A\'', '\'B\'', '\'C\'', '\'D\'', '\'E\'', '\'F\''
        initial_pens = f"{modified_A} + {modified_B}"
        blue_pens = f"{modified_C} * {modified_E}"
        red_pens = f"{modified_D} * {modified_F}"
        total_pens = f"{initial_pens} + {blue_pens} + {red_pens}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=name1, A=modified_A, B=modified_B, C=modified_C, D=modified_D, E=modified_E, F=modified_F)
    answer = answer_text.format(
        NAME1=name1,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        D=modified_D,
        E=modified_E,
        F=modified_F,
        INITIAL_PENS=initial_pens,
        BLUE_PENS=blue_pens,
        RED_PENS=red_pens,
        TOTAL_PENS=total_pens
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
