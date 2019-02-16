import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.random.normal(loc=0,scale=1,size=100)
plt.plot(sorted(x), np.sin(sorted(x)),'b-')

def area_volume_of_cube(sideLength):
    a = sideLength
    b = sideLength * 2
    return a,b

astr = "Bob"
astr2 = 1.5
try:
    print ("helo")
    istr = int(astr2)
    print("There")
except:
    istr = -1
istr = int(astr)
print('Done',istr)

def my_functoin(radius):
    pi = 3.1415926
    area = radius ** 2 * pi
    circle = radius * 2 * pi
    return area, circle

my_f = lambda x :( x ** 2 * np.pi , x * 2 * np.pi )

map(lambda x:x+1,[1,2,3,4])

list(map(lambda x: '.' if not isinstance(x,int) else (0 if x > 4 else 1),['a',1,6]))

pd.read_json()

df = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")

df_famale = df[df['sex']=='Female']
df_famale.sort_values(by=['discipline','service'],ascending=[False,True])

flights = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/flights.csv")

df = pd.DataFrame([[np.nan,2,np.nan,0],[3,4,np.nan,1],[np.nan,np.nan,np.nan,3]],columns = list('ABCD'))

flights.dropna(0,how='any',subset=['hour','minute'])

flights[['dep_delay','arr_delay']].agg(['min','mean','max'])

values = df.mean()
type(values)
df.fillna(value = values)

df1 = pd.DataFrame({
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']
})

df2 = pd.DataFrame({
    'A':['A4','A5','A6','A7'],
    'B':['B4','B5','B6','B7'],
    'C':['C4','C5','C6','C7'],
    'D':['D4','D5','D6','D7']
})

df3 = pd.DataFrame({
    'A':['A8','A9','A10','A11'],
    'B':['B8','B9','B10','B11'],
    'C':['C8','C9','C10','C11'],
    'D':['D8','D9','D10','D11']
})

pd.concat([df1,df2,df3])

def fun_genDataframe(n):
    dfs = []
    for i in range(n):
        num_list = list(range(i*4,i*4+4))
        df = pd.DataFrame({
            'A':['A' + str(num) for num in num_list],
            'B':['B' + str(num) for num in num_list],
            'C':['C' + str(num) for num in num_list],
            'D':['D' + str(num) for num in num_list]
        },index=num_list)
        dfs.append(df)
        globals()['df'+str(i+1)]=df
    return dfs

def fun_concat(dfs,method):
    if method == 1:
        return pd.concat(dfs)
    elif method == 2:
        for i in range(dfs.__len__()):
            if i == 0:
                result = dfs[i]
            else:
                result = result.append(dfs[i])
        return result
    elif method == 3:
        for i in range(dfs.__len__()):
            if i == 0:
                result = dfs[i].T
            else:
                for j in range(4):
                    result.insert(result.columns.__len__(), dfs[i].T.columns[j], dfs[i].T.iloc[:, j])
        return result.T
    elif method == 4:
        result = pd.DataFrame(np.hstack([df.T.values for df in dfs]), columns=list(range(len(dfs) * 4)),
                              index=list('ABCD'))
        return result.T
    elif method == 5:
        result = pd.DataFrame(np.vstack([df.values for df in dfs]), index=list(range(len(dfs) * 4)),
                              columns=list('ABCD'))
        return result
    else:
        for i in range(dfs.__len__()):
            if i == 0:
                result = dfs[i].T
            else:
                result = pd.DataFrame(np.c_[result.values,dfs[i].T.values], columns=list(range((i+1) * 4)),
                                      index=list('ABCD'))
        return result.T

def fun_main(n,method,output=True):
    dfs = fun_genDataframe(n)
    df_result = fun_concat(dfs,method)
    if output:
        df_result.to_csv('df_result.csv')
    return df_result

left = pd.DataFrame({'key':['K0','K1','K2'],
                     'A':[1,2,3],
                     'B':[4,5,6]})

right = pd.DataFrame({'key':['K0','K1','K2'],
                     'C':[6,6,6],
                     'D':[8,8,8]})

pd.merge(left,right,on='key')

df1.combine_first(df2)

pd.merge_asof(df1,df2)

import numpy as np
def fun_d(S,K,r,sigma,t):
    return ((np.log(S/K)+(r+0.5*sigma**2)*t)/(sigma*np.sqrt(t)),(np.log(S/K)+(r-0.5*sigma**2)*t)/(sigma*np.sqrt(t)))

fun_d(61,55,0.05,0.2,0.5)

