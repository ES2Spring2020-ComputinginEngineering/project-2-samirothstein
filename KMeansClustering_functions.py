#Please place your FUNCTION code for step 4 here.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math
#functions

def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification



def normalizeData(glucose, hemoglobin, classification):
    g_min = glucose.min()
    g_max = glucose.max()
    h_min = hemoglobin.min()
    h_max = hemoglobin.max() 
    hemoglobin_scaled = ((hemoglobin - h_min)/(h_max-h_min))
    glucose_scaled = ((glucose - g_min)/(g_max-g_min))
    return (hemoglobin_scaled, glucose_scaled, classification)



def centroid(k):
    #this function is creating random centroids, k
    #2 comes from the amount of features we have
    array = np.random.rand(k,2)
    return array
    


def assign_centroid(k,centroids,glucose,hemoglobin):
    #creates an array with the same amount of rows as centroids
    #the # of columns is equal to amount of data points for hemoglobin
    distance_array = np.zeros((k,len(hemoglobin)))
    for i in range(k):
        distance = np.sqrt((hemoglobin-array[i,0])**2 + (glucose-array[i,1])**2)
        #this calculates the distance between each data point to each centroid








#main script
hemoglobin_scaled,glucose_scaled,classification = normalizeData(glucose,hemoglobin,classification)
