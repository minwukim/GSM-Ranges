import random

def q36(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} walked {A} miles on Monday. On Tuesday, {NAME} walked {B} times as many miles as they walked on Monday. "
        "Their total mileage Monday through Wednesday was {C} miles. How many miles did they walk on Wednesday?"
    )
    answer_text = (
        "{NAME}'s Tuesday walk was {A}*{B} = <<{A}*{B}={TUESDAY_MILES}>>{TUESDAY_MILES} miles.\n"
        "{NAME}'s Monday and Tuesday walks were {A}+{TUESDAY_MILES} = <<{A}+{TUESDAY_MILES}={MONDAY_TUESDAY_MILES}>>{MONDAY_TUESDAY_MILES} miles combined.\n"
        "Their Wednesday walk was {C}-{MONDAY_TUESDAY_MILES} = <<{C}-{MONDAY_TUESDAY_MILES}={WEDNESDAY_MILES}>>{WEDNESDAY_MILES} miles.\n#### {WEDNESDAY_MILES}"
    )
    
    # Original values
    A, B, C = 4, 6, 41  # Miles on Monday, multiplier for Tuesday, total mileage
    default_name = "Walt"

    # Dynamic name generation
    common_names = ["Alice", "Jack", "Sophia", "Michael", "Emma"]
    uncommon_names = ["Haruto", "Yara", "Chen", "Aisha", "Mei"]
    random_strings = ["Tqlpxzv", "Lkrwymx", "Fzbnqpt", "Xmstvpl", "Qrltwzx"]

    if name_level == 1:
        modified_name = default_name
    elif name_level == 2:
        modified_name = random.choice(common_names)
    elif name_level == 3:
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = random.choice(random_strings)

    # Adjust values for difficulty levels
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    else:
        modified_A = random.choice([num for num in range(2, 6) if num != A])
        modified_B = random.choice([num for num in range(2, 8) if num != B])
        modified_C = random.choice([num for num in range(modified_A + modified_A * modified_B + 1, 100) if num != C])

        if num_level == 3:
            modified_B *= multiplier
            modified_C *= multiplier
        elif num_level == 4:
            modified_B = random.randint(multiplier, int(multiplier * 1.5))
            modified_C = random.randint(modified_A + modified_A * modified_B + 1, multiplier * 10 - 1)

    # Calculate totals
    tuesday_miles = modified_A * modified_B
    monday_tuesday_miles = modified_A + tuesday_miles
    wednesday_miles = modified_C - monday_tuesday_miles

    A = modified_A
    B = modified_B
    C = modified_C

    original_values = {
        "A": A, 
        "B": B, 
        "C": C, 
        "ans": C - (A + (A * B))
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        tuesday_miles = f"{modified_A}*{modified_B}"
        monday_tuesday_miles = f"{modified_A}+{tuesday_miles}"
        wednesday_miles = f"{modified_C}-{monday_tuesday_miles}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        TUESDAY_MILES=tuesday_miles,
        MONDAY_TUESDAY_MILES=monday_tuesday_miles,
        WEDNESDAY_MILES=wednesday_miles
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}

