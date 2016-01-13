# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 19:14:49 2015

@author: sunand
"""

import numpy as np
from scipy.spatial import distance


def partitionData(data, p):
    '''Takes in data and shuffles the rows. It then splits it into 
    p parts'''
    
    np.random.shuffle(data)
    outputList = np.array_split(data, p)
    return(outputList)
    
    
def compareTest(data, training, test, classifier, i, *args):
    '''Takes in data, the training data, test data, classifier function,
    and the index. Returns how accurate the classifier was '''
    
    outArray = classifier(training, test, *args)
    #get the correct test values
    testActual = data[i][:,0]
    return(np.sum(outArray == testActual) / len(testActual))
    
    
def KNNclassifier(training, test, k = 1, metric = 'euclidean'):
    '''Takes in a training array and a test array. Function finds the k
    closest observations in the training array for each observation in the
    test array and uses that to label the test observation'''
    
    trainingData = np.delete(training, 0, 1)
    #create an array with distances
    distanceMatrix = distance.cdist(trainingData, test, metric)
    #sort by column so the first row contains the smallest distances 
    #for each test observation
    sortedDistanceIndex = np.argsort(distanceMatrix, 0)
    #get the labels from the training set for the k number of test values
    labeledIndexes = training[sortedDistanceIndex[0:k], 0]
    outputLabels = np.zeros(len(labeledIndexes[0]))
    for i in range(len(labeledIndexes)):
        #add up all the values
        outputLabels += labeledIndexes[i]
    #since k is odd if the value is greater than k // 2 then there 
    #must be more 1 than 0
    for i in range(len(outputLabels)):
        if outputLabels[i] > k // 2:
            outputLabels[i] = 1
        else:
            outputLabels[i] = 0
    return(outputLabels)


def n_validator(data, p, classifier, *args):
    '''takes in data, p, and a classifier. Divided data into p parts and then
    uses the classifier function to classify the test data. Returns how
    accurate the classifier is'''
    
    partitionedData = partitionData(data, p)
    outputNum = []
    #iterate through each value of p so each divided part will be 
    #a test set
    for i in range(p):
        test = partitionedData[i][:,1:]
        #use this create a numpy array with does not contain the array
        #that is being used for the test
        training = np.concatenate([array for j, array in 
        enumerate(partitionedData) if j != i])
        outputNum.append(compareTest(partitionedData, training, test, 
                                 classifier, i, *args))
    return(sum(outputNum) / len(outputNum))  
    
    
def createindArrays(size, mean, cov):
    '''Function creates an array using the given statistical
    parameter'''
    
    mvArray0 = np.random.multivariate_normal(mean, cov, size)
    mvArray0.shape = size*2, 1
    #horizontally stack the two arrays so there are 2 columns
    array0 = np.hstack((mvArray0[:300],mvArray0[300:]))
    return(array0)
    

def combineLabels(array, labels):
    '''function combines the labels and the array with the data'''
    
    labels.shape = len(labels),1
    return(np.hstack((labels, array)))


def createMultivariate(size):
    '''Creates the synthetic data set'''
    
    mean1 = [2.5, 3.5]
    mean2 = [.5 , 1]
    cov1 = [[1,1], [1,4.5]]
    cov2 = [[2,0],[0,1]]
    
    array0 = createindArrays(size, mean1, cov1)
    labels0 = np.zeros(size).astype(int)
    array0 = combineLabels(array0, labels0)
    array1 = createindArrays(size, mean2, cov2)
    labels1 = np.ones(size).astype(int)
    array1 = combineLabels(array1, labels1)    
    
    outputArray = np.vstack((array0, array1))
    return(outputArray)