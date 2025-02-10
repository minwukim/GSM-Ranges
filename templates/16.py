import random

def q16(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} is fundraising for his charity by selling brownies for ${A} a slice and cheesecakes for ${B} a slice. "
        "If {NAME} sells {C} brownies and {D} slices of cheesecake, how much money does {NAME} raise?"
    )
    answer_text = (
        "{NAME} raised {C} brownies x ${A}/brownie = $<<{C}*{A}={BROWNIE_TOTAL}>>{BROWNIE_TOTAL} by selling brownies.\n"
        "{NAME} raised {D} slices x ${B}/slice = $<<{D}*{B}={CHEESECAKE_TOTAL}>>{CHEESECAKE_TOTAL} by selling cheesecakes.\n"
        "In total {NAME} has raised ${BROWNIE_TOTAL} + ${CHEESECAKE_TOTAL} = $<<{BROWNIE_TOTAL}+{CHEESECAKE_TOTAL}={TOTAL_RAISED}>>{TOTAL_RAISED}\n#### {TOTAL_RAISED}"
    )
    
    # Original values
    A, B, C, D = 3, 4, 43, 23  # Price per brownie, price per cheesecake, brownies sold, cheesecakes sold
    original_name = "Tommy"

    # Name pools for name assignment
    common_names = ["James", "Sophia", "Emma", "Liam", "Olivia"]
    uncommon_names = ["Haruto", "Akari", "Sanjay", "Mei", "Ravi"]
    random_strings = ["Tmmjr", "Crtnx", "Fldrp", "Blkrn", "Trmjk"]

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

    # Modify the values for num_level
    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        modified_A = random.choice([num for num in range(2, 10) if num != A])
        modified_B = random.choice([num for num in range(3, 10) if num != B])
        modified_C = random.choice([num for num in range(10, 100) if num != C])
        modified_D = random.choice([num for num in range(10, 100) if num != D])

        if num_level == 3:
            modified_C *= multiplier
            modified_D *= multiplier
        elif num_level == 4:
            modified_C = random.randint(multiplier, multiplier * 10 - 1)
            modified_D = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    brownie_total = modified_C * modified_A
    cheesecake_total = modified_D * modified_B
    total_raised = brownie_total + cheesecake_total

    A = modified_A
    B = modified_B
    C = modified_C
    D = modified_D

    original_values = {
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "ans": (A * C) + (B * D)
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D = '\'A\'', '\'B\'', '\'C\'', '\'D\''
        brownie_total = f"{modified_C} * {modified_A}"
        cheesecake_total = f"{modified_D} * {modified_B}"
        total_raised = f"({brownie_total}) + ({cheesecake_total})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        D=modified_D,
        BROWNIE_TOTAL=brownie_total,
        CHEESECAKE_TOTAL=cheesecake_total,
        TOTAL_RAISED=total_raised
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}