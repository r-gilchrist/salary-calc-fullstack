from pydantic import BaseModel, validator
from salary_calc_fastapi.helpers.marginal_helpers import calculate_marginal_tax
from salary_calc_fastapi.data import get_rate, get_threshold
from salary_calc_fastapi.models.date import Date


class NationalInsurance(BaseModel):
    gross_salary: float
    date: Date

    def _get_basic_contribution(self) -> float:
        rate = get_rate("national_insurance", "basic", self.date)
        threshold_lower = get_threshold("national_insurance", "basic", self.date)
        threshold_upper = get_threshold("national_insurance", "higher", self.date)
        return calculate_marginal_tax(self.gross_salary, rate, threshold_lower, threshold_upper)

    def _get_higher_contribution(self) -> float:
        rate = get_rate("national_insurance", "higher", self.date)
        threshold_lower = get_threshold("national_insurance", "higher", self.date)
        return calculate_marginal_tax(self.gross_salary, rate, threshold_lower)

    def get_amount(self) -> float:
        return self._get_basic_contribution() + \
               self._get_higher_contribution()

    @validator("gross_salary")
    def check_values_are_positive_numbers(cls, value):
        assert isinstance(value, float), "must be numeric"
        assert value >= 0, "cannot be negative"
        return value
