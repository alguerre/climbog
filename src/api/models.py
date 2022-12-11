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


class Grades(enum.Enum):
    fourth_minus = 'IV-'
    fourth = 'IV'
    fourth_plus = 'IV+'
    fifth_minus = 'V-'
    fifth = 'V'
    fifth_plus = 'V+'
    six_a = '6a'
    six_b = '6b'
    six_c = '6c'
    seven_a = '7a'
    seven_b = '7b'
    seven_c = '7c'
    eight_a = '7a'
    eight_b = '8b'
    eight_c = '8c'
    six_a_plus = '6a+'
    six_b_plus = '6b+'
    six_c_plus = '6c+'
    seven_a_plus = '7a+'
    seven_b_plus = '7b+'
    seven_c_plus = '7c+'
    eight_a_plus = '8a+'
    eight_b_plus = '8b+'
    eight_c_plus = '8c+'


class SportRoute(db.Model):
    __tablename__ = 'sport_routes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    crag = db.Column(db.String(32), nullable=False)
    sector = db.Column(db.String(32))
    name = db.Column(db.String(32), nullable=False)
    date = db.Column(db.Date, nullable=False)
    grade = db.Column(db.Enum(Grades))
    perception = db.Column(db.Enum(Grades))
    tries = db.Column(db.Enum(Tries))
    quality = db.Column(db.SmallInteger)
    comment = db.Column(db.Text())

    def __repr__(self):
        return f'<SportRoute {self.crag} -' \
               f'{self.sector} - '\
               f'{self.route_name} - '\
               f'{self.grade} - ' \
               f'{self.date:%Y-%m-%d}>'
