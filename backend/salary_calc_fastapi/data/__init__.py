from datetime import datetime
from pathlib import Path

from salary_calc_fastapi.data.rates_and_thresholds import DATA
from salary_calc_fastapi.models.date import Date


def datetime_from_string(date: str) -> datetime.date:
    return datetime.strptime(date, "%Y-%m")


def _get_value(value_type: str, tax_type: str, category: str, date: Date) -> float:

    values = DATA[value_type][tax_type][category]

    for value in values:
        date_start = datetime.strptime(value["date_start"], "%Y-%m")
        date_end = datetime.strptime(value["date_end"], "%Y-%m")
        comp_date = datetime(year=date.year, month=date.month, day=1)

        if date_start <= comp_date < date_end:
            return value["value"]

    return _get_value(value_type, tax_type, category, datetime.now())


def get_rate(tax_type: str, category: str, date: Date) -> float:
    return _get_value("rate", tax_type, category, date)


def get_threshold(tax_type: str, category: str, date: Date) -> float:
    return _get_value("threshold", tax_type, category, date)
