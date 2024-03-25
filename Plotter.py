import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import missingno as msno
from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot


class Plotter:
    def __init__(self, df):
        self.df = df
        
    def histogram(self, column, bins):
        plt.hist(self.df[column], bins=bins)
        return plt.show
    
    def missing_data(self, nulls):
        nulls = msno.matrix(self.df)
        return nulls
    
    def qqplot(self, column):
        qqplot(self.df[column] , scale=1 ,line='q', fit=True)
        return pyplot.show()
    
    def boxplot(self, column):
        plt.figure(figsize=(10, 5))
        plt.boxplot(self.df[column])
        return plt.show()