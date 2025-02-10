import random

def q9(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} is shoe shopping when she comes across a pair of boots that fit her shoe budget. However, she has to choose between the boots "
        "and two pairs of high heels that together cost {A} dollars less than the boots. If one pair of heels costs ${B} and the other costs twice as much, "
        "how many dollars are the boots?"
    )
    answer_text = (
        "The second pair of heels costs {B} * 2 = $<<{B}*2={SECOND_HEEL_COST}>>{SECOND_HEEL_COST}.\n"
        "The heels together cost {SECOND_HEEL_COST} + {B} = $<<{SECOND_HEEL_COST}+{B}={TOTAL_HEEL_COST}>>{TOTAL_HEEL_COST}.\n"
        "The boots cost ${A} more than both pairs of heels together, so the boots cost {TOTAL_HEEL_COST} + {A} = $<<{TOTAL_HEEL_COST}+{A}={BOOT_COST}>>{BOOT_COST}.\n#### {BOOT_COST}"
    )
    
    # Original values
    A, B = 5, 33  # Difference between boots and heels, cost of the first pair of heels
    original_name = "Gloria"

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        common_names = ["Emma", "Sophia", "Olivia", "Isabella", "Ava"]
        modified_name = random.choice(common_names)
    elif name_level == 3:
        uncommon_names = ["Amara", "Leocadia", "Isolde", "Calliope", "Zephyra"]
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        symbols = ["Z", "Y", "X", "W", "V"]
        modified_name = symbols[0]
    elif name_level == 5:
        random_strings = ["Fljkad", "Bridsa", "Pldaz", "Xyjkl", "Kjkll"]
        modified_name = random.choice(random_strings)

    # Modify the variables based on num_level
    if num_level == 1:
        modified_A, modified_B = A, B
    else:
        # Modify the variables for levels > 1
        modified_A = random.choice([num for num in range(2, 10) if num != A])
        modified_B = random.choice([num for num in range(10, 100) if num != B])

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_B *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_B = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate costs
    second_heel_cost = modified_B * 2
    total_heel_cost = modified_B + second_heel_cost
    boot_cost = total_heel_cost + modified_A

    A = modified_A
    B = modified_B

    # Create dictionary for original values and final answer
    original_values = {
        "A": A,
        "B": B,
        "ans": (B + (B * 2)) + A
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B = '\'A\'', '\'B\''
        second_heel_cost = f"{modified_B} * 2"
        total_heel_cost = f"{modified_B} + ({second_heel_cost})"
        boot_cost = f"{total_heel_cost} + {modified_A}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        SECOND_HEEL_COST=second_heel_cost,
        TOTAL_HEEL_COST=total_heel_cost,
        BOOT_COST=boot_cost
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}

    return {"question": question, "answer": answer}
