import random

def q79(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Question and Answer Templates
    question_text = (
        "{NAME1} is a superstar counter. He has won {A} medals for counting super fast. "
        "His friend {NAME2} is also a really good counter and has {B} less medals than {NAME1}. "
        "Together they have {C} times less medals than have been given out for counting. How many medals have been given out for counting?"
    )
    answer_text = (
        "{NAME2} has {A}-{B}=<<{A}-{B}={MEDALS_NAME2}>>{MEDALS_NAME2} medals.\n"
        "Medals of {NAME1} and {NAME2} {A}+{MEDALS_NAME2}=<<{A}+{MEDALS_NAME2}={TOTAL_MEDALS}>>{TOTAL_MEDALS} medals.\n"
        "{C} times their medals is {TOTAL_MEDALS}*{C}=<<{TOTAL_MEDALS}*{C}={FINAL_MEDALS}>>{FINAL_MEDALS} medals.\n#### {FINAL_MEDALS}"
    )

    # Names
    original_names = ["Ali", "Izzy"]
    common_names = ["Jack", "Emma", "Sophia", "Michael", "Liam"]
    uncommon_names = ["Hiroshi", "Meiyu", "Rajesh", "Aisha", "Kaede"]
    random_strings = ["Xlyfrzq", "Plmqkjt", "Rntfvsz", "Tklqwpx", "Bzxlyjm"]

    # Determine names based on name_level
    if name_level == 1:
        modified_names = original_names
    elif name_level == 2:
        modified_names = random.sample(
            [name for name in common_names if name not in original_names], k=2
        )
    elif name_level == 3:
        modified_names = random.sample(uncommon_names, k=2)
    elif name_level == 4:
        modified_names = ["Z", "Y"]
    elif name_level == 5:
        modified_names = random.sample(random_strings, k=2)

    NAME1, NAME2 = modified_names

    # Numbers
    A, B, C = 22, 5, 10  # Medals won by Ali, medals less than Ali for Izzy, and times less medals

    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    elif num_level == 2:
        modified_A = random.choice([num for num in range(10, 100) if num != A])
        modified_B = random.choice([num for num in range(2, 10) if num != B])
        modified_C = random.choice([num for num in range(5, 100, 10) if num != C])
    elif num_level == 3:
        modified_A = random.choice([num for num in range(10, 100) if num != A]) * multiplier
        modified_B = random.choice([num for num in range(2, 10) if num != B]) * multiplier
        modified_C = random.choice([num for num in range(5, 100, 10) if num != C])
    elif num_level == 4:
        modified_A = random.randint(multiplier + 2, 10 * multiplier - 1)
        modified_B = random.randint(multiplier, modified_A)
        modified_C = random.choice([num for num in range(5, 100, 10) if num != C])

    # Ensure positivity
    modified_MEDALS_NAME2 = modified_A - modified_B
    modified_TOTAL_MEDALS = modified_A + modified_MEDALS_NAME2
    modified_FINAL_MEDALS = modified_TOTAL_MEDALS * modified_C

    # Store original values before modification
    original_values = {
        "A": modified_A,
        "B": modified_B,
        "C": modified_C,
        "ans": modified_FINAL_MEDALS,
    }

    if is_symbolic:
        # Replace numbers with symbolic representations
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        modified_MEDALS_NAME2 = f"({modified_A} - {modified_B})"
        modified_TOTAL_MEDALS = f"({modified_A} + {modified_MEDALS_NAME2})"
        modified_FINAL_MEDALS = f"({modified_TOTAL_MEDALS} * {modified_C})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(
        NAME1=NAME1, NAME2=NAME2, A=modified_A, B=modified_B, C=modified_C
    )
    answer = answer_text.format(
        NAME1=NAME1,
        NAME2=NAME2,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        MEDALS_NAME2=modified_MEDALS_NAME2,
        TOTAL_MEDALS=modified_TOTAL_MEDALS,
        FINAL_MEDALS=modified_FINAL_MEDALS,
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
