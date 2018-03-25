from getCrimeData import get_crime_data
import pandas as pd



def clean_data():
    crimeData = get_crime_data()

    crimeData1 = crimeData.drop(crimeData[crimeData['Rape newDef'].isnull()].index).rename(columns={'Rape newDef':'Rape'})
    del crimeData1['Rape oldDef']

    crimeData2 = crimeData.drop(crimeData[crimeData['Rape oldDef'].isnull()].index).rename(columns={'Rape oldDef':'Rape'})
    del crimeData2['Rape newDef']
    
    crimeStats = pd.concat([crimeData1, crimeData2], axis=0)

    crimeStats['Arson3'] = crimeStats['Arson3'].fillna(crimeStats['Arson3'].mean())
    
    crimes = list(crimeStats.columns)
    for crime in crimes:
            crimeStats[crime+'PerCapita'] = crimeStats[crime]/crimeStats['Population']
    crimeStats = crimeStats.drop('PopulationPerCapita', axis=1)
    crimeStats['MajorMetro']=pd.DataFrame(crimeStats['Population'] > 50000).astype(int)

    #Wanted to convert all appropriate columns to int starting with violent crime
    #didn't really keep the output from being written in scientific notation
    #crimeStats[crimeStats['Violent Crime'].notna()]['Violent Crime'].astype(int)
    
    return crimeStats


