import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

def orderBy(lis):
    sh = dict()
    for fe in lis:
        if 'LOCATION'not in fe:
            continue

        keys = fe['LOCATION'].title()
        #some event are place to many room
        for key in keys.split(","):    
            # il ny a pas de check sur les evenement sur plusieur jour 
            if key in sh:
                sh[key] = fe['DTEND'].dt.hour-fe['DTSTART'].dt.hour + sh[key]
            else:
                sh[key] = fe['DTEND'].dt.hour-fe['DTSTART'].dt.hour

    print(sh)
    obj = pd.DataFrame(
            {
                "piece":list(sh.keys()),
                "nbDecours":list(sh.values())
            })
    return obj.sort('nbDecours')

def onlyRoom(bb , roomsToRemove):
    roomList = roomsToRemove.split(',');
    return bb.query('piece  in @roomList')


def removeRoom(bb , roomsToRemove):
    roomList = roomsToRemove.split(',');
    return bb.query('piece not in @roomList')


def conditionRoom(bb,exprre):
    bb['test'] = bb.piece.str.match(exprre)
    return bb.query('test == True')

def render(df):
    df.plot(kind='bar');
    plt.ylabel('heure')
    plt.xlabel('piece')
    plt.title('Ocupation des pieces')
    plt.xticks(range(0,len(df.piece)), df.piece,rotation='vertical') 
    plt.show()

