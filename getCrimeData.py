import pandas as pd

crimeData_2015 = pd.read_excel('Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2015.xls', skiprows=3, skipfooter=10, index_col=[0,1])


crimeData_2015 = crimeData_2015.rename(columns={'Violent\ncrime':'Violent Crime',
                                                'Murder and\nnonnegligent\nmanslaughter':'Murder and NN Manslaughter',
                                                'Rape\n(revised\ndefinition)1':'Rape newDef',
                                                'Rape\n(legacy\ndefinition)2':'Rape oldDef',
                                                'Aggravated\nassault':'Ag Assault',
                                                'Property\ncrime': 'Property Crime',
                                                'Larceny-\ntheft':'Larceny',
                                                'Motor\nvehicle\ntheft':'Motor Vehicle Theft'
                                                })


