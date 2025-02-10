import random

def q2(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} decides to run {A} sprints {B} times a week. He runs {C} meters each sprint. "
        "How many total meters does he run a week?"
    )
    answer_text = (
        "He sprints {A}*{B}=<<{A}*{B}={TOTAL_SPRINTS}>>{TOTAL_SPRINTS} times\n"
        "So he runs {TOTAL_SPRINTS}*{C}=<<{TOTAL_SPRINTS}*{C}={TOTAL_METERS}>>{TOTAL_METERS} meters\n#### {TOTAL_METERS}"
    )
    
    # Original values
    A, B, C = 3, 3, 60
    original_name = "James"

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        common_names = ["Michael", "John", "Robert", "David", "William"]
        modified_name = random.choice(common_names)
    elif name_level == 3:
        uncommon_asian_names = ["Hikaru", "Chen", "Takeshi", "Minjoon", "Kazuki"]
        modified_name = random.choice(uncommon_asian_names)
    elif name_level == 4:
        name_symbols = ["Z", "Y", "X", "W", "V"]
        modified_name = name_symbols[0]
    elif name_level == 5:
        random_strings = ["Asdkjf", "Qwejkl", "Zmopty", "Bcxvnm", "Hjgtre"]
        modified_name = random.choice(random_strings)

    # Modify numbers based on num_level
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    else:
        # Level 2 and 3: Adjust numbers with the multiplier
        modified_A = random.choice([num for num in range(1, 10) if num != A])
        modified_B = random.choice([num for num in range(1, 10) if num != B])
        modified_C = random.choice([C + 10 * n for n in [-2, -1, 1, 2] if 0 < C + 10 * n < 100])

        if num_level == 3:
            # Apply multiplier for level 3
            modified_A = modified_A * multiplier

    if num_level == 4:
        # Replace numbers with values in the range [100, 999]
        modified_A = random.choice([num for num in range(multiplier, multiplier * 10 - 1)])

    # Calculate total sprints and total meters based on the modified values
    total_sprints = modified_A * modified_B
    total_meters = total_sprints * modified_C

    A = modified_A
    B = modified_B
    C = modified_C

    original_values = {
        "A": A, "B": B, "C": C, "ans": A * B * C
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        total_sprints = f"{modified_A} * {modified_B}"
        total_meters = f"({total_sprints}) * {modified_C}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=modified_name, 
        A=modified_A, 
        B=modified_B, 
        C=modified_C, 
        TOTAL_SPRINTS=total_sprints, 
        TOTAL_METERS=total_meters
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}

