"""
File: dataPlotting.py
Author: Tomas Kmet
Contributor: Jad Khalil
"""


import numpy as np
import matplotlib.pyplot as plt
import terminalPrint as tP
import os

class dataPlotting:

    def __init__(self):
        pass 
    
    def plot_population(self, country_pop_data, country):

        years = list(range(2000, 2021)) #x axis

        plt.plot(years, country_pop_data, label=f'{country}') #plot the x axis, y axis, and label
        plt.title('Population vs Year') #plot title
        plt.xlabel('Years') #x axis title
        plt.ylabel('Population change during 21 years') #y axis title
        plt.legend(loc='upper left', shadow=True) #legend
        plt.xticks(years)
        plt.ticklabel_format(axis='y', style='plain')
        plt.show()

    def Threatened_Species_data(self, country_input, valid_country):

        threatened_species = np.genfromtxt(
            os.path.join("csvData", "Threatened_Species.csv"),  skip_header=True, delimiter=',', usecols=(1, 2, 3, 4)) #numpy array that imports threatened species population from Threatened_Species.csv

        for i in range(len(valid_country)): #gathers selected country threatened species population
            if country_input == valid_country[i]:
                list_of_countries_threatened_species = threatened_species[i][:]
                break

        display_endagered_species = tP.terminalPrint(country_input) #creates an instance of a class called CountryAnalitics_for_Pop. Uses two arguments, country_input and list_of_countries_threatened_species
        display_endagered_species.display_indagered_species(list_of_countries_threatened_species) #calls a method from the class

        return list_of_countries_threatened_species 


    def plot_Threatened_Species_data(self, species_threatend):

        x_points = ['Plans', 'Fish', 'Birds', 'Mamals'] #x axis

        plt.bar(x_points[0], species_threatend[0],
                label='Endangered plants', color='green') #plot the first bar of the bar graph- shows endangered plants
        plt.bar(x_points[1], species_threatend[1],
                label='Endangered Fish', color='blue') #plot the second bar of the bar graph- shows endangered fish
        plt.bar(x_points[2], species_threatend[2],
                label='Endangered Birds', color='yellow') #plot the third bar of the bar graph- shows endangered birds
        plt.bar(x_points[3], species_threatend[3],
                label='Endangered Mammals', color='brown') #plot the fourth bar of the bar graph- shows endangered mammals
        plt.xlabel("Type of endangered species") #x axis title
        plt.ylabel("Endangered species") #y axis title
        plt.title('Threatened Species') #plot title
        plt.legend() #legend
        plt.xticks(x_points)
        plt.show()

    def display_pop_density(self, country, years, country_pop_data):
        # plot population density vs year
        plt.plot(years, country_pop_data, label=f'{country}')
        plt.title('Population density vs Year')  # define axis and title
        plt.xlabel('Years')
        plt.ylabel('Population density change')
        plt.legend(loc='upper left', shadow=True)
        plt.xticks(years)  # xticks to avoid having decimal places in graph
        plt.ticklabel_format(axis='y', style='plain')
        plt.show()
