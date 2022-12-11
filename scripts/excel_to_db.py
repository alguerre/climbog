from src.api.paths import DATA_SOURCE, DB_PATH
import pandas as pd
from sqlalchemy import create_engine

climbing_data = pd.read_excel(DATA_SOURCE, sheet_name='climbing')
climbing_data['tries'] = climbing_data['tries'].replace(
    {'Vista': 'on_sight',
     'Flash': 'flash',
     'Segundo': 'second',
     'Tercero': 'third',
     'Proyecto': 'project',
     'No encadeno': 'not_sent',
     'Repetición': 'repetition',
     'Top Rope': 'top_rope'}
)

engine = create_engine(f'sqlite:///{DB_PATH}', echo=False)

climbing_data.to_sql('sport_routes',
                     con=engine,
                     if_exists='append',
                     index_label='id')
