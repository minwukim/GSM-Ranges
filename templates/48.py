import random

def q48(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} is {A} years older than {NAME2}. {NAME2} is {B} times as old as {NAME3}. "
        "If {NAME3} is the same age as {NAME4}, and {NAME4} is {C} years old, "
        "what's the total age of the four birds?"
    )
    answer_text = (
        "If {NAME4} is {C} years old, the same as {NAME3}, their total age is {C} + {C} = <<{C}+{C}={FOUR_AND_THIRTYTWO_TOTAL}>>{FOUR_AND_THIRTYTWO_TOTAL} years.\n"
        "{NAME2} is {B} times as old as {NAME3}, so {NAME2} is {B} * {C} = <<{B}*{C}={GRANNY_RED_AGE}>>{GRANNY_RED_AGE} years old.\n"
        "{NAME1} is {A} years older than {NAME2}, so {NAME1} is {GRANNY_RED_AGE} + {A} = <<{GRANNY_RED_AGE}+{A}={SALLY_TWO_AGE}>>{SALLY_TWO_AGE} years old.\n"
        "The total age of the four birds is {FOUR_AND_THIRTYTWO_TOTAL} + {GRANNY_RED_AGE} + {SALLY_TWO_AGE} = <<{FOUR_AND_THIRTYTWO_TOTAL}+{GRANNY_RED_AGE}+{SALLY_TWO_AGE}={TOTAL_AGE}>>{TOTAL_AGE} years.\n#### {TOTAL_AGE}"
    )

    # Dynamic name generation
    common_names = ["Robin", "Blue", "Coco", "Penny", "Sky"]
    uncommon_names = ["Kiku", "Ren", "Yumi", "Hana", "Akira"]
    random_strings = ["Nlfxrv", "Trjvkp", "Gqvlzt", "Xrpqtm", "Zkmrwt"]

    if name_level == 1:
        name1, name2, name3, name4 = "Sally Two", "Granny Red", "Sally Four", "Sally Thirtytwo"
    elif name_level == 2:
        name1, name2, name3, name4 = random.sample(common_names, 4)
    elif name_level == 3:
        name1, name2, name3, name4 = random.sample(uncommon_names, 4)
    elif name_level == 4:
        name1, name2, name3, name4 = "Z", "Y", "X", "W"
    elif name_level == 5:
        name1, name2, name3, name4 = random.sample(random_strings, 4)

    # Original values
    A, B, C = 3, 2, 8  # Age difference, multiplier, age of Sally Thirtytwo and Sally Four

    if num_level > 1:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(2, 10) if num != A])  # Age difference
        modified_B = random.choice([num for num in range(2, 10) if num != B])  # Multiplier for Granny Red's age
        modified_C = random.choice([num for num in range(2, 10) if num != C])  # Age of Sally Thirtytwo and Sally Four

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier
        elif num_level == 4:
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_B = random.randint(multiplier, multiplier * 10 - 1)
    else:
        modified_A, modified_B, modified_C = A, B, C

    # Calculate totals
    four_and_thirtytwo_total = modified_C + modified_C
    granny_red_age = modified_B * modified_C
    sally_two_age = granny_red_age + modified_A
    total_age = four_and_thirtytwo_total + granny_red_age + sally_two_age

    # Original and modified values
    original_values = {
        "A": modified_A, 
        "B": modified_B, 
        "C": modified_C, 
        "ans": total_age
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = "\'A\'", "\'B\'", "\'C\'"
        four_and_thirtytwo_total = f"{modified_C} + {modified_C}"
        granny_red_age = f"{modified_B} * {modified_C}"
        sally_two_age = f"{granny_red_age} + {modified_A}"
        total_age = f"{four_and_thirtytwo_total} + {granny_red_age} + {sally_two_age}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(
        NAME1=name1, NAME2=name2, NAME3=name3, NAME4=name4, A=modified_A, B=modified_B, C=modified_C
    )
    answer = answer_text.format(
        NAME1=name1,
        NAME2=name2,
        NAME3=name3,
        NAME4=name4,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        FOUR_AND_THIRTYTWO_TOTAL=four_and_thirtytwo_total,
        GRANNY_RED_AGE=granny_red_age,
        SALLY_TWO_AGE=sally_two_age,
        TOTAL_AGE=total_age,
    )

    return {"question": question, "answer": answer, "original_values": original_values}
