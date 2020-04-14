#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions
glucose,hemoglobin,classification = kmc.openckdfile()
hemoglobin_scaled,glucose_scaled,classification = kmc.normalizeData(glucose,hemoglobin,classification)
centroid = kmc.createCentroid(2)
min_index,distance = kmc.assign_centroid(2,centroid,glucose_scaled,hemoglobin_scaled)
centroid = kmc.update_centroid(2, min_index, glucose,hemoglobin)
kmc.graphingKMeans(glucose,hemoglobin,min_index,centroid)
true_positives, false_positives,true_negatives, false_negatives, CKD, no_CKD = kmc.positives_or_negatives(classification,min_index)
truePos_percent,falsePos_percent,trueNeg_percent,falseNeg_percent = kmc.percentages(true_positives,false_positives,true_negatives, false_negatives, CKD, no_CKD)
print(kmc.percentages(true_positives,false_positives,true_negatives, false_negatives, CKD, no_CKD))
