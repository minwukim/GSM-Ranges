import random

def q41(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} attends {A} times of {B}-hour classes each on Mondays, Wednesdays, and Fridays. "
        "On Tuesdays and Thursdays, {NAME} attends {C} times of {D}-hour classes each. "
        "If the semester lasts for {E} weeks, how many hours does {NAME} spend attending classes during the semester?"
    )
    answer_text = (
        "{NAME} spends {A} x {B} = <<{A}*{B}={MWF_DAILY_HOURS}>>{MWF_DAILY_HOURS} hours on any Monday, Wednesday, or Friday.\n"
        "Over the week, {NAME} spends {MWF_DAILY_HOURS} x 3 = <<{MWF_DAILY_HOURS}*3={MWF_WEEKLY_HOURS}>>{MWF_WEEKLY_HOURS} hours on Monday, Wednesday, and Friday.\n"
        "Throughout the semester, that amounts to {MWF_WEEKLY_HOURS} x {E} = <<{MWF_WEEKLY_HOURS}*{E}={MWF_TOTAL_HOURS}>>{MWF_TOTAL_HOURS} hours.\n"
        "On Tuesdays and Thursdays, {NAME} spends {C} x {D} = <<{C}*{D}={TTH_DAILY_HOURS}>>{TTH_DAILY_HOURS} hours in class.\n"
        "This totals {TTH_DAILY_HOURS} x 2 = <<{TTH_DAILY_HOURS}*2={TTH_WEEKLY_HOURS}>>{TTH_WEEKLY_HOURS} hours per week.\n"
        "Over the semester, this is {TTH_WEEKLY_HOURS} x {E} = <<{TTH_WEEKLY_HOURS}*{E}={TTH_TOTAL_HOURS}>>{TTH_TOTAL_HOURS} hours.\n"
        "In total, {NAME} spends {MWF_TOTAL_HOURS} + {TTH_TOTAL_HOURS} = <<{MWF_TOTAL_HOURS}+{TTH_TOTAL_HOURS}={TOTAL_HOURS}>>{TOTAL_HOURS} hours attending classes in the semester.\n#### {TOTAL_HOURS}"
    )
    
    # Original values
    A, B, C, D, E = 3, 1, 2, 2, 16  # Classes per day (MWF), hours per class (MWF), classes per day (TTh), hours per class (TTh), weeks in the semester
    default_name = "Kimo"

    # Dynamic name generation
    common_names = ["Kimo", "James", "Sophia", "Emma", "Olivia"]
    uncommon_names = ["Akira", "Saanvi", "Leilani", "Anika", "Yuki"]
    random_strings = ["Xbdtrp", "Jkrmvq", "Lvnzdq", "Vwrtpk", "Plznxq"]

    if name_level == 1:
        name = default_name
    elif name_level == 2:
        name = random.choice(common_names)
    elif name_level == 3:
        name = random.choice(uncommon_names)
    elif name_level == 4:
        name = "Z"
    elif name_level == 5:
        name = random.choice(random_strings)

    # Modify the values based on num_level
    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D, modified_E = A, B, C, D, E
    else:
        modified_A = random.choice([num for num in range(2, 6) if num != A])
        modified_B = random.choice([num for num in range(1, 4) if num != B])
        modified_C = random.choice([num for num in range(1, 4) if num != C])
        modified_D = random.choice([num for num in range(1, 4) if num != D])
        modified_E = random.choice([num for num in range(14, 20) if num != E])

        if num_level == 3:
            modified_A *= multiplier
            modified_C *= multiplier
        elif num_level == 4:
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_C = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    mwf_daily_hours = modified_A * modified_B
    mwf_weekly_hours = mwf_daily_hours * 3
    mwf_total_hours = mwf_weekly_hours * modified_E

    tth_daily_hours = modified_C * modified_D
    tth_weekly_hours = tth_daily_hours * 2
    tth_total_hours = tth_weekly_hours * modified_E

    total_hours = mwf_total_hours + tth_total_hours

    A = modified_A
    B = modified_B
    C = modified_C
    D = modified_D
    E = modified_E

    original_values = {
        "A": A, "B": B, "C": C, "D": D, "E": E, 
        "ans": (A * B) * 3 * E + (C * D) * 2 * E
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D, modified_E = '\'A\'', '\'B\'', '\'C\'', '\'D\'', '\'E\''
        mwf_daily_hours = f"{modified_A} * {modified_B}"
        mwf_weekly_hours = f"{mwf_daily_hours} * 3"
        mwf_total_hours = f"{mwf_weekly_hours} * {modified_E}"

        tth_daily_hours = f"{modified_C} * {modified_D}"
        tth_weekly_hours = f"{tth_daily_hours} * 2"
        tth_total_hours = f"{tth_weekly_hours} * {modified_E}"

        total_hours = f"{mwf_total_hours} + {tth_total_hours}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=name, A=modified_A, B=modified_B, C=modified_C, D=modified_D, E=modified_E)
    answer = answer_text.format(
        NAME=name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        D=modified_D,
        E=modified_E,
        MWF_DAILY_HOURS=mwf_daily_hours,
        MWF_WEEKLY_HOURS=mwf_weekly_hours,
        MWF_TOTAL_HOURS=mwf_total_hours,
        TTH_DAILY_HOURS=tth_daily_hours,
        TTH_WEEKLY_HOURS=tth_weekly_hours,
        TTH_TOTAL_HOURS=tth_total_hours,
        TOTAL_HOURS=total_hours
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
