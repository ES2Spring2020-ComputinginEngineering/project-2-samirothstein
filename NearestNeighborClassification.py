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
   plt.show()
    
def testCase():
    newhemoglobin = np.random.random_sample()
    newglucose = np.random.random_sample()
    return (newhemoglobin, newglucose)


def distanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
    np.sqrt((hemoglobin - newhemoglobin)**2 + (glucose - newglucose)**2)


distanceArray(newglucose, newhemoglobin, glucose, hemoglobin)


# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()




hemoglobin_scaled,glucose_scaled,classification = normalizeData(glucose,hemoglobin,classification)

plt.figure()
plt.plot(hemoglobin_scaled[classification==1],glucose_scaled[classification==1], "k.", label = "Class 1")
plt.plot(hemoglobin_scaled[classification==0],glucose_scaled[classification==0], "r.", label = "Class 0")
plt.xlabel("Hemoglobin")
plt.ylabel("Glucose")
plt.legend()
plt.show()



graphData(glucose, hemoglobin, classification)
