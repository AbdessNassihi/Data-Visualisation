import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
# libraries 



root = tk.Tk()
root.geometry("1370x700")   # Size of the window 
root.resizable(False, False)
root.title('Covid Data Visualization')
root.config(background = 'white') # sets background color to white
# window configuration


graphtype = 'line' # first graph shown will be a line graph
GivenCountries = [] # array that will contain the chosen countries
FullData = pd.read_csv('owid-covid-data.csv')   # converting the csv containing the data into a dataframe
ValidCountries = np.array(FullData['location']) # array for checking the validity of the input
FullData = FullData.set_index('date') # set date metric as index
Data = FullData[['location','total_cases','total_cases_per_million','total_deaths','hosp_patients','people_vaccinated']] # select desired metric
Dates = np.array(['2020-03-05','2020-04-10','2020-05-15','2020-06-20','2020-07-25','2020-08-05',
                      '2020-09-10','2020-10-15','2020-11-20','2020-12-25','2021-01-05','2021-02-10',
                      '2021-03-15','2021-04-20','2021-05-25','2021-06-05','2021-07-10','2021-08-15',
                      '2021-09-20','2021-10-25','2021-11-05']) # desired dates
Data = Data.loc[Dates]
# select desired dates




label = tk.Label(root,text="Type Country to visualize", font = ("Courrier",20,'bold'),bg = 'white',fg = 'black')
label.place(x=0,y=0)

Country = tk.StringVar()
ChosenCountry = ttk.Entry(root,width=15, textvariable=Country,font = ("Courrier",20))
ChosenCountry.place(x=0,y=50)

AddCountryBtn =  tk.Button(root, text='Add country',font = ("Courrier",15),bg = '#949494',
                      fg = 'black',width = 10,command = lambda: AddCountry(Country.get()))
AddCountryBtn.place(x = 250,y= 50)

RemoveCountryBtn =  tk.Button(root, text='Remove country',font = ("Courrier",15),bg = '#949494',
                      fg = 'black',width = 15,command = lambda: RemoveCountry(Country.get()))
RemoveCountryBtn.place(x = 380,y= 50)

# adds the necessary elements on the root

def RootElements():
    TotalCasesBtn =  tk.Button(root, text='Show total cases',font = ("Courrier",15),bg = 'black',
                      fg = 'white',width = 15,command = lambda: ShowData(Total_Cases,'Total cases','plot'))
    TotalCasesBtn.place(x = 640,y= 50)

    TotalCasesPerMilBtn =  tk.Button(root, text='Show total cases/mil',font = ("Courrier",15),bg = 'black',
                      fg = 'white',width = 18,command = lambda: ShowData(Total_CasesPerMil,'Total cases per milion','plot'))
    TotalCasesPerMilBtn.place(x = 840,y= 50)

    Hosp_PatientsBtn =  tk.Button(root, text='Show hosp. patients',font = ("Courrier",15),bg = 'black',
                      fg = 'white',width = 18,command = lambda: ShowData(Hosp_Patients,'Hospital patients','plot'))
    Hosp_PatientsBtn.place(x = 1075,y= 50)

    Total_DeathsBtn =  tk.Button(root, text='Show total deaths',font = ("Courrier",15),bg = 'black',
                      fg = 'white',width = 15,command = lambda: ShowData(Total_Deaths,'Total deaths','bar'))
    Total_DeathsBtn.place(x = 720,y= 120)
 
    People_VaccinatedBtn =  tk.Button(root, text='Show people vaccinated',font = ("Courrier",15),bg = 'black',
                      fg = 'white',width = 20,command = lambda: ShowData(People_Vaccinated,'People vaccinated','bar'))
    People_VaccinatedBtn.place(x = 970,y= 120)
    
    LineGraphBtn =  tk.Button(root, text='Line graph',font = ("Courrier",15),bg = 'black',
                      fg = 'white',width = 10,command = lambda: Graphtype('line'))
    LineGraphBtn.place(x =0,y= 280)
    
    BarGraphBtn =  tk.Button(root, text='Bar graph',font = ("Courrier",15),bg = 'black',
                      fg = 'white',width = 10,command = lambda: Graphtype('bar'))
    BarGraphBtn.place(x =0,y= 380)
    
    PieGraphBtn =  tk.Button(root, text='Pie chart',font = ("Courrier",15),bg = 'black',
                      fg = 'white',width = 10,command = lambda: Graphtype('pie'))
    PieGraphBtn.place(x =0,y= 480)
    
    
    # adds the necessary elements on the root after a country has been chosen

def Graphtype(graph): # Changing the graph type if the button was pressed
    global graphtype
    global Total_Cases
    graphtype = graph # changing the variable that indicates the type graph that has to be shown
    ShowData(Total_Cases,'Total cases','plot') # function for plotting the data on the root
    
