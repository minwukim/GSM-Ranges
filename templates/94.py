import random

def q94(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} is doing the laundry, and thinks she has missed some socks. There are {A} socks that need washing. "
        "If she washes {B} pairs of socks and {C} loose socks, how many socks has {NAME} missed?"
    )
    answer_text = (
        "Splitting the pairs shows there were {B} pairs of socks * 2 socks/pair = <<{B}*2={PAIRED_SOCKS}>>{PAIRED_SOCKS} socks paired together.\n"
        "This means she has washed a total of {PAIRED_SOCKS} paired socks + {C} loose socks = <<{PAIRED_SOCKS}+{C}={WASHED_SOCKS}>>{WASHED_SOCKS} socks.\n"
        "She has therefore missed {A} socks - {WASHED_SOCKS} socks = <<{A}-{WASHED_SOCKS}={MISSED_SOCKS}>>{MISSED_SOCKS} socks.\n#### {MISSED_SOCKS}"
    )

    # Original values
    A, B, C = 50, 10, 15
    default_name = "Lindsay"

    # Dynamic name generation
    common_names = ["Alice", "Emma", "Sophia", "Olivia", "Mia"]
    uncommon_names = ["Haruka", "Mingyu", "Kaede", "Rinako", "Takeshi"]
    random_strings = ["Trplqmv", "Nsvktbz", "Rkzfnxp", "Bxvltyq", "Lcmtrpz"]

    if name_level == 1:
        modified_name = default_name
    elif name_level == 2:
        modified_name = random.choice([name for name in common_names if name != default_name])
    elif name_level == 3:
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = random.choice(random_strings)

    # Adjust values for difficulty levels
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    else:
        modified_A = random.choice([num for num in range(50, 100, 10) if num != A])
        modified_B = random.choice([num for num in range(5, 15) if num != B])
        modified_C = random.choice([num for num in range(10, 21, 10) if num != C])

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier
            modified_C *= multiplier

        elif num_level == 4:
            modified_A = random.randint(6 * multiplier, 10 * multiplier - 1)
            modified_B = random.randint(multiplier, 2 * multiplier)
            modified_C = random.randint(multiplier, 2 * multiplier)

    # Calculate totals
    paired_socks = modified_B * 2
    washed_socks = paired_socks + modified_C
    missed_socks = modified_A - washed_socks

    # Save original values
    original_values = {
        "A": modified_A,
        "B": modified_B,
        "C": modified_C,
        "ans": missed_socks
    }

    if is_symbolic:
        # Represent numbers symbolically with quotes
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        paired_socks = f"({modified_B} * 2)"
        washed_socks = f"({paired_socks} + {modified_C})"
        missed_socks = f"({modified_A} - {washed_socks})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A, B=modified_B, C=modified_C,
        PAIRED_SOCKS=paired_socks,
        WASHED_SOCKS=washed_socks,
        MISSED_SOCKS=missed_socks
    )

    return {"question": question, "answer": answer, "original_values": original_values}
