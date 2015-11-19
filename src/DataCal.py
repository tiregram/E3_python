import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

class DataCal(pd.DataFrame):
    
    def BuilderDataCal(lis):
        sh = dict()
        for fe in lis:
            if 'LOCATION'not in fe:
                continue

            keys = fe['LOCATION'].title()
            #some event are place to many room
            for key in keys.split(","):    
                #TODO il ny a pas de check sur les evenement sur plusieur jour 
                if key in sh:
                    sh[key] = fe['DTEND'].dt.hour-fe['DTSTART'].dt.hour + sh[key]
                else:
                    sh[key] = fe['DTEND'].dt.hour-fe['DTSTART'].dt.hour

        retDataFrame = DataCal(
            {
                "piece":list(sh.keys()),
                "HD":list(sh.values())
            })

        retDataFrame = DataCal(retDataFrame.sort_values('HD'))
        
        return retDataFrame

    def onlyRoom(self,  roomsToRemove):
        roomList = roomsToRemove.split(',');
        return DataCal(self.query('piece  in @roomList'))


    def removeRoom(self , roomsToRemove):
        roomList = roomsToRemove.split(',');
        return self.query('piece not in @roomList')


    def conditionRoom(self,exprre):
        self['test'] = self.piece.str.match(exprre)
        return DataCal(self.query('test == True'))
        #TODO remove test colums
        
    def render(self):
        self.plot(kind='bar');
        plt.ylabel('heure')
        plt.xlabel('piece')
        plt.title('Ocupation des pieces')
        plt.xticks(range(0,len(self.piece)), self.piece ,rotation='vertical') 
        plt.show()

