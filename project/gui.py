from Tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from Part1and4.SearchByNameFuncs import *
from Part1and4.PlotDistributionFuncs import *
import pandas as pd
from Part2and3.topRestaurantInStateAndPriceSelect import *
from Part2and3.topRestaurantsInStateSelect import *


data = pd.read_csv('yelp_restaurant_only_dataset.csv')


def nameSearchWindow():
    '''
    Set up a new window for name search function. And this new window allows user to search a restaurant by its name
    '''

    # Initialize the window and set its size.
    nameSearchWindow = Toplevel()
    nameSearchWindow.geometry('{}x{}'.format(600, 600))

    # Initialize a stringvar to get the user's input at the entry
    ment = StringVar()

    # Initialize two labels to instruct the user to input.
    promptLabelOne = Label(nameSearchWindow, text='Input the name of the restaurant you hope to find:', fg='black')
    promptLabelTwo = Label(nameSearchWindow, text='If you want to search again, please press the clear button.')

    # Initialize the entry fot user inputs
    inputNameEntry = Entry(nameSearchWindow, textvariable=ment)

    promptLabelOne.place(relx=0.23, rely=0.25)
    promptLabelTwo.place(relx=0.23, rely=0.3)
    inputNameEntry.pack()
    inputNameEntry.place(relx=0.23, rely=0.35)

    # initialize the function with takes user's inputs as paramaters to show the restaurants' information on the canvas.
    def showRestaurant():
        mtext = ment.get()
        try:
            mylabel = Label(nameSearchWindow, text=NameSearch(data, mtext))
            mylabel.place(relx=0.2, rely=0.5)

        except:
            errorlabel = Label(nameSearchWindow, text="Sorry, Find No Restaurant of This Name!")
            errorlabel.place(relx=0.2,rely=0.45)

    # initialize the search button
    searchButton = Button(nameSearchWindow, text='Search', command=showRestaurant)
    searchButton.pack()
    searchButton.place(relx=0.6, rely=0.35)


    # initialize the function of clear the canvas
    def new_canvas():
        w = Canvas(nameSearchWindow, width=500, height=300)
        w.pack()
        w.place(relx=0.2, rely=0.45)

    # initialize the clear button
    clearButton = Button(nameSearchWindow, text='Clear', command=new_canvas)
    clearButton.pack()
    clearButton.place(relx=0.75, rely=0.35)

    nameSearchWindow.protocol("WM_DELETE_WINDOW")


def popularRestaurantsWindow():
    '''
    initialize the popular restaurants window which allows users to search top rating restaurants in a specific state,
     and see the distribution of the stars of the top restaurants.
    '''

    # initialize the popular restaurants window
    popularRestaurantsWindow = Toplevel()
    popularRestaurantsWindow.geometry('{}x{}'.format(600, 600))

    # initialize two stringvar to catch user's inputs
    stateMent = StringVar()
    numMent = StringVar()

    # set up some prompt labels
    stateLabel = Label(popularRestaurantsWindow, text='Please input the state whose popular restaurants you want to see: ')
    promptLabel = Label(popularRestaurantsWindow, text="(For Example:'WI', 'AZ', 'NV', 'CA', 'ON', 'EDH', 'ELN', 'MLN', 'NY', 'KHL')")
    numLabel = Label(popularRestaurantsWindow, text="Please input the numbers of top restaurants you want to see:(For Example: 5)")

    # set up the necessary entries for user's inputs
    stateEntry = Entry(popularRestaurantsWindow, textvariable=stateMent)
    numEntry = Entry(popularRestaurantsWindow, textvariable=numMent)

    stateLabel.place(relx=0.10, rely=0.20)
    promptLabel.place(relx=0.1, rely=0.25)
    numLabel.place(relx=0.10, rely=0.35)
    stateEntry.pack()
    stateEntry.place(relx=0.10, rely=0.30)
    numEntry.pack()
    numEntry.place(relx=0.10, rely=0.40)

    # initialize the function for show top restaurants button
    def showTopRestaurants():
        numText = numMent.get()
        stateText = stateMent.get()
        try:
            restaurantLabel = Label(popularRestaurantsWindow, text=restaurantsMoreInformation(topRestaurantsInState(stateText, int(numText))))
            restaurantLabel.place(relx=0.1, rely=0.55)
        except:
            errorLabel = Label(popularRestaurantsWindow, text="Sorry, there isn't such a state in the dataset.")
            errorLabel.place(relx=0.1,rely=0.52)

    # initialize the show button
    showButton = Button(popularRestaurantsWindow, text="Show", command=showTopRestaurants)
    showButton.pack()
    showButton.place(relx=0.1, rely=0.47)

    # initialize the function of clear the canvas
    def new_canvas():
        w = Canvas(popularRestaurantsWindow, width=500, height=300)
        w.pack()
        w.place(relx=0.1, rely=0.53)

    # initialize the clear button
    clearButton = Button(popularRestaurantsWindow, text='Clear', command=new_canvas)
    clearButton.pack()
    clearButton.place(relx=0.35, rely=0.47)

    # initialize the function for plot top restaurants button
    def plotTopRestaurants():
        numText = numMent.get()
        stateText = stateMent.get()

        try:
            data = topRestaurantsInState(stateText, int(numText))
            restaurantStarsPlot(data)
        except:
            pass

    # initialize the plot button.
    plotButton = Button(popularRestaurantsWindow, text='plot', command=plotTopRestaurants)
    plotButton.pack()
    plotButton.place(relx=0.6, rely=0.47)


