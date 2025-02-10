import random

def q3(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "Every day, {NAME} feeds each of her chickens {A} cups of mixed chicken feed, containing seeds, mealworms and vegetables to help keep them healthy. "
        "She gives the chickens their feed in three separate meals. In the morning, she gives her flock of chickens {B} cups of feed. "
        "In the afternoon, she gives her chickens another {C} cups of feed. "
        "How many cups of feed does she need to give her chickens in the final meal of the day if the size of {NAME}'s flock is {D} chickens?"
    )
    answer_text = (
        "If each chicken eats {A} cups of feed per day, then for {D} chickens they would need {A}*{D}=<<{A}*{D}={TOTAL_FEED}>>{TOTAL_FEED} cups of feed per day.\n"
        "If she feeds the flock {B} cups of feed in the morning, and {C} cups in the afternoon, then the final meal would require {TOTAL_FEED}-{B}-{C}=<<{TOTAL_FEED}-{B}-{C}={FINAL_FEED}>>{FINAL_FEED} cups of chicken feed.\n#### {FINAL_FEED}"
    )
    
    # Original values
    A, B, C, D = 3, 15, 25, 20
    original_name = "Wendi"

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        common_names = ["Emma", "Sophia", "Olivia", "Ava", "Isabella"]
        modified_name = random.choice(common_names)
    elif name_level == 3:
        uncommon_asian_names = ["Yuki", "Mei", "Chihiro", "Rina", "Satoshi"]
        modified_name = random.choice(uncommon_asian_names)
    elif name_level == 4:
        name_symbols = ["Z", "Y", "X", "W", "V"]
        modified_name = name_symbols[0]
    elif name_level == 5:
        random_strings = ["AsdXyz", "QwePqr", "ZlmAbc", "HjkUvw", "BnmQrs"]
        modified_name = random.choice(random_strings)

    # Modify numbers based on num_level
    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        # Level 2 and 3: Adjust numbers with the multiplier
        modified_A = random.choice([num for num in range(3, 10) if num != A])
        modified_B = random.choice([num for num in range(10, 21, 5) if num != B])
        modified_C = random.choice([num for num in range(20, 31, 5) if num != C])
        modified_D = random.choice([num for num in range(20, 91, 10) if num != D])

        if num_level == 3:
            # Apply multiplier for level 3
            modified_B = modified_B * multiplier
            modified_C = modified_C * multiplier
            modified_D = modified_D * multiplier  

    if num_level == 4:
        # Replace numbers with values in the range [100, 999]
        modified_B = random.randint(multiplier * 1, multiplier * 2)
        modified_C = random.randint(multiplier * 2, multiplier * 3)
        modified_D = random.choice([num for num in range(multiplier * 2, multiplier * 9 + 1, 10)])   

    # Calculate total feed needed and feed for the final meal based on the modified values
    total_feed = modified_A * modified_D
    final_feed = total_feed - modified_B - modified_C

    # Ensure the final feed and intermediate results are non-negative
    if final_feed < 0:
        final_feed = 0  # To comply with constraints

    A = modified_A
    B = modified_B
    C = modified_C
    D = modified_D

    original_values = {"A": A, "B": B, "C": C, "D": D, "ans": final_feed}

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D = '\'A\'', '\'B\'', '\'C\'', '\'D\''
        total_feed = f"{modified_A} * {modified_D}"
        final_feed = f"{total_feed} - {modified_B} - {modified_C}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D)
    answer = answer_text.format(
        NAME=modified_name, 
        A=modified_A, 
        B=modified_B, 
        C=modified_C, 
        D=modified_D, 
        TOTAL_FEED=total_feed, 
        FINAL_FEED=final_feed
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
