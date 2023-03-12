from pydantic import BaseModel, validator


class NationalInsurance(BaseModel):
    gross_salary: float

    def _get_basic_contribution(self):
        if self.gross_salary < 12570:
            return 0
        _valid_salary = min(self.gross_salary - 12570, 50270 - 12570)
        return _valid_salary * 0.12

    def _get_higher_contribution(self):
        if self.gross_salary < 50270:
            return 0
        _valid_salary = min(self.gross_salary - 50270, 125140 - 50270)
        return _valid_salary * 0.02

    def get_amount(self):
        return self._get_basic_contribution() + \
               self._get_higher_contribution()

    @validator("gross_salary")
    def check_values_are_positive_numbers(cls, value):
        assert isinstance(value, float), "must be numeric"
        assert value >= 0, "cannot be negative"
        return value
