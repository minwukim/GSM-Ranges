import random

def q82(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} has a record store where people can trade their own records for new ones. "
        "People can trade {A} old records for {CONSTANT_NEW} new one. {B} people come in with old records and leave with {C} new records between them. "
        "How many old records did the {B} people bring in?"
    )
    answer_text = (
        "People can bring in {A} old records = get {CONSTANT_NEW} new record.\n"
        "{B} people come in with old records and leave with {C} new records, {C} new records x {A} old records traded for each = "
        "<<{C}*{A}={TOTAL_OLD_RECORDS}>>{TOTAL_OLD_RECORDS} old records that the {B} people brought in.\n#### {TOTAL_OLD_RECORDS}"
    )

    # Name options
    common_names = ["Alice", "Emma", "Jack", "Sophia", "Liam"]
    uncommon_names = ["Haruto", "Mei", "Aisha", "Raj", "Lila"]
    random_strings = ["Bkdwlrz", "Xhfqvtn", "Pkzrtlj", "Vmsqyfx", "Lmrpzqw"]

    # Dynamic name generation
    if name_level == 1:
        name = "Ralph"
    elif name_level == 2:
        name = random.choice([n for n in common_names if n != "Ralph"])
    elif name_level == 3:
        name = random.choice(uncommon_names)
    elif name_level == 4:
        name = "Z"
    elif name_level == 5:
        name = random.choice(random_strings)

    # Original values
    A, B, C = 2, 5, 7  # Trade ratio, number of people, new records obtained
    CONSTANT_NEW = 1  # Constant value for 1 new record (unchanging)

    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B, modified_C = A, B, C
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(2, 10) if num != A])  # Old records per trade
        modified_B = random.choice([num for num in range(2, 10) if num != B])  # Number of people
        modified_C = random.choice([num for num in range(2, 10) if num != C])  # New records obtained

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_B *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_B = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    total_old_records = modified_C * modified_A

    # Save original values in the modified format
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "ans": total_old_records
    }

    if is_symbolic:
        # Represent numbers symbolically with quotes
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        total_old_records = f"({modified_C} * {modified_A})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=name, A=modified_A, CONSTANT_NEW=CONSTANT_NEW, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=name,
        A=modified_A, CONSTANT_NEW=CONSTANT_NEW,
        B=modified_B, C=modified_C,
        TOTAL_OLD_RECORDS=total_old_records
    )

    return {"question": question, "answer": answer, "original_values": original_values}
