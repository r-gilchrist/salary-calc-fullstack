from pydantic import BaseModel, validator
import datetime


class Date(BaseModel):
    year: int
    month: int

    @validator("year")
    def validate_year(cls, value):
        assert value > 2015
        assert value < 2030
        return value

    @validator("month")
    def validate_month(cls, value):
        assert value > 0
        assert value < 13
        return value

    def to_datetime(self) -> datetime.datetime:
        return datetime.datetime(self.year, self.month, 1)
