from os import path

API_DIR = path.dirname(__file__)
SRC_DIR = path.dirname(API_DIR)
ROOT_DIR = path.dirname(SRC_DIR)

DATA_DIR = path.join(ROOT_DIR, 'data')
DATA_SOURCE = path.join(DATA_DIR, 'climbing_log.xlsx')
DB_PATH = path.join(DATA_DIR, 'climbog.db')
