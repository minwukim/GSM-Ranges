import random

def q35(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} and {NAME2} went to a carnival. {NAME1} rode the roller coaster {A} times while {NAME2} rode it {B} times. "
        "After that, each of them decided to ride the luge {C} times. "
        "If each ride cost {D} tickets, how many tickets did they use that day?"
    )
    answer_text = (
        "The total times they rode the roller coaster is {A}+{B}=<<{A}+{B}={ROLLER_COASTER_RIDES}>>{ROLLER_COASTER_RIDES} times.\n"
        "The total times they rode the luge is {C}+{C}=<<{C}+{C}={LUGE_RIDES}>>{LUGE_RIDES} times.\n"
        "The total times they rode that day is {ROLLER_COASTER_RIDES}+{LUGE_RIDES}=<<{ROLLER_COASTER_RIDES}+{LUGE_RIDES}={TOTAL_RIDES}>>{TOTAL_RIDES} times.\n"
        "So, {NAME1} and {NAME2} used {TOTAL_RIDES}*{D}=<<{TOTAL_RIDES}*{D}={TOTAL_TICKETS}>>{TOTAL_TICKETS} tickets that day.\n#### {TOTAL_TICKETS}"
    )
    
    # Original values
    A, B, C, D = 2, 4, 2, 6  # Pam's roller coaster rides, Fred's roller coaster rides, luge rides per person, ticket cost per ride
    name1, name2 = "Pam", "Fred"

    # Name pools
    common_names = ["Alice", "Jack", "Sophia", "Michael", "Emma"]
    uncommon_names = ["Haruto", "Yara", "Chen", "Aisha", "Mei"]
    random_strings = ["Tqrmylv", "Zbnxpqw", "Plknqrz", "Vtmswyx", "Fzlrqwp"]

    # Assign names based on name_level
    if name_level == 1:
        modified_name1, modified_name2 = name1, name2
    elif name_level == 2:
        modified_name1 = random.choice(common_names)
        modified_name2 = random.choice([name for name in common_names if name != modified_name1])
    elif name_level == 3:
        modified_name1 = random.choice(uncommon_names)
        modified_name2 = random.choice([name for name in uncommon_names if name != modified_name1])
    elif name_level == 4:
        modified_name1, modified_name2 = "Z", "Y"
    elif name_level == 5:
        modified_name1 = random.choice(random_strings)
        modified_name2 = random.choice([name for name in random_strings if name != modified_name1])

    # Modify the values for levels > 1
    if num_level > 1:
        modified_A = random.choice([num for num in range(2, 10) if num != A])
        modified_B = random.choice([num for num in range(2, 10) if num != B])
        modified_C = random.choice([num for num in range(2, 10) if num != C])
        modified_D = random.choice([num for num in range(2, 10) if num != D])

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier
            modified_C *= multiplier
    else:
        modified_A, modified_B, modified_C, modified_D = A, B, C, D

    if num_level == 4:
        modified_A = random.randint(multiplier, multiplier * 10 - 1)
        modified_B = random.randint(multiplier, multiplier * 10 - 1)
        modified_C = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    roller_coaster_rides = modified_A + modified_B
    luge_rides = modified_C + modified_C  # Each person rides `C` times
    total_rides = roller_coaster_rides + luge_rides
    total_tickets = total_rides * modified_D

    A = modified_A
    B = modified_B
    C = modified_C
    D = modified_D

    original_values = {
        "A": A, "B": B, "C": C, "D": D,
        "ans": ((A + B) + (C + C)) * D
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D = '\'A\'', '\'B\'', '\'C\'', '\'D\''
        roller_coaster_rides = f"{modified_A} + {modified_B}"
        luge_rides = f"{modified_C} + {modified_C}"
        total_rides = f"({roller_coaster_rides}) + ({luge_rides})"
        total_tickets = f"({total_rides}) * {modified_D}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=modified_name1, NAME2=modified_name2, A=modified_A, B=modified_B, C=modified_C, D=modified_D)
    answer = answer_text.format(
        NAME1=modified_name1,
        NAME2=modified_name2,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        D=modified_D,
        ROLLER_COASTER_RIDES=roller_coaster_rides,
        LUGE_RIDES=luge_rides,
        TOTAL_RIDES=total_rides,
        TOTAL_TICKETS=total_tickets
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
