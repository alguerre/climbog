from datetime import datetime
from typing import Dict, Set

import pytest
from pandas import DataFrame

import api.repository as repository


@pytest.mark.parametrize(
    "data,expected",
    [
        (
            DataFrame(
                {
                    "Fecha": [
                        datetime(2022, 5, 1),
                        datetime(2022, 6, 1),
                        datetime(2022, 7, 1),
                        datetime(2023, 5, 1),
                    ]
                }
            ),
            {2022, 2023},
        ),
        (DataFrame({"Fecha": []}), set()),
        (
            DataFrame(
                {
                    "Fecha": [
                        datetime(2022, 5, 1),
                        datetime(2022, 6, 1),
                        datetime(2022, 7, 1),
                    ]
                }
            ),
            {2022},
        ),
    ],
)
def test_get_climbing_years(data: DataFrame, expected: Set[int]):
    repository.climbing_data = data
    assert repository.get_climbing_years() == expected


@pytest.mark.parametrize(
    "data,year,expected",
    [
        (
            DataFrame(
                {
                    "Fecha": [
                        datetime(2022, 5, 1),
                        datetime(2022, 6, 1),
                        datetime(2022, 7, 1),
                        datetime(2023, 5, 1),
                    ]
                }
            ),
            2022,
            3,
        ),
        (DataFrame({"Fecha": []}), 2022, 0),
        (DataFrame({"Fecha": [datetime(2022, 5, 1)]}), 2021, 0),
    ],
)
def test_get_climbing_days_in_year(data: DataFrame, year: int, expected: int):
    repository.climbing_data = data
    assert repository.get_climbing_days_in_year(year) == expected


@pytest.mark.parametrize(
    "data,year,month,expected",
    [
        (
            DataFrame(
                {
                    "Fecha": [
                        datetime(2022, 5, 1),
                        datetime(2022, 6, 1),
                        datetime(2022, 6, 1),
                        datetime(2023, 5, 1),
                    ]
                }
            ),
            2022,
            6,
            2,
        ),
        (DataFrame({"Fecha": []}), 2022, 1, 0),
        (DataFrame({"Fecha": [datetime(2022, 5, 1)]}), 2021, 1, 0),
    ],
)
def test_get_climbing_days_in_month(
    data: DataFrame, year: int, month: int, expected: int
):
    repository.climbing_data = data
    assert repository.get_climbing_days_in_year(year) == expected


@pytest.mark.parametrize(
    "data,expected",
    [
        (
            DataFrame(
                {
                    "Lugar": ["A", "A", "B", "A"],
                    "Fecha": [
                        datetime(2022, 1, 1),
                        datetime(2022, 1, 1),
                        datetime(2022, 1, 2),
                        datetime(2022, 1, 3),
                    ],
                }
            ),
            {"A": 2, "B": 1},
        ),
        (DataFrame({"Lugar": [], "Fecha": []}), dict()),
    ],
)
def test_get_days_per_crag(data: DataFrame, expected: Dict[str, int]):
    repository.climbing_data = data
    assert repository.get_days_per_crag() == expected
