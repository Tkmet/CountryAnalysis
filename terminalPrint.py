"""
File: terminalPrint.py
Author: Tomas Kmet
Contributor: Jad Khalil
"""
import numpy as np

class terminalPrint:
    def __init__(self, country):
        self.country = country

    def display_pop_change(self, year, country_pop_data):
        print("Population change from 2000-2021 in {}".format(self.country))
        # we iterate over the length of the population data
        for i in range(len(country_pop_data)):
            print("Population {}: {:.0f}".format(
                year, country_pop_data[i]))
            year += 1

        print("Highest Population recorded in these years: {:.0f}".format(
            np.max(country_pop_data)))  # the max and min population during these years are also displayed to the user
        print("Lowest Population recorded in these years: {:.0f}".format(
            np.min(country_pop_data)))

    def display_indagered_species(self, list_of_countries_threatened_species):
        print("{} endangered species:".format(self.country))
        print(
            "Plants: {:.0f}\nFish: {:.0f}\nBirds: {:.0f}\nMammals: {:.0f}".format(list_of_countries_threatened_species[0], list_of_countries_threatened_species[1], list_of_countries_threatened_species[2], list_of_countries_threatened_species[3]))

    # total endagered is a value of the sum of the endagered species in a country
    def display_endagered_per_km(self, total_endagered, country_pop_data):
        print('{} has a total of {} endagered species'.format(
            self.country, total_endagered))
        print('{} has {:.2f} km of land for every plant species endangered'.format(
            self.country, country_pop_data[0]))  # displays that the country has x amount of land for every species endagered
        print('{} has {:.2f} km of land for every fish species endangered'.format(
            self.country, country_pop_data[1]))
        print('{} has {:.2f} km of land per every bird species endangered'.format(
            self.country, country_pop_data[2]))
        print('{} has {:.2f} km of land per every mammal species endangered'.format(
            self.country, country_pop_data[3]))

    def display_endagered_per_pop(self, total_endagered, country_pop_data):
        # to find whether there is population growth or decline compare population 2000, and population 2021
        if country_pop_data[0] > country_pop_data[-1]:
            pop_reduction = country_pop_data[0] - \
                country_pop_data[-1]
            print('A Population Reduction of {:.0f} has resulted in {:.0f} endangered species'.format(
                pop_reduction, total_endagered))  # if population is reduced display this to the user

        else:
            pop_reduction = country_pop_data[-1] - \
                country_pop_data[0]
            print('A Population growth of {:.0f} has resulted in {:.0f} endangered species'.format(
                pop_reduction, total_endagered))  # otherwise display this

    def display_indagered_species(self, threatened_species):
            print("{} endagered species:".format(self.country))
            print(
                "Plants: {:.0f}\nFish: {:.0f}\nBirds: {:.0f}\nMammals: {:.0f}".format(threatened_species[0], threatened_species[1], threatened_species[2], threatened_species[3]))
