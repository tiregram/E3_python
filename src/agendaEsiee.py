import pandas as pd
import matplotlib.pyplot as plt



def orderBy(lis):
    sh = dict()
    for fe in lis:
        if 'LOCATION'not in fe:
            continue

        keys = fe['LOCATION'].title()
        print(keys)
        #some event are place to many room
        for key in keys.split(","):    
            if key in sh:
                sh[key] = 1 + sh[key]
            else:
                sh[key] = 1

    print(sh)
    obj = pd.DataFrame(
            {
                "piece":list(sh.keys()),
                "nbDecours":list(sh.values())
            })
    return obj.sort('nbDecours')

def render(df):
    df.plot(kind='bar');
    plt.ylabel('heure')
    plt.xlabel('piece')
    plt.title('Ocupation des pieces')
    plt.xticks(range(0,len(df.piece)), df.piece,rotation='vertical') 
    plt.show()
