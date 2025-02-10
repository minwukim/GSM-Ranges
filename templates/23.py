import random

def q23(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} likes to have {A} glass(es) of water with breakfast, lunch, and dinner. Finally, they have one before going to bed as well. "
        "{NAME} does this every weekday, but on the weekends they like to relax and have a soda with dinner instead. "
        "How many glasses of water does {NAME} drink in a week?"
    )
    answer_text = (
        "{NAME} has {A}*3+1=<<{A}*3+1={DAILY_WATER}>>{DAILY_WATER} glasses of water a day on each of the 5 weekdays, for {DAILY_WATER}*5=<<{DAILY_WATER}*5={WEEKDAY_WATER}>>{WEEKDAY_WATER} glasses.\n"
        "On the weekends, they have {A}*2+1=<<{A}*2+1={WEEKEND_WATER}>>{WEEKEND_WATER} glasses of water each day, for {WEEKEND_WATER}*2=<<{WEEKEND_WATER}*2={TOTAL_WEEKEND_WATER}>>{TOTAL_WEEKEND_WATER} glasses.\n"
        "In total, they drink {WEEKDAY_WATER}+{TOTAL_WEEKEND_WATER}=<<{WEEKDAY_WATER}+{TOTAL_WEEKEND_WATER}={TOTAL_WATER}>>{TOTAL_WATER} glasses of water in a week.\n#### {TOTAL_WATER}"
    )
    
    # Original value
    A = 1  # Number of glasses of water per meal
    original_name = "John"

    # Name pools for name assignment
    common_names = ["Liam", "Sophia", "Noah", "Emma", "James"]
    uncommon_names = ["Haruto", "Mei", "Akari", "Rin", "Sora"]
    random_strings = ["Jndsarx", "Fldfdadpr", "Crstasdan", "Trmfsadnx", "Blkasdn"]

    # Modify name based on name_level
    if name_level == 1:
        # Level 1: Use original name
        modified_name = original_name
    elif name_level == 2:
        # Level 2: Replace with common names
        modified_name = random.choice(common_names)
    elif name_level == 3:
        # Level 3: Replace with uncommon (Asian) names
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        # Level 4: Assign the symbol Z explicitly
        modified_name = "Z"
    elif name_level == 5:
        # Level 5: Replace with random strings without vowels
        modified_name = random.choice(random_strings)

    # Modify the value for num_level
    if num_level == 1:
        # Level 1: Use original value
        modified_A = A
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(2, 10) if num != A])  # Slightly varied values for level 2

        if num_level == 3:
            modified_A *= multiplier  # Scaled values for level 3
        elif num_level == 4:
            modified_A = random.randint(multiplier, multiplier * 10 - 1)  # Randomized range for level 4

    # Calculate water consumption
    daily_water = modified_A * 3 + 1
    weekday_water = daily_water * 5
    weekend_water = modified_A * 2 + 1
    total_weekend_water = weekend_water * 2
    total_water = weekday_water + total_weekend_water

    original_values = {
        "A": A,
        "ans": (A * 3 + 1) * 5 + (A * 2 + 1) * 2
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A = '\'A\''
        daily_water = f"{modified_A}*3+1"
        weekday_water = f"({daily_water})*5"
        weekend_water = f"{modified_A}*2+1"
        total_weekend_water = f"({weekend_water})*2"
        total_water = f"({weekday_water})+({total_weekend_water})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        DAILY_WATER=daily_water,
        WEEKDAY_WATER=weekday_water,
        WEEKEND_WATER=weekend_water,
        TOTAL_WEEKEND_WATER=total_weekend_water,
        TOTAL_WATER=total_water
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
