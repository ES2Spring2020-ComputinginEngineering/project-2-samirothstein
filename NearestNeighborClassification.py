#Please put your code for Step 2 and Step 3 in this file.


import numpy as np
import matplotlib.pyplot as plt



# FUNCTIONS
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification



def normalizeData(glucose, hemoglobin, classification):
#This functiont normalizes the values of the given glucose and hemoglobin values
#Normalizes it to a 0 or 1 with no units
#Has 3 parameters: glucose, hemoglobin, classification
#Returns 3 values: hemoglobin_scaled, glucose_scaled, classification
    g_min = glucose.min()
    g_max = glucose.max()
    h_min = hemoglobin.min()
    h_max = hemoglobin.max()
    hemoglobin_scaled = ((hemoglobin - h_min)/(h_max-h_min))
    glucose_scaled = ((glucose - g_min)/(g_max-g_min))
    return (hemoglobin_scaled, glucose_scaled, classification)


def graphData(glucose, hemoglobin, classification):
#This function graphs the data of the normalized hemoglobin and glucose values
#Has 3 parameters: glucose, hemoglobin, classification
#This is a void function
   plt.figure()
   plt.plot(hemoglobin_scaled[classification==1],glucose_scaled[classification==1], "k.", label = "Class 1")
   plt.plot(hemoglobin_scaled[classification==0],glucose_scaled[classification==0], "r.", label = "Class 0")
   plt.title("Normalized Hemoglobin vs Glucose")
   plt.xlabel("Hemoglobin")
   plt.ylabel("Glucose")
   plt.legend()
    
def testCase():
#This function creates a test case that we can use in the nearest Neighbor Classifier
#Takes no parameters
#Returns newhemoglobin and newglucose, which is the new random data point
    newhemoglobin = np.random.random_sample()
    newglucose = np.random.random_sample()
    return (newhemoglobin, newglucose)


def distanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
#This function finds the value of the distance between the test case and each data point
#Takes 4 parameters: newglucose, newhemoglobin, glucose, hemoglobin
#Returns the distance
    distance_array=np.sqrt((hemoglobin - newhemoglobin)**2 + (glucose - newglucose)**2)
    return distance_array


def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
#This function takes 5 parameters: newglucose, newhemoglobin, glucose, hemoglobin, classification
#Uses the distance array from the previous function, and finds the min index of those values
#Returns the classification of the min_index
    distance = distanceArray(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled)
    min_index = np.argmin(distance)
    nearest_class = classification[min_index]
    return nearest_class


def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classificiation):
#This functions graphs the test case along with the normalized data that we already graphed
#Has 5 parameters: newglucose, newhemoglobin, glucose, hemoglobin, classificiation
#This is a void function
    plt.figure()
    plt.plot(hemoglobin_scaled[classification==1],glucose_scaled[classification==1], "k.", label = "No CKD")
    plt.plot(hemoglobin_scaled[classification==0],glucose_scaled[classification==0], "r.", label = "Has CKD")
    plt.plot(newhemoglobin,newglucose,'o')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.title('Graph with test case')
  

def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
#This function classifies the random data point based on the k nearest neighbor method
#Has 6 parameters: k, newglucose, newhemoglobin, glucose, hemoglobin, classification
#Returns k_classifications (all the classifications) and final_class (which is the majority of classifications)
   class_0 = 0
   class_1 = 0
   final_class = 0
   distance = distanceArray(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled)
   sorted_indices = np.argsort(distance)
   k_indices = sorted_indices[:k]
   k_classifications = classification[k_indices]
   for i in k_classifications:
       if i == 1:
        class_1 = class_1 + 1
       if i == 0:
        class_0 = class_0 + 1
   if class_0 > class_1:
       final_class = 0.0
   if class_1 > class_0:
       final_class = 1.0 
   return k_classifications,final_class


# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
hemoglobin_scaled,glucose_scaled,classification = normalizeData(glucose,hemoglobin,classification)
newglucose,newhemoglobin = testCase()
graphData(glucose, hemoglobin, classification)
graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification)
(nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification))
k_class,final_class = kNearestNeighborClassifier(111, newglucose, newhemoglobin, glucose, hemoglobin, classification)





