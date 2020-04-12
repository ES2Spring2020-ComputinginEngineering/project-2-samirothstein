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



def createCentroid(k):
    #this function is creating a random # of centroids, k
    #has one parameter k and returns centroid, an array
    centroid = np.random.rand(k,2)
    return centroid
    

   
def assign_centroid(k,centroid,glucose,hemoglobin):
#This function is assigning the centroids to a data point
#Has 4 parameters; k,centroids,glucose,hemoglobin
#returns min_index
    distance_array = np.zeros((len(hemoglobin),k))
    min_index = np.zeros(len(hemoglobin))
    for i in range(k):
        distance = np.sqrt((hemoglobin-centroid[i,0])**2 + (glucose-centroid[i,1])**2)
        distance_array[:,i] = distance
    min_index = np.argmin(distance_array, axis=1)
#    assignment[min_index] = min_index
    return min_index,distance

def update_centroid(k, min_index, glucose, hemoglobin):
    #First, I created a random point. Then, I assigned the random point to a centroid.
    #Created double for loop, that appended the value of glucose/hemo at which it was 
    #at which hemo that corresponded to certain classification value
    #Found mean for both Class value of hemo and glucose
    #Has 5 parameters: centroid,glucose,hemoglobin,k,min_index
    #Returns mean_hemo,mean_gluc,centroid
#    mean_hemo = 0
#    mean_gluc = 0
#    gluc_classValues = np.array([])
#    hemo_classValues = np.array([])
##create new point
##    new_point = np.random.random_sample()
#    centroid = assign_centroid(k,centroid,glucose,hemoglobin)
#    for i in range (k):
#        for j in (range(len(min_index))):
#            if min_index[j] == i:
#                gluc_classValues=np.append(gluc_classValues, glucose[j])
#                hemo_classValues=np.append(hemo_classValues,hemoglobin[j])
#        mean_gluc = np.mean(gluc_classValues)
#        mean_hemo = np.mean(hemo_classValues)
#        centroid[i,1] = mean_gluc
#        centroid[i,0] = mean_hemo
#    return (mean_hemo,mean_gluc,centroid)
   
    hemoglobin_centroid = np.zeros((1))
    glucose_centroid = np.zeros((1))
    centroid = np.zeros((k,2))
    for i in range(centroid.shape[0]):
        hemoglobin_centroid = np.mean(hemoglobin[min_index == i])
        glucose_centroid= np.mean(glucose[min_index == i])
        centroid[i] = np.append(hemoglobin_centroid, glucose_centroid) 
    return centroid
    
    
    
    
    

def iteration(k,trials):
#This function iterates the updated centroid by running for an amount of times that the user wants
#Until it hits zero
#Has 2 paramters: k and trials, the amount of times it will run
#Returns assign_centroid,centroids,glucose,hemoglobin,classification
    glucose,hemoglobin,classification = openckdfile()
    glucose,hemoglobin,classification = normalizeData(glucose, hemoglobin, classification)
    centroid = createCentroid(k)
    while trials != 0:
        centroids = assign_centroid(k,centroid,glucose,hemoglobin)
        centroids = (update_centroid,centroid,glucose,hemoglobin,k,min_index)
        trials -= 1
    return (assign_centroid,centroids,glucose,hemoglobin,classification)


def graphingKMeans(glucose,hemoglobin,min_index,centroid):
    plt.figure()
    for i in range(min_index.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[min_index==1],glucose[min_index==1],"o",label="Class"+str(i),color=rcolor)
        plt.plot(centroid[i, 0], centroid[i, 1], "o", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show


glucose,hemoglobin,classification = openckdfile()
hemoglobin_scaled,glucose_scaled,classification = normalizeData(glucose,hemoglobin,classification)
centroid = createCentroid(2)
min_index,distance = assign_centroid(2,centroid,glucose_scaled,hemoglobin_scaled)
#mean_hemo,mean_gluc,centroid = update_centroid(2,centroid,glucose,hemoglobin,min_index)
centroid = update_centroid(2, min_index, glucose,hemoglobin)

graphingKMeans(glucose,hemoglobin,min_index,centroid)
#main script
