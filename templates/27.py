import random

def q27(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} buys {A} pairs of shoes for each of his {B} children. They cost ${C} each. How much did he pay?"
    )
    answer_text = (
        "{NAME} bought {B}*{A}=<<{B}*{A}={TOTAL_PAIRS}>>{TOTAL_PAIRS} pairs of shoes.\n"
        "So he spent {C}*{TOTAL_PAIRS}=$<<{C}*{TOTAL_PAIRS}={TOTAL_COST}>>{TOTAL_COST}.\n#### {TOTAL_COST}"
    )

    # Original values
    A, B, C = 2, 3, 60  # Pairs per child, number of children, cost per pair
    original_name = "John"

    # Name pools for name assignment
    common_names = ["Michael", "Sarah", "David", "Emily", "Daniel"]
    uncommon_names = ["Haruto", "Mei", "Akira", "Riko", "Sora"]
    random_strings = ["Zqwprtkl", "Bvcsxnyl", "Mnfrtkpz", "Plkjhdqw", "Twrplzxq"]

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        modified_name = random.choice(common_names)
    elif name_level == 3:
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = random.choice(random_strings)

    # Modify the values for num_level
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    else:
        modified_A = random.choice([num for num in range(2, 10) if num != A])  # Pairs of shoes per child
        modified_B = random.choice([num for num in range(2, 10) if num != B])  # Number of children
        modified_C = random.choice([num for num in range(10, 91, 10) if num != C])  # Cost per pair

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    total_pairs = modified_A * modified_B
    total_cost = modified_C * total_pairs

    A = modified_A
    B = modified_B
    C = modified_C

    original_values = {"A": A, "B": B, "C": C, "ans": C * (A * B)}

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        total_pairs = f"{modified_B} * {modified_A}"
        total_cost = f"{modified_C} * ({total_pairs})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        TOTAL_PAIRS=total_pairs,
        TOTAL_COST=total_cost
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
