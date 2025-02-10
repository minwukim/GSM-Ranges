import random

def q81(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} is {DIFF1} years older than {NAME2}, and {NAME2} is {DIFF2} years younger than {NAME3}. "
        "If {NAME3} is {AGE3}, how old is {NAME1}?"
    )
    answer_text = (
        "{NAME2} is {AGE3}-{DIFF2}=<<{AGE3}-{DIFF2}={AGE2}>>{AGE2} years old\n"
        "{NAME1} is {AGE2}+{DIFF1}=<<{AGE2}+{DIFF1}={AGE1}>>{AGE1} years old\n#### {AGE1}"
    )

    # Original values
    NAME1, NAME2, NAME3 = "Trent", "Jane", "Quinn"
    DIFF1, DIFF2, AGE3 = 5, 3, 30

    # Modify names based on name_level
    if name_level == 1:
        modified_NAME1, modified_NAME2, modified_NAME3 = NAME1, NAME2, NAME3
    elif name_level == 2:
        common_names = ["Alice", "Emma", "Jack", "Sophia", "Mia", "Noah", "Liam"]
        common_names = [name for name in common_names if name not in [NAME1, NAME2, NAME3]]
        modified_NAME1, modified_NAME2, modified_NAME3 = random.sample(common_names, 3)
    elif name_level == 3:
        uncommon_asian_names = ["Haruto", "Mei", "Aisha", "Raj", "Lila", "Hiro"]
        modified_NAME1, modified_NAME2, modified_NAME3 = random.sample(uncommon_asian_names, 3)
    elif name_level == 4:
        modified_NAME1, modified_NAME2, modified_NAME3 = "Z", "Y", "X"
    elif name_level == 5:
        modified_NAME1, modified_NAME2, modified_NAME3 = (
            ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=7)),
            ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=7)),
            ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=7))
        )

    # Modify numbers based on num_level
    if num_level == 1:
        modified_DIFF1, modified_DIFF2, modified_AGE3 = DIFF1, DIFF2, AGE3
    elif num_level == 2:
        modified_DIFF1 = random.choice([num for num in range(1, 10) if num != DIFF1])
        modified_DIFF2 = random.choice([num for num in range(1, 10) if num != DIFF2])
        modified_AGE3 = random.choice([num for num in range(10, 100, 10) if num != AGE3])
    elif num_level == 3:
        modified_DIFF1 = random.choice([num for num in range(1, 10) if num != DIFF1]) * multiplier
        modified_DIFF2 = random.choice([num for num in range(1, 10) if num != DIFF2]) * multiplier
        modified_AGE3 = random.choice([num for num in range(10, 100, 10) if num != AGE3]) * multiplier
    elif num_level == 4:
        modified_DIFF1 = random.randint(multiplier, multiplier * 10 - 1)
        modified_AGE3 = random.randint(multiplier + 2, multiplier * 10 - 1)
        modified_DIFF2 = random.randint(multiplier, modified_AGE3 - 1)


    # Ensure positivity in the relationship
    modified_AGE2 = modified_AGE3 - modified_DIFF2
    modified_AGE1 = modified_AGE2 + modified_DIFF1

    # Save original values in the modified format
    original_values = {
        "A": modified_DIFF1, "B": modified_DIFF2, "C": modified_AGE3,
        "ans": modified_AGE1
    }

    if is_symbolic:
        # Represent numbers symbolically with quotes
        modified_DIFF1, modified_DIFF2, modified_AGE3 = "'A'", "'B'", "'C'"
        modified_AGE2 = f"({modified_AGE3} - {modified_DIFF2})"
        modified_AGE1 = f"({modified_AGE2} + {modified_DIFF1})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(
        NAME1=modified_NAME1, NAME2=modified_NAME2, NAME3=modified_NAME3,
        DIFF1=modified_DIFF1, DIFF2=modified_DIFF2, AGE3=modified_AGE3
    )
    answer = answer_text.format(
        NAME1=modified_NAME1, NAME2=modified_NAME2, NAME3=modified_NAME3,
        DIFF1=modified_DIFF1, DIFF2=modified_DIFF2, AGE3=modified_AGE3,
        AGE2=modified_AGE2, AGE1=modified_AGE1
    )

    return {"question": question, "answer": answer, "original_values": original_values}
