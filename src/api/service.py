import repository as repository
from typing import Dict, Optional
from collections import defaultdict


def get_climbing_days_per_month(year: int) -> Dict[int, int]:
    return {
        month: repository.get_climbing_days_in_month(year, month)
        for month in range(1, 13)
    }


def get_climbing_days_per_year() -> Dict[int, int]:
    return {year: days for year, days in repository.get_climbing_days_per_year()}


def get_climbing_days_per_crag(year: int) -> Dict[str, int]:
    return {crag: days for crag, days in repository.get_days_per_crag(year)}


def get_climbing_days_per_sector(year: int) -> Dict[str, Dict[str, int]]:
    data = repository.get_days_per_sector(year)
    days_per_sector = defaultdict(dict)
    for crag, sector, days in data:
        days_per_sector[crag] |= {sector: days}

    return days_per_sector

# def get_climbing_days_per_crag(year: Optional[int | str] = None,
#                                zone: Optional[str] = None) -> Dict[str, int]:
#     data = repository.get_zone_days_data(year)
#
#     return repository.get_days_by_zone(data, zone)
#
#
# def get_days_per_crag_year(year: int) -> Dict[str, int]:
#     return repository.get_days_per_crag_year(year)
