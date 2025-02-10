import random

def q11(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} baked {A} apple pies for the fireman's luncheon. She cut each pie into {B} pieces and set the {A} pies out on the buffet table for the guests to serve themselves. "
        "At the end of the evening, after the guests had taken and eaten their pieces of pie, there were {C} pieces of pie remaining. "
        "How many pieces were taken by the guests?"
    )
    answer_text = (
        "To start the evening, there were {A} pies, each with {B} pieces, which is {A}*{B}=<<{A}*{B}={TOTAL_PIECES}>>{TOTAL_PIECES} pieces of pie.\n"
        "If only {C} remained, then {TOTAL_PIECES}-{C}=<<{TOTAL_PIECES}-{C}={TAKEN_PIECES}>>{TAKEN_PIECES} pieces of pie had been taken by guests.\n#### {TAKEN_PIECES}"
    )

    # Original values
    A, B, C = 5, 8, 14  # Number of pies, pieces per pie, remaining pieces
    original_name = "Grandma Jones"

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        common_names = ["Mary", "Linda", "Barbara", "Elizabeth", "Susan"]
        modified_name = random.choice(common_names)
    elif name_level == 3:
        uncommon_names = ["Winifred", "Eulalia", "Cressida", "Dorothea", "Genevieve"]
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        symbols = ["Z", "Y", "X", "W", "V"]
        modified_name = symbols[0]
    elif name_level == 5:
        random_strings = ["Grmjns", "Crtnk", "Fldpr", "Blkrts", "Tmplnx"]
        modified_name = random.choice(random_strings)

    # Modify the values for num_level
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    else:
        modified_A = random.choice([num for num in range(4, 10) if num != A])
        modified_B = random.choice([num for num in range(5, 10) if num != B])
        modified_C = random.choice([num for num in range(10, 20) if num != C])

        if num_level == 3:
            modified_B *= multiplier
            modified_C *= multiplier
        elif num_level == 4:
            modified_B = random.randint(multiplier * 5, multiplier * 10 - 1)
            modified_C = random.randint(multiplier * 10, multiplier * 19)

    # Calculate the total pieces and pieces taken
    total_pieces = modified_A * modified_B
    taken_pieces = total_pieces - modified_C

    A = modified_A
    B = modified_B
    C = modified_C

    original_values = {"A": A, "B": B, "C": C, "ans": (A * B) - C}

    if is_symbolic:
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        total_pieces = f"{modified_A} * {modified_B}"
        taken_pieces = f"{total_pieces} - {modified_C}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        TOTAL_PIECES=total_pieces,
        TAKEN_PIECES=taken_pieces
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
