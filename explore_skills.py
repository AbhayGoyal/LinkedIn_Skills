import pandas as pd
import seaborn as sns

df = pd.read_excel('LinkedIn Top Skills.xlsx')

print(df.head())

print(set(df['Year']))
print(set(df['Skill']))
print(df.groupby('Country').count())
out = pd.value_counts(df['Skill'].values)
print(out)

#print(df.groupby('Skill').count())

def getRank(val):
    for index,row in df.iterrows():
        if(row['Skill'] == val and row['Country'] == 'Canada'):
            print("Canada")
            print(row['Year'], row['Rank'])
        if (row['Skill'] == val and row['Country'] == 'India'):
            print("India")
            print(row['Year'], row['Rank'])
        if (row['Skill'] == val and row['Country'] == 'United States'):
            print("United States")
            print(row['Year'], row['Rank'])
    return 1

countries =[]

def getRank1(val):
    for index,row in df.iterrows():
        if(row['Skill'] == val):
            countries.append(row['Country'])
    return countries


#def byCountries():

def getRank2(val):
    for index,row in df.iterrows():
        if(row['Skill'] == val):
            print(row['Country'],row['Year'],row['Rank'])
    return 1

def getRank3(val):
    for index,row in df.iterrows():
        if(row['Country'] == val and row['Rank'] == 1 and row['Year'] == 2014):
            print(row['Skill'])
    return 1


num = getRank('Network and Information Security')
values = getRank3('United States')
#print(values)
#countries = getRank1('Data Engineering and Data Warehousing')
#print(set(countries))




