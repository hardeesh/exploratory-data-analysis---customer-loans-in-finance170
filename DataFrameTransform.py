import numpy as np
import pandas as pd


class DataFrameTransform:
    def __init__(self, df):
        self.df = df

    def logtransform(self, target_df : pd.DataFrame, column : str):
        log = target_df[[column]].map(lambda i: np.log(i) if i > 0 else 0)
        return log
    
    