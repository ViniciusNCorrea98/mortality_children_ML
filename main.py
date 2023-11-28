import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

nRowsRead = 1000

dataset = pd.read_csv('./deaths.csv', delimiter=';', encoding = "ISO-8859-1", nrows = nRowsRead)

print(dataset.head())


dataset.dataframeName = 'deaths.csv'
nRow, nCol = dataset.shape
print(f'There are {nRow} rows and {nCol} columns')

categorical_columns = [cname for cname in dataset.columns
                       if dataset[cname].nunique() < 10
                       and dataset[cname].dtype == 'object']

numerical_columns = [cname for cname in dataset.columns if
                     dataset[cname].dtype in ['int64', 'float64']]

print(categorical_columns)
print(numerical_columns)

for coluna in dataset.columns:
        print(coluna)

sns.set(rc={'figure.figsize': (19.7, 8.27)})

sns.heatmap(dataset.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.show()

#Unnecessary fields
drops_columns = ['Unnamed: 1', 'Unnamed: 2']

dataset.drop(drops_columns, inplace=True, axis=1)
dataset.dropna(inplace=True)


print(dataset['region'])

sns.displot(dataset['lower'], kde=True)
plt.show()

sns.scatterplot(x='lower', y='median.1', data=dataset)
plt.show()
