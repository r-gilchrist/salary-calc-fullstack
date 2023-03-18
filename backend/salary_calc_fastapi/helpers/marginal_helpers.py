def calculate_marginal_tax(
    gross_salary: float,
    rate: float,
    lower_margin: float,
    upper_margin: float | None = None,
) -> float:
    """Calculates marginal tax amount

    :param gross_salary: Gross salary
    :param rate: Rate of taxation as a percentage
    :param lower_margin: Lower bound of the margin
    :param upper_margin: Upper bound of the margin, defaults to None
    :return: _description_
    """
    if gross_salary < lower_margin:
        return 0

    _valid_amount = gross_salary - lower_margin

    if upper_margin is not None and upper_margin > lower_margin:
        _valid_amount = min(_valid_amount, upper_margin - lower_margin)

    return _valid_amount * rate * 0.01
