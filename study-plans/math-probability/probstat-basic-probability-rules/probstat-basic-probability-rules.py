def basic_probability(p_a: float, p_b: float, p_a_and_b: float) -> list:
    """
    Returns four rounded probability values in the required order.
    """
    p_a_b = round(p_a + p_b - p_a_and_b,4)
    p_a_c = round(1 - p_a,4)
    p_b_c = round(1 - p_b,4)
    p_a_and_b_c = round(p_a - p_a_and_b ,4)
    return [p_a_b, p_a_c, p_b_c, p_a_and_b_c]