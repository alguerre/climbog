from calendar import month_name

from flask import Flask
from flask import make_response
from werkzeug.exceptions import NotImplemented
import api.service as service

app = Flask(__name__)
service.load_data()


@app.route("/")
def index():
    return "<h1>Hello World!</h1>"


@app.route("/climb/days/<int:year>")
def climbing_days_per_year(year: int):
    climbing_days = service.get_climbing_days_per_year(year)

    output = [f'<h2>Climbing days of {year}</h2><br>']
    output += [
        f"Climbing days in {month_name[m]}: {climbing_days[m]}<br>"
        for m in climbing_days
    ]

    return make_response("".join(output))


@app.route("/climb/days/")
def climbing_days_total():
    climbing_days = service.get_climbing_days()

    output = [
        f"Climbing days in {year}: {days}<br>" for year, days in climbing_days.items()
    ]
    return make_response("".join(output))


@app.route("/climb/days/crag")
def climbing_days_per_crag():
    output = ["<h2>Overall crag summary</h2>"]
    output += [
        f"Climbing days in {crag}: {days}<br>"
        for crag, days in service.get_climbing_days_per_crag().items()
    ]
    return make_response("".join(output))


@app.route("/climb/days/crag/<int:year>")
def climbing_days_per_crag_year(year: int):
    output = [f"<h2>Crag summary {year}</h2>"]
    output += [
        f"Climbing days in {crag}: {days}<br>"
        for crag, days in service.get_days_per_crag_year(year).items()
    ]
    return make_response("".join(output))


@app.route("/climb/days/crag/last")
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
