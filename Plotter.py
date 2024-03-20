import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, df):
        self.df = df
        
    def histogram(self, column, bins):
        plt.hist(self.df[column], bins=bins)
        return plt.show
    
