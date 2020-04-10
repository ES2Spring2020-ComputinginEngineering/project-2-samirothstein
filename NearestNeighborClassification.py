#Please put your code for Step 2 and Step 3 in this file.


import numpy as np
import matplotlib.pyplot as plt
#import random

#global variables


# FUNCTIONS
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification



def normalizeData(glucose, hemoglobin, classification):
    
    g_min = glucose.min()
    g_max = glucose.max()
    h_min = hemoglobin.min()
    h_max = hemoglobin.max()
   # matplotlib.colors.Normalize(g_min=None, g_max=None, clip=False)
   #not sure what this does
    
    
    hemoglobin_scaled = ((hemoglobin - h_min)/(h_max-h_min))
    glucose_scaled = ((glucose - g_min)/(g_max-g_min))
    return (hemoglobin_scaled, glucose_scaled, classification)
#print(normalizeData(glucose_scaled,hemoglobin_scared,classification)

def graphData(glucose, hemoglobin, classification):
   plt.figure()
   plt.plot(hemoglobin_scaled[classification==1],glucose_scaled[classification==1], "k.", label = "Class 1")
   plt.plot(hemoglobin_scaled[classification==0],glucose_scaled[classification==0], "r.", label = "Class 0")
   plt.xlabel("Hemoglobin")
   plt.ylabel("Glucose")
   plt.legend()
    
def testCase():
    newhemoglobin = np.random.random_sample()
    newglucose = np.random.random_sample()
    return (newhemoglobin, newglucose)


def distanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
    distance_array=np.sqrt((hemoglobin - newhemoglobin)**2 + (glucose - newglucose)**2)
    return distance_array


def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    distance = distanceArray(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled)
    min_index = np.argmin(distance)
    nearest_class = classification[min_index]
    return nearest_class


def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classificiation):
    plt.figure()
    plt.plot(hemoglobin_scaled[classification==1],glucose_scaled[classification==1], "k.", label = "No CKD")
    plt.plot(hemoglobin_scaled[classification==0],glucose_scaled[classification==0], "r.", label = "Has CKD")
    plt.plot(newhemoglobin,newglucose,'o')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.title('Graph with test case')
  

def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
   class_0 = 0
   class_1 = 0
   final_class = 0
    
   distance = distanceArray(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled)
   sorted_indices = np.argsort(distance)
   k_indices = sorted_indices[:k]
   k_classifications = classification[k_indices]
#   k_class = np.median(k_classifications)
   for i in k_classifications:
    if i == 1:
        class_1 = class_1 + 1
    if i == 0:
        class_0 = class_0 + 1
   if class_0 > class_1:
       final_class = 0.0
   if class_1 > class_0:
       final_class = 1.0
        
   print(k_classifications,final_class)  
    
   return k_classifications,final_class
#    counter = 0
#    for i in k_classifications:
#        
#    return k_classifications
    

# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
hemoglobin_scaled,glucose_scaled,classification = normalizeData(glucose,hemoglobin,classification)
newglucose,newhemoglobin = testCase()
graphData(glucose, hemoglobin, classification)
graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification)
(nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification))
k_class,final_class = kNearestNeighborClassifier(111, newglucose, newhemoglobin, glucose, hemoglobin, classification)





