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

# The digits dataset
digits = datasets.load_digits()
#Added by Raghu
#List Of tuples - Where first element represents 2d numpy array representing a digit and the second element represents label (digit itself)
#zip function takes two equal length collections and merges them together in pairs
images_and_labels = list(zip(digits.images, digits.target))

for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)
plt.show()

# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:   < Added by Raghu: same fashion as the data in csv format.>

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))    

# Create a classifier: a support vector classifier
classifier = svm.SVC(gamma=0.001)

# We learn the digits on the first half of the digits
classifier.fit(data[:n_samples / 2], digits.target[:n_samples / 2])

# Now predict the value of the digit on the second half:
expected = digits.target[n_samples / 2:]
predicted = classifier.predict(data[n_samples / 2:])
print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))


images_and_predictions = list(zip(digits.images[n_samples / 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)

plt.show()