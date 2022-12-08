from calendar import month_name
from typing import Dict, Set

import pandas as pd
from flask import Flask
from werkzeug.exceptions import NotImplemented

from api.paths import DATA_SOURCE

app = Flask(__name__)


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
    if len(dates):
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


@app.route("/")
def index():
    return "<h1>Hello World!</h1>"


@app.route("/climb/days/<int:year>")
def climbing_days_per_year(year: int):
    climbing_days = {
        month: get_climbing_days_in_month(year, month) for month in range(1, 13)
    }

    output = [
        f"Climbing days in {month_name[m]}: {climbing_days[m]}<br>"
        for m in climbing_days
    ]

    return "".join(output)


@app.route("/climb/days/")
def climbing_days_total():
    years = get_climbing_years()
    climbing_days = {y: get_climbing_days_in_year(y) for y in years}

    output = [
        f"Climbing days in {year}: {days}<br>" for year, days in climbing_days.items()
    ]
    return "".join(output)


@app.route("/climb/days/crag")
def climbing_days_per_crag():
    output = ["<h2>Overall crag summary</h2>"]
    output += [
        f"Climbing days in {crag}: {days}<br>"
        for crag, days in get_days_per_crag().items()
    ]
    return "".join(output)


@app.route("/climb/days/crag/<int:year>")
def climbing_days_per_crag_year(year: int):
    output = [f"<h2>Crag summary {year}</h2>"]
    output += [
        f"Climbing days in {crag}: {days}<br>"
        for crag, days in get_days_per_crag_year(year).items()
    ]
    return "".join(output)


@app.route("/climb/days/crag/last_year")
def climbing_days_per_crag_last_year():
    NotImplemented("Not implemented yet")


@app.route("/climb/days/sector")
def climbing_days_per_sector():
    NotImplemented("Not implemented yet")


@app.route("/climb/days/sector/<int:year>")
def climbing_days_per_sector_year(year: int):
    NotImplemented("Not implemented yet")


@app.route("/climb/grade/hist")
def grade_histogram():
    NotImplemented("Not implemented yet")


@app.route("/climb/grade/<int:year>/hist/")  # todo: puede el 'hist' ser una estrategia?
def grade_histogram_per_year(year: int):
    NotImplemented("Not implemented yet")


@app.route("/climb/grade/last/hist")
def grade_histogram_last_year():
    NotImplemented("Not implemented yet")


@app.route("/climb/grade/crag/hist/")
def grade_histogram_per_crag():
    NotImplemented("Not implemented yet")


if __name__ == "__main__":
    app.run()
