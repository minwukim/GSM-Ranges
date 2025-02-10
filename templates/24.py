import random

def q24(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} eats {A} times as many cookies as {NAME2} eats. If {NAME2} eats {B} cookies, "
        "how many cookies do both of them eat together?"
    )
    answer_text = (
        "{NAME1} eats {B}*{A} = <<{B}*{A}={CODY_COOKIES}>>{CODY_COOKIES} cookies.\n"
        "{NAME1} and {NAME2} eat {CODY_COOKIES}+{B} = <<{CODY_COOKIES}+{B}={TOTAL_COOKIES}>>{TOTAL_COOKIES} cookies together.\n#### {TOTAL_COOKIES}"
    )
    
    # Original values
    A, B = 3, 5  # Cody's multiplier, Amir's cookies
    original_names = ["Cody", "Amir"]

    # Name pools for name assignment
    common_names = ["Liam", "Emma", "Noah", "Sophia", "James"]
    uncommon_names = ["Haruto", "Mei", "Akari", "Rin", "Sora"]
    random_strings = ["Tmkpnwqr", "Rndmstrng", "Qwtbrplx", "Lmprxzmt", "Blstckpq"]

    # Modify names based on name_level
    if name_level == 1:
        # Level 1: Use original names
        modified_names = original_names
    elif name_level == 2:
        # Level 2: Replace with common names
        modified_names = random.sample(common_names, 2)
    elif name_level == 3:
        # Level 3: Replace with uncommon (Asian) names
        modified_names = random.sample(uncommon_names, 2)
    elif name_level == 4:
        # Level 4: Assign symbols Z and Y explicitly
        modified_names = ["Z", "Y"]
    elif name_level == 5:
        # Level 5: Replace with random strings
        modified_names = random.sample(random_strings, 2)

    NAME1, NAME2 = modified_names

    # Modify the values for num_level
    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B = A, B
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(2, 10) if num != A])  # NAME1's multiplier
        modified_B = random.choice([num for num in range(2, 10) if num != B])  # NAME2's cookies

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    cody_cookies = modified_B * modified_A
    total_cookies = cody_cookies + modified_B

    original_values = {
        "A": A, 
        "B": B, 
        "ans": A * B + B
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B = '\'A\'', '\'B\''
        cody_cookies = f"{modified_B}*{modified_A}"
        total_cookies = f"{cody_cookies}+{modified_B}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME1=NAME1, NAME2=NAME2, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME1=NAME1,
        NAME2=NAME2,
        A=modified_A,
        B=modified_B,
        CODY_COOKIES=cody_cookies,
        TOTAL_COOKIES=total_cookies
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
