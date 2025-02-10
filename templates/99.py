import random

def q99(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} wants to place {A} more than double the number of books in a shelving system with {B} rows and {C} columns. "
        "How many books will {NAME} need to carry to complete her task?"
    )
    answer_text = (
        "The capacity of the shelving system with {B} rows and {C} columns is {B}*{C}=<<{B}*{C}={CAPACITY}>>{CAPACITY} books.\n"
        "Double the capacity of the shelving system is 2*{CAPACITY}=<<2*{CAPACITY}={DOUBLE_CAPACITY}>>{DOUBLE_CAPACITY}.\n"
        "If {NAME} wants to place {A} more than double the number of books in a shelving system with {B} rows and {C} columns, "
        "she wants to place {A}+{DOUBLE_CAPACITY}=<<{A}+{DOUBLE_CAPACITY}={TOTAL_BOOKS}>>{TOTAL_BOOKS} books.\n#### {TOTAL_BOOKS}"
    )

    # Name options
    common_names = ["Alice", "Emma", "Sophia", "Olivia", "Mia"]
    uncommon_names = ["Haruka", "Mingyu", "Kaede", "Rinako", "Takeshi"]
    random_strings = ["Fjakslf", "Xmvqzpt", "Lcnrtwv", "Bzwxptr", "Qpslzrk"]

    # Detect the name from the question
    original_name = "Wendy"

    # Name levels
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

    # Original numbers
    A, B, C = 20, 6, 6

    if num_level == 1:
        # Level 1: Use original numbers
        modified_A, modified_B, modified_C = A, B, C
    elif num_level == 2:
        # Level 2: Numbers in the same digit range, different from original
        modified_A = random.choice([num for num in range(10, 100) if num != A and num % 10 == 0])
        modified_B = random.choice([num for num in range(2, 10) if num != B])
        modified_C = random.choice([num for num in range(2, 10) if num != C])
    elif num_level == 3:
        # Level 3: Multiply Level 2 numbers by multiplier
        modified_A = random.choice([num for num in range(10, 100) if num != A and num % 10 == 0]) * multiplier
        modified_B = random.choice([num for num in range(2, 10) if num != B]) * multiplier
        modified_C = random.choice([num for num in range(2, 10) if num != C])
    elif num_level == 4:
        # Level 4: Random numbers in the range (multiplier, 10*multiplier - 1)
        modified_A = random.randint(multiplier, 10 * multiplier - 1)
        modified_B = random.randint(multiplier, 10 * multiplier - 1)
        modified_C = random.choice([num for num in range(2, 10) if num != C])

    # Calculate totals
    capacity = modified_B * modified_C
    double_capacity = 2 * capacity
    total_books = modified_A + double_capacity

    # Save original values before is_symbolic modification
    original_values = {
        "A": modified_A,
        "B": modified_B,
        "C": modified_C,
        "ans": total_books
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B, modified_C = '\'A\'', '\'B\'', '\'C\''
        capacity = f"({modified_B} * {modified_C})"
        double_capacity = f"(2 * {capacity})"
        total_books = f"({modified_A} + {double_capacity})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, A=modified_A, B=modified_B, C=modified_C)
    answer = answer_text.format(
        NAME=modified_name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        CAPACITY=capacity,
        DOUBLE_CAPACITY=double_capacity,
        TOTAL_BOOKS=total_books
    )

    return {"question": question, "answer": answer, "original_values": original_values}