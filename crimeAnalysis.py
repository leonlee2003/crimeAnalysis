from cleanCrimeData import clean_data
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import itertools


crimeStats = clean_data()


pd.set_option('display.width', 20000)

perCapitaCrimes = list(crimeStats.columns)[11:-1]

y = crimeStats['MajorMetro']
for i in range(1, 10):
    mostAccurate = pd.DataFrame({'combo':0, 'accuracy':0}, index=[0])   
    for index, combo in enumerate(itertools.combinations(perCapitaCrimes, i)):
        X = crimeStats[list(combo)]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=42, stratify=y)
        knn = KNeighborsClassifier(n_neighbors = 5)
        knn.fit(X_train, y_train)
        mostAccurate = mostAccurate.append({'combo': combo, 'accuracy': knn.score(X_test, y_test)}, ignore_index=True)
    mostAccurate = mostAccurate.drop(mostAccurate.index[0])
    mostAccurate = mostAccurate.sort_values('accuracy', ascending=False)
    print('---------------------')
    print(mostAccurate.iloc[0:5])
