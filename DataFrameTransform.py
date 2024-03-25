import numpy as np


class DataFrameTransform:
    def __init__(self, df):
        self.df = df
    
    def logtransform(self, column):
        log = self.df[column].map(lambda i: np.log(i) if i > 0 else 0)
        return (log)