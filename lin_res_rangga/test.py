import pandas as pd
from sklearn import linear_model 
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('data2.csv', delimiter=";")
features = ['harian','uts','uas','keterampilan']
for x in features:
    df[x] = pd.to_numeric(df[x], downcast="float")
x = df[features]
y = df['grade']
regr = linear_model.LinearRegression()
regr.fit(x,y)
print(regr.predict([[88,88,88,88]]))

# data_copy = x
# data_copy = pd.get_dummies(data_copy)
# data_copy = data_copy.fillna(0)
# print(data_copy.columns.values)
# fig, axes = plt.subplots(1,len(data_copy.columns.values),sharey=True,constrained_layout=True,figsize=(30,15))

# for i,e in enumerate(data_copy.columns):
#     regr.fit(data_copy[e].values[:,np.newaxis], y.values)
#     axes[i].set_title("Best fit line")
#     axes[i].set_xlabel(str(e))
#     axes[i].set_ylabel('Grade')
#     axes[i].scatter(data_copy[e].values[:,np.newaxis], y,color='g')
#     axes[i].plot(data_copy[e].values[:,np.newaxis], 
#     regr.predict(data_copy[e].values[:,np.newaxis]),color='k')
# plt.show()