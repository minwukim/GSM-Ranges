import random

def q49(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} has {A} more crabs than {NAME2}, who has {B} fewer crabs than {NAME3}. "
        "If {NAME3} has {C} crabs, calculate the total number of crabs the three have together."
    )
    answer_text = (
        "If {NAME3} has {C} crabs, then {NAME2}, who has {B} fewer crabs than {NAME3}, has {C} - {B} = <<{C}-{B}={MONIC_CRABS}>>{MONIC_CRABS} crabs.\n"
        "{NAME3} and {NAME2} have a total of {MONIC_CRABS} + {C} = <<{MONIC_CRABS}+{C}={BO_AND_MONIC_CRABS}>>{BO_AND_MONIC_CRABS} crabs.\n"
        "Since {NAME2} has {MONIC_CRABS} crabs, {NAME1}'s number of crabs is {MONIC_CRABS} + {A} = <<{MONIC_CRABS}+{A}={RANI_CRABS}>>{RANI_CRABS}.\n"
        "Together, the three have {BO_AND_MONIC_CRABS} + {RANI_CRABS} = <<{BO_AND_MONIC_CRABS}+{RANI_CRABS}={TOTAL_CRABS}>>{TOTAL_CRABS} crabs.\n#### {TOTAL_CRABS}"
    )
    
    # Original values
    A, B, C = 10, 4, 40  # Rani has 10 more, Monic has 4 fewer, Bo has 40 crabs

    # Dynamic name generation (excluding original names)
    common_names = ["Sam", "Emma", "Chris", "Alex", "Taylor"]
    uncommon_names = ["Hiro", "Aisha", "Mei", "Raj", "Lila"]
    random_strings = ["Xlyfrz", "Tmfqvs", "Prkltz", "Bgjwvs", "Lmzptq"]

    if name_level == 1:
        name1, name2, name3 = "Rani", "Monic", "Bo"
    elif name_level == 2:
        name1, name2, name3 = random.sample(common_names, 3)
    elif name_level == 3:
        name1, name2, name3 = random.sample(uncommon_names, 3)
    elif name_level == 4:
        name1, name2, name3 = "Z", "Y", "X"
    elif name_level == 5:
        name1, name2, name3 = random.sample(random_strings, 3)

    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B, modified_C = A, B, C
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(10, 91, 10) if num != A])
        modified_B = random.choice([num for num in range(2, 10) if num != B])
        modified_C = random.choice([num for num in range(10, 91, 10) if num != C])

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_B *= multiplier
            modified_C *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_B = random.randint(multiplier, multiplier * 5 - 1)
            modified_C = random.randint(multiplier * 5, multiplier * 10 - 1)

    # Calculate totals
    monic_crabs = modified_C - modified_B
    bo_and_monic_crabs = monic_crabs + modified_C
    rani_crabs = monic_crabs + modified_A
    total_crabs = bo_and_monic_crabs + rani_crabs

    # Store original and modified values
    original_values = {
        "A": modified_A, 
        "B": modified_B, 
        "C": modified_C,
        "ans": total_crabs
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = "'A'", "'B'", "'C'"
        monic_crabs = f"{modified_C} - {modified_B}"
        bo_and_monic_crabs = f"{monic_crabs} + {modified_C}"
        rani_crabs = f"{monic_crabs} + {modified_A}"
        total_crabs = f"{bo_and_monic_crabs} + {rani_crabs}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=name1, NAME2=name2, NAME3=name3, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME1=name1,
        NAME2=name2,
        NAME3=name3,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        MONIC_CRABS=monic_crabs,
        BO_AND_MONIC_CRABS=bo_and_monic_crabs,
        RANI_CRABS=rani_crabs,
        TOTAL_CRABS=total_crabs
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
