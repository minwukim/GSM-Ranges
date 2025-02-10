import random

def q74(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} and {NAME2} wanted to get to know each other. They realized that the sum of their ages is {A}. "
        "What will be the sum of their ages in {B} years?"
    )
    answer_text = (
        "There will be an additional {B} (for {NAME1}) + {B} (for {NAME2}) = <<{B}+{B}={AGE_ADDITION}>>{AGE_ADDITION} to {NAME1} and {NAME2}'s current sum of ages in {B} years.\n"
        "Therefore, the sum of their ages in {B} years is {A} + {AGE_ADDITION} = <<{A}+{AGE_ADDITION}={TOTAL_SUM}>>{TOTAL_SUM}.\n#### {TOTAL_SUM}"
    )

    # Name options
    common_names = ["Alice", "Jack", "Sophia", "Michael", "Emma"]
    uncommon_names = ["Haruto", "Yara", "Chen", "Aisha", "Lila"]
    random_strings = ["Trpqksl", "Bqzwxtk", "Nsmflxz", "Lcxptjw", "Rpwvyzn"]

    # Name modifications
    original_name1, original_name2 = "Mico", "Marco"

    if name_level == 1:
        modified_name1, modified_name2 = original_name1, original_name2
    elif name_level == 2:
        available_names = [name for name in common_names if name not in [original_name1, original_name2]]
        modified_name1, modified_name2 = random.sample(available_names, 2)
    elif name_level == 3:
        modified_name1, modified_name2 = random.sample(uncommon_names, 2)
    elif name_level == 4:
        modified_name1, modified_name2 = "Z", "Y"
    elif name_level == 5:
        modified_name1, modified_name2 = random.sample(random_strings, 2)

    # Original values
    A, B = 20, 10  # A = current sum of ages, B = years into the future

    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B = A, B
    elif num_level == 2:
        # Level 2: Use numbers with same digits but different values
        modified_A = random.choice([num for num in range(10, 100) if num != A and num % 10 == 0])  # multiples of 10
        modified_B = random.choice([num for num in range(10, 100) if num != B and num % 10 == 0])  # multiples of 5
    elif num_level == 3:
        # Level 3: Multiply level 2 values by the multiplier
        modified_A = random.choice([num for num in range(10, 100) if num != A and num % 10 == 0]) * multiplier
        modified_B = random.choice([num for num in range(10, 100) if num != B and num % 5 == 0]) * multiplier
    elif num_level == 4:
        # Level 4: Assign random values within a specific range
        modified_A = random.randint(multiplier, 10 * multiplier - 1)
        modified_B = random.randint(multiplier, 10 * multiplier - 1)

    # Ensure positivity of relationships
    age_addition = modified_B * 2  # Sum of both names' ages in B years
    total_sum = modified_A + age_addition

    # Save original values before symbolic changes
    original_values = {"A": modified_A, "B": modified_B, "ans": total_sum}

    # Symbolic representation
    if is_symbolic:
        modified_A, modified_B = "'A'", "'B'"
        age_addition = f"({modified_B} + {modified_B})"
        total_sum = f"({modified_A} + {age_addition})"

    # Replace placeholders in question and answer
    question = question_text.format(NAME1=modified_name1, NAME2=modified_name2, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME1=modified_name1, NAME2=modified_name2, A=modified_A, B=modified_B,
        AGE_ADDITION=age_addition, TOTAL_SUM=total_sum
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
