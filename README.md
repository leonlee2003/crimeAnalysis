# crimeAnalysis

This project uses data from fbi.gov along with the k-nearest neighbors algorithm to predict whether a municipality population is over the threshold using the per capita crime rates for 10 different crimes. Every possible combiation of the features (the crimes) is used on the training data so that the user can see which combination of features most accurately predicts whether the population is over the threshold (currently at 50,000). Upon intialization 30% of the data is reserved for testing and 5 neighbors are used in the k nearest neighbors algorithm.

Eventually, this project will be used to determine how well per capita crime rates (and which per captia crime rates) can be used to predict the size of a particular population. 
