import random

def q32(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} needed chicken sausages and fish sausages to make sausage buns at a party. "
        "He bought {A} chicken sausages and {B} more fish sausages than chicken sausages. "
        "How many sausages did {NAME} buy in all?"
    )
    answer_text = (
        "{NAME} bought {A} + {B} = <<{A}+{B}={FISH_SAUSAGES}>>{FISH_SAUSAGES} fish sausages.\n"
        "{NAME} bought {A} + {FISH_SAUSAGES} = <<{A}+{FISH_SAUSAGES}={TOTAL_SAUSAGES}>>{TOTAL_SAUSAGES} sausages in all.\n#### {TOTAL_SAUSAGES}"
    )
    
    # Original values
    A, B = 38, 6  # Number of chicken sausages, additional fish sausages
    original_name = "Dylan"

    # Name pools
    common_names = ["Jacob", "Ethan", "Michael", "William", "Daniel"]
    uncommon_names = ["Akira", "Ravi", "Yuto", "Ibrahim", "Jin"]
    random_strings = ["Xlmnqrz", "Tqjrfpv", "Zswqykx", "Prtvlmn", "Qxyskrz"]

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        modified_name = random.choice(common_names)
    elif name_level == 3:
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = random.choice(random_strings)

    # Modify the values for level
    if num_level == 1:
        modified_A, modified_B = A, B
    else:
        modified_A = random.choice([num for num in range(10, 100) if num != A])  # Number of chicken sausages
        modified_B = random.choice([num for num in range(2, 10) if num != B])  # Additional fish sausages

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier

    if num_level == 4:
        modified_A = random.randint(multiplier, multiplier * 10 - 1)
        modified_B = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    fish_sausages = modified_A + modified_B
    total_sausages = modified_A + fish_sausages

    A = modified_A
    B = modified_B

    original_values = {
        "A": A, 
        "B": B, 
        "ans": A + (A + B)
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B = '\'A\'', '\'B\''
        fish_sausages = f"{modified_A} + {modified_B}"
        total_sausages = f"{modified_A} + ({fish_sausages})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        FISH_SAUSAGES=fish_sausages,
        TOTAL_SAUSAGES=total_sausages
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}

