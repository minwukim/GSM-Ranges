import random

def q86(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original question and answer templates
    question_text = (
        "{NAME1}'s friend gave her {A} baby outfits that her child no longer needed. "
        "At her baby shower, {NAME1} received twice the amount of new baby outfits. "
        "Then, {NAME1}'s mom gifted her with another {B} baby outfits. "
        "How many outfits does she have for her baby?"
    )
    answer_text = (
        "Her friend gave her {A} outfits and she received twice as many at the baby shower so she received 2*{A} = "
        "<<2*{A}={SHOWER_OUTFITS}>>{SHOWER_OUTFITS} baby outfits\n"
        "Her friend gave her {A} outfits, she received {SHOWER_OUTFITS} at the baby shower and her mom gave her another {B} for a "
        "total of {A}+{SHOWER_OUTFITS}+{B} = <<{A}+{SHOWER_OUTFITS}+{B}={TOTAL_OUTFITS}>>{TOTAL_OUTFITS} baby outfits\n#### {TOTAL_OUTFITS}"
    )

    # Name adjustments
    original_name = "Laurel"
    common_names = ["Emma", "Sophia", "Olivia", "Mia", "Ava"]
    uncommon_names = ["Haruka", "Mei", "Aisha", "Raj", "Yara"]

    if name_level == 1:
        name1 = original_name
    elif name_level == 2:
        name1 = random.choice([name for name in common_names if name != original_name])
    elif name_level == 3:
        name1 = random.choice(uncommon_names)
    elif name_level == 4:
        name1 = "Z"
    elif name_level == 5:
        name1 = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=7))

    # Number adjustments
    A, B = 24, 15

    if num_level == 1:
        modified_A, modified_B = A, B
    else:
        # Level 2: Adjust numbers while preserving characteristics
        modified_A = random.choice([num for num in range(10, 100) if num != A])
        modified_B = random.choice([num for num in range(10, 100) if num != B])

        if num_level == 3:
            # Multiply Level 2 values by multiplier
            modified_A *= multiplier
            modified_B *= multiplier
        elif num_level == 4:
            # Random numbers in range (multiplier, 10 * multiplier - 1)
            modified_A = random.randint(multiplier, 10 * multiplier - 1)
            modified_B = random.randint(multiplier, 10 * multiplier - 1)

    # Calculate results
    shower_outfits = 2 * modified_A
    total_outfits = modified_A + shower_outfits + modified_B

    # Original values for symbolic mode
    original_values = {
        "A": modified_A, "B": modified_B, "ans": total_outfits
    }

    if is_symbolic:
        # Symbolic representation
        modified_A, modified_B = "'A'", "'B'"
        shower_outfits = f"(2*{modified_A})"
        total_outfits = f"({modified_A}+{shower_outfits}+{modified_B})"

    # Replace placeholders
    question = question_text.format(NAME1=name1, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME1=name1,
        A=modified_A,
        B=modified_B,
        SHOWER_OUTFITS=shower_outfits,
        TOTAL_OUTFITS=total_outfits
    )

    return {
        "question": question,
        "answer": answer,
        "original_values": original_values if is_symbolic else None
    }
