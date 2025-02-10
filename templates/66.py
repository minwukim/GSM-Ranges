import random

def q66(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME1} has {A} books. {NAME2} has {B}. If both {NAME1} and {NAME2} read each others' books as well as their own, how many books will they collectively read by the end?"
    )
    answer_text = (
        "There are {A} + {B} = <<{A}+{B}={TOTAL_BOOKS}>>{TOTAL_BOOKS} books in total.\n"
        "{NAME1} and {NAME2} both read all {TOTAL_BOOKS} books, so {TOTAL_BOOKS} books/person x 2 people = "
        "<<{TOTAL_BOOKS}*2={TOTAL_READ}>>{TOTAL_READ} books total\n#### {TOTAL_READ}"
    )

    # Name options
    common_names = ["Alice", "Emma", "Sophia", "Jack", "Michael"]
    uncommon_names = ["Haruto", "Kaede", "Aisha", "Mei", "Raj"]
    random_strings = ["Fgkwnsd", "Jkldvqw", "Xbwtrmf", "Lmzgtyp", "Prtzfqs"]
    
    # Detect names and modify
    if name_level == 1:
        name1, name2 = "Dolly", "Pandora"
    elif name_level == 2:
        name_pool = [n for n in common_names if n not in ["Dolly", "Pandora"]]
        name1, name2 = random.sample(name_pool, 2)
    elif name_level == 3:
        name1, name2 = random.sample(uncommon_names, 2)
    elif name_level == 4:
        name1, name2 = "Z", "Y"
    elif name_level == 5:
        name1, name2 = random.sample(random_strings, 2)
    
    # Original values
    A, B = 2, 1

    if num_level == 1:
        modified_A, modified_B = A, B
    else:
        # Level 2: Change numbers to same digit count, avoid overlap
        modified_A = random.choice([num for num in range(2, 10) if num != A])
        modified_B = random.choice([num for num in range(2, 10) if num != B])
        
        if num_level == 3:
            # Level 3: Multiply Level 2 numbers by the multiplier
            modified_A *= multiplier
            modified_B *= multiplier
        elif num_level == 4:
            # Level 4: Random range (multiplier, 10 * multiplier - 1)
            modified_A = random.randint(multiplier, 10 * multiplier - 1)
            modified_B = random.randint(multiplier, 10 * multiplier - 1)
    
    # Ensure positivity and logical relationships
    total_books = modified_A + modified_B
    total_read = total_books * 2
    
    # Save original values
    original_values = {
        "A": modified_A,
        "B": modified_B,
        "ans": total_read
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_A, modified_B = "'A'", "'B'"
        total_books = f"({modified_A} + {modified_B})"
        total_read = f"({total_books} * 2)"

    # Replace placeholders
    question = question_text.format(NAME1=name1, NAME2=name2, A=modified_A, B=modified_B)
    answer = answer_text.format(
        NAME1=name1, NAME2=name2, 
        A=modified_A, B=modified_B, 
        TOTAL_BOOKS=total_books, 
        TOTAL_READ=total_read
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