def AddCountry(name): # function for adding the chosen country in the array 
    RootElements() # function for adding the elements on the root
    ChosenCountry.delete(0,END) # delete context of textbox
    global GivenCountries
    global Total_Cases
    global ArrOfLocations
    global Data
    global ValidCountries
    # global varaible
    
    if name in ValidCountries : # checks if the chosen country is a valid one
        GivenCountries.append(name) # adding country in the array
        ArrOfLocations = np.array(GivenCountries) # transforms array into a numpy array
        SelectData(Data) # function for selecting the desired data
        ShowData(Total_Cases,'Total cases','plot') # function for plotting the data
    else:
        messagebox.showinfo('Error','Please enter valid country') # showing this message if the entry is not a valid one
     
def RemoveCountry(name): # function for removing the chosen country from the array
    RootElements() # function for adding the elements on the root
    ChosenCountry.delete(0,END) # delete context of textbox
    global GivenCountries
    global Total_Cases
    global ArrOfLocations
    global Data
    global ValidCountries
    # global varaiables
    
    if name in ValidCountries:
        GivenCountries.remove(name) # removes the entered country from the array
        ArrOfLocations = np.array(GivenCountries)  # transforms array into a numpy array
        SelectData(Data)  # function for selecting the desired data
        ShowData(Total_Cases,'Total cases','plot') # function for plotting the data
    else:
        messagebox.showinfo('Error','Please enter valid country') # showing this message if the entry is not a valid one

def SelectData(data): # function that selects the desired data 
    global ArrOfLocations
    global Total_CasesPerMil
    global Total_Cases
    global Total_Deaths
    global Hosp_Patients
    global People_Vaccinated
    # gloabal variables
    
   
    Total_CasesPerMil = data[data['location'].isin(ArrOfLocations)]  # Selecting the data of countries that are part of the array of location
    Total_CasesPerMil = ArrangeData(Total_CasesPerMil,'total_cases_per_million')
    
    Total_Cases = data[data['location'].isin(ArrOfLocations)]  # Selecting the data of countries that are part of the array of location
    Total_Cases = ArrangeData(Total_Cases,'total_cases') # function that selects the chosen metric and arrange the data
    
    Total_Deaths = data[data['location'].isin(ArrOfLocations)]  # Selecting the data of countries that are part of the array of location
    Total_Deaths = ArrangeData(Total_Deaths,'total_deaths') # function that selects the chosen metric and arrange the data
    
    Hosp_Patients = data[data['location'].isin(ArrOfLocations)]  # Selecting the data of countries that are part of the array of location
    Hosp_Patients = ArrangeData(Hosp_Patients,'hosp_patients') # function that selects the chosen metric and arrange the data
    
    People_Vaccinated = data[data['location'].isin(ArrOfLocations)]  # Selecting the data of countries that are part of the array of location
    People_Vaccinated = ArrangeData(People_Vaccinated,'people_vaccinated') # function that selects the chosen metric and arrange the data
       
def ArrangeData(frame,metric): # arrange the data in way to have the possiblity to create a proper graph
     global ArrOfLocations # global variable
   
     arr =[] # creating the data that will contain the dataframes
     for location in ArrOfLocations:
         arr.append(frame[frame['location']== location][[metric]].rename(columns = {metric:location})) # filling the array with the dataframes with column name the name of the country
     MergedFrames = arr [0]
     for i in range(1,len(arr)):
         MergedFrames = MergedFrames.merge(arr[i],on = 'date',how = 'left')
     MergedFrames = MergedFrames.fillna(method = "ffill")
     # merging all the datafrmes in the array in order to have to have one dataframe containing the data of all the selected countries
     return MergedFrames
         
def ShowData(frame,metric,graph): # function thats shows the data on the window

  global graphtype # global variable
  
  fig = Figure(figsize=(23,10), dpi=55)  # creating the figure
  ax = fig.add_subplot(111) # adding a subplot 
  canvas = FigureCanvasTkAgg(fig, master=root) # creating a canvas that will be placed on the figure
  canvas.get_tk_widget().place(x=180,y=160) # placing the canvas
  
  if graphtype != 'pie': # if the line or bar graph
      frame.plot(kind = graphtype,title = metric,ax=ax, rot =15).yaxis.set_label_text('Number of people') # creating a graph of the data
  else: # pie chart graph
      Numbers = frame.iloc[19] # selecting the last data
      Numbers.plot(kind = "pie",title = metric,figsize= (15,5), ax=ax,
             autopct=lambda p: '{:.1f}%'.format(p) if p > 0 else '').yaxis.set_label_text("") # creating the pie chart of the data
      
root.mainloop() # keeping the window open