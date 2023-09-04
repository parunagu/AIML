#multivarient
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("C:/Users/SPTINT-08/Desktop/iris/titanic.csv")
data

data = np.random.randint(low=1,high=100,size=(10, 10))
  
# setting the parameter values
cmap = "tab20"
  
# plotting the heatmap
hm = sns.heatmap(data=data,cmap=cmap)
  
# displaying the plotted heatmap
plt.show()

