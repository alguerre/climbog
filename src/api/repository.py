from typing import Dict, Set, Optional
from enum import Enum
import pandas as pd

from api.paths import DATA_SOURCE

climbing_data: pd.DataFrame


class Zone(Enum):
    crag = "CRAG"
    sector = "SECTOR"


def load_data():
    global climbing_data
    climbing_data = pd.read_excel(DATA_SOURCE, sheet_name="Escalada")


def get_yearly_data(year: int) -> pd.DataFrame:
    return climbing_data[climbing_data["Fecha"].dt.year == year]


def get_last_year_data() -> pd.DataFrame:
    pass  # todo


def get_climbing_years() -> Set[int]:
    dates = climbing_data["Fecha"]
    if len(dates) > 0:
        return set(dates.dt.year)
    return set()


def get_climbing_days_in_year(year: int) -> int:
    dates = climbing_data["Fecha"]
    if len(dates) == 0:
        return 0
    return len(set(climbing_data[dates.dt.year == year]["Fecha"]))


def get_climbing_days_in_month(year: int, month: int) -> int:
    dates = climbing_data["Fecha"]
    if len(dates) == 0:
        return 0
    return len(
        set(climbing_data[(dates.dt.year == year) & (dates.dt.month == month)]["Fecha"])
    )


def get_days_per_crag() -> Dict[str, int]:
    data = climbing_data[["Fecha", "Lugar"]]
    data = data.drop_duplicates()

    return data.groupby(["Lugar"]).count()["Fecha"].to_dict()


def get_days_per_crag_year(year: int):
    data = get_yearly_data(year)
    data = data[["Fecha", "Lugar"]]
    data = data.drop_duplicates()

    return data.groupby(["Lugar"]).count()["Fecha"].to_dict()


def get_zone_days_data(year: Optional[int | str]) -> pd.DataFrame:
    data = climbing_data[["Fecha", "Lugar", "Sector"]]
    if not year:
        return data
    elif isinstance(year, int):
        return data[data["Fecha"].dt.year == year]
    elif year == 'last':
        raise NotImplementedError


def get_days_by_zone(data: pd.DataFrame, zone: Zone):
    common_columns = ["Lugar"] if zone == Zone.crag else ["Lugar", "Sector"]
    data = data[["Fecha"] + common_columns]
    data = data.drop_duplicates()

    return data.groupby(common_columns).count()["Fecha"].to_dict()
