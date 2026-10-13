total_students = 20
programming_students = 12
python_and_programming = 5

def conditional_probability(all_outcomes, intersection, condition):
    # P(A ∩ B) = intersection / all_outcomes
    # P(B)     = condition / all_outcomes
    # P(A | B) = P(A ∩ B) / P(B)

    p_intersection = intersection / all_outcomes
    p_condition = condition / all_outcomes

    # Avoid division by zero
    if p_condition == 0:
        return 0

    prob_a_given_b = p_intersection / p_condition
    return prob_a_given_b * 100  # as percentage

prob = conditional_probability(
    total_students,
    python_and_programming,   # A ∩ B
    programming_students      # B
)

print(f"{prob:.2f}%")  # 41.67%