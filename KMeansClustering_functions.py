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
#   assignment[min_index] = min_index
    
    return min_index,distance

def update_centroid(k, min_index, glucose, hemoglobin):
    #First, I created a random point for hemoglobin and glucose. Then, I assigned the random point to a centroid.
    #Found mean for both assignments of glucose and hemoglobin
    #Updates cluster location based on the average
    #Has 4 parameters: k, min_index, glucose, hemoglobin
    #Returns centroid
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
#This function graphs the KMeans data
#Uses random colors to graph the different clusters
#this is a void function
    plt.figure()
    for i in range(min_index.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[min_index==i],glucose[min_index==i],"o",label="Class"+str(i),color=rcolor)
        plt.plot(centroid[i, 0], centroid[i, 1], "+", label = "Centroid " + str(i), color = rcolor)
    plt.title("K Means Clustering")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show
    
def positives_or_negatives(classification,min_index):
#This function uses counters to find the amount of true pos, false pos, true neg, and false neg
#has 2 parameters, classification and min_index
#returns true_positives, false_positives,true_negatives, false_negatives, CKD, no_CKD
    true_positives = 0
    false_positives = 0
    true_negatives = 0
    false_negatives = 0
    CKD = 0
    no_CKD = 0
    for i in range(158):
        if classification[i] == 0 and min_index[i] == 0:
            CKD += 1
            true_positives += 1
        elif classification[i] == 0 and min_index[i] == 1:
            false_negatives +=1
            no_CKD += 1
        elif classification[i] == 1 and min_index[i] == 0:
            no_CKD +=1
            false_positives += 1
        elif classification[i] == 1 and min_index[i] == 1:
            no_CKD += 1
            true_negatives += 1
    return  true_positives, false_positives,true_negatives, false_negatives, CKD, no_CKD

def percentages(true_positives,false_positives,true_negatives, false_negatives, CKD, no_CKD):
#This function finds the rate for true pos, true neg, false pos, and false neg.
#Has 6 parameters: true_positives,false_positives,true_negatives, false_negatives, CKD, no_CKD
#Returns truePos_percent,falsePos_percent,trueNeg_percent,falseNeg_percent
    truePos_percent = "True positives Rate:" + str((true_positives/CKD)* 100)+"percent"
    falsePos_percent = "False positives Rate:" + str((false_positives/no_CKD)*100)+ "percent"
    trueNeg_percent = "True negatives Rate:" + str((true_negatives/no_CKD)*100)+ "percent"
    falseNeg_percent = "False megatives Rate:" + str((false_negatives/CKD)*100)+ "percent"
    return truePos_percent,falsePos_percent,trueNeg_percent,falseNeg_percent
    
            
            
            
        



