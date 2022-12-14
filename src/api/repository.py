from collections import Counter
from typing import List, Dict

from sqlalchemy import extract, func
from sqlalchemy.engine.row import Row
from sqlalchemy.orm import aliased

from extensions import db
from models import SportRoute


def get_climbing_days_per_year() -> List[Row]:
    dates_sbq = db.session.query(SportRoute.date).distinct().subquery()
    dates_alias = aliased(SportRoute, dates_sbq)
    q = db.session.query(extract('year', dates_alias.date), func.count()).group_by(
        extract('year', dates_alias.date))
    return q.all()


def get_routes_per_year() -> List[Row]:
    return (
        db.session.query(SportRoute.date, func.count(extract("year", SportRoute.date)))
        .group_by(extract("year", SportRoute.date))
        .all()
    )


def get_climbing_days_in_month(year: int, month: int) -> int:
    return (
        db.session.query(SportRoute.date)
        .distinct()
        .filter(
            (extract("year", SportRoute.date) == year)
            & (extract("month", SportRoute.date) == month)
        )
        .count()
    )


def get_days_per_crag(year: int) -> List[Row]:
    crag_summary_sbq = (
        db.session.query(func.distinct(SportRoute.date), SportRoute.crag)
        .filter(extract("year", SportRoute.date) == year)
        .subquery()
    )
    sbq = aliased(SportRoute, crag_summary_sbq)

    return (
        db.session.query(sbq.crag, func.count())
        .group_by(
            sbq.crag,
        )
        .all()
    )


def get_days_per_sector(year: int):
    sector_summary_sbq = (
        db.session.query(
            func.distinct(SportRoute.date), SportRoute.crag, SportRoute.sector
        )
        .filter(extract("year", SportRoute.date) == year)
        .subquery()
    )
    sbq = aliased(SportRoute, sector_summary_sbq)

    return (
        db.session.query(sbq.crag, sbq.sector, func.count())
        .group_by(sbq.crag, sbq.sector)
        .all()
    )
