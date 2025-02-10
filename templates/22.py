import random

def q22(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} is an avid gardener. Yesterday, {NAME} received {A} new potted plant(s) from their favorite plant nursery. "
        "They already have {B} potted plant(s) on each of the {C} window ledges of their large country home. "
        "Feeling generous, {NAME} has decided that they will give {D} potted plant(s) from each ledge to friends and family tomorrow. "
        "How many potted plant(s) will {NAME} remain with?"
    )
    answer_text = (
        "Yesterday, before receiving the plants, {NAME} had {B}*{C} = <<{B}*{C}={INITIAL_PLANTS}>>{INITIAL_PLANTS} potted plants.\n"
        "After receiving an additional {A} plants, they therefore had a total of {INITIAL_PLANTS} + {A} = <<{INITIAL_PLANTS}+{A}={TOTAL_PLANTS}>>{TOTAL_PLANTS} potted plants.\n"
        "Tomorrow, {NAME}’s plant giveaway will be {C}*{D} = <<{C}*{D}={GIVEN_PLANTS}>>{GIVEN_PLANTS} potted plants.\n"
        "They will therefore remain with {TOTAL_PLANTS} - {GIVEN_PLANTS} = <<{TOTAL_PLANTS}-{GIVEN_PLANTS}={REMAINING_PLANTS}>>{REMAINING_PLANTS} potted plants.\n#### {REMAINING_PLANTS}"
    )
    
    # Original values
    A, B, C, D = 18, 2, 40, 1  # New plants, plants per ledge, number of ledges, plants given per ledge
    original_name = "Mary"

    # Name pools for name assignment
    common_names = ["Liam", "Emma", "Sophia", "Olivia", "James"]
    uncommon_names = ["Haruto", "Akari", "Rin", "Takeshi", "Sanjay"]
    random_strings = ["Gnmrk", "Fldpr", "Trmnx", "Blkrn", "Crstn"]

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        modified_name = random.choice(common_names)
    elif name_level == 3:
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = random.choice(random_strings)

    # Modify the values for num_level
    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(10, 100) if num != A])  # New plants
        modified_B = random.choice([num for num in range(2, 9) if num != B])  # Plants per ledge
        modified_C = random.choice([num for num in range(10, 91, 10) if num != C])  # Number of ledges
        modified_D = random.choice([num for num in range(1, modified_B) if num != D])  # Plants given per ledge

        if num_level == 3:
            modified_A *= multiplier
            modified_C *= multiplier

        if num_level == 4:
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_C = random.choice([num for num in range(multiplier, multiplier * 10, 10)])

    # Calculate totals
    initial_plants = modified_B * modified_C
    total_plants = initial_plants + modified_A
    given_plants = modified_C * modified_D
    remaining_plants = total_plants - given_plants

    A = modified_A
    B = modified_B
    C = modified_C
    D = modified_D

    original_values = {
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "ans": remaining_plants
    }

    if is_symbolic:
        modified_A, modified_B, modified_C, modified_D = '\'A\'', '\'B\'', '\'C\'', '\'D\''
        initial_plants = f"{modified_B}*{modified_C}"
        total_plants = f"{initial_plants}+{modified_A}"
        given_plants = f"{modified_C}*{modified_D}"
        remaining_plants = f"{total_plants}-{given_plants}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        D=modified_D,
        INITIAL_PLANTS=initial_plants,
        TOTAL_PLANTS=total_plants,
        GIVEN_PLANTS=given_plants,
        REMAINING_PLANTS=remaining_plants
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
