import random

def q85(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} decides to take up juggling to perform at the school talent show a month in the future.  "
        "He starts off practicing juggling {A} balls, and slowly gets better adding {B} ball(s) to his juggling act each week.  "
        "After the end of {C} weeks the talent show begins, but when {NAME} walks on stage he slips and drops {D} of his balls.  "
        "{E} of them are caught by people in the crowd as they roll off the stage, but one gets lost completely since the auditorium is dark.  "
        "With a sigh, {NAME} starts to juggle on stage with how many balls?"
    )
    answer_text = (
        "{NAME} starts with {A} balls and adds {B} ball each week for {C} weeks for a total of ({A}+{B}*{C}) = "
        "<<{A}+{B}*{C}={TOTAL_BALLS}>>{TOTAL_BALLS}.\n"
        "{NAME} drops {D} balls when he trips on stage, leaving him with ({TOTAL_BALLS}-{D}) = "
        "<<{TOTAL_BALLS}-{D}={FINAL_BALLS}>>{FINAL_BALLS} balls.\n#### {FINAL_BALLS}"
    )

    # Name options
    common_names = ["Emma", "Sophia", "Liam", "Noah", "Olivia"]
    uncommon_names = ["Hiroshi", "Meilin", "Arun", "Yuki", "Ayesha"]
    random_strings = ["Tgfdwer", "Asvklmn", "Qpwxoer", "Lkrucvn", "Mzpltxf"]

    # Extract original name
    original_name = "Josh"

    # Name level adjustments
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

    # Original numbers
    A, B, C, D, E = 3, 1, 4, 3, 2

    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D, modified_E = A, B, C, D, E
    else:
        # Level 2: Numbers of the same digit length, different from the original
        modified_A = random.choice([num for num in range(2, 10) if num != A])
        modified_B = random.choice([num for num in range(1, 10) if num != B])
        modified_C = random.choice([num for num in range(2, 10) if num != C])
        modified_D = random.choice([num for num in range(3, min(10, modified_A + modified_B * modified_C)) if num != D])
        modified_E = random.choice([num for num in range(2, modified_D) if num != E])

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_C *= multiplier
            modified_D *= multiplier
            modified_E *= multiplier
        elif num_level == 4:
            # Generate values in the range (multiplier, 10 * multiplier - 1)
            modified_A = random.randint(multiplier, 10 * multiplier - 1)
            modified_C = random.randint(multiplier, 10 * multiplier - 1)
            modified_D = random.randint(multiplier+2, min(10 * multiplier - 1, modified_A + modified_B * modified_C))
            modified_E = random.randint(multiplier, modified_D)

    # Calculate totals
    total_balls = modified_A + modified_B * modified_C
    final_balls = total_balls - modified_D

    # Store original values
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, 
        "D": modified_D, "E": modified_E, "ans": final_balls
    }

    if is_symbolic:
        # Symbolic representation
        modified_A, modified_B, modified_C = "'A'", "'B'", "'C'"
        modified_D, modified_E = "'D'", "'E'"
        total_balls = f"({modified_A} + {modified_B} * {modified_C})"
        final_balls = f"({total_balls} - {modified_D})"

    # Replace placeholders in question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D, E=modified_E)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A, B=modified_B, C=modified_C, 
        D=modified_D, E=modified_E, 
        TOTAL_BALLS=total_balls, FINAL_BALLS=final_balls
    )

    return {"question": question, "answer": answer, "original_values": original_values if is_symbolic else None}
