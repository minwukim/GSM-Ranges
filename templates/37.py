import random

def q37(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} gets {A} car washes a month. If each car wash costs ${B}, how much does {NAME} pay in a year?"
    )
    answer_text = (
        "{NAME} gets {A}*12=<<{A}*12={YEARLY_WASHES}>>{YEARLY_WASHES} car washes a year.\n"
        "That means it costs {YEARLY_WASHES}*{B}=$<<{YEARLY_WASHES}*{B}={TOTAL_COST}>>{TOTAL_COST}.\n#### {TOTAL_COST}"
    )
    
    # Original values
    A, B = 4, 15  # Car washes per month, cost per car wash
    default_name = "Tom"

    # Dynamic name generation
    common_names = ["Alice", "Jack", "Sophia", "Michael", "Emma"]
    uncommon_names = ["Haruto", "Yara", "Chen", "Aisha", "Mei"]
    random_strings = ["Trplqmv", "Nsvktbz", "Rkzfnxp", "Bxvltyq", "Lcmtrpz"]

    if name_level == 1:
        modified_name = default_name
    elif name_level == 2:
        modified_name = random.choice(common_names)
    elif name_level == 3:
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = random.choice(random_strings)

    # Adjust values for difficulty levels
    if num_level == 1:
        modified_A, modified_B = A, B
    else:
        modified_A = random.choice([num for num in range(2, 9) if num != A])
        modified_B = random.choice([num for num in range(10, 51, 5) if num != B])

        if num_level == 3:
            modified_A *= multiplier
        elif num_level == 4:
            modified_A = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    yearly_washes = modified_A * 12  # 12 months in a year is fixed
    total_cost = yearly_washes * modified_B

    A = modified_A
    B = modified_B

    original_values = {"A": A, "B": B, "ans": A * 12 * B}

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B = '\'A\'', '\'B\''
        yearly_washes = f"{modified_A} * 12"
        total_cost = f"{yearly_washes} * {modified_B}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        YEARLY_WASHES=yearly_washes,
        TOTAL_COST=total_cost
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}

