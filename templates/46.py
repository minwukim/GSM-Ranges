import random

def q46(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} walks {A} miles a day. Except on weekends when {NAME} walks {B} miles. How many miles does {NAME} walk in a week?"
    )
    answer_text = (
        "{NAME} walks 5 weekdays * {A} miles/day = <<5*{A}={WEEKDAY_MILES}>>{WEEKDAY_MILES} miles during the weekdays.\n"
        "{NAME} walks 2 weekend days * {B} miles/day = <<2*{B}={WEEKEND_MILES}>>{WEEKEND_MILES} miles during the weekend.\n"
        "In total, {NAME} walks {WEEKDAY_MILES} + {WEEKEND_MILES} = <<{WEEKDAY_MILES}+{WEEKEND_MILES}={TOTAL_MILES}>>{TOTAL_MILES} miles in a week.\n#### {TOTAL_MILES}"
    )
    
    # Original values
    A, B = 20, 10  # Miles walked on weekdays and weekends

    # Dynamic name generation
    common_names = ["Sam", "Emma", "Chris", "Alex", "Taylor"]
    uncommon_names = ["Hiro", "Aisha", "Mei", "Raj", "Lila"]
    random_strings = ["Xlyfrz", "Tmfqvs", "Prkltz", "Bgjwvs", "Lmzptq"]

    if name_level == 1:
        name = "Pancho"
    elif name_level == 2:
        name = random.choice(common_names)
    elif name_level == 3:
        name = random.choice(uncommon_names)
    elif name_level == 4:
        name = "Z"
    elif name_level == 5:
        name = random.choice(random_strings)

    # Adjust values for difficulty levels
    if num_level == 1:
        modified_A, modified_B = A, B
    else:
        modified_A = random.choice([num for num in range(10, 91, 10) if num != A])
        modified_B = random.choice([num for num in range(10, 91, 10) if num != B])

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier
        elif num_level == 4:
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_B = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    weekday_miles = 5 * modified_A  # 5 weekdays
    weekend_miles = 2 * modified_B  # 2 weekend days
    total_miles = weekday_miles + weekend_miles

    # Store original and modified values
    original_values = {
        "A": modified_A, 
        "B": modified_B,
        "ans": total_miles
    }

    if is_symbolic:
        # Represent numbers symbolically with quotes
        modified_A, modified_B = "'A'", "'B'"
        weekday_miles = f"5 * {modified_A}"
        weekend_miles = f"2 * {modified_B}"
        total_miles = f"{weekday_miles} + {weekend_miles}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=name, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME=name,
        A=modified_A,
        B=modified_B,
        WEEKDAY_MILES=weekday_miles,
        WEEKEND_MILES=weekend_miles,
        TOTAL_MILES=total_miles
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
