import random

def q62(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} and {NAME2} are at the beach. {NAME1} rents a canoe for ${A} an hour and {NAME2} rents a banana boat raft for ${B} an hour. "
        "If {NAME1} uses the boat for {C} hours and {NAME2} uses the raft for {D} hours, how much will they pay for their rentals, altogether?"
    )
    answer_text = (
        "{NAME1} would have to pay ${A} x {C} = $<<{A}*{C}={CARLOS_COST}>>{CARLOS_COST}\n"
        "{NAME2} would have to pay ${B} x {D} = $<<{B}*{D}={BENJI_COST}>>{BENJI_COST}\n"
        "All together, {NAME1} and {NAME2} will have to pay ${CARLOS_COST} + ${BENJI_COST} = $<<{CARLOS_COST}+{BENJI_COST}={TOTAL_COST}>>{TOTAL_COST}\n#### {TOTAL_COST}"
    )

    # Name options
    common_names = ["Alice", "Emma", "Sophia", "Jack", "Michael", "Liam"]
    uncommon_names = ["Haruto", "Mei", "Aisha", "Raj", "Chen", "Lila"]
    random_strings = ["Fkasldj", "Xhrweop", "Pqlznmv", "Jqwvmcx", "Zpywruf"]
    
    # Detect original names and declare name logic
    name1, name2 = "Carlos", "Benji"
    if name_level == 1:
        modified_name1, modified_name2 = name1, name2
    elif name_level == 2:
        names = [n for n in common_names if n not in [name1, name2]]
        modified_name1, modified_name2 = random.sample(names, 2)
    elif name_level == 3:
        modified_name1, modified_name2 = random.sample(uncommon_names, 2)
    elif name_level == 4:
        modified_name1, modified_name2 = "Z", "Y"
    elif name_level == 5:
        modified_name1, modified_name2 = random.sample(random_strings, 2)

    # Original values
    A, B, C, D = 30, 18, 3, 5  # Canoe cost, raft cost, hours for Carlos, hours for Benji
    
    # Adjust numbers based on num_level
    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        # Level 2: Same digit changes, preserving multiples where applicable
        modified_A = random.choice([num for num in range(10, 100, 10) if num != A])
        modified_B = random.choice([num for num in range(10, 100, 5) if num != B])
        modified_C = random.choice([num for num in range(2, 10) if num != C])
        modified_D = random.choice([num for num in range(2, 10) if num != D])

        if num_level == 3:
            # Multiply by multiplier
            modified_C *= multiplier
            modified_D *= multiplier
        elif num_level == 4:
            # Random range within (multiplier, 10 * multiplier - 1)
            modified_C = random.randint(multiplier, multiplier * 10 - 1)
            modified_D = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate costs
    carlos_cost = modified_A * modified_C
    benji_cost = modified_B * modified_D
    total_cost = carlos_cost + benji_cost

    # Save original values before symbolic adjustments
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "D": modified_D,
        "ans": total_cost
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D = "'A'", "'B'", "'C'", "'D'"
        carlos_cost = f"{modified_A} * {modified_C}"
        benji_cost = f"{modified_B} * {modified_D}"
        total_cost = f"{carlos_cost} + {benji_cost}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(
        NAME1=modified_name1, NAME2=modified_name2, A=modified_A, B=modified_B, C=modified_C, D=modified_D
    )
    answer = answer_text.format(
        NAME1=modified_name1, NAME2=modified_name2,
        A=modified_A, B=modified_B, C=modified_C, D=modified_D,
        CARLOS_COST=carlos_cost, BENJI_COST=benji_cost, TOTAL_COST=total_cost
    )

    return {"question": question, "answer": answer, "original_values": original_values}
