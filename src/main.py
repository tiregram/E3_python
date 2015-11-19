import Frame

   


def getData(form):
    import DataGet
    lap = DataGet.DateDataForm()

    lap.online      =not form.optionFile.get()
    if form.date1:
        lap.dateStart   = form.date1

    if form.date2:    
        lap.dateEnd     = form.date2

    lap.icsFileName = form.filePath.get()

    lis = lap.getDict('LOCATION','DESCRIPTION','DTSTART','DTEND')
    
    import DataCal
    print(dir(DataCal))
     
    dc = DataCal.DataCal.BuilderDataCal(lis)
    if form.uniqueSelect.get():
       dc = dc.onlyRoom(form.uniqueSelected.get())
    if form.groupSelect.get():
       dc = dc.conditionRoom(form.groupSelected.get())
    dc.render()

## super filter
#agendaEsiee.removeRoom(bb,"Vi")
#agendaEsiee.
#agendaEsiee.conditionRoom(bb,'[0-9]4[0-9]{2}')

#agendaEsiee.render(bb)

if __name__ == "__main__":
    app = Frame.Frame(None)
    app.funcToCall = getData
    app.mainloop()
 
