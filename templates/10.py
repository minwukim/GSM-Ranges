import random

def q10(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1}'s iPhone is {A} times as old as {NAME2}'s iPhone. {NAME2}'s iPhone is {B} times older than {NAME3}'s iPhone. "
        "If {NAME3}’s iPhone is {C} year(s) old, how old is {NAME1}’s iPhone?"
    )
    answer_text = (
        "{NAME2}’s iPhone is {C}*{B} = <<{C}*{B}={NAME2_IPHONE_AGE}>>{NAME2_IPHONE_AGE} years old.\n"
        "{NAME1}’s iPhone is {A}*{NAME2_IPHONE_AGE} = <<{A}*{NAME2_IPHONE_AGE}={NAME1_IPHONE_AGE}>>{NAME1_IPHONE_AGE} years old.\n#### {NAME1_IPHONE_AGE}"
    )

    # Original values
    A, B, C = 4, 2, 1  # Multipliers for NAME1's, NAME2's, and NAME3's iPhone ages
    original_names = ["Brandon", "Ben", "Suzy"]

    # Modify names based on name_level
    if name_level == 1:
        modified_names = original_names
    elif name_level == 2:
        common_names = ["James", "Emma", "Michael", "Sophia", "Olivia"]
        modified_names = random.sample(common_names, 3)
    elif name_level == 3:
        uncommon_names = ["Ephraim", "Isolde", "Calliope", "Leocadia", "Thaddeus"]
        modified_names = random.sample(uncommon_names, 3)
    elif name_level == 4:
        symbols = ["Z", "Y", "X", "W", "V"]
        modified_names = symbols[0:3]
    elif name_level == 5:
        random_strings = ["Pldasrn", "Klyrsd", "Zyndsaph", "Crdvn", "Jydasfs"]
        modified_names = random.sample(random_strings, 3)

    # Unpack modified names
    name1, name2, name3 = modified_names

    # Modify the multipliers based on num_level
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    else:
        modified_A = random.choice([num for num in range(2, 10) if num != A])
        modified_B = random.choice([num for num in range(2, 10) if num != B])
        modified_C = random.choice([num for num in range(1, 10) if num != C])

        if num_level == 3:
            modified_C *= multiplier
        elif num_level == 4:
            modified_C = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate ages
    name2_iphone_age = modified_C * modified_B
    name1_iphone_age = modified_A * name2_iphone_age

    A = modified_A
    B = modified_B
    C = modified_C

    original_values = {
        "A": A, 
        "B": B, 
        "C": C, 
        "ans": A * (B * C)
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        name2_iphone_age = f"{modified_C}*{modified_B}"
        name1_iphone_age = f"{modified_A}*({name2_iphone_age})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=name1, NAME2=name2, NAME3=name3, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME1=name1,
        NAME2=name2,
        NAME3=name3,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        NAME2_IPHONE_AGE=name2_iphone_age,
        NAME1_IPHONE_AGE=name1_iphone_age
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
