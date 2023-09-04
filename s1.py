# univanient
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("C:/Users/SPTINT-08/Desktop/iris/titanic.csv")
data

data.head(10)
data.info()
data.shape
data.describe
data['Age'].hist

sns.countplot(x='Pclass',data=data)
data['Pclass'].value_counts()

sns.boxplot(x='Age',data=data)
data['Sex'].plot(kind='bar')

sns.countplot(x='Sex',data=data)
data['Age'].value_counts().plot(kind='bar')


