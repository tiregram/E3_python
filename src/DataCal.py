import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')


# class qui herite de DataFrame et permet de trier , filtré et  count le nombre d'heure
class DataCal(pd.DataFrame):
    
    #builder de dataCall avec la list des event
    def BuilderDataCal(lis):
        sh = dict()
        for fe in lis:
            #check si on a bien le lieux dans le dict
            if 'LOCATION'not in fe:
                continue
            
            keys = fe['LOCATION'].title()
            #some event are place to many room exemple 110,210 etc.. then split
            
            for key in keys.split(","):
                #TODO il ny a pas de check sur les evenement sur plusieur jour mais il sont rare
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

    
    #selectionne uniquement les rooms separé par des virgule
    def onlyRoom(self,  rooms):
        roomList = rooms.split(',');
        return DataCal(self.query('piece  in @roomList'))

#inverse de only room
    def removeRoom(self , roomsToRemove):
        roomList = roomsToRemove.split(',');
        return DataCal(self.query('piece not in @roomList'))

#utilise une expresion regu pour select des room 
    def conditionRoom(self,exprre):
        self['test'] = self.piece.str.match(exprre) 
        return  DataCal(self.query('test == True').drop('test',1))
    
#utilise une expresion pour remove des room a la selection
    def conditionRoomRemove(self,exprre):
        self['test'] =  self.piece.str.match(exprre)
        
        return  DataCal(self.query('test != True').drop('test',1))
         
#permet de faire le rendue      
    def render(self):
        moyeneetc = self.describe()
        self.mean()
        self.plot(kind='bar');
        plt.axhline(y=moyeneetc.HD["mean"], color='r')
        plt.axhline(moyeneetc.HD["25%"])
        plt.axhline(moyeneetc.HD["50%"])
        plt.axhline(moyeneetc.HD["75%"])
        plt.ylabel('heure')
        plt.xlabel('piece')
        plt.title('Ocupation des pieces')
        plt.xticks(range(0, len(self.piece)), self.piece , rotation='vertical') 
        plt.show()

