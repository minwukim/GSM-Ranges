import random

def q21(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{PARENT} has 4 kids named {CHILD1}, {CHILD2}, {CHILD3}, and {CHILD4}. {CHILD1} is {A} years older than {CHILD2} and {B} years younger than {CHILD3}. "
        "If {CHILD4} is {C} and is {D} years younger than {CHILD3}, how old is {CHILD2}?"
    )
    answer_text = (
        "{CHILD4} is {C} and {D} years younger than {CHILD3}, so {CHILD3} is {C} + {D} = <<{C}+{D}={COREY_AGE}>>{COREY_AGE} years old.\n"
        "{CHILD1} is {B} years younger than {CHILD3} so is {COREY_AGE} - {B} = <<{COREY_AGE}-{B}={AMY_AGE}>>{AMY_AGE} years old.\n"
        "{CHILD1} is also {A} years older than {CHILD2}, so {CHILD2} is {AMY_AGE} - {A} = <<{AMY_AGE}-{A}={JACKSON_AGE}>>{JACKSON_AGE} years old.\n#### {JACKSON_AGE}"
    )
    
    # Original values
    A, B, C, D = 5, 2, 10, 1  # Age differences and relations
    parent_name = "Emily"
    child_names = ["Amy", "Jackson", "Corey", "James"]

    # Name pools for name assignment
    common_names = ["Sophia", "Liam", "Olivia", "Emma", "James", "Ethan", "Chloe", "Noah", "Ava"]
    uncommon_names = ["Haruto", "Akari", "Rin", "Takeshi", "Mei", "Kaoru", "Sanjay", "Sora", "Yuki"]
    random_strings = ["Prntx", "Chld1", "Chld2", "Fldpr", "Trmnx"]

    # Modify names based on name_level
    if name_level == 1:
        modified_parent = parent_name
        modified_children = child_names
    elif name_level == 2:
        modified_parent = random.choice(common_names)
        modified_children = random.sample(common_names, 4)
    elif name_level == 3:
        modified_parent = random.choice(uncommon_names)
        modified_children = random.sample(uncommon_names, 4)
    elif name_level == 4:
        modified_parent = "Z"
        modified_children = ["Y", "X", "W", "V"]
    elif name_level == 5:
        modified_parent = random.choice(random_strings)
        modified_children = random.sample(random_strings, 4)

    PARENT, CHILD1, CHILD2, CHILD3, CHILD4 = (
        modified_parent,
        *modified_children,
    )

    # Modify the values for num_level
    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        modified_A = random.choice([num for num in range(2, 7) if num != A])
        modified_B = random.choice([num for num in range(2, 4) if num != B])
        modified_C = random.choice([num for num in range(8, 15) if num != C])
        modified_D = random.choice([num for num in range(2, 10) if num != D])

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier
            modified_C *= multiplier
            modified_D *= multiplier

    if num_level == 4:
        modified_A = random.randint(multiplier * 2, multiplier * 6)
        modified_B = random.randint(multiplier * 2, multiplier * 3)
        modified_C = random.randint(multiplier * 8, multiplier * 15)
        modified_D = random.randint(multiplier * 2, multiplier * 10)

    # Calculate ages
    corey_age = modified_C + modified_D
    amy_age = corey_age - modified_B
    jackson_age = amy_age - modified_A


    A = modified_A
    B = modified_B
    C = modified_C
    D = modified_D

    original_values = {
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "ans": ((C + D) - B) - A
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D = '\'A\'', '\'B\'', '\'C\'', '\'D\''
        corey_age = f"{modified_C} + {modified_D}"
        amy_age = f"{corey_age} - {modified_B}"
        jackson_age = f"{amy_age} - {modified_A}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(
        PARENT=PARENT, CHILD1=CHILD1, CHILD2=CHILD2, CHILD3=CHILD3, CHILD4=CHILD4, A=modified_A, B=modified_B, C=modified_C, D=modified_D
    )
    answer = answer_text.format(
        PARENT=PARENT,
        CHILD1=CHILD1,
        CHILD2=CHILD2,
        CHILD3=CHILD3,
        CHILD4=CHILD4,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        D=modified_D,
        COREY_AGE=corey_age,
        AMY_AGE=amy_age,
        JACKSON_AGE=jackson_age,
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