def expenseSearchWindow():
    '''
    initialize the expense search window which allows users to input a specific state and the price range and the numbers of top restaurants they want to see.
    '''

    # initialize the expense search window
    expenseSearchWindow = Toplevel()
    expenseSearchWindow.geometry('{}x{}'.format(600, 600))

    # initialize three stringvar to catch user's inputs
    stateMent = StringVar()
    priceRangeMent = StringVar()
    numMent = StringVar()

    # initialize some prompt labels
    promptLabelOne = Label(expenseSearchWindow, text="According to Yelp's definition, there are four categories in price ranges:")
    promptLabelTwo = Label(expenseSearchWindow, text="$ -- corresponding to '1' in our data, price range: under 10;")
    promptLabelThree = Label(expenseSearchWindow, text="$$ -- corresponding to '2' in our data, price range: $11-30;")
    promptLabelFour = Label(expenseSearchWindow, text="$$$ -- corresponding to '3' in our data, price range: $31-60;")
    promptLabelFive = Label(expenseSearchWindow, text="$$$$ -- corresponding to '4' in our data, price range: Above 61$")
    promptLabelOne.place(relx=0.1, rely=0.05)
    promptLabelTwo.place(relx=0.1, rely=0.1)
    promptLabelThree.place(relx=0.1, rely=0.15)
    promptLabelFour.place(relx=0.1, rely=0.2)
    promptLabelFive.place(relx=0.1, rely=0.25)

    stateLabel = Label(expenseSearchWindow, text="Please input the state whose restaurants's expense range you want to see: ")
    promptLabel = Label(expenseSearchWindow, text="(For Example:'WI', 'AZ', 'NV', 'CA', 'ON', 'EDH', 'ELN', 'MLN', 'NY', 'KHL')")
    numLabel = Label(expenseSearchWindow, text="Please input the numbers of top restaurants you want to see:(For Example: 5)")
    priceRangeLabel = Label(expenseSearchWindow, text="Please input the price range of restaurants you want to find:(For Example: 1)")

    # initialize three entries for user inputs
    stateEntry = Entry(expenseSearchWindow, textvariable=stateMent)
    numEntry = Entry(expenseSearchWindow, textvariable=numMent)
    priceRangeEntry = Entry(expenseSearchWindow, textvariable=priceRangeMent)

    stateLabel.place(relx=0.10, rely=0.33)
    promptLabel.place(relx=0.1, rely=0.38)
    stateEntry.pack()
    stateEntry.place(relx=0.10, rely=0.43)

    priceRangeLabel.place(relx=0.1, rely=0.48)
    priceRangeEntry.pack()
    priceRangeEntry.place(relx=0.1, rely=0.53)

    numLabel.place(relx=0.10, rely=0.58)
    numEntry.pack()
    numEntry.place(relx=0.10, rely=0.63)

    # initialize the function for show price range button
    def showPriceRange():
        stateText = stateMent.get()
        priceRangeText = priceRangeMent.get()
        numText = numMent.get()

        try:
            showPriceRangeRestaurants = Label(expenseSearchWindow, text=restaurantInStateandPrice(stateText, int(priceRangeText), int(numText)))
            showPriceRangeRestaurants.place(relx=0.1, rely=0.79)
        except InputError:
            inputErrorLabel = Label(expenseSearchWindow, text="Sorry, your input state or price range or number of TOP is wrong.")
            inputErrorLabel.place(relx=0.1, rely=0.74)

    # initialize the show price range button
    showPriceRangeRestaurantButton = Button(expenseSearchWindow, text='Show Restaurant', command=showPriceRange)
    showPriceRangeRestaurantButton.pack()
    showPriceRangeRestaurantButton.place(relx=0.1, rely=0.69)

    def plotRestaurantRegion():
        stateText2 = stateMent.get()
        priceRangeText = priceRangeMent.get()
        numText = numMent.get()
        try:
            data = restaurantInStateandPrice(stateText2, int(priceRangeText), int(numText))
            restaurantStarsPlot(data)
        except:
            pass

    plotButton = Button(expenseSearchWindow, text='plot', command=plotRestaurantRegion)
    plotButton.pack()
    plotButton.place(relx=0.7, rely=0.69)

    # initialize the function for clear button
    def new_canvas():
        w = Canvas(expenseSearchWindow, width=500, height=400)
        w.pack()
        w.place(relx=0.1, rely=0.74)

    # initialize the clear button
    clearButton = Button(expenseSearchWindow, text='Clear', command=new_canvas)
    clearButton.pack()
    clearButton.place(relx=0.4, rely=0.69)


