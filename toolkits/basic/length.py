import logging
import pandas as pd
from kywy.client.kawa_decorators import outputs, inputs

logger = logging.getLogger('script-logger')


@inputs(text=str)
@outputs(length1=int, length2=int, length3=int)
def execute(df: pd.DataFrame):
    logger.info('Starting the execution')
    
    df['length1'] = df.apply(lambda row: 9 * len(row['text']), axis=1)
    df['lenght2'] = df.apply(lambda row: 2 * len(row['text']), axis=1)
    df['length3'] = df.apply(lambda row: 3 * len(row['text']), axis=1)
    
    return df
