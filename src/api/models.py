from extensions import db
import enum


class AutoName(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class Tries(AutoName):
    on_sight = enum.auto()
    flash = enum.auto()
    second = enum.auto()
    third = enum.auto()
    project = enum.auto()
    not_sent = enum.auto()
    repetition = enum.auto()
    top_rope = enum.auto()


class SportRoute(db.Model):
    __tablename__ = 'sport_routes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    crag = db.Column(db.String(32), nullable=False)
    sector = db.Column(db.String(32))
    name = db.Column(db.String(32), nullable=False)
    date = db.Column(db.Date, nullable=False)
    grade = db.Column(db.String(3))
    perception = db.Column(db.String(3))
    tries = db.Column(db.Enum(Tries))
    quality = db.Column(db.SmallInteger)
    comment = db.Column(db.Text())

    def __repr__(self):
        return f'<SportRoute {self.crag} -' \
               f'{self.sector} - '\
               f'{self.name} - '\
               f'{self.grade} - ' \
               f'{self.date:%Y-%m-%d}>'
