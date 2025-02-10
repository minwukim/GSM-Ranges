import random

def q4(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} went to the bakery and bought various types of pastries. She bought {A} dozen donuts which cost ${B} per dozen, "
        "{C} dozen mini cupcakes which cost ${D} per dozen, and {E} dozen mini cheesecakes for ${F} per dozen. "
        "How much was the total cost?"
    )
    answer_text = (
        "The total charge for the donuts was {A} x ${B} = $<<{A}*{B}={DONUTS_COST}>>{DONUTS_COST}.\n"
        "The total charge for the mini cupcakes was {C} x ${D} = $<<{C}*{D}={CUPCAKES_COST}>>{CUPCAKES_COST}.\n"
        "The total charge for the mini cheesecakes was {E} x ${F} = $<<{E}*{F}={CHEESECAKES_COST}>>{CHEESECAKES_COST}.\n"
        "Therefore the total amount {NAME} paid for the pastries was ${DONUTS_COST} + ${CUPCAKES_COST} + ${CHEESECAKES_COST} = $<<{DONUTS_COST}+{CUPCAKES_COST}+{CHEESECAKES_COST}={TOTAL_COST}>>{TOTAL_COST}.\n#### {TOTAL_COST}"
    )
    
    # Original values
    A, B = 3, 68   # Dozens of donuts and their cost per dozen
    C, D = 2, 80   # Dozens of mini cupcakes and their cost per dozen
    E, F = 6, 55   # Dozens of mini cheesecakes and their cost per dozen
    original_name = "Toula"

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        common_names = ["Sophia", "Emma", "Olivia", "Ava", "Isabella"]
        modified_name = random.choice(common_names)
    elif name_level == 3:
        uncommon_names = ["Haruka", "Nimrah", "Chihiro", "Mei", "Rinako"]
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        name_symbols = ["Z", "Y", "X"]
        modified_name = random.choice(name_symbols)
    elif name_level == 5:
        random_strings = ["Asdf123", "Qwe456", "Zxc789", "Plm101", "Jkl303"]
        modified_name = random.choice(random_strings)

    # Modify numbers based on num_level
    if num_level == 1:
        modified_A, modified_B = A, B
        modified_C, modified_D = C, D
        modified_E, modified_F = E, F
    else:
        # Level 2: Change numbers with the same digits but different values
        modified_A = random.choice([num for num in range(2, 10) if num != A])
        modified_B = random.choice([num for num in range(10, 100) if num != B])
        modified_C = random.choice([num for num in range(2, 10) if num != C])
        modified_D = random.choice([num for num in range(10, 100) if num != D])
        modified_E = random.choice([num for num in range(2, 10) if num != E])
        modified_F = random.choice([num for num in range(10, 100) if num != F])

        if num_level == 3:
            # Apply multiplier for level 3
            modified_A = modified_A * multiplier
            modified_C = modified_C * multiplier
            modified_E = modified_E * multiplier

    if num_level == 4:
        # Replace numbers with values in the range [100, 999]
        modified_A = random.randint(multiplier, multiplier * 10 - 1)
        modified_C = random.randint(multiplier, multiplier * 10 - 1)
        modified_E = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate the total costs for each pastry type and the overall cost
    donuts_cost = modified_A * modified_B
    cupcakes_cost = modified_C * modified_D
    cheesecakes_cost = modified_E * modified_F
    total_cost = donuts_cost + cupcakes_cost + cheesecakes_cost

    A = modified_A
    B = modified_B
    C = modified_C
    D = modified_D
    E = modified_E
    F = modified_F

    original_values = {
        "A": A, "B": B, "C": C, "D": D, "E": E, "F": F,
        "ans": A * B + C * D + E * F
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D, modified_E, modified_F = '\'A\'', '\'B\'', '\'C\'', '\'D\'', '\'E\'', '\'F\''
        donuts_cost = f"{modified_A} * {modified_B}"
        cupcakes_cost = f"{modified_C} * {modified_D}"
        cheesecakes_cost = f"{modified_E} * {modified_F}"
        total_cost = f"{donuts_cost} + {cupcakes_cost} + {cheesecakes_cost}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(
        NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D, E=modified_E, F=modified_F
    )
    answer = answer_text.format(
        NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D, E=modified_E, F=modified_F,
        DONUTS_COST=donuts_cost, CUPCAKES_COST=cupcakes_cost, CHEESECAKES_COST=cheesecakes_cost, TOTAL_COST=total_cost
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
