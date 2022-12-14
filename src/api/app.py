from calendar import month_name

from flask import Flask
from flask import make_response
from werkzeug.exceptions import NotImplemented
import service as service
from paths import DB_PATH
from extensions import db, migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
db.init_app(app)
migrate.init_app(app, db)


@app.route("/")
def index():
    return "<h1>Hello World!</h1>"


@app.route("/climb/days/")
def climbing_days():
    days_per_year = service.get_climbing_days_per_year()

    output = [
        f"Climbing days in {year}: {days}<br>" for year, days in days_per_year.items()
    ]
    return make_response("".join(output))


@app.route("/climb/days/<int:year>")
def climbing_days_per_year(year: int):
    days_per_month = service.get_climbing_days_per_month(year)

    output = [f'<h2>Climbing days of {year}</h2><br>']
    output += [
        f"Climbing days in {month_name[m]}: {days_per_month[m]}<br>"
        for m in days_per_month
    ]

    return make_response("".join(output))


@app.route("/climb/days/crag")
def climbing_days_per_crag_overall():
    raise NotImplementedError
    output = ["<h2>Overall crag summary</h2>"]
    output += [
        f"Climbing days in {crag}: {days}<br>"
        for crag, days in service.get_climbing_days_per_crag().items()
    ]
    return make_response("".join(output))


@app.route("/climb/days/crag/<int:year>")
def climbing_days_per_crag(year: int):
    output = [f"<h2>Crag summary {year}</h2>"]
    output += [
        f"Climbing days in {crag}: {days}<br>"
        for crag, days in service.get_climbing_days_per_crag(year).items()
    ]
    return make_response("".join(output))


@app.route("/climb/days/crag/last")
def climbing_days_per_crag_last_year():
    NotImplemented("Not implemented yet")


@app.route("/climb/days/sector")
def climbing_days_per_sector_overall():
    NotImplemented("Not implemented yet")


@app.route("/climb/days/sector/<int:year>")
def climbing_days_per_sector(year: int):
    output = [f"<h2>Crag summary {year}</h2>"]
    output += [
        f"Climbing days in {crag} - {sector}: {days}<br>"
        for crag, data in service.get_climbing_days_per_sector(year).items()
        for sector, days in data.items()
    ]
    return make_response("".join(output))


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
