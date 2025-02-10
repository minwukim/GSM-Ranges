import random

def q98(num_level=1, multiplier=100, name_level=1, is_symbolic=False):
    # Question and answer templates
    question_text = (
        "{NAME1} and {NAME2} went to the carnival, where there are {A} rides.  Each ride costs {B} ride tickets at ${C} per ticket.  "
        "You can also buy a ride bracelet for ${D} which gives you {A} rides.  If {NAME1} buys a ride bracelet and {NAME2} buys tickets, and they ride all {A} rides, "
        "how much money does {NAME1} save?"
    )
    answer_text = (
        "Each ride cost {B} x ${C} = $<<{B}*{C}={COST_PER_RIDE}>>{COST_PER_RIDE}.\n"
        "All {A} rides cost ${COST_PER_RIDE} x {A} = $<<{COST_PER_RIDE}*{A}={TOTAL_COST_TICKETS}>>{TOTAL_COST_TICKETS}.\n"
        "By buying the ride bracelet, {NAME1} saves ${TOTAL_COST_TICKETS} - ${D} = $<<{TOTAL_COST_TICKETS}-{D}={SAVINGS}>>{SAVINGS}.\n#### {SAVINGS}"
    )

    # Original values
    A, B, C, D = 9, 2, 2, 30  # Number of rides, tickets per ride, cost per ticket, cost of bracelet
    original_name1, original_name2 = "David", "Dasha"

    # Modify names based on name_level
    if name_level == 1:
        modified_name1, modified_name2 = original_name1, original_name2
    elif name_level == 2:
        common_names = ["Alice", "Emma", "Sophia", "Olivia", "Mia", "Jack", "Michael", "Chris", "Taylor"]
        modified_name1, modified_name2 = random.sample([n for n in common_names if n not in [original_name1, original_name2]], 2)
    elif name_level == 3:
        uncommon_asian_names = ["Haruto", "Mingyu", "Kaede", "Rinako", "Takeshi", "Aisha", "Raj"]
        modified_name1, modified_name2 = random.sample(uncommon_asian_names, 2)
    elif name_level == 4:
        modified_name1, modified_name2 = "Z", "Y"
    elif name_level == 5:
        random_strings = ["Fjakslf", "Tmlwqrz", "Rksfnpq", "Bzowvls", "Lmrptzx"]
        modified_name1, modified_name2 = random.sample(random_strings, 2)

    # Modify numbers based on num_level
    if num_level == 1:
        modified_A, modified_B, modified_C, modified_D = A, B, C, D
    else:
        modified_A = random.choice([num for num in range(3, 10) if num != A])  # Number of rides
        modified_B = random.choice([num for num in range(2, 10) if num != B])  # Tickets per ride
        modified_C = random.choice([num for num in range(2, 10) if num != C])  # Cost per ticket
        modified_D = random.choice([num for num in range(10, modified_A * modified_B * modified_C) if num != D])  # Cost of bracelet

        if num_level == 3:
            modified_B *= multiplier
            modified_D *= multiplier
        elif num_level == 4:
            modified_B = random.randint(multiplier, 10 * multiplier - 1)
            modified_D = random.randint(multiplier, modified_A * modified_B * modified_C)

    # Calculate totals
    cost_per_ride = modified_B * modified_C
    total_cost_tickets = cost_per_ride * modified_A
    savings = total_cost_tickets - modified_D

    # Store original values before symbolic modifications
    original_values = {
        "A": modified_A, "B": modified_B, "C": modified_C, "D": modified_D, "ans": savings
    }

    if is_symbolic:
        # Symbolic representation
        modified_A, modified_B, modified_C, modified_D = "'A'", "'B'", "'C'", "'D'"
        cost_per_ride = f"({modified_B} * {modified_C})"
        total_cost_tickets = f"({cost_per_ride} * {modified_A})"
        savings = f"({total_cost_tickets} - {modified_D})"

    # Replace placeholders in question and answer templates
    question = question_text.format(
        NAME1=modified_name1, NAME2=modified_name2, A=modified_A, B=modified_B, C=modified_C, D=modified_D
    )
    answer = answer_text.format(
        NAME1=modified_name1, A=modified_A, B=modified_B, C=modified_C, D=modified_D,
        COST_PER_RIDE=cost_per_ride, TOTAL_COST_TICKETS=total_cost_tickets, SAVINGS=savings
    )

    return {"question": question, "answer": answer, "original_values": original_values}

