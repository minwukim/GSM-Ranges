import random

def q53(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} initially had {A} Pokemon cards. After a month, they collected {B} times that number. "
        "In the second month, they collected {C} fewer cards than those collected in the first month. "
        "In the third month, they collected twice the combined number of Pokemon cards collected in the first and second months. "
        "How many Pokemon cards does {NAME} have now in total?"
    )
    answer_text = (
        "In the first month, {NAME} collected {B} * {A} = <<{B}*{A}={FIRST_MONTH_CARDS}>>{FIRST_MONTH_CARDS} Pokemon cards.\n"
        "In the second month, they collected {FIRST_MONTH_CARDS} - {C} = <<{FIRST_MONTH_CARDS}-{C}={SECOND_MONTH_CARDS}>>{SECOND_MONTH_CARDS} cards.\n"
        "After the first two months, the new Pokemon cards collected is {FIRST_MONTH_CARDS} + {SECOND_MONTH_CARDS} = "
        "<<{FIRST_MONTH_CARDS}+{SECOND_MONTH_CARDS}={FIRST_TWO_MONTHS_CARDS}>>{FIRST_TWO_MONTHS_CARDS}.\n"
        "The number of cards in the third month is twice the combined number in the first and second months, which totals "
        "2 * {FIRST_TWO_MONTHS_CARDS} = <<2*{FIRST_TWO_MONTHS_CARDS}={THIRD_MONTH_CARDS}>>{THIRD_MONTH_CARDS} Pokemon cards.\n"
        "In total, {NAME} has {A} cards they initially had + {FIRST_TWO_MONTHS_CARDS} cards collected in the first and second months + "
        "{THIRD_MONTH_CARDS} cards collected in the third month = <<{A}+{FIRST_TWO_MONTHS_CARDS}+{THIRD_MONTH_CARDS}={TOTAL_CARDS}>>{TOTAL_CARDS} cards.\n#### {TOTAL_CARDS}"
    )
    
    # Original values
    A, B, C = 20, 3, 20  # Initial cards, multiplier for first month, cards fewer in second month

    # Dynamic name generation (excluding original name "Elaine")
    common_names = ["Emma", "Noah", "Olivia", "Liam", "Sophia"]
    uncommon_names = ["Yuki", "Akira", "Mei", "Arjun", "Saanvi"]
    random_strings = ["Xqrzp", "Tmlcy", "Jpkfr", "Bvlnx", "Kztpq"]

    if name_level == 1:
        name = "Elaine"
    elif name_level == 2:
        name = random.choice(common_names)
    elif name_level == 3:
        name = random.choice(uncommon_names)
    elif name_level == 4:
        name = "Z"
    elif name_level == 5:
        name = random.choice(random_strings)

    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B, modified_C = A, B, C
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(20, 91, 10) if num != A])  # Initial cards
        modified_B = random.choice([num for num in range(2, 5) if num != B])  # Multiplier for first month
        modified_C = random.choice([num for num in range(10, 31, 10) if num != C])  # Cards fewer in second month

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_C *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier * 9, multiplier * 10 - 1)
            modified_C = random.randint(multiplier, multiplier * 2)

    # Calculate totals
    first_month_cards = modified_B * modified_A
    second_month_cards = first_month_cards - modified_C
    first_two_months_cards = first_month_cards + second_month_cards
    third_month_cards = 2 * first_two_months_cards
    total_cards = modified_A + first_two_months_cards + third_month_cards

    original_values = {
        "A": modified_A, 
        "B": modified_B, 
        "C": modified_C, 
        "ans": total_cards
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        first_month_cards = f"{modified_B} * {modified_A}"
        second_month_cards = f"{first_month_cards} - {modified_C}"
        first_two_months_cards = f"{first_month_cards} + {second_month_cards}"
        third_month_cards = f"2 * {first_two_months_cards}"
        total_cards = f"{modified_A} + {first_two_months_cards} + {third_month_cards}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        FIRST_MONTH_CARDS=first_month_cards,
        SECOND_MONTH_CARDS=second_month_cards,
        FIRST_TWO_MONTHS_CARDS=first_two_months_cards,
        THIRD_MONTH_CARDS=third_month_cards,
        TOTAL_CARDS=total_cards
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer, "original_values": original_values}
