import pandas as pd

df=pd.DataFrame(
        {   'info':["a","b","c","d"],
            'year':[10,20,30,40],
            'pop':[1.2,1.5,1.7,1.8]
            }
        )
df.describe()
graph =  df.plot(x='year', y='pop') 
print(dir(graph))  
print(df)
