import random

def q93(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} made a dozen bread rolls for breakfast. After feeding her {A} children with one each, she broke each of the remaining rolls into {B} pieces and fed them to the chickens. How many pieces of rolls did she feed to the chickens?"
    )
    answer_text = (
        "After feeding her children, {NAME} was left with 12 - {A} = <<12-{A}={REMAINING_ROLLS}>>{REMAINING_ROLLS} rolls\n"
        "She fed {REMAINING_ROLLS} x {B} = <<{REMAINING_ROLLS}*{B}={TOTAL_PIECES}>>{TOTAL_PIECES} pieces of rolls to the chickens.\n#### {TOTAL_PIECES}"
    )

    # Name options
    common_names = ["Alice", "Emma", "Sophia", "Olivia", "Mia"]
    uncommon_names = ["Haruka", "Mei", "Aisha", "Rinako", "Takeshi"]
    random_strings = ["Fjakslf", "Ghdjsqo", "Vmkernq", "Plxoeiw", "Qxjfhar"]

    # Original values
    name = "Mrs. Sherman"
    A, B = 6, 8  # Number of children, pieces per roll

    # Adjust name based on name_level
    if name_level == 1:
        modified_name = name
    elif name_level == 2:
        modified_name = random.choice([n for n in common_names if n not in name])
    elif name_level == 3:
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = random.choice(random_strings)

    # Adjust numbers based on num_level
    if num_level == 1:
        modified_A, modified_B = A, B
    else:
        modified_A = random.choice([num for num in range(1, 12) if num != A])  # Number of children
        modified_B = random.choice([num for num in range(5, 15) if num != B])  # Pieces per roll

        if num_level == 3:
            modified_B *= multiplier
        elif num_level == 4:
            modified_B = random.randint(multiplier, 10 * multiplier - 1)

    # Calculate results
    remaining_rolls = 12 - modified_A
    total_pieces = remaining_rolls * modified_B

    # Save original values before modifying for symbolic
    original_values = {
        "A": modified_A, "B": modified_B, "ans": total_pieces
    }

    if is_symbolic:
        # Represent numbers symbolically with quotes
        modified_A, modified_B = '\'A\'', '\'B\''
        remaining_rolls = f"(12 - {modified_A})"
        total_pieces = f"({remaining_rolls} * {modified_B})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        REMAINING_ROLLS=remaining_rolls,
        TOTAL_PIECES=total_pieces
    )

    return {"question": question, "answer": answer, "original_values": original_values}
