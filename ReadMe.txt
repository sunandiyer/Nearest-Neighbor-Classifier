File Name: nn.py

Function Name: partitionData(data, p)

This is a helper function that partitions the data into p parts. It first randomly
shuffles the data. Then it uses the np.array_split function to split the data into p 
parts. This returns a list with p elements with each element being a numpy array.
The function returns this list.

Function Name: compareTest(data, training, test, classifier, i, *args)

The function takes in seven inputs. The data is a list that is the output
of the partitionData function. This list contains the correct labels for the 
test data set. The training and test inputs are the training and test data 
that will be arguments for the classification function. The classifier is the 
classification function. I is the index of the data in which is being used as the
testing data. *args can store the k value and the distance metric being used. 
The function calculates the predicted labels for the testing data using 
the classification function. The variable testActual gets the correct labels for the 
test data. It uses the index value to find which element within the list is the numpy
array with the test data. It then gets the first column which is the labels. The 
function uses the np.sum function to calculate how many labels were classified correctly.
It then divides this value by the total number of labels to return the accuracy.

Function Name: KNNclassifier(training, test, k, metric = "euclidean")

The function takes in two arrays as input, the training and test arrays. The function also
takes in the k value as input. The function also has a keyword/positional parameter set to a
default value of "euclidean". I do this because that way if the user does input a metric as 
an argument, the function still runs with the metric being euclidean. Otherwise, the user can
specify a distance metric. 
The function first deletes the first column of the training array which contained the patient labels. 
This allows the training and test array to be of the same dimension. The function then uses the 
distance.cdist function on the training Data array and the test array to calculate the 
euclidean distance. It stores the output array as a variable called distanceMatrix.
Each column in distanceMatrix represents each test observation and each row is the
distance to the respective training observation.
The function then uses the np.argsort function on distanceMatrix with the axis being 0.
The function returns an array where the first row contains the index for the training value 
closest to the test value and the second row is the index for the second closest value and so on.
The function then indexes the training set and returns an array which has the training values
corresponding to the indexes of the k number of rows containing the closest values. The function
intializes an array of all 0s that is the length of one of these rows. The function then adds the values
of all the rows. The function then iterates through each element of this array and if the sum is greater
than k // 2 it sets the value at 1. Since the value of the rows being added is either 1 or 0, if there are more
ones than zeros, the sum will be greater than k//2. Otherwise, the value is set to 0. The output labels are returned.

Function Name: n_validator(data, p, classifier, *args)

Function takes in data in the form on a numpy array. *args can store the k value and 
the distance metric that is used. The function then calls the partitionData function on 
this array and  stores the list in a variable called partitionedData. I then created an 
empty list  called outputNum which will store the different accuracy values for each iteration. 
Since the data is divided into p parts, I created a for loop that iterates through p.
In this loop, I created a variable called test which captures the numpy array element 
in the partionedData list that will be used as the test data set. This also removes the 
labels for the test. I then use list comprehension to get a list which has all the elements 
of the previous list except the numpy array being used as test. I then concatenate this list
to create an array. I then call the compareTest function with partitionedData,
training, test, classifier, i, and *args as the arguments. I append this sum to the list
outputNum. The function then finds the average of the values in outputNum and returns
this.

Function Name: createindArrays(size, mean, cov)

Function takes in an integer for size as an input that determines the size of the 
array to be created. Mean and cov are lists. The function creates an array using
the np.random.multivariate_normal function. The shape of this array is then changed 
to have 2*size rows and 1 column. The np.hstack function adds the first 300 rows
horizontally to the last 300 rows. This creates an array of 300 rows and 2 columns
which is returned.

Function Name: combineLabels(array, labels)

The function takes in two arrays, one containing the values and the other containing the labels.
The function makes the labels a 2-D array. It then horizontally stacks the labels to the array.
It returns this output array.

Function Name: createMultivariate(size)

The function takes in an input which determines the size. The 2 means and 2 covariances provided
in the assignment are hardcoded. The two arrays are created using the createindArrays and 
combineLabels functions. One array has 0s and the other arrays has 1s as their labels. The array is 
then vertically stacked using the np.vstack function and returned.

File Name: nn_tester.py

Function Name: main()

This is the main function. It reads in the file using the np.genfromtxt file with the delimiter
being space. I have preprocessed the data by replacing the 'B' and 'M' with 0 and 1 respectively.
I also replaced the commas in the text file with spaces. In the main function, I then deleted
the first column of the inFile because we do not need the patient IDs. The function then creates
the synthetic data. I then create two empty dictionaries to be used later. I use a for loop to
iterate through the three different distance metrics that I used. I then set a k value equal to 1,
a bestBCAvg to 0, and a bestSynAvg to 0. I then iterate through while k is less than or equal to 15.
For each k value I create two empty lists to store the averages for each trial for the data sets.
I call the n_validator function on the breast cancer data and the synthetic data. I then get the 
average accuracy value for the the breast cancer and synthetic data. This allows the function to 
figure out which k value is the best. If the current average is better than the best average, I
change the best average to the current average and store the k value. I then add k by 2 since we
only want odd values of k. I then use a dictionary to store the best k value and the respective 
average accuracy for each distance metric. The function then prints the results. I then create two
new dictionaries to get the best overall distance metric k value combination. The function iterates
through key in the main dictionary and adds the accuracy for the metric to the new dictionary.
The function then finds the key that is associated with the maximum accuracy value. The function 
then finds the best k value for the given key. This is the best k value distance metric combination.
The function then prints out the results.



                                                                                       
