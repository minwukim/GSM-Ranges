import random

def q40(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} and her mom go to the museum. The cost of admission is ${A} for adults and ${B} for children. "
        "{NAME1}'s mom gives the cashier money for 1 child ticket and 1 adult ticket. If she received ${C} in change, "
        "how much money, in dollars, did she give the cashier?"
    )
    answer_text = (
        "The total cost of the tickets is {A}+{B}=<<{A}+{B}={TOTAL_COST}>>{TOTAL_COST} dollars.\n"
        "{NAME1}'s mom gave the cashier {TOTAL_COST}+{C}=<<{TOTAL_COST}+{C}={MONEY_GIVEN}>>{MONEY_GIVEN} dollars.\n#### {MONEY_GIVEN}"
    )
    
    # Original values
    A, B, C = 12, 10, 8  # Adult ticket cost, child ticket cost, change received

    # Dynamic name generation
    common_names = ["Brittany", "Sophie", "Emily", "Grace", "Olivia"]
    uncommon_names = ["Yumi", "Anika", "Leilani", "Saanvi", "Aisha"]
    random_strings = ["Xbdtrp", "Jkrmvq", "Lvnzdq", "Vwrtpk", "Plznxq"]

    if name_level == 1:
        name1 = "Brittany"
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
        modified_A, modified_B, modified_C = A, B, C
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(10, 100) if num != A])  # Adult ticket cost
        modified_B = random.choice([num for num in range(10, 100) if num != B])  # Child ticket cost
        modified_C = random.choice([num for num in range(1, 10) if num != C])  # Change received

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_B *= multiplier
            modified_C *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_B = random.randint(multiplier, multiplier * 10 - 1)
            modified_C = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    total_cost = modified_A + modified_B
    money_given = total_cost + modified_C

    A = modified_A
    B = modified_B
    C = modified_C

    original_values = {"A": A, "B": B, "C": C, "ans": A + B + C}

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        total_cost = f"{modified_A} + {modified_B}"
        money_given = f"{total_cost} + {modified_C}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=name1, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME1=name1,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        TOTAL_COST=total_cost,
        MONEY_GIVEN=money_given
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
