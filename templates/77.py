import random

def q77(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "If {NAME1} is {A} years old and her brother is {B} times her age, how old will her brother be in {C} years?"
    )
    answer_text = (
        "{NAME1}'s brother is {A} * {B} = <<{A}*{B}={BROTHER_AGE_NOW}>>{BROTHER_AGE_NOW} years old now.\n"
        "This means, in {C} years, her brother will be {BROTHER_AGE_NOW} + {C} = <<{BROTHER_AGE_NOW}+{C}={BROTHER_AGE_IN_FUTURE}>>{BROTHER_AGE_IN_FUTURE} years old.\n#### {BROTHER_AGE_IN_FUTURE}"
    )

    # Name options
    common_names = ["Alice", "Emma", "Sophia", "Olivia", "Mia"]
    uncommon_names = ["Haruka", "Mingyu", "Kaede", "Rinako", "Takeshi"]
    random_strings = ["Xyzabcd", "Lmnqrst", "Prkltxz", "Bgjwopr", "Fzptmlq"]

    # Detect and modify names
    if name_level == 1:
        name1 = "Ann"
    elif name_level == 2:
        name1 = random.choice([name for name in common_names if name != "Ann"])
    elif name_level == 3:
        name1 = random.choice(uncommon_names)
    elif name_level == 4:
        name1 = "Z"
    elif name_level == 5:
        name1 = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=7))

    # Original values
    A, B, C = 9, 2, 3  # Ann's age, brother's multiplier, years in the future

    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B, modified_C = A, B, C
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(2, 10) if num != A])  # Ann's age
        modified_B = random.choice([num for num in range(2, 10) if num != B])  # Multiplier for brother's age
        modified_C = random.choice([num for num in range(2, 10) if num != C])  # Years in the future

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_C *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_C = random.randint(multiplier, multiplier * 10 - 1)

    # Ensure positivity of calculations
    brother_age_now = modified_A * modified_B
    brother_age_in_future = brother_age_now + modified_C

    # Save original values in the modified format
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "ans": brother_age_in_future
    }

    if is_symbolic:
        # Represent numbers symbolically with quotes
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        brother_age_now = f"({modified_A} * {modified_B})"
        brother_age_in_future = f"({brother_age_now} + {modified_C})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=name1, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME1=name1,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        BROTHER_AGE_NOW=brother_age_now,
        BROTHER_AGE_IN_FUTURE=brother_age_in_future
    )

    return {"question": question, "answer": answer, "original_values": original_values if is_symbolic else None}
