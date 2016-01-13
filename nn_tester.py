# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 19:28:14 2015

@author: sunand
"""

# -*- coding: utf-8 -*-
#Name: Sunand Iyer
#UNI: sri2117
#Code contains a main function that tests the accuracy of the 
#classifier created in the nn.py file


import nn
import numpy as np


def main():
    '''Main function that calculates the accuracy of the 
    classifier using the breast cancer data set and the 
    synthetic data set'''
    
    #read in the file and separate by commas
    inFile = np.genfromtxt('wdbc.data.txt', delimiter = " ")
    #delete patient IDs
    inFile = np.delete(inFile, 0 , 1)
    syntheticData = nn.createMultivariate(300)
    BCDict = {}
    synDict = {}
    for i in range(3):
        if i == 0:
            metric = 'euclidean'
        elif i == 1:
            metric = 'cityblock'
        elif i == 2:
            metric = 'cosine'
        k = 1
        bestBCAvg = 0
        bestSynAvg = 0
        while k <= 15:
            bcDataOutput = []
            syntheticOutput = []
            for j in range(100):
                bcDataTest = nn.n_validator(inFile, 5, nn.KNNclassifier, k,
                    metric)
                #append accuracy values for the given k value
                bcDataOutput.append(bcDataTest)
                syntheticValidator = nn.n_validator(syntheticData, 5, 
                nn.KNNclassifier, k, metric)
                syntheticOutput.append(syntheticValidator)  
            curBCAvg = sum(bcDataOutput) / len(bcDataOutput)
            curSynAvg = sum(syntheticOutput) / len(syntheticOutput)
            #replace the value for the best average and best k value
            if curBCAvg > bestBCAvg:
                bestBCAvg = curBCAvg
                kBestBC = k
            if curSynAvg > bestSynAvg:
                bestSynAvg = curSynAvg
                kBestSyn = k
            k += 2
        #store the accuracy value for each metric
        BCDict[metric] = (kBestBC, bestBCAvg)
        synDict[metric] = (kBestSyn, bestSynAvg)
    
    newBC = {}
    newSyn = {}
    #get the best k and distance metric combo
    for keys in BCDict:
        newBC[keys] = BCDict[keys][1]
    maxBCDist = max(newBC, key = newBC.get)
    bestKValBC = BCDict[maxBCDist][0]
    for keys in synDict:
        newSyn[keys] = synDict[keys][1]
    maxSynDist = max(newSyn, key = newSyn.get)
    bestKValSyn = synDict[maxSynDist][0]
        
    print("Best k values using euclidean distance metric \n"
    "     Breast Cancer Data Set: {} with an accuracy of {} \n"
    "     Synthetic Data Set: {} with an accuracy of {}".format(
    BCDict['euclidean'][0], BCDict['euclidean'][1], 
    synDict['euclidean'][0], synDict['euclidean'][1]))
    print("Best k values using cityblock distance metric \n"
    "     Breast Cancer Data Set: {} with an accuracy of {} \n"
    "     Synthetic Data Set: {} with an accuracy of {}".format(
    BCDict['cityblock'][0], BCDict['cityblock'][1], 
    synDict['cityblock'][0], synDict['cityblock'][1]))
    print("Best k values using cosine distance metric \n"
    "     Breast Cancer Data Set: {} with an accuracy of {} \n"
    "     Synthetic Data Set: {} with an accuracy of {}".format(
    BCDict['cosine'][0], BCDict['cosine'][1], 
    synDict['cosine'][0], synDict['cosine'][1]))
    
    print("Best metric for {} is {} with a k value of {} \n"
    "and an accuracy of {}".format(
    'Breast Cancer', maxBCDist, bestKValBC, BCDict[maxBCDist][1])) 
    print("Best metric for {} is {} with a k value of {} \n"  
    "and an accuracy of {}".format(
    'Synthetic Data', maxSynDist, bestKValSyn, synDict[maxSynDist][1]))


main()

    
    
    

    
