import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline



lr = LinearRegression()

#[hot, crazy, caring, stupid]

X = [[3,8,2,5,0],[2,4,8,2,1],[6,2,2,6,1],[7,8,3,3,1],[4,5,6,8,0],[5,8,2,9,0],[4,9,8,3,1],[8,7,5,9,1],[9,6,2,7,0],[8,2,8,4,1]]
L = ['hot','crazy','caring','stupid','datable']

#X = [L]+X
#print(X)

#inps = np.array(X)

#print(inps.shape)


df = pd.DataFrame(columns = L, data = X)

print(df)
 
A = df[['hot','crazy','caring','stupid']]
print(A)
B = df['datable']

# lr = lr.fit(A, B)

# results = lr.predict([[9,6,2,8]])

# res = lr.predict(A)

Input = [('scale' , StandardScaler()),('polynomial', PolynomialFeatures(degree  =2)), ('mode', LinearRegression())]
Pipe = Pipeline(Input)

Pipe.fit(A ,B)

res = Pipe.predict(A)
print(res)

s  = Pipe.score(A,B) 
print(s)
# if(results>0.5):
#     print("date : "+ str(results))
# else:
#     print("don't date : "+ str(results))

ax1 = sns.distplot(df['datable'], hist = False, color="r", label ="actual")
sns.distplot(res, hist = False, color = "b" , label ="predicted", ax = ax1)               
plt.show(sns)


f = np.polyfit(df['hot'],res,2)

p = np.poly1d(f)

print(p)