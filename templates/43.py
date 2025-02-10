import random

def q43(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} and {NAME2} went to the beach today. {NAME1} caught {A} starfish, {B} sea horses, and {C} clownfish. "
        "Meanwhile, {NAME2} caught {D} fewer starfish than {NAME1}, {E} fewer sea horses than {NAME1}, and {F} more clownfish than {NAME1}. "
        "How many fish did they catch in total?"
    )
    answer_text = (
        "{NAME2} caught {A} - {D} = <<{A}-{D}={LOCSIN_STARFISH}>>{LOCSIN_STARFISH} starfish.\n"
        "Together, they caught {A} + {LOCSIN_STARFISH} = <<{A}+{LOCSIN_STARFISH}={TOTAL_STARFISH}>>{TOTAL_STARFISH} starfish.\n"
        "{NAME2} caught {B} - {E} = <<{B}-{E}={LOCSIN_SEAHORSES}>>{LOCSIN_SEAHORSES} sea horses.\n"
        "Together, they caught {B} + {LOCSIN_SEAHORSES} = <<{B}+{LOCSIN_SEAHORSES}={TOTAL_SEAHORSES}>>{TOTAL_SEAHORSES} sea horses.\n"
        "{NAME2} caught {C} + {F} = <<{C}+{F}={LOCSIN_CLOWNFISH}>>{LOCSIN_CLOWNFISH} clownfish.\n"
        "Together, they caught {C} + {LOCSIN_CLOWNFISH} = <<{C}+{LOCSIN_CLOWNFISH}={TOTAL_CLOWNFISH}>>{TOTAL_CLOWNFISH} clownfish.\n"
        "In total, {NAME1} and {NAME2} caught {TOTAL_STARFISH} + {TOTAL_SEAHORSES} + {TOTAL_CLOWNFISH} = <<{TOTAL_STARFISH}+{TOTAL_SEAHORSES}+{TOTAL_CLOWNFISH}={TOTAL_FISH}>>{TOTAL_FISH} fish.\n#### {TOTAL_FISH}"
    )

    # Dynamic name generation
    common_names = ["Anakin", "Locsin", "Sophia", "Milo", "Liam"]
    uncommon_names = ["Akira", "Leilani", "Saanvi", "Tenzin", "Yuki"]
    random_strings = ["Xyrth", "Lnvtr", "Plzmq", "Vwndrp", "Jkrmv"]

    if name_level == 1:
        name1, name2 = "Anakin", "Locsin"
    elif name_level == 2:
        name1, name2 = random.sample(common_names, 2)
    elif name_level == 3:
        name1, name2 = random.sample(uncommon_names, 2)
    elif name_level == 4:
        name1, name2 = "Z", "Y"
    elif name_level == 5:
        name1, name2 = random.sample(random_strings, 2)

    # Original values
    A, B, C = 10, 6, 3  # Anakin's catches: starfish, sea horses, clownfish
    D, E, F = 5, 3, 2  # Differences in Locsin's catches

    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B, modified_C, modified_D, modified_E, modified_F = A, B, C, D, E, F
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(8, 15) if num != A])
        modified_B = random.choice([num for num in range(5, 10) if num != B])
        modified_C = random.choice([num for num in range(2, 5) if num != C])
        modified_D = random.choice([num for num in range(3, 6) if num != D])
        modified_E = random.choice([num for num in range(2, 4) if num != E])
        modified_F = random.choice([num for num in range(1, 3) if num != F])

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_B *= multiplier
            modified_C *= multiplier
            modified_D *= multiplier
            modified_E *= multiplier
            modified_F *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier * 2, multiplier * 10 - 1)
            modified_B = random.randint(multiplier * 2, multiplier * 10 - 1)
            modified_C = random.randint(multiplier, multiplier * 10 - 1)
            modified_D = random.randint(multiplier, modified_A - 1)
            modified_E = random.randint(multiplier, modified_B - 1)
            modified_F = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    locsin_starfish = modified_A - modified_D
    total_starfish = modified_A + locsin_starfish

    locsin_seahorses = modified_B - modified_E
    total_seahorses = modified_B + locsin_seahorses

    locsin_clownfish = modified_C + modified_F
    total_clownfish = modified_C + locsin_clownfish

    total_fish = total_starfish + total_seahorses + total_clownfish

    A = modified_A
    B = modified_B
    C = modified_C
    D = modified_D
    E = modified_E
    F = modified_F

    original_values = {
        "A": A, "B": B, "C": C, "D": D, "E": E, "F": F,
        "ans": A + (A - D) + B + (B - E) + C + (C + F)
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        modified_D, modified_E, modified_F = '\'D\'', '\'E\'', '\'F\''
        locsin_starfish = f"{modified_A} - {modified_D}"
        total_starfish = f"{modified_A} + {locsin_starfish}"
        locsin_seahorses = f"{modified_B} - {modified_E}"
        total_seahorses = f"{modified_B} + {locsin_seahorses}"
        locsin_clownfish = f"{modified_C} + {modified_F}"
        total_clownfish = f"{modified_C} + {locsin_clownfish}"
        total_fish = f"{total_starfish} + {total_seahorses} + {total_clownfish}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(
        NAME1=name1, NAME2=name2, A=modified_A, B=modified_B, C=modified_C, D=modified_D, E=modified_E, F=modified_F
    )
    answer = answer_text.format(
        NAME1=name1,
        NAME2=name2,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        D=modified_D,
        E=modified_E,
        F=modified_F,
        LOCSIN_STARFISH=locsin_starfish,
        TOTAL_STARFISH=total_starfish,
        LOCSIN_SEAHORSES=locsin_seahorses,
        TOTAL_SEAHORSES=total_seahorses,
        LOCSIN_CLOWNFISH=locsin_clownfish,
        TOTAL_CLOWNFISH=total_clownfish,
        TOTAL_FISH=total_fish,
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
