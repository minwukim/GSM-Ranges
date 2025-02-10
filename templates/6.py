import random

def q6(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} and {NAME2} are cousins. {NAME1} was born {A} years before {NAME2}. "
        "{NAME1} had a son at the age of {B}. If {NAME2} is now {C} years old, how many years ago was {NAME1}'s son born?"
    )
    answer_text = (
        "When {NAME1}'s son was born {NAME2} was {B} - {A} = <<{B}-{A}={NAME2_AGE_AT_SON_BIRTH}>>{NAME2_AGE_AT_SON_BIRTH} years old.\n"
        "Thus it has been {C} - {NAME2_AGE_AT_SON_BIRTH} = <<{C}-{NAME2_AGE_AT_SON_BIRTH}={YEARS_AGO}>>{YEARS_AGO} years since {NAME1}'s son was born.\n#### {YEARS_AGO}"
    )

    # Original values
    A, B, C = 6, 23, 31  # Age difference, age at which NAME1 had his son, NAME2's current age
    original_names = ["Raymond", "Samantha"]

    # Modify names based on name_level
    if name_level == 1:
        modified_names = original_names
    elif name_level == 2:
        common_names = ["James", "Emma", "Michael", "Sophia", "John", "Olivia"]
        modified_names = random.sample(common_names, 2)
    elif name_level == 3:
        uncommon_names = ["Haruto", "Meera", "Chihiro", "Rinako", "Kazuki", "Takeshi"]
        modified_names = random.sample(uncommon_names, 2)
    elif name_level == 4:
        symbols = ["Z", "Y", "X", "W", "V"]
        modified_names = symbols[0], symbols[1]
    elif name_level == 5:
        random_strings = ["Abcshs", "Defvxzx", "Gjklasd", "Jkjgkl", "Mnokals", "Pqrjkfl"]
        modified_names = random.sample(random_strings, 2)

    # Unpack modified names
    name1, name2 = modified_names

    # Modify values based on num_level
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    else:
        modified_A = random.choice([num for num in range(1, 20) if num != A])
        modified_B = random.choice([num for num in range(20, 26) if num != B])
        modified_C = random.choice([num for num in range(30, 71) if num != C])

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier
            modified_C *= multiplier

        elif num_level == 4:
            modified_A = random.randint(multiplier * 10, multiplier * 20)
            modified_B = random.randint(multiplier * 20, multiplier * 25)
            modified_C = random.randint(multiplier * 30, multiplier * 70)

    # Calculate the intermediate and final answers
    name2_age_at_son_birth = modified_B - modified_A
    years_ago = modified_C - name2_age_at_son_birth

    A = modified_A
    B = modified_B
    C = modified_C

    original_values = {
        "A": A,
        "B": B,
        "C": C,
        "ans": C - (B - A)
    }

    if is_symbolic:
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        name2_age_at_son_birth = f"{modified_B} - {modified_A}"
        years_ago = f"{modified_C} - ({name2_age_at_son_birth})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=name1, NAME2=name2, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME1=name1, NAME2=name2, A=modified_A, B=modified_B, C=modified_C,
        NAME2_AGE_AT_SON_BIRTH=name2_age_at_son_birth, YEARS_AGO=years_ago
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}

    return {"question": question, "answer": answer}
