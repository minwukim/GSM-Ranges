import random

def q20(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} has {A} times the number of pets as {NAME2}. {NAME2} has {B} more pets than {NAME3}. "
        "If {NAME3} has {C} pets, how many total pets do the three have?"
    )
    answer_text = (
        "{NAME2} has {C} + {B} = <<{C}+{B}={MARCIA_PETS}>>{MARCIA_PETS} pets.\n"
        "{NAME1} has {A} * {MARCIA_PETS} = <<{A}*{MARCIA_PETS}={JAN_PETS}>>{JAN_PETS} pets.\n"
        "In total, the three have {C} + {MARCIA_PETS} + {JAN_PETS} = <<{C}+{MARCIA_PETS}+{JAN_PETS}={TOTAL_PETS}>>{TOTAL_PETS} pets.\n#### {TOTAL_PETS}"
    )

    # Original values
    A, B, C = 3, 2, 4  # Times pets (Jan to Marcia), additional pets (Marcia to Cindy), Cindy's pets
    original_names = ["Jan", "Marcia", "Cindy"]

    # Name pools for name assignment
    common_names = ["Liam", "Emma", "Sophia", "Olivia", "James", "Alice", "Ethan", "Chloe", "Noah", "Ava"]
    uncommon_names = ["Haruto", "Akari", "Rin", "Takeshi", "Sanjay", "Yuki", "Mei", "Kaoru", "Sora", "Hikaru"]
    random_strings = ["Jnrqx", "Mrtnz", "Cnrdv", "Flpnk", "Trmnx"]

    # Modify names based on name_level
    if name_level == 1:
        modified_names = original_names
    elif name_level == 2:
        modified_names = random.sample(common_names, 3)
    elif name_level == 3:
        modified_names = random.sample(uncommon_names, 3)
    elif name_level == 4:
        modified_names = ["Z", "Y", "X"]
    elif name_level == 5:
        modified_names = random.sample(random_strings, 3)

    NAME1, NAME2, NAME3 = modified_names

    # Modify the values for num_level
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    else:
        modified_A = random.choice([num for num in range(2, 10) if num != A])
        modified_B = random.choice([num for num in range(2, 6) if num != B])
        modified_C = random.choice([num for num in range(2, 5) if num != C])

        if num_level == 3:
            modified_B *= multiplier
            modified_C *= multiplier
        elif num_level == 4:
            modified_B = random.randint(multiplier * 2, multiplier * 5)
            modified_C = random.randint(multiplier * 2, multiplier * 5)

    # Calculate totals
    marcia_pets = modified_C + modified_B
    jan_pets = modified_A * marcia_pets
    total_pets = modified_C + marcia_pets + jan_pets

    A = modified_A
    B = modified_B
    C = modified_C

    original_values = {"A": A, "B": B, "C": C, "ans": total_pets}

    if is_symbolic:
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        marcia_pets = f"{modified_C} + {modified_B}"
        jan_pets = f"{modified_A} * ({marcia_pets})"
        total_pets = f"{modified_C} + {marcia_pets} + {jan_pets}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=NAME1, NAME2=NAME2, NAME3=NAME3, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME1=NAME1,
        NAME2=NAME2,
        NAME3=NAME3,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        MARCIA_PETS=marcia_pets,
        JAN_PETS=jan_pets,
        TOTAL_PETS=total_pets
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
