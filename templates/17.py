import random

def q17(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} had {A} stickers. {NAME} bought {B} stickers from a store in the mall and got {C} stickers for their birthday. "
        "Then {NAME} gave {D} of the stickers to their sibling and used {E} to decorate a greeting card. "
        "How many stickers does {NAME} have left?"
    )
    answer_text = (
        "The total number of stickers is {A} + {B} + {C} = <<{A}+{B}+{C}={TOTAL_STICKERS}>>{TOTAL_STICKERS}.\n"
        "The number of stickers given away and used on the greeting card is {D} + {E} = <<{D}+{E}={STICKERS_USED}>>{STICKERS_USED}.\n"
        "{NAME} has {TOTAL_STICKERS} − {STICKERS_USED} = <<{TOTAL_STICKERS}-{STICKERS_USED}={STICKERS_LEFT}>>{STICKERS_LEFT} stickers left.\n#### {STICKERS_LEFT}"
    )
    
    # Original values
    A, B, C, D, E = 10, 21, 23, 9, 28  # Initial stickers, bought stickers, birthday stickers, given stickers, used stickers
    original_name = "Charlie"

    # Name pools for name assignment
    common_names = ["Liam", "Emma", "Olivia", "Sophia", "James"]
    uncommon_names = ["Haruto", "Akari", "Rin", "Takeshi", "Sanjay"]
    random_strings = ["Chrlx", "Ktrmn", "Plrfn", "Fldrx", "Trmnk"]

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
        modified_A, modified_B, modified_C, modified_D, modified_E = A, B, C, D, E
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(10, 31) if num != A])
        modified_B = random.choice([num for num in range(20, 31) if num != B])
        modified_C = random.choice([num for num in range(20, 31) if num != C])
        modified_D = random.choice([num for num in range(5, 20) if num != D])
        modified_E = random.choice([num for num in range(10, 30) if num != E])

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_B *= multiplier
            modified_C *= multiplier
            modified_D *= multiplier
            modified_E *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier * 1, multiplier * 3)
            modified_B = random.randint(multiplier * 2, multiplier * 3)
            modified_C = random.randint(multiplier * 2, multiplier * 3)
            modified_D = random.randint(multiplier // 2, multiplier * 2)
            modified_E = random.randint(multiplier * 1, multiplier * 3 - 1)

    # Calculate totals
    total_stickers = modified_A + modified_B + modified_C
    stickers_used = modified_D + modified_E
    stickers_left = total_stickers - stickers_used

    A = modified_A
    B = modified_B
    C = modified_C
    D = modified_D
    E = modified_E

    original_values = {
        "A": A, 
        "B": B, 
        "C": C, 
        "D": D, 
        "E": E, 
        "ans": (A + B + C) - (D + E)
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D, modified_E = '\'A\'', '\'B\'', '\'C\'', '\'D\'', '\'E\''
        total_stickers = f"{modified_A} + {modified_B} + {modified_C}"
        stickers_used = f"{modified_D} + {modified_E}"
        stickers_left = f"({total_stickers}) - ({stickers_used})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D, E=modified_E)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        D=modified_D,
        E=modified_E,
        TOTAL_STICKERS=total_stickers,
        STICKERS_USED=stickers_used,
        STICKERS_LEFT=stickers_left
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
