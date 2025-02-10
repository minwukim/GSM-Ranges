import random

def q1(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME}\u2019s ducks lay {A} eggs per day. She eats {B} for breakfast every morning and bakes muffins for her friends every day with {C}. "
        "She sells the remainder at the farmers' market daily for ${D} per fresh duck egg. How much in dollars does she make every day at the farmers' market?"
    )
    answer_text = (
        "{NAME} sells {A} - {B} - {C} = <<{A} - {B} - {C} = {REMAINING_EGGS}>>{REMAINING_EGGS} duck eggs a day.\n"
        "She makes {REMAINING_EGGS} * {D} = $<<({REMAINING_EGGS}) * {D} = {ANS}>>{ANS} every day at the farmer's market.\n#### {ANS}"
    )
    
    # Original values
    A, B, C, D = 16, 3, 4, 2
    original_name = "Janet"

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        common_names = ["Alice", "Emma", "Sophia", "Olivia", "Mia"]
        modified_name = random.choice(common_names)
    elif name_level == 3:
        uncommon_asian_names = ["Haruka", "Mingyu", "Kaede", "Rinako", "Takeshi"]
        modified_name = random.choice(uncommon_asian_names)
    elif name_level == 4:
        name_symbols = ["Z", "Y", "X", "W", "V"]
        modified_name = name_symbols[0]
    elif name_level == 5:
        random_strings = ["Dsafasf", "Hfhajfw", "Wkejrnf", "Bqewpzx", "Zufhjka"]
        modified_name = random.choice(random_strings)

    # Modify numbers based on num_level
    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        # Level 2 and 3: Adjust numbers with the multiplier
        modified_A = random.choice([num for num in range(11, 20) if num != A])
        modified_B = random.choice([num for num in range(1, 5) if num != B])
        modified_C = random.choice([num for num in range(1, 5) if num != C])
        modified_D = random.choice([num for num in range(1, 10)])

        if num_level == 3:
            # Apply multiplier for level 3
            modified_A = modified_A * multiplier
            modified_B = modified_B * multiplier
            modified_C = modified_C * multiplier

    if num_level == 4:
        # Replace numbers with values in the range [100, 999]
        modified_A = random.choice([num for num in range(multiplier * 5, multiplier * 10 - 1)])
        modified_B = random.choice([num for num in range(multiplier, multiplier * 2)])
        modified_C = random.choice([num for num in range(multiplier, multiplier * 2)])

    # Calculate the remaining eggs and the answer
    remaining_eggs = modified_A - modified_B - modified_C
    ans = remaining_eggs * modified_D

    A = modified_A
    B = modified_B
    C = modified_C
    D = modified_D
    original_values = {"A": A, "B": B, "C": C, "D": D, "ans": (A - B - C) * D}

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D = '\'A\'', '\'B\'', '\'C\'', '\'D\''
        remaining_eggs = f"{modified_A} - {modified_B} - {modified_C}"
        ans = f"({remaining_eggs}) * {modified_D}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D)
    answer = answer_text.format(
        NAME=modified_name, 
        A=modified_A, 
        B=modified_B, 
        C=modified_C, 
        D=modified_D, 
        REMAINING_EGGS=remaining_eggs, 
        ANS=ans
    )
    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
