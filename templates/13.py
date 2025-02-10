import random

def q13(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "The {NAME} sisters are driving home with {A} kittens adopted from the local animal shelter when their mother calls to inform them that their two house cats have just had kittens. "
        "She says that Patchy, the first cat, has had thrice the number of adopted kittens, while Trixie, the other cat, has had {B}. "
        "How many kittens does the {NAME} family now have?"
    )
    answer_text = (
        "Patchy has just had thrice the number of adopted kittens, so she has 3 * {A} = <<3*{A}={PATCHY_KITTENS}>>{PATCHY_KITTENS} kittens.\n"
        "Since Trixie's kittens are {B}, both cats have {PATCHY_KITTENS} + {B} = <<{PATCHY_KITTENS}+{B}={CAT_KITTENS}>>{CAT_KITTENS} kittens.\n"
        "Combining the adopted kittens with those from the two cats, the {NAME} family now has {A} + {CAT_KITTENS} = <<{A}+{CAT_KITTENS}={TOTAL_KITTENS}>>{TOTAL_KITTENS} kittens.\n#### {TOTAL_KITTENS}"
    )

    # Original values
    A, B = 7, 12  # Adopted kittens, Trixie's kittens
    original_name = "Doubtfire"

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        common_names = ["Smith", "Johnson", "Brown", "Taylor", "Wilson"]
        modified_name = random.choice(common_names)
    elif name_level == 3:
        uncommon_names = ["Ashworth", "Beauregard", "Montague", "Carroway", "Winslow"]
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        symbols = ["Z", "Y", "X", "W", "V"]
        modified_name = symbols[0]
    elif name_level == 5:
        random_strings = ["Dbtfr", "Smltn", "Grnbx", "Clrkx", "Rdnfs"]
        modified_name = random.choice(random_strings)

    # Modify the values for num_level
    if num_level == 1:
        modified_A, modified_B = A, B
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(2, 10) if num != A])  # Adopted kittens
        modified_B = random.choice([num for num in range(10, 20) if num != B])  # Trixie's kittens

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_B *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_B = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate the number of kittens
    patchy_kittens = 3 * modified_A  # Thrice the adopted kittens
    cat_kittens = patchy_kittens + modified_B
    total_kittens = modified_A + cat_kittens

    A = modified_A
    B = modified_B

    original_values = {"A": A, "B": B, "ans": A + (3 * A + B)}

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B = '\'A\'', '\'B\''
        patchy_kittens = f"3 * {modified_A}"
        cat_kittens = f"{patchy_kittens} + {modified_B}"
        total_kittens = f"{modified_A} + {cat_kittens}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        PATCHY_KITTENS=patchy_kittens,
        CAT_KITTENS=cat_kittens,
        TOTAL_KITTENS=total_kittens
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
