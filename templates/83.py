import random

def q83(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original question and answer templates
    question_text = (
        "{NAME1} has {A} lollipops. Her mother gives {NAME1} another {B} lollipops. "
        "If {NAME1} gives {C} of her lollipops to {NAME2}, how many lollipops does she have left?"
    )
    answer_text = (
        "{NAME1} has {A} + {B} = <<({A})+({B})={TOTAL_LOLLIPOPS}>>{TOTAL_LOLLIPOPS} lollipops\n"
        "After she gives {C} lollipops to {NAME2}, she has {TOTAL_LOLLIPOPS} - {C} = <<({TOTAL_LOLLIPOPS})-({C})={REMAINING_LOLLIPOPS}>>{REMAINING_LOLLIPOPS} lollipops.\n#### {REMAINING_LOLLIPOPS}"
    )

    # Extract original names and numbers
    original_names = ["Erin", "Ella"]
    A, B, C = 7, 10, 3  # Original numbers in the problem

    # Modify names based on name_level
    if name_level == 1:
        name1, name2 = original_names
    elif name_level == 2:
        common_names = ["Alice", "Emma", "Sophia", "Jack", "Olivia"]
        name1, name2 = random.sample([n for n in common_names if n not in original_names], 2)
    elif name_level == 3:
        uncommon_asian_names = ["Haruto", "Mei", "Kaede", "Rinako", "Takeshi"]
        name1, name2 = random.sample(uncommon_asian_names, 2)
    elif name_level == 4:
        name1, name2 = "Z", "Y"
    elif name_level == 5:
        random_strings = ["Xlyfrtz", "Tmfqvws", "Prkltyz", "Bgjwvqr", "Lmzptqr"]
        name1, name2 = random.sample(random_strings, 2)

    # Modify numbers based on num_level
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    elif num_level == 2:
        modified_A = random.choice([num for num in range(1, 10) if num != A])
        modified_B = random.choice([num for num in range(10, 100, 10) if num != B])
        modified_C = random.choice([num for num in range(1, 10) if num != C])
    elif num_level == 3:
        modified_A = random.choice([num for num in range(1, 10) if num != A]) * multiplier
        modified_B = random.choice([num for num in range(10, 100, 10) if num != B]) * multiplier
        modified_C = random.choice([num for num in range(1, 10) if num != C]) * multiplier
    elif num_level == 4:
        modified_A = random.randint(multiplier, 10 * multiplier - 1)
        modified_B = random.randint(multiplier, 10 * multiplier - 1)
        modified_C = random.randint(multiplier, min(10 * multiplier - 1, modified_A + modified_B))

    # Ensure positivity of remaining lollipops
    if modified_A + modified_B <= modified_C:
        modified_C = random.randint(1, (modified_A + modified_B) - 1)

    # Declare original_values before handling symbolic mode
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C,
        "ans": (modified_A + modified_B) - modified_C
    }

    if is_symbolic:
        # Represent numbers symbolically with quotes
        modified_A, modified_B, modified_C = "'A'", "'B'", "'C'"
        total_lollipops = f"({modified_A}) + ({modified_B})"
        remaining_lollipops = f"({total_lollipops}) - ({modified_C})"
    else:
        total_lollipops = modified_A + modified_B
        remaining_lollipops = total_lollipops - modified_C

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=name1, NAME2=name2, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME1=name1,
        NAME2=name2,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        TOTAL_LOLLIPOPS=total_lollipops,
        REMAINING_LOLLIPOPS=remaining_lollipops
    )

    # Return the final result
    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}