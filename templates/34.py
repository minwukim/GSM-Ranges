import random

def q34(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1}'s mother sells watermelons, peppers, and oranges at the local store. "
        "One watermelon costs {A} times what each pepper costs. An orange costs {B} less than what a watermelon costs. "
        "{NAME2} is sent to the store to buy {C} watermelons, {D} peppers, and {E} oranges. "
        "What's the total amount of money they will spend if each pepper costs ${F}?"
    )
    answer_text = (
        "A watermelon costs {A} times what a pepper costs, which is {A} * {F} = $<<{A}*{F}={WATERMELON_COST}>>{WATERMELON_COST}.\n"
        "An orange costs {WATERMELON_COST} - {B} = $<<{WATERMELON_COST}-{B}={ORANGE_COST}>>{ORANGE_COST}.\n"
        "{NAME2} buys {C} watermelons at a total cost of {WATERMELON_COST} * {C} = $<<{WATERMELON_COST}*{C}={TOTAL_WATERMELONS_COST}>>{TOTAL_WATERMELONS_COST}.\n"
        "They also purchase peppers at a total cost of {D} * {F} = $<<{D}*{F}={TOTAL_PEPPERS_COST}>>{TOTAL_PEPPERS_COST}.\n"
        "The oranges cost a total of {E} * {ORANGE_COST} = $<<{E}*{ORANGE_COST}={TOTAL_ORANGES_COST}>>{TOTAL_ORANGES_COST}.\n"
        "The total amount spent is {TOTAL_WATERMELONS_COST} + {TOTAL_PEPPERS_COST} + {TOTAL_ORANGES_COST} = $<<{TOTAL_WATERMELONS_COST}+{TOTAL_PEPPERS_COST}+{TOTAL_ORANGES_COST}={TOTAL_COST}>>{TOTAL_COST}.\n#### {TOTAL_COST}"
    )
    
    # Original values
    A, B, C, D, E, F = 3, 5, 4, 20, 10, 15
    name1, name2 = "Well", "Dillon"

    # Name pools
    common_names = ["Alice", "Jack", "Sophia", "Michael", "Emma"]
    uncommon_names = ["Haruto", "Yara", "Chen", "Aisha", "Mei"]
    random_strings = ["Xnlqyzrm", "Wrjktzqp", "Zmtplvks", "Ncrvwxyl", "Qvlprnxk"]

    # Assign names based on name_level
    if name_level == 1:
        modified_name1, modified_name2 = name1, name2
    elif name_level == 2:
        modified_name1 = random.choice(common_names)
        modified_name2 = random.choice([name for name in common_names if name != modified_name1])
    elif name_level == 3:
        modified_name1 = random.choice(uncommon_names)
        modified_name2 = random.choice([name for name in uncommon_names if name != modified_name1])
    elif name_level == 4:
        modified_name1, modified_name2 = "Z", "Y"
    elif name_level == 5:
        modified_name1 = random.choice(random_strings)
        modified_name2 = random.choice([name for name in random_strings if name != modified_name1])

    # Modify the values for levels > 1
    if num_level > 1:
        modified_A = random.choice([num for num in range(2, 10) if num != A])
        modified_B = random.choice([num for num in range(2, 10) if num != B])
        modified_C = random.choice([num for num in range(2, 10) if num != C])
        modified_D = random.choice([num for num in range(10, 91, 10) if num != D])
        modified_E = random.choice([num for num in range(10, 91, 10) if num != E])
        modified_F = random.choice([num for num in range(10, 91, 5) if num != F])

        if num_level == 3:
            modified_F *= multiplier
        elif num_level == 4:
            modified_F = random.randint(multiplier, multiplier * 10 - 1)
    else:
        modified_A, modified_B, modified_C, modified_D, modified_E, modified_F = A, B, C, D, E, F

    # Calculate costs
    watermelon_cost = modified_A * modified_F
    orange_cost = watermelon_cost - modified_B
    total_watermelons_cost = modified_C * watermelon_cost
    total_peppers_cost = modified_D * modified_F
    total_oranges_cost = modified_E * orange_cost
    total_cost = total_watermelons_cost + total_peppers_cost + total_oranges_cost

    A = modified_A
    B = modified_B
    C = modified_C
    D = modified_D
    E = modified_E
    F = modified_F

    original_values = {
        "A": A, "B": B, "C": C, "D": D, "E": E, "F": F,
        "ans": total_cost
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D, modified_E, modified_F = '\'A\'', '\'B\'', '\'C\'', '\'D\'', '\'E\'', '\'F\''
        watermelon_cost = f"{modified_A} * {modified_F}"
        orange_cost = f"{watermelon_cost} - {modified_B}"
        total_watermelons_cost = f"{watermelon_cost} * {modified_C}"
        total_peppers_cost = f"{modified_D} * {modified_F}"
        total_oranges_cost = f"{modified_E} * {orange_cost}"
        total_cost = f"{total_watermelons_cost} + {total_peppers_cost} + {total_oranges_cost}"

        return {
            "question": question_text.format(NAME1=modified_name1, NAME2=modified_name2, A=modified_A, B=modified_B, C=modified_C, D=modified_D, E=modified_E, F=modified_F),
            "answer": answer_text.format(
                NAME1=modified_name1,
                NAME2=modified_name2,
                A=modified_A,
                B=modified_B,
                C=modified_C,
                D=modified_D,
                E=modified_E,
                F=modified_F,
                WATERMELON_COST=watermelon_cost,
                ORANGE_COST=orange_cost,
                TOTAL_WATERMELONS_COST=total_watermelons_cost,
                TOTAL_PEPPERS_COST=total_peppers_cost,
                TOTAL_ORANGES_COST=total_oranges_cost,
                TOTAL_COST=total_cost
            ),
            "original_values": original_values
        }

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=modified_name1, NAME2=modified_name2, A=modified_A, B=modified_B, C=modified_C, D=modified_D, E=modified_E, F=modified_F)
    answer = answer_text.format(
        NAME1=modified_name1,
        NAME2=modified_name2,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        D=modified_D,
        E=modified_E,
        F=modified_F,
        WATERMELON_COST=watermelon_cost,
        ORANGE_COST=orange_cost,
        TOTAL_WATERMELONS_COST=total_watermelons_cost,
        TOTAL_PEPPERS_COST=total_peppers_cost,
        TOTAL_ORANGES_COST=total_oranges_cost,
        TOTAL_COST=total_cost
    )

    return {"question": question, "answer": answer}
