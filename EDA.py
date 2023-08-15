import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class EDA_Tool:
    def __init__(self, data):
        self.data = data

    def plot_histogram(self, column):
        plt.figure(figsize=(8, 6))
        sns.histplot(self.data[column], kde=True)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

# Example usage
data = pd.read_csv('your_data.csv')
eda_tool = EDA_Tool(data)
eda_tool.plot_histogram('numeric_column_name')
