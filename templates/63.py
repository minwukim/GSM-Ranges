import random

def q63(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original question and answer templates
    question_text = (
        "{NAME1} and {NAME2} enjoy going to the beach to collect shells. On Monday, {NAME1} collects {B} more shells than {NAME2}, who collects {A} shells. "
        "On Tuesday, {NAME1} collects {MULTIPLIER_TUESDAY} times more shells than {PRONOUN} did on Monday. How many shells does {NAME1} collect on Tuesday?"
    )
    answer_text = (
        "On Monday, {NAME1} collects {A} + {B} = <<{A}+{B}={KYLIE_MONDAY}>>{KYLIE_MONDAY} shells\n"
        "On Tuesday, {NAME1} collects {KYLIE_MONDAY} * {MULTIPLIER_TUESDAY} = <<{KYLIE_MONDAY}*{MULTIPLIER_TUESDAY}={KYLIE_TUESDAY}>>{KYLIE_TUESDAY} shells\n#### {KYLIE_TUESDAY}"
    )
    
    # Detect and modify names based on levels
    original_names = ["Kylie", "Robert"]
    common_names = ["Emma", "Jack", "Olivia", "Michael", "Sophia"]
    uncommon_asian_names = ["Haruka", "Yuto", "Mei", "Rin", "Takeshi"]
    random_strings = ["Fjhsltr", "Wqmpsvk", "Nvdzlru", "Brxwqlp", "Ktjvscm"]
    
    if name_level == 1:
        name1, name2 = original_names
    elif name_level == 2:
        name1, name2 = random.sample([name for name in common_names if name not in original_names], 2)
    elif name_level == 3:
        name1, name2 = random.sample(uncommon_asian_names, 2)
    elif name_level == 4:
        name1, name2 = "Z", "Y"
    elif name_level == 5:
        name1, name2 = random.sample(random_strings, 2)
    
    # Pronoun for NAME1 (assuming female for Kylie)
    pronoun = "she"
    
    # Original values
    A, B, MULTIPLIER_TUESDAY = 20, 5, 2
    
    # Number modification levels
    if num_level == 1:
        modified_A, modified_B, modified_MULTIPLIER_TUESDAY = A, B, MULTIPLIER_TUESDAY
    else:
        # Ensure same-digit replacements
        modified_A = random.choice([num for num in range(10, 100, 10) if num != A])
        modified_B = random.choice([num for num in range(2, 10) if num != B])
        modified_MULTIPLIER_TUESDAY = random.choice([num for num in range(2, 10) if num != MULTIPLIER_TUESDAY])

        if num_level == 3:
            modified_A *= multiplier
            modified_B *= multiplier
        elif num_level == 4:
            modified_A = random.randint(multiplier, 10 * multiplier - 1)
            modified_B = random.randint(multiplier, 10 * multiplier - 1)
    
    # Calculate Monday and Tuesday values
    kylie_monday = modified_A + modified_B
    kylie_tuesday = kylie_monday * modified_MULTIPLIER_TUESDAY
    
    # Save original values before symbolic replacement
    original_values = {
        "A": modified_A, "B": modified_B, "ans": kylie_tuesday
    }

    # Symbolic representation
    if is_symbolic:
        modified_A, modified_B, modified_MULTIPLIER_TUESDAY = "'A'", "'B'", "2"
        kylie_monday = f"({modified_A} + {modified_B})"
        kylie_tuesday = f"({kylie_monday}) * {modified_MULTIPLIER_TUESDAY}"

    # Replace placeholders in templates
    question = question_text.format(
        NAME1=name1, NAME2=name2, A=modified_A, B=modified_B, MULTIPLIER_TUESDAY=modified_MULTIPLIER_TUESDAY, PRONOUN=pronoun
    )
    answer = answer_text.format(
        NAME1=name1, A=modified_A, B=modified_B, MULTIPLIER_TUESDAY=modified_MULTIPLIER_TUESDAY,
        KYLIE_MONDAY=kylie_monday, KYLIE_TUESDAY=kylie_tuesday
    )
    
    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
