import random

def q60(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "It takes {NAME} {A} minutes to finish a crossword puzzle and {B} minutes to finish a sudoku puzzle. "
        "Over the weekend {NAME} solved {C} crossword puzzles and {D} sudoku puzzles. "
        "How many minutes did {NAME} spend playing these games?"
    )
    answer_text = (
        "It takes {A} minutes to complete a crossword puzzle and {NAME} completed {C} for a total of {A}*{C} = "
        "<<{A}*{C}={CROSSWORD_TOTAL}>>{CROSSWORD_TOTAL} minutes\n"
        "It takes {B} minutes to complete a sudoku puzzle and {NAME} completed {D} for a total of {B}*{D} = "
        "<<{B}*{D}={SUDOKU_TOTAL}>>{SUDOKU_TOTAL} minutes\n"
        "{NAME} spent {CROSSWORD_TOTAL} minutes on crosswords and {SUDOKU_TOTAL} minutes on sudoku for a total of "
        "{CROSSWORD_TOTAL}+{SUDOKU_TOTAL} = <<{CROSSWORD_TOTAL}+{SUDOKU_TOTAL}={TOTAL_TIME}>>{TOTAL_TIME} minutes\n#### {TOTAL_TIME}"
    )

    # Name options
    common_names = ["Alice", "Emma", "Sophia", "Olivia", "Liam"]
    uncommon_names = ["Haruto", "Yara", "Kaede", "Rinako", "Aarav"]
    random_strings = ["Xptzqwl", "Nkjdfvq", "Ghrwzlp", "Bvxskfr", "Lmndtrq"]
    
    # Original values
    original_name = "Carmen"
    A, B, C, D = 10, 5, 3, 8  # Time for crossword, sudoku, number of crosswords, number of sudokus

    # Name modification
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        modified_name = random.choice([name for name in common_names if name != original_name])
    elif name_level == 3:
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = random.choice(random_strings)

    # Number modification
    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        # Level 2: Same digit numbers with constraints
        modified_A = random.choice([num for num in range(10, 100, 10) if num != A and num % 5 == 0])
        modified_B = random.choice([num for num in range(5, 50, 5) if num != B and num % 5 == 0])
        modified_C = random.choice([num for num in range(2, 10) if num != C])
        modified_D = random.choice([num for num in range(2, 10) if num != D])
        
        # Level 3: Multiply by multiplier
        if num_level == 3:
            modified_A *= multiplier
            modified_D *= multiplier
        
        # Level 4: Random range
        elif num_level == 4:
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_D = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    crossword_total = modified_A * modified_C
    sudoku_total = modified_B * modified_D
    total_time = crossword_total + sudoku_total

    # Original values dictionary
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "D": modified_D, "ans": total_time
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D = "'A'", "'B'", "'C'", "'D'"
        crossword_total = f"{modified_A} * {modified_C}"
        sudoku_total = f"{modified_B} * {modified_D}"
        total_time = f"{crossword_total} + {sudoku_total}"
    
    # Generate question and answer
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D)
    answer = answer_text.format(
        NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D,
        CROSSWORD_TOTAL=crossword_total, SUDOKU_TOTAL=sudoku_total, TOTAL_TIME=total_time
    )
    
    # Return outputs
    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
