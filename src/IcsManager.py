from tkinter import *



class GUI(Frame):
	def init__(self, fenetre, **kwargs):
        	Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        	self.pack(fill=BOTH)
        	self.nb_clic = 0

        
   	     # Création de nos widgets
        	self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")
        	self.message.pack()

        	self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        	self.bouton_quitter.pack(side="left")

        

        	self.bouton_cliquer = Button(self, text="Cliquez ici", fg="red",command=self.cliquer)
        	self.bouton_cliquer.pack(side="right")
    

	def cliquer(self):
        	self.nb_clic += 1

        	self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)

       



fenetre = Tk()
interface = Interface(fenetre)
interface.mainloop()
interface.destroy() 
