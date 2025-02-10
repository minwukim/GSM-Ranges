import random

def q70(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Question and answer templates
    question_text = (
        "{NAME} starts on floor {START_FLOOR}. He rides the elevator up to the floor that's equal to {MULTIPLIER} times his starting floor plus {ADD}. "
        "What floor is {NAME} on now?"
    )
    answer_text = (
        "First multiply {NAME}'s starting floor number by {MULTIPLIER}: {START_FLOOR} * {MULTIPLIER} = "
        "<<{START_FLOOR}*{MULTIPLIER}={STEP1}>>{STEP1}\n"
        "Then add {ADD} to find the ending floor {NAME} is on: {STEP1} + {ADD} = <<{STEP1}+{ADD}={FINAL_FLOOR}>>{FINAL_FLOOR}\n#### {FINAL_FLOOR}"
    )
    
    # Name options
    common_names = ["Tom", "Emma", "Jack", "Sophia", "Lucas"]
    uncommon_names = ["Haruto", "Mei", "Aisha", "Raj", "Lila"]
    random_strings = ["Lzqwfhs", "Mnvxprd", "Qbrwpls", "Zjfhtmd", "Xtkhspr"]

    # Dynamic name selection
    original_name = "Bill"
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

    # Original values
    START_FLOOR, MULTIPLIER, ADD = 3, 4, 6

    # Adjust values based on num_level
    if num_level == 1:
        modified_start, modified_multiplier, modified_add = START_FLOOR, MULTIPLIER, ADD
    else:
        # Generate numbers based on rules for each level
        modified_start = random.choice([num for num in range(2, 10) if num != START_FLOOR])
        modified_multiplier = random.choice([num for num in range(2, 10) if num != MULTIPLIER])
        modified_add = random.choice([num for num in range(2, 10) if num != ADD and num % 5 == 0])

        if num_level == 3:
            modified_multiplier *= multiplier
            modified_add *= multiplier
        elif num_level == 4:
            modified_multiplier = random.randint(multiplier, multiplier * 10 - 1)
            modified_add = random.randint(multiplier, multiplier * 10 - 1)
    
    # Calculate intermediate and final steps
    step1 = modified_start * modified_multiplier
    final_floor = step1 + modified_add

    # Declare original values dictionary before any modifications for symbolic representation
    original_values = {
        "A": modified_start, 
        "B": modified_multiplier, 
        "C": modified_add, 
        "ans": final_floor
    }

    if is_symbolic:
        # Symbolic representation with 'A', 'B', 'C', etc.
        modified_start, modified_multiplier, modified_add = "'A'", "'B'", "'C'"
        step1 = f"({modified_start} * {modified_multiplier})"
        final_floor = f"({step1} + {modified_add})"

    # Format question and answer
    question = question_text.format(
        NAME=modified_name, START_FLOOR=modified_start, MULTIPLIER=modified_multiplier, ADD=modified_add
    )
    answer = answer_text.format(
        NAME=modified_name, START_FLOOR=modified_start, MULTIPLIER=modified_multiplier, ADD=modified_add,
        STEP1=step1, FINAL_FLOOR=final_floor
    )

    # Return output
    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
