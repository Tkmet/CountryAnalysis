"""
File: data.py
Author: Tomas Kmet
Contributor: Jad Khalil
"""

import numpy as np
import terminalPrint as tP
import dataPlotting as dP
import os

class data:

    def __init__(self):
        pass 

    def Threatened_Species_data(self, country_input, valid_country):

        threatened_species = np.genfromtxt(

            os.path.join("csvData", "Threatened_Species.csv"), #gets full file path
            skip_header=True, delimiter=',', usecols=(1, 2, 3, 4)) #numpy array that imports threatened species population from Threatened_Species.csv

        for i in range(len(valid_country)): #gathers selected country threatened species population
            if country_input == valid_country[i]:
                list_of_countries_threatened_species = threatened_species[i][:]
                break

        display_endagered_species = tP.terminalPrint(country_input)
        #creates an instance of a class called CountryAnalitics_for_Pop. Uses two arguments, country_input and list_of_countries_threatened_species

        display_endagered_species.display_indagered_species(list_of_countries_threatened_species) #calls a method from the class

        return list_of_countries_threatened_species 


    def endagered_species_per_km(self, country_input, valid_country):

        threatened_species = np.genfromtxt(
            os.path.join("csvData", "Threatened_Species.csv"),  skip_header=True, delimiter=',', usecols=(1, 2, 3, 4)) #numpy array that imports threatened species data from Threatened_Species.csv

        Population_size = np.genfromtxt(
            os.path.join("csvData", "Country_Data.csv"), skip_header=True, delimiter=',', usecols=(-1)) #numpy array that imports country area from Country_Data.csv

        threat_species = [] #threatened_species list

        for i in range(len(valid_country)):
            if country_input == valid_country[i]:
                threat_species = threatened_species[i][:] #gets threatened species
                country_size = Population_size[i] #gets country size
                break

        endagered_per_km = [] #endangered per km list
        total_endagered = sum(threat_species) #sum of threatened species

        for i in range(len(threat_species)):
            density = country_size / threat_species[i] #calculates land per threatened species
            if threat_species[i] == 0: #catches division error
                endagered_per_km.append(0)
            else:
                endagered_per_km.append(density) #adds to endager_per_km list

        endagered_per_km = tP.terminalPrint(country_input) #creates an instance of a class (class is called PopDensity)
        endagered_per_km.display_endagered_per_km(total_endagered, Population_size) #endangered_per_km


    def endagered_species_per_pop(self, country_input, valid_country):

        threatened_species = np.genfromtxt(
            os.path.join("csvData", "Threatened_Species.csv"), skip_header=True, delimiter=',', usecols=(1, 2, 3, 4)) #numpy array that imports threatened species population data from Threatened_Species.csv

        Population_data = np.genfromtxt(
            os.path.join("csvData", "Population_Data.csv"),  skip_header=True, delimiter=',', usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)) #numpy array that imports population data from Populaiton_Data.csv

        for i in range(len(valid_country)):
            if country_input == valid_country[i]:
                threat_species = threatened_species[i][:] #gets threatened species
                Pop_change = Population_data[i][:] #gets population change
                break

        total_endagered = sum(threat_species) #adds total amount of endangered

        endagered_per_pop = tP.terminalPrint(country_input) #creates an instance of a class (class is called PopDensity)
        endagered_per_pop.display_endagered_per_pop(total_endagered, Pop_change) #uses a method to display endangered per population


    def country_Pop(self, country_input, valid_country):

        pop_data = np.genfromtxt(
            os.path.join("csvData", "Population_Data.csv"),  skip_header=True, delimiter=',', usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)) #numpy array that imports population data from 2000- 2021 from Population_Data.csv

        for i in range(len(valid_country)): #gathers selected country population
            if country_input == valid_country[i]:
                country_pop_data = pop_data[i][:]
                break

        year = 2000 #define a year variable
        pop_display = tP.terminalPrint(country_input) #creates an instance of a class called CountryAnalitics_for_Pop. Uses two arguments, country_input and country_pop_data 
        pop_display.display_pop_change(year, country_pop_data) #calls a method from the class

        return country_pop_data 


    def Population_Density_and_graph(self, country_input, valid_country):

        Population_data = np.genfromtxt(
            os.path.join("csvData", "Population_Data.csv"),
            skip_header=True, delimiter=',', usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)) #numpy array that imports population data from 2000- 2021 from Population_Data.csv

        Population_size = np.genfromtxt(
            os.path.join("csvData", "Country_Data.csv"),
            skip_header=True, delimiter=',', usecols=(-1)) #numpy array that imports country area from Country_data.csv

        for i in range(len(valid_country)): 
            if country_input == valid_country[i]:
                population_change = Population_data[i][:] #gets population
                country_size = Population_size[i] #gets country size 
                break

        pop_density = [] #population density 

        for i in range(len(population_change)): 
            density = population_change[i] / country_size #calculates density
            pop_density.append(density) #adds density to population list
    
        years = list(range(2000, 2021)) #x axis

        density_display_and_graph = dP.dataPlotting() #create an instance of a class (class called PopDensity)
        density_display_and_graph.display_pop_density(country_input, years, pop_density) #use the method .display_pop_density() to display population density