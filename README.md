This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

To run the code:

For my NearestNeighborClassification.py, just run the code. You will see 2 graphs. The first is a graph with the normalized values of hemoglobin and glucose; the second is the same graph except with the test case.

For my KMeansClustering_Functions.py, this is just the code that holds the functions, so it does not need to run. This is the code that will be carried out in the driver.


For my KMeansClustering_Driver.py, here you will see the graphs with a different # of clusters. You need to plug in a value for K for this to work.




Located in KMeansClustering_functions.py file:




normalizeData(glucose, hemoglobin, classification)

This function normalizes the values of the given glucose and hemoglobin values. It normalizes it on a scale from 0 to 1, with no units. This function has 3 parameters: glucose, hemoglobin, and classification and returns 3 values: hemoglobin_scaled, glucose_scaled, classification.




createCentroid(k)

This function is creating a random # of centroids, k. Has one parameter k and returns centroid, an array that represents the centroids that were created.




assign_centroid(k,centroid,glucose,hemoglobin)

This function is assigning the centroids to a data point. Has 4 parameters: k,centroids,glucose, and hemoglobin. It calculates the distance from each point to each centroid and uses min index to assign it to the nearest one. It returns min_index.




update_centroid(k, min_index, glucose, hemoglobin)

First, I created a random point for hemoglobin and glucose. Then, I assigned the random point to a centroid. Found mean for both assignments of glucose and hemoglobin. Updates cluster location based on the average. Has 4 parameters: k, min_index, glucose, hemoglobin. Returns centroid




iteration(k,trials)

This function iterates the updated centroid by running for an amount of times that the user wants until it hits zero. Has 2 parameters: k and trials, the amount of times it will run. Returns assign_centroid,centroids,glucose,hemoglobin,classification.




graphingKMeans(glucose,hemoglobin,min_index,centroid)

This function graphs the KMeans data for the number of clusters you plug in for K. Uses random colors to graph the different clusters. Has 4 parameters: glucose, hemoglobin, min_index, and centroid. This is a void function.




positives_or_negatives(classification,min_index)

This function uses counters to find the amount of true pos, false pos, true neg, and false neg. Has 2 parameters, classification and min_index. Returns true_positives, false_positives,true_negatives, false_negatives, CKD, no_CKD.




percentages(true_positives,false_positives,true_negatives, false_negatives, CKD, no_CKD)

This function finds the rate for true pos, true neg, false pos, and false neg. Has 6 parameters: true_positives,false_positives,true_negatives, false_negatives, CKD, no_CKD. Returns truePos_percent,falsePos_percent,trueNeg_percent,falseNeg_percent


