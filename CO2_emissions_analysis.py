import pandas as pd
import pycountry_convert as pc
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt



# Defining a function to return a continent based on country name passed in 
# from https://stackoverflow.com/questions/55910004/get-continent-name-from-country-using-pycountry

def country_to_continent(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name

# Adding continent column based on country name

def add_continent_column(df):
    df['Continent'] = df.apply(lambda row: country_to_continent(row.Country), axis=1)
    return df

# Visualizing data dynamically as line grpahs

def plot_data(df, column, graph_title):



    # Summing emissions by continent

    df_europe = df[df['Continent'] == 'Europe']
    df_europe = df_europe.groupby('Year').sum(numeric_only = True)

    df_na = df[df['Continent'] == 'North America']
    df_na = df_na.groupby('Year').sum(numeric_only = True)

    df_asia = df[df['Continent'] == 'Asia']
    df_asia = df_asia.groupby('Year').sum(numeric_only = True)

    df_africa = df[df['Continent'] == 'Africa']
    df_africa = df_africa.groupby('Year').sum(numeric_only = True)

    df_sa = df[df['Continent'] == 'South America']
    df_sa = df_sa.groupby('Year').sum(numeric_only = True)

    df_oceania = df[df['Continent'] == 'Oceania']
    df_oceania = df_oceania.groupby('Year').sum(numeric_only = True)



    # Plotting emissions as line graph

    ax = plt.plot(df_europe[column], label = 'Europe')

    ax = plt.plot(df_na[column], label = 'North America')

    ax = plt.plot(df_asia[column], label = 'Asia')

    ax = plt.plot(df_africa[column], label = 'Africa')

    ax = plt.plot(df_sa[column], label = 'South America')

    ax = plt.plot(df_oceania[column], label = 'Oceania')


    plt.legend(title = 'Region', title_fontsize = 16)
    plt.ylabel('Megatons CO2')
    plt.xlabel('Year')
    plt.title(graph_title)
    plt.show()


def clean_data(df):

    #below: removing all years before 1950 because there is no data for any of them in the data set

    df = df[df['Year'] >= 1950]


     #below: removing entries from data set that do not represent actual countries and/or have no relevant data

    df = df[df['Country'] != 'Antarctica']
    df = df[df['Country'] != 'Kuwaiti Oil Fires']
    df = df[df['Country'] != 'International Transport']
    df = df[df['Country'] != 'Global']


    #Sorting out data records not recognized as countries by pycountry 

    df = df.replace('Bonaire, Saint Eustatius and Saba', 'Netherlands')
    df = df.replace('Faeroe Islands', 'Denmark')
    df = df.replace('Micronesia (Federated States of)', 'United States')
    df = df.replace('Panama Canal Zone', 'Panama')
    df = df.replace('French Equatorial Africa', 'France')
    df = df.replace('French West Africa', 'France')
    df = df.replace('Kosovo', 'Serbia')
    df = df.replace('Leeward Islands', 'United States')
    df = df.replace('Occupied Palestinian Territory', 'Palestine')
    df = df.replace('Pacific Islands (Palau)', 'Palau')
    df = df.replace('Ryukyu Islands', 'Japan')
    df = df.replace('Saint Helena', 'United Kingdom')
    df = df.replace('Sint Maarten (Dutch part)', 'Saint Martin')
    df = df.replace('St. Kitts-Nevis-Anguilla', 'United Kingdom')
    df = df.replace('Timor-Leste', 'Indonesia')
    df = df.replace('Wallis and Futuna Islands', 'France')

    return df

# Reading data from csv

df = pd.read_csv('CO2_data/megatons_CO2.csv')

df = clean_data(df)



#below: adding a continent column to assist in easier visualization and analysis

df = add_continent_column(df)


plot_data(df, 'Total', 'CO2 Emissions (Total)')

plot_data(df, 'Per Capita', 'CO2 Emissions (Per Capita Total)')

plot_data(df, 'Coal', 'CO2 Emission (Coal)')

plot_data(df, 'Oil', 'CO2 Emissions (Oil)')

plot_data(df, 'Gas', 'CO2 Emissions (Gas)')

plot_data(df, 'Cement', 'CO2 Emissions (Cement)')

plot_data(df, 'Flaring', 'CO2 Emissions (Flaring)')

plot_data(df, 'Other', 'CO2 Emissions (Other)')













              


