import random

def q5(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} gets paid ${A} per hour to teach and ${B} to be a cheerleading coach. "
        "If she works {C} weeks a year, {D} hours a week as a teacher and {E} hours a week as a coach, what's her annual salary?"
    )
    answer_text = (
        "First find the total amount {NAME} makes per week teaching: ${A}/hour * {D} hours/week = $<<{A}*{D}={TEACHING_WEEKLY}>>{TEACHING_WEEKLY}/week\n"
        "Then find the total amount {NAME} makes per week coaching: ${B}/hour * {E} hours/week = $<<{B}*{E}={COACHING_WEEKLY}>>{COACHING_WEEKLY}/week\n"
        "Then add those two amounts to find the total amount {NAME} makes per week: ${TEACHING_WEEKLY}/week + ${COACHING_WEEKLY}/week = $<<{TEACHING_WEEKLY}+{COACHING_WEEKLY}={TOTAL_WEEKLY}>>{TOTAL_WEEKLY}/week\n"
        "Then multiply that number by the number of weeks {NAME} works in a year to find her annual salary: ${TOTAL_WEEKLY}/week * {C} weeks/year = $<<{TOTAL_WEEKLY}*{C}={ANNUAL_SALARY}>>{ANNUAL_SALARY}\n#### {ANNUAL_SALARY}"
    )
    
    # Original values
    A, B = 20, 30  # Hourly rates for teaching and coaching
    C = 50         # Weeks worked per year (multiple of 10)
    D, E = 35, 15  # Weekly hours for teaching and coaching
    original_name = "Jill"

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        common_names = ["Emma", "Sophia", "Olivia", "Isabella", "Mia"]
        modified_name = random.choice(common_names)
    elif name_level == 3:
        uncommon_names = ["Haruka", "Meera", "Saniya", "Rinako", "Takeshi"]
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        symbols = ["Z", "Y", "X"]
        modified_name = random.choice(symbols)
    elif name_level == 5:
        random_strings = ["Asdfds", "Qwedsaf", "Zxcnnds", "Lmncklx", "Vghiogkl"]
        modified_name = random.choice(random_strings)

    # Modify numbers based on num_level
    if num_level == 1:
        modified_A, modified_B = A, B
        modified_C = C
        modified_D, modified_E = D, E
    else:
        # Level 2: Change numbers with the same digits but different values
        modified_A = random.choice([num for num in range(10, 51, 10) if num != A])
        modified_B = random.choice([num for num in range(10, 51, 10) if num != B])
        modified_C = random.choice([num for num in range(30, 51, 10) if num != C])
        modified_D = random.choice([num for num in range(20, 41, 5) if num != D])
        modified_E = random.choice([num for num in range(10, 31, 5) if num != E])

        if num_level == 3:
            # Apply multiplier for level 3
            modified_A = modified_A * multiplier
            modified_B = modified_B * multiplier

    if num_level == 4:
        # Replace numbers with values in the range [100, 999]
        modified_A = random.randint(multiplier, multiplier * 10 - 1)
        modified_B = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate weekly and annual salary based on the modified values
    teaching_weekly = modified_A * modified_D
    coaching_weekly = modified_B * modified_E
    total_weekly = teaching_weekly + coaching_weekly
    annual_salary = total_weekly * modified_C

    A = modified_A
    B = modified_B
    C = modified_C
    D = modified_D
    E = modified_E

    original_values = {
        "A": A, "B": B, "C": C, "D": D, "E": E,
        "ans": annual_salary
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D, modified_E = '\'A\'', '\'B\'', '\'C\'', '\'D\'', '\'E\''
        teaching_weekly = f"{modified_A} * {modified_D}"
        coaching_weekly = f"{modified_B} * {modified_E}"
        total_weekly = f"{teaching_weekly} + {coaching_weekly}"
        annual_salary = f"{total_weekly} * {modified_C}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(
        NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D, E=modified_E
    )
    answer = answer_text.format(
        NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D, E=modified_E,
        TEACHING_WEEKLY=teaching_weekly, COACHING_WEEKLY=coaching_weekly,
        TOTAL_WEEKLY=total_weekly, ANNUAL_SALARY=annual_salary
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}

    return {"question": question, "answer": answer}
