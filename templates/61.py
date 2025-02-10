import random

def q61(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} plants {A} geraniums and {B} fewer petunias than geraniums. How many flowers does he plant total?"
    )
    answer_text = (
        "First find the number of petunias {NAME} plants: {A} flowers - {B} = <<{A}-{B}={PETUNIAS}>>{PETUNIAS} flowers\n"
        "Then add the number of each kind of flower he plants to find the total number: {PETUNIAS} flowers + {A} flowers = "
        "<<{PETUNIAS}+{A}={TOTAL_FLOWERS}>>{TOTAL_FLOWERS} flowers\n#### {TOTAL_FLOWERS}"
    )

    # Name levels
    common_names = ["John", "Emma", "Michael", "Sophia", "Chris"]
    uncommon_names = ["Haruto", "Mei", "Aarav", "Yara", "Chen"]
    random_strings = ["Kdjfpqt", "Bxlytmv", "Wnzlsqv", "Lqrfzpt", "Tmwsjvp"]
    
    # Dynamic name generation
    if name_level == 1:
        name = "Andy"
    elif name_level == 2:
        name = random.choice([n for n in common_names if n != "Andy"])
    elif name_level == 3:
        name = random.choice(uncommon_names)
    elif name_level == 4:
        name = "Z"
    elif name_level == 5:
        name = random.choice(random_strings)
    
    # Original values
    A, B = 90, 40  # A = geraniums, B = fewer petunias (must be < A)

    # Adjust numbers based on num_level
    if num_level == 1:
        modified_A, modified_B = A, B
    elif num_level == 2:
        modified_A = random.choice([num for num in range(30, 100) if num != A and num % 10 == 0])
        modified_B = random.choice([num for num in range(10, modified_A) if num != B and num % 5 == 0])
    elif num_level == 3:
        modified_A = A * multiplier
        modified_B = random.randint(multiplier, modified_A - 1)  # Ensure B < A
    elif num_level == 4:
        modified_A = random.randint(multiplier+2, 10 * multiplier - 1)
        modified_B = random.randint(multiplier, modified_A - 1)  # Ensure B < A

    # Calculate values
    petunias = modified_A - modified_B
    total_flowers = petunias + modified_A

    # Save original values before symbolic replacement
    original_values = {
        "A": modified_A, "B": modified_B, "ans": total_flowers
    }

    # Handle symbolic representation
    if is_symbolic:
        modified_A, modified_B = "'A'", "'B'"
        petunias = f"{modified_A} - {modified_B}"
        total_flowers = f"{petunias} + {modified_A}"
    
    # Replace placeholders
    question = question_text.format(NAME=name, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME=name, A=modified_A, B=modified_B, 
        PETUNIAS=petunias, TOTAL_FLOWERS=total_flowers
    )

    return {"question": question, "answer": answer, "original_values": original_values}

