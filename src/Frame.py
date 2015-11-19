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
        self.main_panel = tkinter.LabelFrame(self, text="Planif Dates", padx=5, pady=5, height=200, width=200)
        self.main_panel.pack(side=tkinter.LEFT , padx=10, pady=10)

        
        tkinter.Label(self.main_panel, text="Start Date : ").grid(row=1, column=1)

        #Date 1
        self.start_date = tkinter.Entry(self.main_panel)
        self.start_date.insert(0,'dd/mm/yyyy')
        self.start_date.grid(row=2, column=1)

        tkinter.Label(self.main_panel, text="Start Date : ").grid(row=3, column=1)

        #Date2
        self.end_date = tkinter.Entry(self.main_panel)
        self.end_date.insert(0,'dd/mm/yyyy')
        self.end_date.grid(row=4, column=1)

        #Bouton "Générer"
        self.generate_button = tkinter.Button(self.main_panel, text="Générer", command=self.Generate)
        self.generate_button.grid(row=5, column=1, pady=25)

        #Label Affichage des Dates
        self.information_label_string = tkinter.StringVar()
        self.information_label = tkinter.Label(self.main_panel, textvariable=self.information_label_string, text="Texte de Base")
        self.information_label.grid(row=6,column=1)


        ############################
        #     Option Panel         #
        ############################

        #Panel Labelisé 
        self.option_panel = tkinter.LabelFrame(self, text="File Options", padx=5, pady=5 , height=200, width=200)
        self.option_panel.pack(side=tkinter.LEFT, padx=10, pady=10)

        #CheckBox File Browser
        self.option_file = tkinter.IntVar()
        self.checkbutton_file = tkinter.Checkbutton(self.option_panel, text="File Browser", variable=self.option_file, command=self.IsSelected)
        self.checkbutton_file.grid(row=1, column=1, pady=10)

        #Bouton File Browser
        self.file_browser_button = tkinter.Button(self.option_panel, text="File...", command=self.SelectFile)
        self.file_browser_button.grid(row=2, column=1, pady=10)

        #Chemin du Fichier
        self.file_path = tkinter.StringVar()
        self.file_path.set("File Path : None")
        self.path_label = tkinter.Label(self.option_panel,text="File Path : ",textvariable=self.file_path)
        self.path_label.grid(row=3, column=1, pady=10)


        ############################
        #     Advanced Panel       #
        ############################

        #Panel Labelisé
        self.advanced_panel = tkinter.LabelFrame(self, text="Advanced Panel", padx=5, pady=5 , height=200, width=200)
        self.advanced_panel.pack(side=tkinter.LEFT, padx=10, pady=10)

        #CheckBox Select
        self.unique_select = tkinter.IntVar()
        self.unique_select_checkbutton = tkinter.Checkbutton(self.advanced_panel, text="Select Unique", variable=self.unique_select, command=self.UniqueSelectCheck)
        self.unique_select_checkbutton.grid(row=1, column=1, pady=10)

        #CheckBox Select Group
        self.group_select = tkinter.IntVar()
        self.group_select_button = tkinter.Checkbutton(self.advanced_panel, text="Select Group", variable=self.group_select, command=self.GroupSelectCheck)
        self.group_select_button.grid(row=2, column=1, pady=10)

        #CheckBox Delete
        self.unique_delete = tkinter.IntVar()
        self.unique_delete_button = tkinter.Checkbutton(self.advanced_panel, text="Delete Unique", variable=self.unique_delete, command=self.UniqueDeleteCheck)
        self.unique_delete_button.grid(row=3, column=1, pady=10)

        #CheckBox Delete Group
        self.group_delete = tkinter.IntVar()
        self.group_delete_checkbutton = tkinter.Checkbutton(self.advanced_panel, text="Delete Group", variable=self.group_delete, command=self.GroupDeleteCheck)
        self.group_delete_checkbutton.grid(row=4, column=1, pady=10)

        #Entrée Select
        self.selected = tkinter.Entry(self.advanced_panel)
        self.selected.grid(row=1, column=2)

        #Entrée Group Select
        self.group_selected = tkinter.Entry(self.advanced_panel)
        self.group_selected.grid(row=2, column=2)

        #Entrée Delete
        self.deleted = tkinter.Entry(self.advanced_panel)
        self.deleted.grid(row=3, column=2)

        #Entrée Group Delete
        self.group_deleted = tkinter.Entry(self.advanced_panel)
        self.group_deleted.grid(row=4, column=2)

        #Désactive toutes les entrées
        self.selected.configure(state='disabled')
        self.group_selected.configure(state='disabled')
        self.deleted.configure(state='disabled')
        self.group_deleted.configure(state='disabled')

    #Gestion CheckBox Select 
    def UniqueSelectCheck(self):
        
        if(self.unique_select.get() != 1):
            self.selected.configure(state='disabled')
        else:
            self.selected.configure(state='normal')

    #Gestion CheckBox Select Group
    def GroupSelectCheck(self):
        
        if(self.group_select.get() != 1):
            self.group_selected.configure(state='disabled')
        else:
            self.group_selected.configure(state='normal')
            
    #Gestion CheckBox Delete
    def UniqueDeleteCheck(self):
        
        if(self.unique_delete.get() != 1):
            self.deleted.configure(state='disabled')
        else:
            self.deleted.configure(state='normal')
            
    #Gestion CheckBox Delete Group
    def GroupDeleteCheck(self):
        
        if(self.group_delete.get() != 1):
            self.group_deleted.configure(state='disabled')
        else:
            self.group_deleted.configure(state='normal')
            

    #Gestion File Browser
    def SelectFile(self):

        if(self.option_file.get()==1):

            file_name = askopenfilename(filetypes=(("ICS Files", "*.ics"),("All files", "*.*")))
            self.file_path.set(file_name)
        else:
            showerror("You can't", "The file browser is disable.")

    #Gestion CheckBox File Browser
    def IsSelected(self):
    
        if(self.option_file.get() ==1):
            a=""
        else:

            self.file_path.set("File Path : None")


	#Gestion Bouton "Générer"
    def Generate(self):

        #Récupération des Champs Dates
        d1 = self.start_date.get()
        d2 = self.end_date.get()
        #Regex des valeurs
        mat1=re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', d1)
        mat2=re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', d2)

        mess1 = ""
        mess2 = ""


        if( mat1): 
            try: 
                list_date1 = d1.split('/')
                self.date1 = datetime.date(int(list_date1[2]), int(list_date1[1]), int(list_date1[0]))     
                
            except ValueError as detail:
                mess1 = str(detail)
                mat1 = None

        if(mat2):
            try: 
                list_date2 = d2.split('/')
                self.date2 = datetime.date(int(list_date2[2]), int(list_date2[1]), int(list_date2[0]))
                
            except ValueError as detail: 
                mess2 = str(detail)
                mat2 = None


        self.information_label_string.set("Date 1 : "+ ("valide" if mat1 else ("invalid" + mess1)) + " , Date 2 : "+ ("valide" if mat2 else ("invalid" + mess2)))

        if(mat1 and mat2):
            self.funcToCall(self)

                


#if __name__ == "__main__":
#    app = Frame(None)
#    app.mainloop()
    