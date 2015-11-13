import pandas as pd

df=pd.DataFrame(
        {   'info':["a","b","c","d"],
            'year':[10,20,30,40],
            'pop':[1.2,1.5,1.7,1.8]
            }
        )

print(df.plot(x='year', y='pop'))
