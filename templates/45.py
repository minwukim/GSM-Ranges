import random

def q45(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} has ${B} more than twice the money {NAME2} has. If {NAME2} has ${A}, how much money does {NAME1} have?"
    )
    answer_text = (
        "The total amount of money {NAME1} has that is twice {NAME2}'s money is 2 * ${A} = $<<2*{A}={TWICE_ETH}>>{TWICE_ETH}.\n"
        "If {NAME1} has ${B} more than twice the money {NAME2} has, they have {TWICE_ETH} + {B} = $<<{TWICE_ETH}+{B}={JIMMY_MONEY}>>{JIMMY_MONEY}.\n#### {JIMMY_MONEY}"
    )
    
    # Original values
    A, B = 8, 2  # Ethel's money, additional money Jimmy has

    # Dynamic name generation
    common_names = ["Sam", "Emma", "Chris", "Alex", "Taylor"]
    uncommon_names = ["Hiro", "Aisha", "Mei", "Raj", "Lila"]
    random_strings = ["Xlyfrz", "Tmfqvs", "Prkltz", "Bgjwvs", "Lmzptq"]

    if name_level == 1:
        name1, name2 = "Jimmy", "Ethel"
    elif name_level == 2:
        name1, name2 = random.sample(common_names, 2)
    elif name_level == 3:
        name1, name2 = random.sample(uncommon_names, 2)
    elif name_level == 4:
        name1, name2 = "Z", "Y"
    elif name_level == 5:
        name1, name2 = random.sample(random_strings, 2)

    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B = A, B
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(2, 10) if num != A])
        modified_B = random.choice([num for num in range(2, 10) if num != B])

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier
        elif num_level == 4:
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_B = random.randint(multiplier, multiplier * 10 - 1)

    # Store modified and original values
    original_values = {
        "A": modified_A,
        "B": modified_B,
        "ans": (2 * modified_A) + modified_B
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B = "\'A\'", "\'B\'"
        twice_eth = f"2 * {modified_A}"
        jimmy_money = f"{twice_eth} + {modified_B}"
    else:
        twice_eth = 2 * modified_A
        jimmy_money = twice_eth + modified_B

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=name1, NAME2=name2, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME1=name1,
        NAME2=name2,
        A=modified_A,
        B=modified_B,
        TWICE_ETH=twice_eth,
        JIMMY_MONEY=jimmy_money
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer, "original_values": original_values}
