import random

def q100(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Question and answer templates
    question_text = (
        "{NAME} made {A} Valentine's cards to pass out. Her dad brought her {B} boxes of pre-made Valentine's cards that had {C} cards each. "
        "She passed out {D} to her classmates, {E} to her family and received {F} from family and friends. How many Valentine's Day cards does {NAME} now have?"
    )
    answer_text = (
        "Her dad gave her {B} boxes of {C} cards so {B} * {C} = <<{B}*{C}={CARDS_FROM_DAD}>>{CARDS_FROM_DAD}\n"
        "She made {A}, was given {CARDS_FROM_DAD} and received {F} so {A}+{CARDS_FROM_DAD}+{F} = <<{A}+{CARDS_FROM_DAD}+{F}={TOTAL_CARDS}>>{TOTAL_CARDS} cards\n"
        "She passed out {D} and gave {E} cards to family and friends so she gave away {D}+{E} = <<{D}+{E}={CARDS_GIVEN}>>{CARDS_GIVEN} cards\n"
        "She had {TOTAL_CARDS} cards and gave away {CARDS_GIVEN} cards so {TOTAL_CARDS}-{CARDS_GIVEN} = <<{TOTAL_CARDS}-{CARDS_GIVEN}={CARDS_LEFT}>>{CARDS_LEFT} cards left\n#### {CARDS_LEFT}"
    )

    # Original values
    A, B, C, D, E, F = 20, 2, 15, 24, 5, 17
    original_name = "Erica"

    # Name levels
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        common_names = ["Emma", "Sophia", "Mia", "Olivia", "Ava"]
        modified_name = random.choice([name for name in common_names if name != original_name])
    elif name_level == 3:
        uncommon_asian_names = ["Haruka", "Kaede", "Meilin", "Rinako", "Takeshi"]
        modified_name = random.choice(uncommon_asian_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=7))

    # Number levels
    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D, modified_E, modified_F = A, B, C, D, E, F
    else:
        modified_A = random.choice([num for num in range(10, 100) if num != A])
        modified_B = random.choice([num for num in range(2, 10) if num != B])
        modified_C = random.choice([num for num in range(10, 21, 5) if num != C])
        modified_D = random.choice([num for num in range(10, 30) if num != D])
        modified_E = random.choice([num for num in range(1, 5) if num != E])
        modified_F = random.choice([num for num in range(10, 100) if num != F])

        if num_level == 3:
            modified_A *= multiplier
            modified_C *= multiplier
            modified_D *= multiplier
            modified_E *= multiplier
            modified_F *= multiplier
        elif num_level == 4:
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_C = random.randint(multiplier, multiplier * 10 - 1)
            modified_D = random.randint(multiplier, multiplier * 2 - 1)
            modified_E = random.randint(multiplier, multiplier * 2 - 1)
            modified_F = random.randint(multiplier, multiplier * 2 - 1)

    # Ensure positivity of the final result
    cards_from_dad = modified_B * modified_C
    total_cards = modified_A + cards_from_dad + modified_F
    cards_given = modified_D + modified_E
    cards_left = total_cards - cards_given

    if cards_left < 0:
        raise ValueError("Adjusted numbers resulted in a negative card count. Adjust relationships between numbers.")

    # Save original values before symbolic handling
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C,
        "D": modified_D, "E": modified_E, "F": modified_F,
        "ans": cards_left
    }

    if is_symbolic:
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        modified_D, modified_E, modified_F = '\'D\'', '\'E\'', '\'F\''
        cards_from_dad = f"({modified_B} * {modified_C})"
        total_cards = f"({modified_A} + {cards_from_dad} + {modified_F})"
        cards_given = f"({modified_D} + {modified_E})"
        cards_left = f"({total_cards} - {cards_given})"

    # Format question and answer
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D, E=modified_E, F=modified_F)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A, B=modified_B, C=modified_C,
        D=modified_D, E=modified_E, F=modified_F,
        CARDS_FROM_DAD=cards_from_dad,
        TOTAL_CARDS=total_cards,
        CARDS_GIVEN=cards_given,
        CARDS_LEFT=cards_left
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
