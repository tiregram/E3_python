import pandas as pd
import matplotlib.pyplot as plt



def orderBy(lis):
    sh = dict()
    for fe in lis:
        if 'LOCATION'not in fe:
            continue

        key = fe['LOCATION'].title()
        print(key)
        if key in sh:
           sh[key] = 1 + sh[key]
        else:
           sh[key] = 1

    print(sh)
    return pd.DataFrame(
            {
                "piece":list(sh.keys()),
                "nbDecours":list(sh.values())
            })

def render(df):
    df.plot(kind='bar');
    plt.show()
