import random

def q96(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} hiked {A} kilometers per hour for {B} hours. {NAME2} hiked {C} kilometers per hour and stopped after {D} hours. "
        "How many kilometers farther did {NAME1} hike?"
    )
    answer_text = (
        "{NAME1} = {A} * {B} = <<({A})*({B})={DISTANCE1}>>{DISTANCE1} km\n"
        "{NAME2} = {C} * {D} = <<({C})*({D})={DISTANCE2}>>{DISTANCE2} km\n"
        "{DISTANCE1} - {DISTANCE2} = <<({DISTANCE1})-({DISTANCE2})={ANS}>>{ANS} km\n"
        "{NAME1} hiked {ANS} kilometers farther than {NAME2}.\n#### {ANS}"
    )

    # Detect names
    original_name1, original_name2 = "Cho", "Chloe"

    # Handle name levels
    common_names = ["Emma", "Liam", "Sophia", "Olivia", "Noah"]
    uncommon_names = ["Haruto", "Mei", "Aarav", "Rina", "Kaede"]
    random_strings = ["fjaskdf", "qwertzx", "plmnkjo", "ghrueos", "bvlcwie"]

    if name_level == 1:
        name1, name2 = original_name1, original_name2
    elif name_level == 2:
        name1, name2 = random.sample([n for n in common_names if n not in [original_name1, original_name2]], 2)
    elif name_level == 3:
        name1, name2 = random.sample(uncommon_names, 2)
    elif name_level == 4:
        name1, name2 = "Z", "Y"
    elif name_level == 5:
        name1, name2 = random.sample(random_strings, 2)

    # Original numbers
    A, B, C, D = 14, 8, 9, 5

    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        # Modify numbers for higher levels
        modified_A = random.choice([n for n in range(10, 100) if n != A and n % 1 == 0])
        modified_B = random.choice([n for n in range(2, 10) if n != B])
        modified_C = random.choice([n for n in range(2, 5) if n != C and n % 1 == 0])
        modified_D = random.choice([n for n in range(2, 5) if n != D])

        if num_level == 3:
            # Scale values by multiplier
            modified_B *= multiplier
            modified_C *= multiplier

        elif num_level == 4:
            # Use a range within multiplier bounds
            modified_B = random.randint(2 * multiplier, 10 * multiplier - 1)
            modified_C = random.randint(2 * multiplier, 5 * multiplier - 1)

    # Calculate distances
    distance1 = modified_A * modified_B
    distance2 = modified_C * modified_D
    ans = distance1 - distance2

    # Store original values
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "D": modified_D, "ans": ans
    }

    if is_symbolic:
        # Represent values symbolically
        modified_A, modified_B, modified_C, modified_D = "'A'", "'B'", "'C'", "'D'"
        distance1 = f"({modified_A})*({modified_B})"
        distance2 = f"({modified_C})*({modified_D})"
        ans = f"({distance1})-({distance2})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=name1, NAME2=name2, A=modified_A, B=modified_B, C=modified_C, D=modified_D)
    answer = answer_text.format(
        NAME1=name1, NAME2=name2,
        A=modified_A, B=modified_B, C=modified_C, D=modified_D,
        DISTANCE1=distance1, DISTANCE2=distance2, ANS=ans
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}

    return {"question": question, "answer": answer}
