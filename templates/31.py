import random

def q31(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} was preparing for a dinner party at her house, where she intended to serve stew. She noticed that she was out of plastic spoons, "
        "so she bought a new package of spoons. Later, her husband also bought a package of {A} new spoons and gave them to {NAME}. "
        "While {NAME} was making the stew, she used {B} of the spoons to sample her stew. Later, when she went to set the table, she had a total of {C} spoons. "
        "How many spoons were in the package that {NAME} bought?"
    )
    answer_text = (
        "The total number of spoons from {NAME} and her husband was {C}+{B}=<<{C}+{B}={TOTAL_SPOONS}>>{TOTAL_SPOONS} spoons.\n"
        "Since the husband bought a package of {A} spoons, then {NAME}'s package contained {TOTAL_SPOONS}-{A}=<<{TOTAL_SPOONS}-{A}={JULIA_SPOONS}>>{JULIA_SPOONS} spoons.\n#### {JULIA_SPOONS}"
    )
    
    # Original values
    A, B, C = 5, 3, 12  # Husband's spoons, spoons used by Julia, spoons left after sampling
    original_name = "Julia"

    # Name pools
    common_names = ["Emma", "Olivia", "Sophia", "Isabella", "Mia"]
    uncommon_names = ["Sakura", "Ananya", "Meilin", "Hana", "Aarushi"]
    random_strings = ["Zxqpwrn", "Tslbnmk", "Ywcrfpk", "Vtnzqly", "Qwrnmvz"]

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        modified_name = random.choice(common_names)
    elif name_level == 3:
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"  # Explicit symbol for name
    elif name_level == 5:
        modified_name = random.choice(random_strings)

    # Modify the values for num_level
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    else:
        modified_A = random.choice([num for num in range(3, 8) if num != A])  # Husband's spoons
        modified_B = random.choice([num for num in range(1, 5) if num != B])  # Spoons used by Julia
        modified_C = random.choice([num for num in range(10, 16) if num != C])  # Spoons left after sampling

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier
            modified_C *= multiplier
        elif num_level == 4:
            modified_A = random.randint(multiplier * 3, multiplier * 8)
            modified_B = random.randint(multiplier * 1, multiplier * 5)
            modified_C = random.randint(multiplier * 10, multiplier * 15)

    # Calculate totals
    total_spoons = modified_C + modified_B
    julia_spoons = total_spoons - modified_A

    A = modified_A
    B = modified_B
    C = modified_C

    # Store original values and final answer
    original_values = {"A": A, "B": B, "C": C, "ans": (C + B) - A}

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        total_spoons = f"{modified_C} + {modified_B}"
        julia_spoons = f"({total_spoons}) - {modified_A}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        TOTAL_SPOONS=total_spoons,
        JULIA_SPOONS=julia_spoons
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
