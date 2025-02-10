import random

def q12(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} is a freelance blogger who writes about health topics and submits to clients each day as her permanent job. "
        "One blog article takes an average of {A} hours to research and write about. "
        "Last week, she wrote {B} articles on Monday and {C}/5 times more articles on Tuesday than on Monday. "
        "On Wednesday, she wrote {D} times the number of articles she wrote on Tuesday. "
        "Calculate the total number of hours she spent writing articles in the three days."
    )
    answer_text = (
        "If she wrote {B} articles on Monday, then on Tuesday she wrote {C}/5 * {B} = <<{C}/{DENOMINATOR}*{B}={TUESDAY_ADDITIONAL}>>{TUESDAY_ADDITIONAL} more articles.\n"
        "The total number of articles she wrote on Tuesday is {B}+{TUESDAY_ADDITIONAL} = <<{B}+{TUESDAY_ADDITIONAL}={TUESDAY_TOTAL}>>{TUESDAY_TOTAL}.\n"
        "On Wednesday, the number of articles was {D}*{TUESDAY_TOTAL} = <<{D}*{TUESDAY_TOTAL}={WEDNESDAY_TOTAL}>>{WEDNESDAY_TOTAL} articles.\n"
        "Over the three days, she wrote {B}+{TUESDAY_TOTAL}+{WEDNESDAY_TOTAL} = <<{B}+{TUESDAY_TOTAL}+{WEDNESDAY_TOTAL}={TOTAL_ARTICLES}>>{TOTAL_ARTICLES} articles.\n"
        "If each article takes her {A} hours to research and write about, she spent {A}*{TOTAL_ARTICLES} = <<{A}*{TOTAL_ARTICLES}={TOTAL_HOURS}>>{TOTAL_HOURS} hours on all the articles.\n#### {TOTAL_HOURS}"
    )
    
    # Original values
    A, B, C, D = 4, 5, 2, 2  # Hours per article, Monday articles, numerator for Tuesday fraction, multiplier for Wednesday
    DENOMINATOR = 5  # Fixed denominator for Tuesday's fraction
    original_name = "Meredith"

    # Modify name based on name_level
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        common_names = ["Emma", "Sophia", "Olivia", "Isabella", "Ava"]
        modified_name = random.choice(common_names)
    elif name_level == 3:
        uncommon_names = ["Eulalia", "Calliope", "Zephyra", "Thalassa", "Rhiannon"]
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        symbols = ["Z", "Y", "X", "W", "V"]
        modified_name = symbols[0]
    elif name_level == 5:
        random_strings = ["Mrdth", "Crlnk", "Blkrf", "Plndr", "Trmnb"]
        modified_name = random.choice(random_strings)

    # Modify the values for num_level
    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        modified_A = random.choice([num for num in range(2, 10) if num != A])
        modified_B = random.choice([num for num in range(5, 11, 5) if num != B])
        modified_C = random.choice([num for num in range(2, 5) if num != C])  # Only the numerator changes
        modified_D = random.choice([num for num in range(2, 10) if num != D])

        if num_level == 3:
            modified_B *= multiplier
        elif num_level == 4:
            modified_B = random.choice([num for num in range(multiplier, multiplier * 10, 5)])

    # Calculate the number of articles and total hours
    tuesday_additional = int((modified_C / DENOMINATOR) * modified_B)
    tuesday_total = modified_B + tuesday_additional
    wednesday_total = int(modified_D * tuesday_total)
    total_articles = modified_B + tuesday_total + wednesday_total
    total_hours = int(modified_A * total_articles)

    A = modified_A
    B = modified_B
    C = modified_C
    D = modified_D

    original_values = {
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "ans": int(A * (B + (B + int((C / DENOMINATOR) * B)) + int(D * (B + int((C / DENOMINATOR) * B)))))
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C, modified_D = '\'A\'', '\'B\'', '\'C\'', '\'D\''
        tuesday_additional = f"{modified_C}/{DENOMINATOR} * {modified_B}"
        tuesday_total = f"{modified_B} + ({tuesday_additional})"
        wednesday_total = f"{modified_D} * ({tuesday_total})"
        total_articles = f"{modified_B} + ({tuesday_total}) + ({wednesday_total})"
        total_hours = f"{modified_A} * ({total_articles})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C, D=modified_D)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        DENOMINATOR=DENOMINATOR,
        D=modified_D,
        TUESDAY_ADDITIONAL=tuesday_additional,
        TUESDAY_TOTAL=tuesday_total,
        WEDNESDAY_TOTAL=wednesday_total,
        TOTAL_ARTICLES=total_articles,
        TOTAL_HOURS=total_hours
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
