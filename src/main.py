
import icalendar 

class DateDataForm:
    resourceToGet = 0;
    username="lecteur1"
    password=""
    online=False
    areDownload=False
    areParse=False
    icsFileName = "data/cal.ics"
    optdict = None 
    
    def getICS():
        if(self.online == False ):
            return 

        #ton code


        return

    def parseICS(self):
        if(self.online == True and self.areDownload == False):
            self.getICS()

        icsFile = open(self.icsFileName)
        self.optdict = icalendar.Calendar.from_ical(icsFile.read())
            
        icsFile.close()

        return

    def getDict(self, *lis):

        returnlist = list()
        #if the file are not parse and load
        if(self.areParse == False):
            self.parseICS()
    
        
        for oneRDV in self.optdict.walk():
            data = dict(oneRDV)

        #if no name are pass in list 
            if not lis:
                returnlist.append(data)

            else:
                #the new dict to add 
                oneElement = dict()
                for nameOfParam in lis:
                    if nameOfParam in  data.keys():    
                        #TODO export all data in nice form
                        oneElement[nameOfParam] = oneRDV[nameOfParam]
                    else:
                        print (nameOfParam +"n'est pas valide ")
                
                returnlist.append(oneElement);

        return returnlist;
             

lap = DateDataForm();
print(lap.getDict('LOCATION','DESCRIPTION','DATE'))

