import random

def q75(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} makes designer jewelry. Her specialty is topaz necklaces. She uses {A} topaz gemstones per necklace, "
        "and fills the space between gemstones using sterling silver beads. If each topaz gemstone is one inch long, "
        "each sterling silver bead is 1/{C} of an inch long, and each necklace is made to a total length of {B} inches, "
        "how many sterling silver beads does {NAME} use per necklace?"
    )
    answer_text = (
        "{A} topaz gemstones, at 1 inch per gemstone, contribute a total of {A}*1=<<{A}*1={TOPAZ_TOTAL}>>{TOPAZ_TOTAL} inches to each necklace.\n"
        "Since each necklace is {B} inches in length, then there are {B}-{TOPAZ_TOTAL}=<<{B}-{TOPAZ_TOTAL}={SPACE_BETWEEN}>>{SPACE_BETWEEN} inches of space between gemstones.\n"
        "Since {NAME} uses 1/{C} inch sterling silver beads to fill the space, then she will require {SPACE_BETWEEN}*{C}=<<{SPACE_BETWEEN}*{C}={TOTAL_BEADS}>>{TOTAL_BEADS} sterling silver beads per necklace.\n#### {TOTAL_BEADS}"
    )
    
    # Name options
    common_names = ["Alice", "Sophia", "Emma", "Mia", "Olivia"]
    uncommon_names = ["Haruto", "Kaede", "Mei", "Rinako", "Takeshi"]
    random_strings = ["Fgihajk", "Lmsytkp", "Rqvsnwl", "Ktrjwfb", "Xpqmdvb"]
    
    # Dynamic name generation
    if name_level == 1:
        name = "Katerina"
    elif name_level == 2:
        name = random.choice([n for n in common_names if n != "Katerina"])
    elif name_level == 3:
        name = random.choice(uncommon_names)
    elif name_level == 4:
        name = "Z"
    elif name_level == 5:
        name = random.choice(random_strings)
    
    # Original values
    A, B, C = 8, 25, 4  # A: topaz gemstones, B: total necklace length, C: sterling bead fractional denominator
    
    # Number modifications
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    elif num_level == 2:
        modified_A = random.choice([num for num in range(2, 10) if num != A])  # Same digit range, different value
        modified_B = random.choice([num for num in range(20, 100, 5) if num != B])  # Multiple of 5
        modified_C = random.choice([num for num in range(2, 10) if num != C])  # Same range for fractional denominator
    elif num_level == 3:
        modified_A = random.choice([num for num in range(2, 10) if num != A]) * multiplier
        modified_B = random.choice([num for num in range(20, 100, 5) if num != B]) * multiplier
        modified_C = random.choice([num for num in range(2, 10) if num != C])
    elif num_level == 4:
        modified_B = random.randint(multiplier + 2, 10 * multiplier - 1)
        modified_A = random.randint(multiplier, modified_B)
        modified_C = random.choice([num for num in range(2, 10) if num != C])  # Same range for fractional denominator
    
    # Ensure logical relationships
    topaz_total = modified_A  # Each gemstone is 1 inch, so total gemstone length = modified_A
    space_between = modified_B - topaz_total  # Remaining space after accounting for gemstone length
    total_beads = space_between * modified_C  # Beads required to fill the remaining space

    # Store original values before symbolic modification
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "ans": total_beads
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = "'A'", "'B'", "'C'"
        topaz_total = f"{modified_A}"
        space_between = f"({modified_B} - {topaz_total})"
        total_beads = f"({space_between} * {modified_C})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=name, A=modified_A, B=modified_B, C=modified_C,
        TOPAZ_TOTAL=topaz_total, SPACE_BETWEEN=space_between, TOTAL_BEADS=total_beads
    )

    return {"question": question, "answer": answer, "original_values": original_values}
