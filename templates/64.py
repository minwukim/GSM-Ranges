import random

def q64(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} took his allowance of ${A} and added an extra ${B} to it. He then invested this sum of money, which tripled in a year. "
        "How much money did he have after a year?"
    )
    answer_text = (
        "{NAME} invested {A} and {B} dollars for a total of ({A} + {B}) = <<{A}+{B}={TOTAL_INVESTED}>>{TOTAL_INVESTED} dollars invested.\n"
        "{NAME} tripled this amount of money over the year, for a total of ({TOTAL_INVESTED} * 3) = <<{TOTAL_INVESTED}*3={TOTAL_AMOUNT}>>{TOTAL_AMOUNT} dollars.\n#### {TOTAL_AMOUNT}"
    )
    
    # Name options
    common_names = ["Jack", "Emma", "Sophia", "Michael", "Oliver"]
    uncommon_names = ["Haru", "Rinako", "Minjun", "Kaede", "Tenzin"]
    random_strings = ["Xvlskej", "Kznpwfa", "Lsrqtuz", "Bmnxfla", "Ywzprjk"]

    # Detect original name and modify
    original_name = "Johnny"
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        modified_name = random.choice([name for name in common_names if name != original_name])
    elif name_level == 3:
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = random.choice(random_strings)
    
    # Original values
    A, B, fixed_multiplier = 20, 10, 3  # Allowance, extra money, and fixed multiplier

    # Modify numbers
    if num_level == 1:
        modified_A, modified_B = A, B
    elif num_level == 2:
        modified_A = random.choice([num for num in range(10, 100) if num != A and num % 10 == 0])
        modified_B = random.choice([num for num in range(10, 100) if num != B and num % 10 == 0])
    elif num_level == 3:
        modified_A = random.choice([num for num in range(10, 100) if num != A and num % 10 == 0]) * multiplier
        modified_B = random.choice([num for num in range(10, 100) if num != B and num % 10 == 0]) * multiplier
    elif num_level == 4:
        modified_A = random.randint(multiplier, 10 * multiplier - 1)
        modified_B = random.randint(multiplier, 10 * multiplier - 1)

    # Ensure positivity of calculations
    total_invested = modified_A + modified_B
    total_amount = total_invested * fixed_multiplier
    
    # Save original values before any symbolic modifications
    original_values = {
        "A": modified_A, "B": modified_B,"ans": total_amount
    }

    # Handle symbolic representation
    if is_symbolic:
        modified_A, modified_B = "'A'", "'B'"
        total_invested = f"({modified_A} + {modified_B})"
        total_amount = f"({total_invested} * {fixed_multiplier})"

    # Replace placeholders in templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME=modified_name, 
        A=modified_A, 
        B=modified_B, 
        TOTAL_INVESTED=total_invested, 
        TOTAL_AMOUNT=total_amount
    )
    
    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
