import random

def q92(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original question and answer template
    question_text = (
        "{NAME} had dance practice for {TUESDAY_HOURS} hour(s) on Tuesdays and {THURSDAY_HOURS} hour(s) on Thursdays. "
        "On Saturdays, she had dance practice that lasted twice as long as Tuesday's night class. "
        "How many hours a week did she have dance practice?"
    )
    answer_text = (
        "She had practice for {TUESDAY_HOURS} hour on Tuesday and {THURSDAY_HOURS} hours on Thursday so she practiced for {TUESDAY_HOURS}+{THURSDAY_HOURS} = "
        "<<{TUESDAY_HOURS}+{THURSDAY_HOURS}={WEEKDAY_HOURS}>>{WEEKDAY_HOURS} hours\n"
        "Saturday's class was twice as long as Tuesday's so she danced 2*{TUESDAY_HOURS} = "
        "<<2*{TUESDAY_HOURS}={SATURDAY_HOURS}>>{SATURDAY_HOURS} hours on Saturday\n"
        "In one week she danced {WEEKDAY_HOURS} hours on the weekdays and {SATURDAY_HOURS} hours on the weekend for a total of "
        "{WEEKDAY_HOURS}+{SATURDAY_HOURS} = <<{WEEKDAY_HOURS}+{SATURDAY_HOURS}={TOTAL_HOURS}>>{TOTAL_HOURS} hours\n#### {TOTAL_HOURS}"
    )

    # Original values
    name = "Hallie"
    TUESDAY_HOURS, THURSDAY_HOURS = 1, 2  # Hours for Tuesday and Thursday

    # Modify name based on name_level
    if name_level == 1:
        modified_name = name
    elif name_level == 2:
        common_names = ["Emma", "Sophia", "Olivia", "Mia", "Isabella"]
        modified_name = random.choice([n for n in common_names if n != name])
    elif name_level == 3:
        uncommon_names = ["Haruka", "Kaede", "Rinako", "Aiko", "Mingyu"]
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=7))

    # Modify numbers based on num_level
    if num_level == 1:
        modified_tuesday_hours, modified_thursday_hours = TUESDAY_HOURS, THURSDAY_HOURS
    elif num_level == 2:
        modified_tuesday_hours = random.choice([n for n in range(1, 10) if n != TUESDAY_HOURS])
        modified_thursday_hours = random.choice([n for n in range(1, 10) if n != THURSDAY_HOURS])
    elif num_level == 3:
        modified_tuesday_hours = random.choice([n for n in range(1, 10) if n != TUESDAY_HOURS]) * multiplier
        modified_thursday_hours = random.choice([n for n in range(1, 10) if n != THURSDAY_HOURS]) * multiplier
    elif num_level == 4:
        modified_tuesday_hours = random.randint(multiplier, multiplier * 2)
        modified_thursday_hours = random.randint(multiplier, multiplier * 3)

    # Ensure relationships and calculate derived values
    modified_saturday_hours = 2 * modified_tuesday_hours
    modified_weekday_hours = modified_tuesday_hours + modified_thursday_hours
    modified_total_hours = modified_weekday_hours + modified_saturday_hours

    # Prepare original_values dictionary before modifications for symbolic case
    original_values = {
        "A": modified_tuesday_hours,
        "B": modified_thursday_hours,
        "C": modified_saturday_hours,
        "ans": modified_total_hours
    }

    if is_symbolic:
        # Replace numbers with symbols
        modified_tuesday_hours, modified_thursday_hours = "'A'", "'B'"
        modified_saturday_hours = "2*'A'"
        modified_weekday_hours = "('A'+'B')"
        modified_total_hours = f"({modified_weekday_hours}+{modified_saturday_hours})"

    # Format question and answer
    question = question_text.format(
        NAME=modified_name,
        TUESDAY_HOURS=modified_tuesday_hours,
        THURSDAY_HOURS=modified_thursday_hours
    )
    answer = answer_text.format(
        NAME=modified_name,
        TUESDAY_HOURS=modified_tuesday_hours,
        THURSDAY_HOURS=modified_thursday_hours,
        WEEKDAY_HOURS=modified_weekday_hours,
        SATURDAY_HOURS=modified_saturday_hours,
        TOTAL_HOURS=modified_total_hours
    )

    return {"question": question, "answer": answer, "original_values": original_values}
