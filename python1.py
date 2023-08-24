import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("C:/Users/SPTINT-08/Desktop/iris/tips1.csv")
print(data)

plt.scatter(data['day'],data['tip'])
plt.xlable('day')
plt.ylabel('tip')
plt.title("sactter plot")
data['day'].value_counts()
plt.show()

#line chart
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("C:/Users/SPTINT-08/Desktop/iris/tips1.csv")
print(data)

plt.xlabel("days")
plt.ylabel("tip" "size")

plt.plot(data['tip'])
plt.plot(data['size'])
plt.show()

#bar chart
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("C:/Users/SPTINT-08/Desktop/iris/tips1.csv")
print(data)

print(data['days'].value_counts())

plt.bar(data['day'],data['tip'])
plt.xlabel('days')
plt.ylabel('tip')
plt.show()

#histgrom
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("C:/Users/SPTINT-08/Desktop/iris/tips1.csv")
print(data)
plt.hist(data['total_bill'])

print(data['total_bill'].max())
