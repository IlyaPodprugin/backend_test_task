from typing import Union


def calculate_credit_payment(
        price: Union[int, str],
        deposit: Union[int, str],
        term: Union[int, str],
        rate_min: Union[int, str]
) -> int:
    """
    Function calculates monthly credit payment
    :param price: amount of money needed
    :param deposit: an initial fee
    :param term: term for credit
    :param rate_min: minimum credit rate
    :return payment: calculated monthly payment
    """
    credit_sum: int = int(price) - int(deposit)
    monthly_rate: float = float(rate_min) / 12
    term_in_months: int = int(term) * 12
    payment: float = credit_sum * monthly_rate / (1 - (1 / (1 + monthly_rate)) * term_in_months)
    return int(-payment)
