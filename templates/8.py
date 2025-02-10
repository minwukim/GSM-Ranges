import random

def q8(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} made two stops during his {A}-mile bike trip. He first stopped after {B} miles. "
        "His second stop was {C} miles before the end of the trip. How many miles did {NAME} travel between his first and second stops?"
    )
    answer_text = (
        "{NAME} traveled {B} miles + {C} miles = <<{B}+{C}={NON_STOP_DISTANCE}>>{NON_STOP_DISTANCE} miles not counting the distance between stops.\n"
        "{NAME} traveled {A} miles - {NON_STOP_DISTANCE} miles = <<{A}-{NON_STOP_DISTANCE}={BETWEEN_DISTANCE}>>{BETWEEN_DISTANCE} miles between his first and second stop.\n#### {BETWEEN_DISTANCE}"
    )

    # Original values
    A, B, C = 60, 20, 15  # Total distance, first stop distance, and second stop distance before the end
    original_name = "Henry"

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        common_names = ["James", "William", "Michael", "David", "Richard"]
        modified_name = random.choice(common_names)
    elif name_level == 3:
        uncommon_names = ["Simeon", "Quillon", "Ephraim", "Aurelian", "Thaddeus"]
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        symbols = ["Z", "Y", "X", "W", "V"]
        modified_name = symbols[0]
    elif name_level == 5:
        random_strings = ["Plkro", "Qwert", "Asdfg", "Zxcvb", "Mjnhy"]
        modified_name = random.choice(random_strings)

    # Modify the distances based on num_level
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    else:
        # Modify the distances for levels > 1
        modified_A = random.choice([num for num in range(50, 91, 10) if num != A])
        modified_B = random.choice([num for num in range(10, 26, 5) if num != B])
        modified_C = random.choice([num for num in range(10, 21, 5) if num != C])

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_B *= multiplier
            modified_C *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.choice([num for num in range(multiplier * 5, multiplier * 9)])
            modified_B = random.choice([num for num in range(multiplier * 1, multiplier * 2)])
            modified_C = random.choice([num for num in range(multiplier * 1, multiplier * 2)])

    # Calculate the non-stop distance and the distance between stops
    non_stop_distance = modified_B + modified_C
    between_distance = modified_A - non_stop_distance

    A = modified_A
    B = modified_B
    C = modified_C

    original_values = {
        "A": A, 
        "B": B, 
        "C": C, 
        "ans": A - (B + C)
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        non_stop_distance = f"{modified_B} + {modified_C}"
        between_distance = f"{modified_A} - ({non_stop_distance})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=modified_name, 
        A=modified_A, 
        B=modified_B, 
        C=modified_C,
        NON_STOP_DISTANCE=non_stop_distance, 
        BETWEEN_DISTANCE=between_distance
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}

    return {"question": question, "answer": answer}

