# -*- coding: utf-8 -*-
"""
Created on Fri May 26 15:20:01 2017

#Digit Recognition for V & V

#Following note added by Raghu
Note: 
1. The actual digits data from the http://archive.ics.uci.edu/ml/datasets/Pen-Based+Recognition+of+Handwritten+Digits is different than the one referred in this sklearn example
2. For more info, refer this link http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html and the above one.
3. The digits data referred by this Sklearn example can be downloaded from the following link.
https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/data/digits.csv.gz
"""

# Standard scientific Python imports
import matplotlib.pyplot as plt

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics

import numpy as np
import _pickle as cPickle

digits = np.loadtxt('digits_Train.csv', delimiter = ',')
digits_images_flat = digits[:, :-1] #Every array is 1x64
digits_images =  digits_images_flat.view()
digits_images.shape = (-1,8,8)
digits_target = digits[:,-1].astype(np.int) #Label

#Load Test Data

digits_test = np.loadtxt('digits_Test.csv', delimiter = ',')
digits_test_images_flat = digits_test[:, :-1] #Every array is 1x64
digits_test_images =  digits_test_images_flat.view()
digits_test_images.shape = (-1,8,8)
digits_test_target = digits_test[:,-1].astype(np.int) #Label
# The digits dataset
#digits = datasets.load_digits()
#Added by Raghu
#List Of tuples - Where first element represents 2d numpy array representing a digit and the second element represents label (digit itself)
#zip function takes two equal length collections and merges them together in pairs
images_and_labels = list(zip(digits_images, digits_target))

#for index, (image, label) in enumerate(images_and_labels[:4]):
#    plt.subplot(2, 4, index + 1)
#    plt.axis('off')
#    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
#    plt.title('Training: %i' % label)
#plt.show()

# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:   < Added by Raghu: same fashion as the data in csv format.>

n_samples = len(digits_images)
#data = digits_images.reshape((n_samples, -1))    

# Create a classifier: a support vector classifier
classifier = svm.SVC(gamma=0.001) #default is ovo

# We learn the digits on the digits_Train.csv
classifier.fit(digits_images_flat, digits_target)

# Now predict the value of the digit on the second half:
expected = digits_test_target
predicted = classifier.predict(digits_test_images_flat)
print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
print("accuracy:", metrics.accuracy_score(expected, predicted))

images_and_predictions = list(zip(digits_test_images, predicted))
#for index, (image_test, prediction) in enumerate(images_and_predictions[:2]):
#    plt.subplot(2, 4, index + 5)
#    plt.axis('off')
#    plt.imshow(image_test, cmap=plt.cm.gray_r, interpolation='nearest')
#    plt.title('Prediction: %i' % prediction)
#
#plt.show()

#Save the output
np.savetxt("output.txt",classifier.decision_function(digits_test_images_flat))
outputData = {'data_array' : metrics.confusion_matrix(expected, predicted)}

with open("output.pkl",'wb') as outputFile:
	cPickle.dump(outputData,outputFile)

with open("model.pkl",'wb') as modelFile:
	cPickle.dump(classifier,modelFile)