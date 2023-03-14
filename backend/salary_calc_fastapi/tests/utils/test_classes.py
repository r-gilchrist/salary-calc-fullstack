from unittest import TestCase
from salary_calc_fastapi.models.date import Date


class TestCaseWithDate(TestCase):
    date = Date(year=2023, month=3)
