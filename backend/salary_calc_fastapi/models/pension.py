from pydantic import BaseModel, validator


class Pension(BaseModel):
    reference_salary: float
    percentage_employee: float | None = 0
    percentage_employer: float | None = 0

    def total_percentage(self):
        return self.percentage_employee + self.percentage_employer

    def get_amount(self):
        return self.reference_salary * 0.01 * self.total_percentage()

    @validator("percentage_employee", "percentage_employer")
    def check_values_are_positive_numbers(cls, value):
        assert isinstance(value, float), "must be numeric"
        assert value >= 0, "cannot be negative"
        return value
