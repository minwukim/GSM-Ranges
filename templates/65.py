import random

def q65(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} is {A} years younger than {NAME2}, who is {B} years older than {NAME3}. "
        "If {NAME3} is {C} years old, what is the sum of the ages of the three girls?"
    )
    answer_text = (
        "{NAME2} is {C} + {B} = <<{C}+{B}={AGE2}>>{AGE2} years old.\n"
        "{NAME1} is {AGE2} – {A} = <<{AGE2}-{A}={AGE1}>>{AGE1} years old.\n"
        "Therefore, the sum of their ages is {C} + {AGE2} + {AGE1} = <<{C}+{AGE2}+{AGE1}={TOTAL}>>{TOTAL}.\n#### {TOTAL}"
    )
    
    # Name options
    common_names = ["Emma", "Sophia", "Isabella", "Mia", "Charlotte"]
    uncommon_names = ["Haruka", "Mingyu", "Kaede", "Rinako", "Takeshi"]
    random_strings = ["Fjksdnl", "Qwzrptx", "Bvxhjkn", "Lmprzqy", "Nfgtsdl"]
    original_names = ["Mary", "Joan", "Jessa"]

    # Modify names based on name_level
    if name_level == 1:
        modified_names = original_names
    elif name_level == 2:
        modified_names = random.sample([n for n in common_names if n not in original_names], 3)
    elif name_level == 3:
        modified_names = random.sample(uncommon_names, 3)
    elif name_level == 4:
        modified_names = ["Z", "Y", "X"]
    elif name_level == 5:
        modified_names = random.sample(random_strings, 3)

    NAME1, NAME2, NAME3 = modified_names

    # Original values
    A, B, C = 2, 5, 20  # Mary is 2 years younger, Joan is 5 years older, Jessa is 20 years old

    # Adjust values for number levels
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    else:
        # Level 2: Same digit, different values
        modified_A = random.choice([num for num in range(2, 10) if num != A])
        modified_B = random.choice([num for num in range(2, 10) if num != B])
        modified_C = random.choice([num for num in range(20, 100, 10) if num != C])

        if num_level == 3:
            # Multiply Level 2 values by the multiplier
            modified_A *= multiplier
            modified_B *= multiplier
            modified_C *= multiplier

        elif num_level == 4:
            # Assign random values in range (multiplier, 10*multiplier - 1)
            modified_B = random.randint(multiplier, 10 * multiplier - 1)
            modified_C = random.randint(multiplier, 10 * multiplier - 1)
            modified_A = random.randint(multiplier, modified_B + modified_C)

    # Calculate intermediate and final answers
    AGE2 = modified_C + modified_B  # Joan's age
    AGE1 = AGE2 - modified_A        # Mary's age
    TOTAL = modified_C + AGE2 + AGE1  # Total sum of ages

    # Save original and modified values before symbolic replacement
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "ans": TOTAL
    }

    if is_symbolic:
        # Replace numbers with symbolic variables
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        AGE2 = f"({modified_C} + {modified_B})"
        AGE1 = f"({AGE2} - {modified_A})"
        TOTAL = f"({modified_C} + {AGE2} + {AGE1})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=NAME1, NAME2=NAME2, NAME3=NAME3, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME1=NAME1, NAME2=NAME2, NAME3=NAME3,
        A=modified_A, B=modified_B, C=modified_C,
        AGE2=AGE2, AGE1=AGE1, TOTAL=TOTAL
    )

    return {"question": question, "answer": answer, "original_values": original_values if is_symbolic else None}
