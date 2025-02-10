import random

def q78(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Original template for question and answer
    question_text = (
        "{NAME} has {QUARTERS} quarters and {DIMES} dimes. If she buys a can of pop for {PRICE} cents, how many cents will she have left?"
    )
    answer_text = (
        "Her quarters are worth {QUARTERS} * 25 = <<{QUARTERS}*25={QUARTER_VALUE}>>{QUARTER_VALUE} cents.\n"
        "The dimes are worth {DIMES} * 10 = <<{DIMES}*10={DIME_VALUE}>>{DIME_VALUE} cents\n"
        "{NAME} has a total of {QUARTER_VALUE} + {DIME_VALUE} = <<{QUARTER_VALUE}+{DIME_VALUE}={TOTAL_VALUE}>>{TOTAL_VALUE} cents\n"
        "After buying the can of pop, {NAME} will have {TOTAL_VALUE} - {PRICE} = <<{TOTAL_VALUE}-{PRICE}={REMAINING}>>{REMAINING} cents left.\n#### {REMAINING}"
    )

    # Original values
    QUARTERS, DIMES, PRICE = 5, 2, 55
    default_name = "Kelly"

    # Name modification levels
    common_names = ["Alice", "Emma", "Sophia", "Olivia", "Mia"]
    uncommon_names = ["Haruka", "Mingyu", "Kaede", "Rinako", "Takeshi"]
    random_strings = ["Fjdklsa", "Xhtrplm", "Wzqnjkf", "Bcmxvqp", "Lksztrn"]

    if name_level == 1:
        modified_name = default_name
    elif name_level == 2:
        modified_name = random.choice([name for name in common_names if name != default_name])
    elif name_level == 3:
        modified_name = random.choice(uncommon_names)
    elif name_level == 4:
        modified_name = "Z"
    elif name_level == 5:
        modified_name = random.choice(random_strings)

    # Number modification levels
    if num_level == 1:
        modified_QUARTERS, modified_DIMES, modified_PRICE = QUARTERS, DIMES, PRICE
    else:
        modified_QUARTERS = random.choice([num for num in range(3, 10) if num != QUARTERS])
        modified_DIMES = random.choice([num for num in range(3, 10) if num != DIMES])
        modified_PRICE = random.choice([num for num in range(10, 100, 5) if num != PRICE])

        if num_level == 3:
            modified_QUARTERS *= multiplier
            modified_DIMES *= multiplier
            modified_PRICE *= multiplier
        elif num_level == 4:
            modified_QUARTERS = random.randint(multiplier, multiplier * 10 - 1)
            modified_DIMES = random.randint(multiplier, multiplier * 10 - 1)
            modified_PRICE = random.randint(multiplier, multiplier * 10 - 1)

    # Calculate intermediate and final values
    quarter_value = modified_QUARTERS * 25
    dime_value = modified_DIMES * 10
    total_value = quarter_value + dime_value
    remaining = total_value - modified_PRICE

    # Original values dictionary
    original_values = {
        "A": modified_QUARTERS,
        "B": modified_DIMES,
        "C": modified_PRICE,
        "ans": remaining
    }

    if is_symbolic:
        # Represent numbers symbolically
        modified_QUARTERS, modified_DIMES, modified_PRICE = "'A'", "'B'", "'C'"
        quarter_value = f"({modified_QUARTERS} * 25)"
        dime_value = f"({modified_DIMES} * 10)"
        total_value = f"({quarter_value} + {dime_value})"
        remaining = f"({total_value} - {modified_PRICE})"

    # Replace placeholders in the question and answer templates
    question = question_text.format(NAME=modified_name, QUARTERS=modified_QUARTERS, DIMES=modified_DIMES, PRICE=modified_PRICE)
    answer = answer_text.format(
        NAME=modified_name,
        QUARTERS=modified_QUARTERS,
        DIMES=modified_DIMES,
        PRICE=modified_PRICE,
        QUARTER_VALUE=quarter_value,
        DIME_VALUE=dime_value,
        TOTAL_VALUE=total_value,
        REMAINING=remaining
    )

    if is_symbolic:
        return {"question": question, "answer": answer, "original_values": original_values}
    return {"question": question, "answer": answer}
