import random

def q95(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} bought {A} cookies and {NAME2} gave her {B} cookies. The other day her brother ate {C} of those cookies. "
        "How many cookies are left for {NAME1}?"
    )
    answer_text = (
        "The number of {NAME1}'s cookies is {A} + {B} = <<({A})+({B})={TOTAL_COOKIES}>>{TOTAL_COOKIES} cookies.\n"
        "After her brother’s feast, she was left with {TOTAL_COOKIES} – {C} = <<({TOTAL_COOKIES})-({C})={COOKIES_LEFT}>>{COOKIES_LEFT} cookies.\n#### {COOKIES_LEFT}"
    )
    
    # Detect and modify names
    original_name1, original_name2 = "Rachel", "Janet"
    if name_level == 1:
        modified_name1, modified_name2 = original_name1, original_name2
    elif name_level == 2:
        common_names = ["Alice", "Emma", "Sophia", "Olivia", "Mia"]
        common_names = [name for name in common_names if name not in [original_name1, original_name2]]
        modified_name1, modified_name2 = random.sample(common_names, 2)
    elif name_level == 3:
        uncommon_asian_names = ["Haruka", "Mingyu", "Kaede", "Rinako", "Takeshi"]
        modified_name1, modified_name2 = random.sample(uncommon_asian_names, 2)
    elif name_level == 4:
        modified_name1, modified_name2 = "Z", "Y"
    elif name_level == 5:
        random_strings = ["fjakslf", "qwertyu", "asdfghj", "zxcvbnm", "lkjhgfd"]
        modified_name1, modified_name2 = random.sample(random_strings, 2)

    # Original values
    A, B, C = 23, 42, 44  # Cookies bought, given, and eaten

    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B, modified_C = A, B, C
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(10, 100) if num != A and num % 5 == 0])
        modified_B = random.choice([num for num in range(10, 100) if num != B and num % 5 == 0])
        modified_C = random.choice([num for num in range(10, 100) if num != C and num < (modified_A + modified_B)])

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_B *= multiplier
            modified_C *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_B = random.randint(multiplier, multiplier * 10 - 1)
            modified_C = random.randint(multiplier, multiplier * 10 - 1)
            modified_C = min(modified_C, modified_A + modified_B - 1)  # Ensure positivity

    # Calculate totals
    total_cookies = modified_A + modified_B
    cookies_left = total_cookies - modified_C

    # Save original values
    original_values = {
        "A": modified_A,
        "B": modified_B,
        "C": modified_C,
        "ans": cookies_left
    }

    if is_symbolic:
        # Represent numbers symbolically with quotes
        modified_A, modified_B, modified_C = "'A'", "'B'", "'C'"
        total_cookies = f"({modified_A} + {modified_B})"
        cookies_left = f"({total_cookies} - {modified_C})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=modified_name1, NAME2=modified_name2, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME1=modified_name1,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        TOTAL_COOKIES=total_cookies,
        COOKIES_LEFT=cookies_left
    )

    return {"question": question, "answer": answer, "original_values": original_values}
