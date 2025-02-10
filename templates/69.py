import random

def q69(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original question and answer templates
    question_text = (
        "Last night {NAME} killed {A} wolves and {B} cougars while hunting. Today {NAME} killed {C} times as many wolves as cougars "
        "and {D} fewer cougars than the previous night. How many animals did {NAME} kill?"
    )
    answer_text = (
        "The total number of animals that {NAME} killed while hunting yesterday is {B}+{A} = <<{B}+{A}={TOTAL_YESTERDAY}>>{TOTAL_YESTERDAY}\n"
        "Today, {NAME} killed {D} fewer cougars than the previous night, a total of {B}-{D} = <<{B}-{D}={TODAY_COUGARS}>>{TODAY_COUGARS} cougars.\n"
        "He also killed {C} times as many wolves as cougars today, a total of {C}*{TODAY_COUGARS} = <<{C}*{TODAY_COUGARS}={TODAY_WOLVES}>>{TODAY_WOLVES} wolves.\n"
        "Together, his hunt today yielded {TODAY_WOLVES}+{TODAY_COUGARS} = <<{TODAY_WOLVES}+{TODAY_COUGARS}={TOTAL_TODAY}>>{TOTAL_TODAY} animals.\n"
        "In total, he has {TOTAL_TODAY}+{TOTAL_YESTERDAY} = <<{TOTAL_TODAY}+{TOTAL_YESTERDAY}={TOTAL_ANIMALS}>>{TOTAL_ANIMALS} animals from the hunt.\n#### {TOTAL_ANIMALS}"
    )

    # Name modification based on level
    common_names = ["John", "Emma", "Lucas", "Sophia", "Jack"]
    uncommon_names = ["Rin", "Haruto", "Mei", "Aarav", "Lian"]
    random_strings = ["Plxtrqz", "Frwvjsn", "Xmqtwzn", "Drpqvks", "Bzvwltx"]

    if name_level == 1:
        name = "Rick"
    elif name_level == 2:
        name = random.choice([n for n in common_names if n != "Rick"])
    elif name_level == 3:
        name = random.choice(uncommon_names)
    elif name_level == 4:
        name = "Z"
    elif name_level == 5:
        name = random.choice(random_strings)

    # Original values
    A, B, C, D = 10, 15, 3, 3  # Wolves (last night), cougars, multiplier for wolves, fewer cougars

    # Modified values based on num_level
    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    elif num_level == 2:
        modified_A = random.choice([num for num in range(10, 100) if num != A and num % 10 == 0])
        modified_B = random.choice([num for num in range(10, 100) if num != B and num % 5 == 0])
        modified_C = random.choice([num for num in range(2, 10) if num != C])
        modified_D = random.choice([num for num in range(1, 10) if num != D])
    elif num_level == 3:
        modified_A = random.choice([num for num in range(10, 100) if num != A and num % 10 == 0]) * multiplier
        modified_B = random.choice([num for num in range(10, 100) if num != B and num % 5 == 0]) * multiplier
        modified_C = random.choice([num for num in range(2, 10) if num != C])
        modified_D = random.choice([num for num in range(1, 10) if num != D])
    elif num_level == 4:
        modified_A = random.randint(multiplier, 10 * multiplier - 1)
        modified_B = random.randint(multiplier + 2, 10 * multiplier - 1)
        modified_C = random.choice([num for num in range(2, 10) if num != C])
        modified_D = random.randint(multiplier, modified_B - 1)

    # Ensure logical consistency for positivity
    today_cougars = modified_B - modified_D  # Cougars today
    today_wolves = modified_C * today_cougars  # Wolves today
    total_yesterday = modified_A + modified_B  # Animals yesterday
    total_today = today_wolves + today_cougars  # Animals today
    total_animals = total_yesterday + total_today  # Total animals

    # Original values before modification for symbolic cases
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "D": modified_D,
        "ans": total_animals
    }

    if is_symbolic:
        # Symbolic representation
        modified_A, modified_B, modified_C, modified_D = "'A'", "'B'", "'C'", "'D'"
        today_cougars = f"({modified_B} - {modified_D})"
        today_wolves = f"({modified_C} * {today_cougars})"
        total_yesterday = f"({modified_A} + {modified_B})"
        total_today = f"({today_wolves} + {today_cougars})"
        total_animals = f"({total_yesterday} + {total_today})"

    # Replace placeholders in templates
    question = question_text.format(NAME=name, A=modified_A, B=modified_B, C=modified_C, D=modified_D)
    answer = answer_text.format(
        NAME=name,
        A=modified_A, B=modified_B, C=modified_C, D=modified_D,
        TOTAL_YESTERDAY=total_yesterday,
        TODAY_COUGARS=today_cougars,
        TODAY_WOLVES=today_wolves,
        TOTAL_TODAY=total_today,
        TOTAL_ANIMALS=total_animals
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
