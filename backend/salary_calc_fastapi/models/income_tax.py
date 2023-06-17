from pydantic import BaseModel, validator
from salary_calc_fastapi.helpers.marginal_helpers import calculate_marginal_tax
from salary_calc_fastapi.data import get_rate, get_threshold
from salary_calc_fastapi.models.date import Date


class IncomeTax(BaseModel):
    gross_salary: float
    date: Date

    def _get_basic_contribution(self) -> float:
        rate = get_rate("income_tax", "basic", self.date)
        threshold_lower = self._get_threshold("basic")
        threshold_upper = self._get_threshold("higher")
        return calculate_marginal_tax(
            self.gross_salary, rate, threshold_lower, threshold_upper
        )

    def _get_higher_contribution(self) -> float:
        rate = get_rate("income_tax", "higher", self.date)
        threshold_lower = self._get_threshold("higher")
        threshold_upper = get_threshold("income_tax", "additional", self.date)
        return calculate_marginal_tax(
            self.gross_salary, rate, threshold_lower, threshold_upper
        )

    def _get_additional_contribution(self) -> float:
        rate = get_rate("income_tax", "additional", self.date)
        threshold = get_threshold("income_tax", "additional", self.date)
        return calculate_marginal_tax(self.gross_salary, rate, threshold)

    def get_amount(self) -> float:
        return (
            self._get_basic_contribution()
            + self._get_higher_contribution()
            + self._get_additional_contribution()
        )

    def _get_threshold(self, category: str) -> float:
        """
        Adjusts the basic rate threshold if gross salary is over £100,000. Reduction
        is £1 for every £2 earned over £100,000, up until the additional rate threshold.

        :return: A reduced basic rate threshold
        """
        threshold = get_threshold("income_tax", category, self.date)
        if self.gross_salary <= 100000:
            return threshold
        if self.gross_salary > 125140:
            return threshold - 12570
        return threshold - int((self.gross_salary - 100000) / 2)

    @validator("gross_salary")
    def check_values_are_positive_numbers(cls, value):
        assert isinstance(value, float), "must be numeric"
        assert value >= 0, "cannot be negative"
        return value
