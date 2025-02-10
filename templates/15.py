import random

def q15(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} has two recipes for preparing dishes, one having {A} instructions and the second one having twice as many instructions as the first one. "
        "How many instructions does {NAME} have to read to prepare the two dishes?"
    )
    answer_text = (
        "The second recipe has 2 * {A} instructions = <<2*{A}={SECOND_RECIPE}>>{SECOND_RECIPE} instructions.\n"
        "The total for the two dishes is {SECOND_RECIPE} instructions + {A} instructions = "
        "<<{SECOND_RECIPE}+{A}={TOTAL_INSTRUCTIONS}>>{TOTAL_INSTRUCTIONS} instructions.\n#### {TOTAL_INSTRUCTIONS}"
    )
    
    # Name levels
    original_name = "Kelian"
    common_names = ["Alex", "Emma", "Chris", "Taylor", "Jordan"]  # Avoid "Kelian"
    uncommon_names = ["Haruto", "Mei", "Raj", "Yara", "Kaede"]
    random_strings = ["Rnfqzxt", "Pldjwyv", "Xlvtsnm", "Zxktqbp", "Mjwcpqr"]
    
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        modified_name = random.choice(common_names)
    elif name_level == 3:
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = random.choice(random_strings)

    # Original number
    A = 20  # Instructions in the first recipe

    # Adjust number levels
    if num_level == 1:
        modified_A = A
    elif num_level == 2:
        modified_A = random.choice([num for num in range(10, 100) if num != A and num % 10 == 0])
    elif num_level == 3:
        modified_A = random.choice([num for num in range(10, 100) if num != A and num % 10 == 0]) * multiplier
    elif num_level == 4:
        modified_A = random.randint(multiplier, 10 * multiplier - 1)

    # Calculate derived values
    second_recipe = 2 * modified_A
    total_instructions = second_recipe + modified_A

    # Store original values
    original_values = {
        "A": modified_A, 
        "ans": modified_A * 3
    }

    # Symbolic handling
    if is_symbolic:
        modified_A = "'A'"
        second_recipe = f"(2 * {modified_A})"
        total_instructions = f"({second_recipe} + {modified_A})"

    # Format question and answer
    question = question_text.format(NAME=modified_name, A=modified_A)
    answer = answer_text.format(
        A=modified_A, 
        SECOND_RECIPE=second_recipe, 
        TOTAL_INSTRUCTIONS=total_instructions
    )
    
    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
