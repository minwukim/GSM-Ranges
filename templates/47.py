import random

def q47(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} is walking through the Museum of Entomology. {NAME} sees {A} spiders with {B} legs each, "
        "{C} insects with {D} legs each, and {E} rare mutant invertebrates with {F} legs each. "
        "How many legs does {NAME} see total?"
    )
    answer_text = (
        "First find the total number of spider legs: {A} spiders * {B} legs/spider = <<{A}*{B}={SPIDER_LEGS}>>{SPIDER_LEGS} legs.\n"
        "Then find the total number of insect legs: {C} insects * {D} legs/insect = <<{C}*{D}={INSECT_LEGS}>>{INSECT_LEGS} legs.\n"
        "Then find the total number of mutant invertebrate legs: {E} mutants * {F} legs/mutant = <<{E}*{F}={MUTANT_LEGS}>>{MUTANT_LEGS} legs.\n"
        "Then add the number of each kind of leg to find the total seen: {SPIDER_LEGS} legs + {INSECT_LEGS} legs + {MUTANT_LEGS} legs = "
        "<<{SPIDER_LEGS}+{INSECT_LEGS}+{MUTANT_LEGS}={TOTAL_LEGS}>>{TOTAL_LEGS} legs.\n#### {TOTAL_LEGS}"
    )
    
    # Original values
    A, B, C, D, E, F = 80, 8, 90, 6, 3, 10  # Spider count, spider legs, insect count, insect legs, mutant count, mutant legs

    # Dynamic name generation
    common_names = ["Emma", "Lucas", "Sophia", "Mason", "Olivia"]
    uncommon_names = ["Hiroshi", "Meiling", "Aarav", "Zahra", "Kavya"]
    random_strings = ["Zpyxtr", "Qrnfpl", "Tlwshm", "Bmjcqr", "Xlvkpq"]

    if name_level == 1:
        name = "Jake"
    elif name_level == 2:
        name = random.choice(common_names)
    elif name_level == 3:
        name = random.choice(uncommon_names)
    elif name_level == 4:
        name = "Z"
    elif name_level == 5:
        name = random.choice(random_strings)

    if num_level == 1:
        # Level 1: Use original values
        modified_A, modified_B, modified_C, modified_D, modified_E, modified_F = A, B, C, D, E, F
    else:
        # Modify the values for levels > 1
        modified_A = random.choice([num for num in range(10, 91, 10) if num != A])  # Spider count
        modified_B = 8
        modified_C = random.choice([num for num in range(10, 91, 10) if num != C])  # Insect count
        modified_D = 6
        modified_E = random.choice([num for num in range(2, 10) if num != E])  # Mutant count
        modified_F = 10

        if num_level == 3:
            # Scale values for level 3
            modified_A *= multiplier
            modified_C *= multiplier
            modified_E *= multiplier
        elif num_level == 4:
            # Use values within a scaled range for level 4
            modified_A = random.randint(multiplier, multiplier * 10 - 1)
            modified_C = random.randint(multiplier, multiplier * 10 - 1)
            modified_E = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate totals
    spider_legs = modified_A * modified_B
    insect_legs = modified_C * modified_D
    mutant_legs = modified_E * modified_F
    total_legs = spider_legs + insect_legs + mutant_legs

    # Original and modified values
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "D": modified_D,
        "E": modified_E, "F": modified_F, "ans": total_legs
    }

    if is_symbolic:
        # Represent numbers symbolically with quotes
        modified_A, modified_B = '\'A\'', '\'B\''
        modified_C, modified_D = '\'C\'', '\'D\''
        modified_E, modified_F = '\'E\'', '\'F\''
        spider_legs = f"{modified_A} * {modified_B}"
        insect_legs = f"{modified_C} * {modified_D}"
        mutant_legs = f"{modified_E} * {modified_F}"
        total_legs = f"{spider_legs} + {insect_legs} + {mutant_legs}"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=name, A=modified_A, B=modified_B, C=modified_C, D=modified_D, E=modified_E, F=modified_F)
    answer = answer_text.format(
        NAME=name,
        A=modified_A,
        B=modified_B,
        C=modified_C,
        D=modified_D,
        E=modified_E,
        F=modified_F,
        SPIDER_LEGS=spider_legs,
        INSECT_LEGS=insect_legs,
        MUTANT_LEGS=mutant_legs,
        TOTAL_LEGS=total_legs
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
