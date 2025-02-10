import random

def q29(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} slept {A} hours on Monday. For the next two days, {NAME} slept {B} hours less, each, because of assignments. "
        "For the rest of the week, {NAME} slept {C} hour more than those two days. How many hours did {NAME} sleep in total throughout the week?"
    )
    answer_text = (
        "If {NAME} slept {A} hours on Monday, then {NAME} slept {A}-{B} = <<{A}-{B}={NEXT_DAY_SLEEP}>>{NEXT_DAY_SLEEP} hours on each of the next two days.\n"
        "The total for the two days is {NEXT_DAY_SLEEP}*2 = <<{NEXT_DAY_SLEEP}*2={NEXT_TWO_DAYS_SLEEP}>>{NEXT_TWO_DAYS_SLEEP} hours.\n"
        "For the rest of the week, {NAME} slept {NEXT_DAY_SLEEP}+{C} = <<{NEXT_DAY_SLEEP}+{C}={REST_DAY_SLEEP}>>{REST_DAY_SLEEP} hours each day.\n"
        "Over 4 days, this is 4*{REST_DAY_SLEEP} = <<4*{REST_DAY_SLEEP}={REST_WEEK_SLEEP}>>{REST_WEEK_SLEEP} hours.\n"
        "The total sleep for the week is {A}+{NEXT_TWO_DAYS_SLEEP}+{REST_WEEK_SLEEP} = <<{A}+{NEXT_TWO_DAYS_SLEEP}+{REST_WEEK_SLEEP}={TOTAL_SLEEP}>>{TOTAL_SLEEP} hours.\n#### {TOTAL_SLEEP}"
    )
    
    # Original values
    A, B, C = 8, 2, 1  # Hours on Monday, hours less for two days, hours more for rest of the week
    original_name = "Sadie"

    # Name pools
    common_names = ["John", "Alice", "Mia", "Chris", "Emily"]
    uncommon_names = ["Yuki", "Arjun", "Mei", "Ravi", "Hana"]
    random_strings = ["Zjxptlm", "Wkzrntg", "Lpsdrmj", "Txbwqkr", "Vlnczxk"]

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        modified_name = random.choice(common_names)
    elif name_level == 3:
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"  # Explicit symbol assignment
    elif name_level == 5:
        modified_name = random.choice(random_strings)

    # Modify the values for num_level
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    else:
        modified_A = random.choice([num for num in range(6, 10) if num != A])
        modified_B = random.choice([num for num in range(2, 6) if num != B])
        modified_C = random.choice([num for num in range(1, 3) if num != C])

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier
            modified_C *= multiplier
        elif num_level == 4:
            modified_A = random.randint(multiplier * 6, multiplier * 10 - 1)
            modified_B = random.randint(multiplier * 2, multiplier * 5)
            modified_C = random.randint(multiplier * 1, multiplier * 10 - 1)

    # Calculate totals
    next_day_sleep = modified_A - modified_B
    next_two_days_sleep = next_day_sleep * 2
    rest_day_sleep = next_day_sleep + modified_C
    rest_week_sleep = 4 * rest_day_sleep
    total_sleep = modified_A + next_two_days_sleep + rest_week_sleep

    A = modified_A
    B = modified_B
    C = modified_C

    original_values = {
        "A": A,
        "B": B,
        "C": C,
        "ans": A + ((A - B) * 2) + (4 * ((A - B) + C))
    }

    if is_symbolic:
        # Represent values symbolically
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        next_day_sleep = f"{modified_A}-{modified_B}"
        next_two_days_sleep = f"2*({next_day_sleep})"
        rest_day_sleep = f"{next_day_sleep}+{modified_C}"
        rest_week_sleep = f"4*({rest_day_sleep})"
        total_sleep = f"{modified_A}+{next_two_days_sleep}+{rest_week_sleep}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        NEXT_DAY_SLEEP=next_day_sleep,
        NEXT_TWO_DAYS_SLEEP=next_two_days_sleep,
        REST_DAY_SLEEP=rest_day_sleep,
        REST_WEEK_SLEEP=rest_week_sleep,
        TOTAL_SLEEP=total_sleep
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
