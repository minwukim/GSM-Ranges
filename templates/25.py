import random

def q25(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} has {A} boxes. Each box is {B} inches by {C} inches by {D} inches. "
        "The walls are {E} inch thick. What is the total inner volume of all {A} boxes?"
    )
    answer_text = (
        "The walls subtract 2*{E}=<<2*{E}={WALL_REDUCTION}>>{WALL_REDUCTION} inches from each dimension.\n"
        "So each box has {B}-{WALL_REDUCTION}=<<{B}-{WALL_REDUCTION}={INNER_WIDTH}>>{INNER_WIDTH} inch width.\n"
        "It also has a {C}-{WALL_REDUCTION}=<<{C}-{WALL_REDUCTION}={INNER_HEIGHT}>>{INNER_HEIGHT} inch height.\n"
        "Finally, it has a {D}-{WALL_REDUCTION}=<<{D}-{WALL_REDUCTION}={INNER_DEPTH}>>{INNER_DEPTH} inch depth.\n"
        "So the inner volume of one box is {INNER_WIDTH}*{INNER_HEIGHT}*{INNER_DEPTH}=<<{INNER_WIDTH}*{INNER_HEIGHT}*{INNER_DEPTH}={INNER_VOLUME_ONE}>>{INNER_VOLUME_ONE} cubic inches.\n"
        "So in total the inner volume of the {A} boxes is {A}*{INNER_VOLUME_ONE}=<<{A}*{INNER_VOLUME_ONE}={TOTAL_VOLUME}>>{TOTAL_VOLUME} cubic inches.\n#### {TOTAL_VOLUME}"
    )
    
    # Original values
    A, B, C, D, E = 3, 5, 6, 4, 1  # Number of boxes, dimensions of the box, wall thickness
    original_name = "John"

    # Name pools for name assignment
    common_names = ["Liam", "Emma", "Noah", "Sophia", "James"]
    uncommon_names = ["Haruto", "Akari", "Mei", "Sora", "Rin"]
    random_strings = ["Jnwrbslz", "Fqrkpmdl", "Zmnrxplq", "Blktrpsz", "Cwtlqvnr"]

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
        # Level 5: Replace with random strings
        modified_name = random.choice(random_strings)

    # Modify the values for num_level
    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B, modified_C, modified_D, modified_E = A, B, C, D, E
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(1, 10) if num != A])  # Number of boxes
        modified_B = random.choice([num for num in range(3, 10) if num != B])  # Box length
        modified_C = random.choice([num for num in range(3, 10) if num != C])  # Box width
        modified_D = random.choice([num for num in range(3, 10) if num != D])  # Box height
        modified_E = 1

        if num_level == 3:
            # Scale values for level 3
            modified_B *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_B = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    wall_reduction = 2 * modified_E
    inner_width = modified_B - wall_reduction
    inner_height = modified_C - wall_reduction
    inner_depth = modified_D - wall_reduction
    inner_volume_one = inner_width * inner_height * inner_depth
    total_volume = modified_A * inner_volume_one

    # Original values for symbolic mode
    original_values = {
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "E": E,
        "ans": A * ((B - 2 * E) * (C - 2 * E) * (D - 2 * E))
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D, modified_E = '\'A\'', '\'B\'', '\'C\'', '\'D\'', '\'E\''
        wall_reduction = f"2*{modified_E}"
        inner_width = f"{modified_B}-{wall_reduction}"
        inner_height = f"{modified_C}-{wall_reduction}"
        inner_depth = f"{modified_D}-{wall_reduction}"
        inner_volume_one = f"({inner_width})*({inner_height})*({inner_depth})"
        total_volume = f"{modified_A}*({inner_volume_one})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D, E=modified_E)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        D=modified_D,
        E=modified_E,
        WALL_REDUCTION=wall_reduction,
        INNER_WIDTH=inner_width,
        INNER_HEIGHT=inner_height,
        INNER_DEPTH=inner_depth,
        INNER_VOLUME_ONE=inner_volume_one,
        TOTAL_VOLUME=total_volume
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
