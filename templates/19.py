import random

def q19(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} is sewing a quilt out of old souvenir t-shirts. {NAME} has one shirt from each vacation they have been on. Every shirt is its own quilt block. "
        "Each row is made of blocks from a different year of vacations. They go on {A} vacations a year and have been vacationing since they were {B} years old. "
        "They are now {C}. How many quilt blocks does {NAME} have in total?"
    )
    answer_text = (
        "{NAME} has been on {C} - {B} = <<{C}-{B}={YEARS_OF_VACATIONS}>>{YEARS_OF_VACATIONS} years of vacations, so they have {YEARS_OF_VACATIONS} rows of blocks.\n"
        "They go on {A} vacations a year, so they have been on {A} * {YEARS_OF_VACATIONS} = <<{A}*{YEARS_OF_VACATIONS}={TOTAL_VACATIONS}>>{TOTAL_VACATIONS} vacations.\n"
        "{NAME} has 1 shirt from each vacation, so they have {TOTAL_VACATIONS} * 1 = <<{TOTAL_VACATIONS}*1={TOTAL_BLOCKS}>>{TOTAL_BLOCKS} quilt blocks in all.\n#### {TOTAL_BLOCKS}"
    )
    
    # Original values
    A, B, C = 4, 23, 34  # Vacations per year, starting age, current age
    original_name = "Gene"

    # Name pools for name assignment
    common_names = ["Liam", "Emma", "Sophia", "Olivia", "James"]
    uncommon_names = ["Haruto", "Akari", "Rin", "Takeshi", "Sanjay"]
    random_strings = ["Gnmrk", "Fldpr", "Trmnx", "Blkrn", "Crstn"]

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

    # Modify the values for num_level
    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B, modified_C = A, B, C
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(2, 9) if num != A])  # Vacations per year
        modified_B = random.choice([num for num in range(20, 30) if num != B])  # Starting age
        modified_C = random.choice([num for num in range(35, 50) if num != C])  # Current age

        if num_level == 3:
            # Scale values for level 3
            modified_B *= multiplier
            modified_C *= multiplier

    if num_level == 4:
        # Use values within a scaled range for level 4
        modified_B = random.randint(multiplier * 2, multiplier * 3 - 1)
        modified_C = random.randint(multiplier * 3, multiplier * 5)

    # Calculate totals
    years_of_vacations = modified_C - modified_B
    total_vacations = modified_A * years_of_vacations
    total_blocks = total_vacations  # One quilt block per vacation

    A = modified_A
    B = modified_B
    C = modified_C

    # Dictionary of original values
    original_values = {
        "A": A, 
        "B": B, 
        "C": C, 
        "ans": A * (C - B)  # Final answer in original values
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        years_of_vacations = f"{modified_C} - {modified_B}"
        total_vacations = f"{modified_A} * ({years_of_vacations})"
        total_blocks = total_vacations

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        YEARS_OF_VACATIONS=years_of_vacations,
        TOTAL_VACATIONS=total_vacations,
        TOTAL_BLOCKS=total_blocks
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
