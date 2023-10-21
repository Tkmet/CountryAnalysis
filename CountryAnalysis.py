"""
Project: Country Analysis
Author: Tomas Kmet
Contributor: Jad Khalil
"""

import numpy as np
import dataPlotting as dP
import data as dA
import os



def list_option(answer, option_list):
    if answer == 'y':
        print(option_list, '\n')

def get_region():

    Country_continents_and_sub_region = np.genfromtxt(
        os.path.join("csvData", "Country_Data.csv"), skip_header=True, delimiter=',', usecols=(0, 1, 2), dtype=None, encoding='UTF-8') #numpy array that imports from Country_Data.csv countries, continent, sub region

    continent = [] #list of continents
    sub_region = [] #list of sub regions
    valid_contries = [] #list of countries

    for i in range(len(Country_continents_and_sub_region)): 
        if Country_continents_and_sub_region[i][1] not in continent: #logic that prevents repetition
            continent.append(Country_continents_and_sub_region[i][1]) #creates a list of possible continents

        valid_contries.append(Country_continents_and_sub_region[i][0]) #adds countries to the list of countries
    print("\n----Country Analytics----")
    print("A terminal based application\n")
    #print("Please Input a continent: ")
    continent_input = input("Please Input a continent: ").capitalize() #prompts user to input a continent

    while True:
        if continent_input not in continent: #condition that is True until user enters a valid continent
            print("Please enter a valid continent") 
            answer = input('Would you like to see the list? (y/n): ') #prompts user to enter either y or n
            list_option(answer, continent) #list_option function is called to display the possible inputs upon user request
            continent_input = input().capitalize() #user is prompted to try again
            continue #while loop continues
        break #loop is broken if user enters a valid continent

    for i in range(len(Country_continents_and_sub_region)): #creates a list of sub regions
        if Country_continents_and_sub_region[i][1] == continent_input and Country_continents_and_sub_region[i][2] not in sub_region:
            sub_region.append(Country_continents_and_sub_region[i][2])

    sub_region_input = input(f"Please Input a sub region Inside The Continent of {continent_input}: ").title() #prompts user to input a sub region

    while True:
        if sub_region_input not in sub_region: #condition that is True until user enters a valid sub region
            print(f"Please enter a valid sub-region in The Continent of {continent_input}")
            answer = input('Would you like to see the list? (y/n): ') #prompts user to enter either y or n
            list_option(answer, sub_region) #list_option function is called to display the possible inputs upon user request
            sub_region_input = input().title() #user is prompted to try again
            continue #while loop continues
        break #loop is broken if user enters a valid sub continent

    Countries_in_Sub_region = [] #list of specific countries that are located in the sub region
    for i in range(len(Country_continents_and_sub_region)):
        if Country_continents_and_sub_region[i][2] == sub_region_input and Country_continents_and_sub_region[i][2] not in Countries_in_Sub_region: #condition that filters countries in sub region and doesn't allow duplicates
            Countries_in_Sub_region.append(
                Country_continents_and_sub_region[i][0]) #adds countries in sub region to the countries in sub region list

    print(f"\nThe following are countries located in the sub region of {sub_region_input} in The continent of {continent_input}\n")
    for j in range(len(Countries_in_Sub_region)): #displays which countries that are located in the sub region and continent
        print(Countries_in_Sub_region[j])

    selected_country = input("\nFrom the above please type a contry for the CountryAnalytics software to Analyze: ").title() #prompt user to enter a country
    while True:
        if selected_country not in Countries_in_Sub_region: #condition that is True until user input is valid
            print("Please enter a valid contry from the above list")
            selected_country = input().title() #prompts user to re-enter
            continue #while loop continues
        break #loop is broken if user enters a valid sub continent

    return selected_country, valid_contries #returns user selected country and a list of countries (which are valid)

def getInput():
    print('\n-----Data Selection Menu-----\n')
    print('Press 1 for population change')
    print('Press 2 for threatened species data')
    print('Press 3 for population density')
    print('Press 4 for endangered species per square km')
    print('Press 5 for Population Growth and total number of endangered species\n')
    return input('Please select an option: ')

def menu(country_input, valid_country):

    plotter = dP.dataPlotting()
    data = dA.data()
    user_input = getInput()

    if user_input == '1': #if user selects 1
        country_pop_data = data.country_Pop(country_input, valid_country) #country population data is given from the country_Pop() function
        plotter.plot_population(country_pop_data, country_input) #plot_population() function is called

    elif user_input == '2': #if user selects 2
        plotter.plot_Threatened_Species_data(
        data.Threatened_Species_data(country_input, valid_country)) #threatened species data is plotted by calling the plot_Threatened_Species_Data(). Threatened_species_data(country_input, valid_country) is used as an argument for the plot function

    elif user_input == '3': #if user selects 3
        data.Population_Density_and_graph(country_input, valid_country) #Population_Density_and_graph() funciton is called

    elif user_input == '4': #if user selects 4
        data.endagered_species_per_km(country_input, valid_country) #endagered_species_per_km() function is called
    
    elif user_input == '5': #if user selects 5
        data.endagered_species_per_pop(country_input, valid_country) #endagered_species_per_pop() function is called

    else: #user enters an invalid selection and is prompted to try again
        menu(country_input, valid_country)

def main(): #main function
    country_input, valid_country = get_region() #get_region function is called
    menu(country_input, valid_country) #menu() funciton is called with two arguments being country_input and valid_country

if __name__ == '__main__':
    main()

