import pandas as pd
data=pd.DataFrame({'paris':[15,25,36],
                   'landon':[28,24,63],
                   'newyork':[45,25,32]})
print(data)
print(data.melt())

