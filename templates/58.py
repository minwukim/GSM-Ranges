import random

def q58(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} loves riding a bike. He rode it at least {A} times a week and makes {B} kilometers each time. "
        "He did that for {C} weeks, and then he decided to ride the bike only {D} times a week, but for {E} kilometers each time, "
        "and he did that for {F} weeks. How many kilometers did {NAME} do in total?"
    )
    answer_text = (
        "In the first part, {NAME} did {A} * {B} = <<{A}*{B}={WEEKLY_DISTANCE_PART1}>>{WEEKLY_DISTANCE_PART1} kilometers every week.\n"
        "He did that for {C} weeks, which means he made during that time {WEEKLY_DISTANCE_PART1} * {C} = "
        "<<{WEEKLY_DISTANCE_PART1}*{C}={DISTANCE_PART1}>>{DISTANCE_PART1} kilometers.\n"
        "After that, he made {D} * {E} = <<{D}*{E}={WEEKLY_DISTANCE_PART2}>>{WEEKLY_DISTANCE_PART2} kilometers a week.\n"
        "And {NAME} did that for {F} weeks, so he rode {WEEKLY_DISTANCE_PART2} * {F} = "
        "<<{WEEKLY_DISTANCE_PART2}*{F}={DISTANCE_PART2}>>{DISTANCE_PART2} kilometers during that time.\n"
        "In total, {NAME} did {DISTANCE_PART1} + {DISTANCE_PART2} = <<{DISTANCE_PART1}+{DISTANCE_PART2}={TOTAL_DISTANCE}>>{TOTAL_DISTANCE} kilometers.\n#### {TOTAL_DISTANCE}"
    )
    
    # Name options
    common_names = ["Sam", "Emma", "Chris", "Taylor", "Alex"]
    uncommon_names = ["Hiro", "Mei", "Aisha", "Raj", "Lila"]
    random_strings = ["Xlyfrz", "Tmfqvs", "Prkltz", "Bgjwvs", "Lmzptq"]
    
    # Dynamic name generation
    if name_level == 1:
        name = "Micheal"
    elif name_level == 2:
        name = random.choice(common_names)
    elif name_level == 3:
        name = random.choice(uncommon_names)
    elif name_level == 4:
        name = "Z"
    elif name_level == 5:
        name = random.choice(random_strings)
    
    # Original values
    A, B, C, D, E, F = 5, 25, 4, 2, 60, 3  # Weekly rides part 1, distance per ride part 1, weeks part 1, rides part 2, distance part 2, weeks part 2

    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B, modified_C, modified_D, modified_E, modified_F = A, B, C, D, E, F
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(2, 10) if num != A])  # Weekly rides part 1
        modified_B = random.choice([num for num in range(20, 31, 5) if num != B])  # Distance per ride part 1
        modified_C = random.choice([num for num in range(2, 10) if num != C])  # Weeks part 1
        modified_D = random.choice([num for num in range(2, 10) if num != D])  # Weekly rides part 2
        modified_E = random.choice([num for num in range(50, 71, 10) if num != E])  # Distance per ride part 2
        modified_F = random.choice([num for num in range(2, 10) if num != F])  # Weeks part 2

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_D *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_D = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    weekly_distance_part1 = modified_A * modified_B
    distance_part1 = weekly_distance_part1 * modified_C
    weekly_distance_part2 = modified_D * modified_E
    distance_part2 = weekly_distance_part2 * modified_F
    total_distance = distance_part1 + distance_part2

    # Save original values in the modified format
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C,
        "D": modified_D, "E": modified_E, "F": modified_F,
        "ans": total_distance
    }

    if is_symbolic:
        # Represent numbers symbolically with quotes
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        modified_D, modified_E, modified_F = '\'D\'', '\'E\'', '\'F\''
        weekly_distance_part1 = f"{modified_A} * {modified_B}"
        distance_part1 = f"{weekly_distance_part1} * {modified_C}"
        weekly_distance_part2 = f"{modified_D} * {modified_E}"
        distance_part2 = f"{weekly_distance_part2} * {modified_F}"
        total_distance = f"{distance_part1} + {distance_part2}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=name, A=modified_A, B=modified_B, C=modified_C, D=modified_D, E=modified_E, F=modified_F)
    answer = answer_text.format(
        NAME=name,
        A=modified_A, B=modified_B, C=modified_C,
        D=modified_D, E=modified_E, F=modified_F,
        WEEKLY_DISTANCE_PART1=weekly_distance_part1,
        DISTANCE_PART1=distance_part1,
        WEEKLY_DISTANCE_PART2=weekly_distance_part2,
        DISTANCE_PART2=distance_part2,
        TOTAL_DISTANCE=total_distance
    )

    return {"question": question, "answer": answer, "original_values": original_values}
