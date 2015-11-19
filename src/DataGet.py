import pycurl 
import icalendar 
from datetime import date 

class DateDataForm:
    resourceToGet = 0;
    username="lecteur1"
    password=""
    dateStart   =None
    dateEnd     = None 
    online=False
    areDownload=False
    areParse=False
    icsFileName = "data/cal.ics"
    optdict = None 

    def getDateToUrl(self):
        ret = "startDay="+str(self.dateStart.day)
        ret+= "&startMonth="+str(self.dateStart.month)
        ret+= "&startYear="+str(self.dateStart.year)
        ret+= "&endDay="+str(self.dateEnd.day)
        ret+= "&endMonth="+str(self.dateEnd.month)
        ret+= "&endYear="+str(self.dateEnd.year)

        return ret
        
    
    def getICS(self):
        if(self.online == False ):
            return 



        rooms="3474,682,683,684,685,772,2112,2841,719,2556,2842,183,185,196,4051,4679,749,737,154,713,700,1057,724,1858,705,2281,1908,758,707,708,759,712,714,2090,2108,725,726,701,715,716,163,167,2276,2272,2072,2074,2089,428,2274,2279,2265,717,720,721,722,745,704,746,747,748,3286,2781,2782,2117,728,2282,2270,2277,2278,2275,789,790,786,787,788,1852,780,4350,740,782,2584,742,741,731,732,734,736,735,674,998,727,733,680,659,665,2555,1295,5215,681,785,2743,5321,744,739,743,738,773,4937,775,776,147,3132,2907,2909,2911,2908,3134,2353,2844,2910,1135,2899,2912,2904,2905,2902,3129,2913,2898,2901,2007,3135,2903,1892,68,2273,2261,2703,2262,833,752,777,767,2031,779,1987,300,1861,1439,1357,2354,2573,90,686,1727,1578,65,590,1579,778"
 
        c = pycurl.Curl()
        c.setopt(pycurl.COOKIEJAR,  'data/cookie.txt')
        c.setopt(pycurl.COOKIEFILE, 'data/cookie.txt')


        c.setopt(c.URL, "https://planif.esiee.fr:8443/jsp/custom/modules/plannings/direct_planning.jsp?projectId=0"+
        "&login=" +self.username+
        "&password="+self.password+
        "&resources="+rooms)
        c.perform()

        c.setopt(c.URL, "https://planif.esiee.fr:8443/jsp/custom/modules/plannings/icalDates.jsp")
        c.perform()

        with open('data/output.ics', 'wb') as f:
                #c.setopt(c.URL,'https://www.google.fr')
                c.setopt(c.URL,"https://planif.esiee.fr:8443/jsp/custom/modules/plannings/ical.jsp?"+self.getDateToUrl()+"&ClientCal=palm")
                c.setopt(c.WRITEDATA,f)
                c.perform()
                f.close()
                c.close()

        self.icsFileName= "data/output.ics";



 
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
                        oneElement[nameOfParam] = oneRDV[nameOfParam]
                    else:
                        print (nameOfParam +"n'est pas valide ")
                
                    
                returnlist.append(oneElement);

        return returnlist;
             


