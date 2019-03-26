import numpy as np
import pandas as pd

data = pd.read_csv('ML CODES/DataSets/zoo.csv', delimiter=',')
X=data.iloc[:,0:17].values
Y=data.iloc[:,17].values
df = pd.DataFrame(X)

def findS(df,Y,key):
    col = len(list(df))
    row = np.size(df[0])
    
    temp=0
    hypothesis = ['0']*col
    
    for temp in range(row):
       if key==Y[temp]:
           hypothesis = df.iloc[temp,:].values.tolist()
           break
    
    for i in range(temp+1,row):
        if key==Y[i]:
            for j in range(col):
                if not df.iloc[i][j]==hypothesis[j]:
                    hypothesis[j]='?'
                    
    print(hypothesis)
    
findS(df,Y,1)
findS(df,Y,2)
findS(df,Y,3)
findS(df,Y,4)
findS(df,Y,5)
findS(df,Y,6)
findS(df,Y,7)
