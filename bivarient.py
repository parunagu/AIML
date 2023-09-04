import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("C:/Users/SPTINT-08/Desktop/iris/titanic.csv")
data
data.head(10)
sns.scatterplot(x=data['Age'],y=data['Fare'])
sns.countplot(x='Sex',hue='Survived',data=data)
sns.countplot(x='Pclass',hue='Survived',data=data)
sns.countplot(x='Pclass',hue='Sex',data=data)
sns.countplot(x='Embarked',hue='Survived',data=data)
sns.countplot(x='Embarked',hue='Pclass',data=data)

