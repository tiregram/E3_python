import tkinter 
import re
import datetime
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

class Frame(tkinter.Tk):

    def __init__(self,parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        
        self.title("ESIEE Planif")

        ############################
        #     Main Panel           #
        ############################

        #Panel Labelisé
        self.mainPanel = tkinter.LabelFrame(self, text="Planif Dates", padx=5, pady=5, height=200, width=200)
        self.mainPanel.pack(side=tkinter.LEFT , padx=10, pady=10)

        
        tkinter.Label(self.mainPanel, text="Start Date : ").grid(row=1, column=1)

        #Date 1
        self.startDate = tkinter.Entry(self.mainPanel)
        self.startDate.insert(0,'01/09/2015')
        self.startDate.grid(row=2, column=1)

        tkinter.Label(self.mainPanel, text="Start Date : ").grid(row=3, column=1)

        #Date2
        self.endDate = tkinter.Entry(self.mainPanel)
        self.endDate.insert(0,'31/07/2016')
        self.endDate.grid(row=4, column=1)

        #Bouton "Générer"
        self.generateButton = tkinter.Button(self.mainPanel, text="Générer", command=self.generate)
        self.generateButton.grid(row=5, column=1, pady=25)

        #Label Affichage des Dates
        self.informationLabelString = tkinter.StringVar()
        self.informationLabel = tkinter.Label(self.mainPanel, textvariable=self.informationLabelString, text="Texte de Base")
        self.informationLabel.grid(row=6,column=1)


        ############################
        #     Option Panel         #
        ############################

        #Panel Labelisé 
        self.optionPanel = tkinter.LabelFrame(self, text="File Options", padx=5, pady=5 , height=200, width=200)
        self.optionPanel.pack(side=tkinter.LEFT, padx=10, pady=10)

        #CheckBox File Browser
        self.optionFile = tkinter.IntVar()
        self.checkbuttonFile = tkinter.Checkbutton(self.optionPanel, text="File Browser", variable=self.optionFile, command=self.isSelected)
        self.checkbuttonFile.grid(row=1, column=1, pady=10)

        #Bouton File Browser
        self.fileBrowserButton = tkinter.Button(self.optionPanel, text="File...", command=self.selectFile)
        self.fileBrowserButton.grid(row=2, column=1, pady=10)

        #Chemin du Fichier
        self.filePath = tkinter.StringVar()
        self.filePath.set("")
        self.pathLabel = tkinter.Label(self.optionPanel,text="",textvariable=self.filePath)
        self.pathLabel.grid(row=3, column=1, pady=10)


        ############################
        #     Advanced Panel       #
        ############################

        #Panel Labelisé
        self.advancedPanel = tkinter.LabelFrame(self, text="Advanced Panel", padx=5, pady=5 , height=200, width=200)
        self.advancedPanel.pack(side=tkinter.LEFT, padx=10, pady=10)

        #CheckBox Select
        self.uniqueSelect = tkinter.IntVar()
        self.uniqueSelectCheckButton = tkinter.Checkbutton(self.advancedPanel, text="Select Unique", variable=self.uniqueSelect, command=self.uniqueSelectCheck)
        self.uniqueSelectCheckButton.grid(row=1, column=1, pady=10)

        #CheckBox Select Group
        self.groupSelect = tkinter.IntVar()
        self.groupSelectButton = tkinter.Checkbutton(self.advancedPanel, text="Select Group", variable=self.groupSelect, command=self.groupSelectCheck)
        self.groupSelectButton.grid(row=2, column=1, pady=10)

        #CheckBox Delete
        self.uniqueDelete = tkinter.IntVar()
        self.uniqueDeleteButton = tkinter.Checkbutton(self.advancedPanel, text="Delete Unique", variable=self.uniqueDelete, command=self.uniqueDeleteCheck)
        self.uniqueDeleteButton.grid(row=3, column=1, pady=10)

        #CheckBox Delete Group
        self.groupDelete = tkinter.IntVar()
        self.groupDeleteCheckbutton = tkinter.Checkbutton(self.advancedPanel, text="Delete Group", variable=self.groupDelete, command=self.groupDeleteCheck)
        self.groupDeleteCheckbutton.grid(row=4, column=1, pady=10)

        #Entrée Select
        self.uniqueSelected = tkinter.Entry(self.advancedPanel)
        self.uniqueSelected.grid(row=1, column=2)

        #Entrée Group Select
        self.groupSelected = tkinter.Entry(self.advancedPanel)
        self.groupSelected.grid(row=2, column=2)

        #Entrée Delete
        self.uniqueDeleted = tkinter.Entry(self.advancedPanel)
        self.uniqueDeleted.grid(row=3, column=2)

        #Entrée Group Delete
        self.groupDeleted = tkinter.Entry(self.advancedPanel)
        self.groupDeleted.grid(row=4, column=2)

        #Désactive toutes les entrées
        self.uniqueSelected.configure(state='disabled')
        self.groupSelected.configure(state='disabled')
        self.uniqueDeleted.configure(state='disabled')
        self.groupDeleted.configure(state='disabled')

    #Gestion CheckBox Select 
    def uniqueSelectCheck(self):
        
        if(self.uniqueSelect.get() != 1):
            self.uniqueSelected.configure(state='disabled')
        else:
            self.uniqueSelected.configure(state='normal')

    #Gestion CheckBox Select Group
    def groupSelectCheck(self):
        
        if(self.groupSelect.get() != 1):
            self.groupSelected.configure(state='disabled')
        else:
            self.groupSelected.configure(state='normal')
            
    #Gestion CheckBox Delete
    def uniqueDeleteCheck(self):
        
        if(self.uniqueDelete.get() != 1):
            self.uniqueDeleted.configure(state='disabled')
        else:
            self.uniqueDeleted.configure(state='normal')
            
    #Gestion CheckBox Delete Group
    def groupDeleteCheck(self):
        
        if(self.groupDelete.get() != 1):
            self.groupDeleted.configure(state='disabled')
        else:
            self.groupDeleted.configure(state='normal')
            

    #Gestion File Browser
    def selectFile(self):

        if(self.optionFile.get()==1):

            fileName = askopenfilename(filetypes=(("ICS Files", "*.ics"),("All files", "*.*")))
            self.filePath.set(""+fileName)
        else:
            showerror("You can't", "The file browser is disable.")

    #Gestion CheckBox File Browser
    def isSelected(self):
    
        if(self.optionFile.get() ==1):
            a=""
        else:

            self.filePath.set("")


	#Gestion Bouton "Générer"
    def generate(self):

        #Récupération des Champs Dates
        startDateToMatch = self.startDate.get()
        endDateToMatch = self.endDate.get()
        #Regex des valeurs
        startDateMatch=re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', startDateToMatch)
        endDateMatch=re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', endDateToMatch)

        startDateMessage = ""
        endDateMessage = ""


        if( startDateMatch): 
            try: 
                startDateSplit = startDateToMatch.split('/')
                self.date1 = datetime.date(int(startDateSplit[2]), int(startDateSplit[1]), int(startDateSplit[0]))     
                
            except ValueError as detail:
                startDateMessage = str(detail)
                startDateMatch = None

        if(endDateMatch):
            try: 
                endDateSplit = endDateToMatch.split('/')
                self.date2 = datetime.date(int(endDateSplit[2]), int(endDateSplit[1]), int(endDateSplit[0]))
                
            except ValueError as detail: 
                endDateMessage = str(detail)
                endDateMatch = None

        self.informationLabelString.set("StartDate : "+ ("valide" if startDateMatch else ("invalid" + startDateMessage)) + " , EndDate : "+ ("valide" if endDateMatch else ("invalid" + endDateMessage)))


        if((startDateMatch and endDateMatch) or (self.optionFile.get()==1)):
            self.funcToCall(self)
                

        

#if __name__ == "__main__":
#    app = Frame(None)
#    app.mainloop()
    
