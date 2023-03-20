import pandas as pd
import pycountry_convert as pc

def country_to_continent(country_name):
    #print(country_name)
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    #print(country_alpha2)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name

def add_continent_column(df):
    df['Continent'] = df.apply(lambda row: country_to_continent(row.Country), axis=1)
    return df


df = pd.read_csv('CO2_data/megatons_CO2.csv')


#below: removing all years before 1950 because there is no data for any of them in the data set

df = df[df['Year'] >= 1950]



#below: removing "countries" from data set because they cannot be converted to a country and also have no relevant info

df = df[df['Country'] != 'Antarctica']
df = df[df['Country'] != 'Kuwaiti Oil Fires']
df = df[df['Country'] != 'International Transport']
df = df[df['Country'] != 'Global']




#TO DO: FIGURE OUT REGEX! Below: Sorting out annoying countries

df = df.replace('Bonaire, Saint Eustatius and Saba', 'Netherlands', regex = True)
df = df.replace('Faeroe Islands', 'Denmark', regex = True)
df = df.replace('Micronesia (Federated States of)', 'United States', regex = False)
df = df.replace('Panama Canal Zone', 'Panama', regex = False)
df = df.replace('French Equatorial Africa', 'France', regex = False)
df = df.replace('French West Africa', 'France', regex = False)
df = df.replace('Kosovo', 'Serbia', regex = False)
df = df.replace('Leeward Islands', 'United States', regex = False)
df = df.replace('Occupied Palestinian Territory', 'Palestine', regex = False)
df = df.replace('Pacific Islands (Palau)', 'Palau', regex = False)
df = df.replace('Ryukyu Islands', 'Japan', regex = False)
df = df.replace('Saint Helena', 'United Kingdom', regex = False)
df = df.replace('Sint Maarten (Dutch part)', 'Saint Martin', regex = False)
df = df.replace('St. Kitts-Nevis-Anguilla', 'United Kingdom', regex = False)
df = df.replace('Timor-Leste', 'Indonesia', regex = False)
df = df.replace('Wallis and Futuna Islands', 'France', regex = False)



#below: adding a continent column to assist in easier visualization and analysis

df = add_continent_column(df)






print (df)

