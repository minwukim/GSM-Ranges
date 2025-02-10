import random

def q76(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Question and answer templates
    question_text = (
        "{NAME1}'s family decided that the children should write stories of any kind. They were then required to read all of the stories they'd written to the family at the end of the weekend. "
        "{NAME1} wrote {A} stories in the first week, her brother {NAME2} wrote {B} stories, and her sister {NAME3} wrote {C} stories. "
        "If they each doubled the number of stories they'd written in the first week in the second week, calculate the total number of stories they wrote altogether."
    )
    answer_text = (
        "In the first week, {NAME1} wrote {A} stories, and if she doubled the number in the second week, the total number of stories in the second week is ({A}*2) = <<{A}*2={A_SECOND_WEEK}>>{A_SECOND_WEEK}.\n"
        "In total, {NAME1} had written ({A_SECOND_WEEK}+{A}) = <<{A_SECOND_WEEK}+{A}={A_TOTAL}>>{A_TOTAL} stories in the two weeks.\n"
        "{NAME2} also wrote {B} stories in the first week, and on doubling that number in the second week the number became (2*{B}) =<<{B}*2={B_SECOND_WEEK}>>{B_SECOND_WEEK}.\n"
        "His total number of stories in the two weeks is ({B_SECOND_WEEK}+{B}) = <<{B_SECOND_WEEK}+{B}={B_TOTAL}>>{B_TOTAL}.\n"
        "Together, {NAME1} and her brother {NAME2} had written ({A_TOTAL}+{B_TOTAL}) = <<{A_TOTAL}+{B_TOTAL}={A_B_TOTAL}>>{A_B_TOTAL} stories.\n"
        "When {NAME3} doubled the number of stories she wrote in the first week in the second week, she wrote (2*{C}) = <<2*{C}={C_SECOND_WEEK}>>{C_SECOND_WEEK} stories in the second week.\n"
        "In total, she wrote ({C}+{C_SECOND_WEEK}) = <<{C}+{C_SECOND_WEEK}={C_TOTAL}>>{C_TOTAL} stories.\n"
        "Altogether, the three siblings wrote ({A_B_TOTAL}+{C_TOTAL}) = <<{A_B_TOTAL}+{C_TOTAL}={TOTAL}>>{TOTAL} stories in the two weeks.\n#### {TOTAL}"
    )

    # Original values
    A, B, C = 20, 40, 60
    names = ["Alani", "Braylen", "Margot"]

    # Name modifications
    if name_level == 1:
        modified_names = names
    elif name_level == 2:
        common_names = ["Sophia", "Oliver", "Emma", "Liam", "Ava"]
        modified_names = random.sample([name for name in common_names if name not in names], 3)
    elif name_level == 3:
        uncommon_names = ["Haruto", "Mei", "Kaede", "Rin", "Takeshi"]
        modified_names = random.sample(uncommon_names, 3)
    elif name_level == 4:
        modified_names = ["Z", "Y", "X"]
    elif name_level == 5:
        modified_names = ["fjakslf", "bqwezxc", "rnltywo"]

    NAME1, NAME2, NAME3 = modified_names

    # Number modifications
    if num_level == 1:
        modified_A, modified_B, modified_C = A, B, C
    elif num_level == 2:
        modified_A = random.choice([num for num in range(10, 100) if num != A and num % 10 == A % 10])
        modified_B = random.choice([num for num in range(10, 100) if num != B and num % 10 == B % 10])
        modified_C = random.choice([num for num in range(10, 100) if num != C and num % 10 == C % 10])
    elif num_level == 3:
        modified_A = random.choice([num for num in range(10, 100) if num != A and num % 10 == A % 10]) * multiplier
        modified_B = random.choice([num for num in range(10, 100) if num != B and num % 10 == B % 10]) * multiplier
        modified_C = random.choice([num for num in range(10, 100) if num != C and num % 10 == C % 10]) * multiplier
    elif num_level == 4:
        modified_A = random.randint(multiplier, 10 * multiplier - 1)
        modified_B = random.randint(multiplier, 10 * multiplier - 1)
        modified_C = random.randint(multiplier, 10 * multiplier - 1)

    # Calculate totals
    A_SECOND_WEEK = modified_A * 2
    B_SECOND_WEEK = modified_B * 2
    C_SECOND_WEEK = modified_C * 2

    A_TOTAL = modified_A + A_SECOND_WEEK
    B_TOTAL = modified_B + B_SECOND_WEEK
    C_TOTAL = modified_C + C_SECOND_WEEK

    A_B_TOTAL = A_TOTAL + B_TOTAL
    TOTAL = A_B_TOTAL + C_TOTAL

    # Original values dictionary
    original_values = {
        "A": modified_A,
        "B": modified_B,
        "C": modified_C,
        "ans": TOTAL
    }

    if is_symbolic:
        # Symbolic representation
        modified_A, modified_B, modified_C = "'A'", "'B'", "'C'"
        A_SECOND_WEEK = f"({modified_A} * 2)"
        B_SECOND_WEEK = f"({modified_B} * 2)"
        C_SECOND_WEEK = f"({modified_C} * 2)"

        A_TOTAL = f"({A_SECOND_WEEK} + {modified_A})"
        B_TOTAL = f"({B_SECOND_WEEK} + {modified_B})"
        C_TOTAL = f"({C_SECOND_WEEK} + {modified_C})"

        A_B_TOTAL = f"({A_TOTAL} + {B_TOTAL})"
        TOTAL = f"({A_B_TOTAL} + {C_TOTAL})"

    # Replace placeholders in question and answer
    question = question_text.format(NAME1=NAME1, NAME2=NAME2, NAME3=NAME3, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME1=NAME1, NAME2=NAME2, NAME3=NAME3,
        A=modified_A, B=modified_B, C=modified_C,
        A_SECOND_WEEK=A_SECOND_WEEK, B_SECOND_WEEK=B_SECOND_WEEK, C_SECOND_WEEK=C_SECOND_WEEK,
        A_TOTAL=A_TOTAL, B_TOTAL=B_TOTAL, C_TOTAL=C_TOTAL,
        A_B_TOTAL=A_B_TOTAL, TOTAL=TOTAL
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
