import random

def q7(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} sells DVDs. He has 8 customers on Tuesday. His first 3 customers buy {A} DVD(s) each. "
        "His next 2 customers buy {B} DVD(s) each. His last 3 customers don't buy any DVDs. "
        "How many DVDs did {NAME} sell on Tuesday?"
    )
    answer_text = (
        "His first 3 customers buy 3 * {A} = <<3*{A}={FIRST_DVDS}>>{FIRST_DVDS} DVDs.\n"
        "His next 2 customers buy 2 * {B} = <<2*{B}={SECOND_DVDS}>>{SECOND_DVDS} DVDs.\n"
        "He sells a total of {FIRST_DVDS} + {SECOND_DVDS} + 0 = <<{FIRST_DVDS}+{SECOND_DVDS}+0={TOTAL_DVDS}>>{TOTAL_DVDS} DVDs.\n#### {TOTAL_DVDS}"
    )
    
    # Original values
    A, B = 1, 2  # DVDs bought by the first group and second group
    original_name = "Billy"

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        common_names = ["James", "Michael", "Robert", "David", "John"]
        modified_name = random.choice(common_names)
    elif name_level == 3:
        uncommon_names = ["Haruto", "Sanjay", "Ravi", "Tariq", "Chen"]
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        symbols = ["Z", "Y", "X", "W", "V"]
        modified_name = symbols[0]
    elif name_level == 5:
        random_strings = ["Asdfds", "Qwerml,", "Zxcvzx", "Plmnds", "Hjklkl"]
        modified_name = random.choice(random_strings)

    # Modify the number of DVDs for num_level
    if num_level == 1:
        modified_A, modified_B = A, B
    else:
        modified_A = random.choice([num for num in range(1, 10) if num != A])
        modified_B = random.choice([num for num in range(1, 10) if num != B])

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier
        elif num_level == 4:
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_B = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate DVDs sold
    first_dvds = 3 * modified_A
    second_dvds = 2 * modified_B
    total_dvds = first_dvds + second_dvds + 0  # Last group doesn't buy any DVDs

    A = modified_A
    B = modified_B

    original_values = {
        "A": A,
        "B": B,
        "ans": 3 * A + 2 * B
    }

    if is_symbolic:
        modified_A, modified_B = '\'A\'', '\'B\''
        first_dvds = f"3*{modified_A}"
        second_dvds = f"2*{modified_B}"
        total_dvds = f"{first_dvds} + {second_dvds} + 0"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        FIRST_DVDS=first_dvds,
        SECOND_DVDS=second_dvds,
        TOTAL_DVDS=total_dvds
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
