import api.repository as repository
from typing import Dict


def load_data():
    repository.load_data()


def get_climbing_days_per_year(year: int) -> Dict[int, int]:
    return {
        month: repository.get_climbing_days_in_month(year, month)
        for month in range(1, 13)
    }


def get_climbing_days() -> Dict[int, int]:
    years = repository.get_climbing_years()
    return {y: repository.get_climbing_days_in_year(y) for y in years}


def get_climbing_days_per_crag() -> Dict[str, int]:
    return repository.get_days_per_crag()


def get_days_per_crag_year(year: int) -> Dict[str, int]:
    return repository.get_days_per_crag_year(year)
