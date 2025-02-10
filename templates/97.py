import random

def q97(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} has {A} silver pesos and {B} gold pesos. He visits his friend {NAME2} who has {C} times as many silver pesos as he has and {D} more gold pesos. "
        "What's the total number of pesos they have together?"
    )
    answer_text = (
        "{NAME1} has {A} + {B} = <<{A}+{B}={TOTAL_NAME1}>>{TOTAL_NAME1} pesos.\n"
        "His friend {NAME2} has {C} * {A} = <<{C}*{A}={SILVER_NAME2}>>{SILVER_NAME2} silver pesos.\n"
        "{NAME2} also has {B} + {D} = <<{B}+{D}={GOLD_NAME2}>>{GOLD_NAME2} gold pesos.\n"
        "The total number of pesos that {NAME2} has is {GOLD_NAME2} + {SILVER_NAME2} = <<{GOLD_NAME2}+{SILVER_NAME2}={TOTAL_NAME2}>>{TOTAL_NAME2}.\n"
        "The combined total for the two friends is {TOTAL_NAME1} + {TOTAL_NAME2} = <<{TOTAL_NAME1}+{TOTAL_NAME2}={TOTAL_COMBINED}>>{TOTAL_COMBINED} pesos.\n#### {TOTAL_COMBINED}"
    )

    # Original values
    A, B, C, D = 50, 80, 2, 40
    original_name1, original_name2 = "Axel", "Anna"

    # Modify names based on name_level
    if name_level == 1:
        name1, name2 = original_name1, original_name2
    elif name_level == 2:
        common_names = ["Sam", "Emma", "Chris", "Taylor", "Alex"]
        name1, name2 = random.sample([n for n in common_names if n not in [original_name1, original_name2]], 2)
    elif name_level == 3:
        uncommon_asian_names = ["Hiro", "Mei", "Aisha", "Raj", "Lila"]
        name1, name2 = random.sample(uncommon_asian_names, 2)
    elif name_level == 4:
        name1, name2 = "Z", "Y"
    elif name_level == 5:
        random_strings = ["Xlyfrz", "Tmfqvs", "Prkltz", "Bgjwvs", "Lmzptq"]
        name1, name2 = random.sample(random_strings, 2)

    # Modify numbers based on num_level
    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        modified_A = random.choice([num for num in range(10, 100, 10) if num != A])
        modified_B = random.choice([num for num in range(10, 100, 10) if num != B])
        modified_C = random.choice([num for num in range(2, 10) if num != C])
        modified_D = random.choice([num for num in range(10, 100, 10) if num != D])

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier
            modified_D *= multiplier
        elif num_level == 4:
            modified_A = random.randint(multiplier, 10 * multiplier - 1)
            modified_B = random.randint(multiplier, 10 * multiplier - 1)
            modified_D = random.randint(multiplier, 10 * multiplier - 1)

    # Ensure relationships remain valid
    total_name1 = modified_A + modified_B
    silver_name2 = modified_C * modified_A
    gold_name2 = modified_B + modified_D
    total_name2 = silver_name2 + gold_name2
    total_combined = total_name1 + total_name2

    # Original values dictionary
    original_values = {
        "A": modified_A,
        "B": modified_B,
        "C": modified_C,
        "D": modified_D,
        "ans": total_combined
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D = '\'A\'', '\'B\'', '\'C\'', '\'D\''
        total_name1 = f"({modified_A} + {modified_B})"
        silver_name2 = f"({modified_C} * {modified_A})"
        gold_name2 = f"({modified_B} + {modified_D})"
        total_name2 = f"({silver_name2} + {gold_name2})"
        total_combined = f"({total_name1} + {total_name2})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=name1, NAME2=name2, A=modified_A, B=modified_B, C=modified_C, D=modified_D)
    answer = answer_text.format(
        NAME1=name1, NAME2=name2,
        A=modified_A, B=modified_B, C=modified_C, D=modified_D,
        TOTAL_NAME1=total_name1, SILVER_NAME2=silver_name2, GOLD_NAME2=gold_name2,
        TOTAL_NAME2=total_name2, TOTAL_COMBINED=total_combined
    )

    return {"question": question, "answer": answer, "original_values": original_values}
