import pandas as pd

class DataFrameInfo:
    def column_description(self, df):
        return df.info()

    def describe_data(self, df):
        return df.describe()

    def distinct_values(self, df):
        return df.value_counts()

    def print_shape(self, df):
        shape = df.shape
        return print(shape)

    def percent_missing(self, df):
        return df.isnull().sum() * 100 / len(df)