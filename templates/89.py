import random

def q89(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} just turned {CARVER_AGE} years old, which makes him {DIFFERENCE} years less than twice the age of his son. "
        "How old is his son, in years?"
    )
    answer_text = (
        "Let x be the age of {NAME}'s son.\n"
        "Since {NAME}'s age ({CARVER_AGE}) is {DIFFERENCE} years less than twice the age of his son, then "
        "{CARVER_AGE}=(2*x)-{DIFFERENCE}.\n"
        "Add {DIFFERENCE} to each side of the equation and we get {CARVER_AGE}+{DIFFERENCE}=2*x.\n"
        "Thus, the age of {NAME}'s son is x=({CARVER_AGE}+{DIFFERENCE})/2 years old.\n#### {SON_AGE}"
    )

    # Original values
    CARVER_AGE, DIFFERENCE = 45, 5
    SON_AGE = (CARVER_AGE + DIFFERENCE) // 2

    # Name handling based on levels
    original_name = "Carver"
    if name_level == 1:
        modified_name = original_name
    elif name_level == 2:
        common_names = ["Michael", "John", "Emma", "Sophia", "James"]
        modified_name = random.choice([name for name in common_names if name != original_name])
    elif name_level == 3:
        uncommon_asian_names = ["Haruto", "Aiko", "Mei", "Takeshi", "Kaori"]
        modified_name = random.choice(uncommon_asian_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=7))

    # Number handling based on levels
    if num_level == 1:
        modified_carver_age, modified_difference = CARVER_AGE, DIFFERENCE
    else:
        modified_carver_age = random.choice([num for num in range(15, 100, 10) if num != CARVER_AGE])
        modified_difference = random.choice([num for num in range(3, 10, 2) if num != DIFFERENCE])

        if num_level == 3:
            modified_carver_age *= multiplier
            modified_difference *= multiplier
        elif num_level == 4:
            modified_carver_age = random.randint(multiplier, 5 * multiplier) * 2 
            modified_difference = random.randint(multiplier, 5 * multiplier) * 2

    # Ensure positivity of son's age
    modified_son_age = (modified_carver_age + modified_difference) // 2

    # Original values for symbolic case
    original_values = {
        "A": modified_carver_age,
        "B": modified_difference,
        "ans": (modified_carver_age + modified_difference) // 2
    }

    if is_symbolic:
        modified_carver_age, modified_difference = "'A'", "'B'"
        modified_son_age = "('A' + 'B') / 2"

    # Replace placeholders in templates
    question = question_text.format(
        NAME=modified_name, 
        CARVER_AGE=modified_carver_age, 
        DIFFERENCE=modified_difference
    )
    answer = answer_text.format(
        NAME=modified_name, 
        CARVER_AGE=modified_carver_age, 
        DIFFERENCE=modified_difference, 
        SON_AGE=modified_son_age
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
