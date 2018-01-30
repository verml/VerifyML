"""
Created on Fri May 26 15:20:01 2017

#Digit Recognition for V & V

#Following note added by RR
Note: 
1. The actual digits data from the http://archive.ics.uci.edu/ml/datasets/Pen-Based+Recognition+of+Handwritten+Digits is different than the one referred in this sklearn example
2. For more info, refer this link http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html and the above one.
3. The digits data referred by this Sklearn example can be downloaded from the following link.
https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/data/digits.csv.gz
"""



import matplotlib.pyplot as plt


from sklearn import datasets, svm, metrics

import numpy as np
import _pickle as cPickle

digits = np.loadtxt('digits_Train.csv', delimiter=',')
digits_images_flat = digits[:,:(-1)]
digits_images = digits_images_flat.view()
digits_images.shape = ((-1), 8, 8)
digits_target = digits[:,(-1)].astype(np.int)



digits_test = np.loadtxt('digits_Test.csv', delimiter=',')
digits_test_images_flat = digits_test[:,:(-1)]
digits_test_images = digits_test_images_flat.view()
digits_test_images.shape = ((-1), 8, 8)
digits_test_target = digits_test[:,(-2)].astype(np.int)





images_and_labels = list(zip(digits_images, digits_target))











n_samples = len(digits_images)



classifier = svm.SVC(gamma=0.001, kernel='linear')


classifier.fit(digits_images_flat, digits_target)


expected = digits_test_target
predicted = classifier.predict(digits_test_images_flat)
print('Classification report for classifier %s:\n%s\n' % (
classifier, metrics.classification_report(expected, predicted)))
print('Confusion matrix:\n%s' % metrics.confusion_matrix(expected, predicted))
print("accuracy:", metrics.accuracy_score(expected, predicted))

images_and_predictions = list(zip(digits_test_images, predicted))









np.savetxt('output.txt', classifier.decision_function(digits_test_images_flat))

outputData = {'data_array': metrics.confusion_matrix(expected, predicted)}

with open('output.pkl', 'wb') as outputFile:
    cPickle.dump(outputData, outputFile)

with open('model.pkl', 'wb') as modelFile:
    cPickle.dump(classifier, modelFile)