def overallInformationWindow():
    '''
    initialize the overall information window which allows users to see the stars distribution in each state.
    '''

    # initialize the overall information window
    overallInformationWindow = Toplevel()
    overallInformationWindow.geometry('{}x{}'.format(600, 600))

    # initialize the star distribution button which can show the overall star distribution of six states
    starDistButton = Button(overallInformationWindow, text='Show the Star Distribution of Six States!', command=PlotStarDistribution)
    starDistButton.pack()
    starDistButton.place(relx=0.2, rely=0.2)

    promptLabel = Label(overallInformationWindow, text='Press the button to see the star distribution!')
    promptLabel.pack()
    promptLabel.place(relx=0.2, rely=0.15)

    # initialize a state list box for user to see.
    stateListbox = Listbox(overallInformationWindow)
    stateListbox.pack()
    stateListbox.place(relx=0.2, rely=0.4)
    for item in ['ON', 'EDH', 'MLN', 'WI', 'AZ', 'NV']:
        stateListbox.insert(END, item)

    # initialize a select state button for user to select a certain state they want to see
    selectButtonLabel = Label(overallInformationWindow, text='Select a button to see the pie charts for the star distribution for that state!')
    selectButtonLabel.pack()
    selectButtonLabel.place(relx=0.05, rely=0.33)

    # initialize every state's show button
    buttonON = Button(overallInformationWindow, text='ON state', command=lambda x='ON':PlotPieChartForOneState(x))
    buttonON.pack()
    buttonON.place(relx=0.5, rely=0.4)

    buttonEDH = Button(overallInformationWindow, text='EDH state', command=lambda x='EDH':PlotPieChartForOneState(x))
    buttonEDH.pack()
    buttonEDH.place(relx=0.5, rely=0.52)

    buttonMLN = Button(overallInformationWindow, text='MLN state', command=lambda x='MLN':PlotPieChartForOneState(x))
    buttonMLN.pack()
    buttonMLN.place(relx=0.7, rely=0.4)

    buttonWI = Button(overallInformationWindow, text='WI state', command=lambda x='WI':PlotPieChartForOneState(x))
    buttonWI.pack()
    buttonWI.place(relx=0.5, rely=0.64)

    buttonAZ = Button(overallInformationWindow, text='AZ state', command=lambda x='AZ':PlotPieChartForOneState(x))
    buttonAZ.pack()
    buttonAZ.place(relx=0.7, rely=0.52)

    buttonNV = Button(overallInformationWindow, text='NV state', command=lambda x='NV':PlotPieChartForOneState(x))
    buttonNV.pack()
    buttonNV.place(relx=0.7, rely=0.64)

def main():
    '''
    main function of this gui application.
    '''

    # set up the top window's size
    WIDTH = 950
    HEIGHT = 534

    # initialize the top window
    top = Tk()
    top.geometry('{}x{}'.format(WIDTH, HEIGHT))

    # set up the top window's background picture.
    backImage = PhotoImage(file="yelp.gif")
    panel = Label(top, image=backImage)
    panel.pack(side='top', fill='both', expand='yes')

    # set up four main buttons
    nameSearchButton = Button(text='Name Search', command=nameSearchWindow)
    nameSearchButton.pack()
    nameSearchButton.place(relx=0.33, rely=0.33, anchor='center')

    expenseSearchButton = Button(text='Expense Search', command=expenseSearchWindow)
    expenseSearchButton.pack()
    expenseSearchButton.place(relx=0.33, rely=0.66, anchor='center')

    popularRestaurantsButton = Button(text='Popular Restaurants', command=popularRestaurantsWindow)
    popularRestaurantsButton.pack()
    popularRestaurantsButton.place(relx=0.66, rely=0.33, anchor='center')

    overallInformationButton = Button(text='Overall Information', command=overallInformationWindow)
    overallInformationButton.pack()
    overallInformationButton.place(relx=0.66, rely=0.66, anchor='center')

    top.mainloop()


if __name__ == '__main__':
    main()