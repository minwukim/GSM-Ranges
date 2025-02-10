import random

def q33(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "After transferring to a new school, {NAME1} made {A} more friends than {NAME2}. "
        "If {NAME2} made {B} friends, how many friends do {NAME1} and {NAME2} have together?"
    )
    answer_text = (
        "If {NAME2} made {B} friends, {NAME1} made {B}+{A} = <<{B}+{A}={AMY_FRIENDS}>>{AMY_FRIENDS} friends.\n"
        "Together, they made {AMY_FRIENDS}+{B} = <<{AMY_FRIENDS}+{B}={TOTAL_FRIENDS}>>{TOTAL_FRIENDS} friends at the new school.\n#### {TOTAL_FRIENDS}"
    )
    
    # Original values
    A, B = 20, 50  # Additional friends Amy made, number of friends Lily made
    name1, name2 = "Amy", "Lily"

    # Name pools
    common_names = ["Olivia", "Emma", "Sophia", "Isabella", "Mia"]
    uncommon_names = ["Yuki", "Ananya", "Hyejin", "Rashmi", "Meilin"]
    random_strings = ["Xlqypnrs", "Wrfjknt", "Zlsmtpr", "Ndykrvz", "Qxntvzp"]

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

    # Modify the values for level
    if num_level == 1:
        modified_A, modified_B = A, B
    else:
        modified_A = random.choice([num for num in range(10, 91, 10) if num != A])  # Additional friends Amy made
        modified_B = random.choice([num for num in range(10, 91, 10) if num != B])  # Friends Lily made

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier
        elif num_level == 4:
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_B = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    amy_friends = modified_B + modified_A
    total_friends = amy_friends + modified_B

    A = modified_A
    B = modified_B

    original_values = {
        "A": A,
        "B": B,
        "ans": (A + B) + B
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B = '\'A\'', '\'B\''
        amy_friends = f"{modified_B} + {modified_A}"
        total_friends = f"{amy_friends} + {modified_B}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=modified_name1, NAME2=modified_name2, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME1=modified_name1,
        NAME2=modified_name2,
        A=modified_A,
        B=modified_B,
        AMY_FRIENDS=amy_friends,
        TOTAL_FRIENDS=total_friends
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
