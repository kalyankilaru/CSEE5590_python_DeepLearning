from sklearn import svm

from sklearn import datasets

from sklearn import metrics

from sklearn.model_selection import train_test_split

# Loading the data
iris = datasets.load_wine()
# x_data and y_target are loaded with data and the target
x_data = iris.data
y_target = iris.target

# Divide the data into 20 percent testing the remaining is training data.
x_training, x_testing, y_training, y_testing = train_test_split(x_data, y_target, test_size=0.2)

print("SVM with linear kernel:")
# Linear Model

linear_kernel_model = svm.SVC(kernel="linear")
linear_kernel_model.fit(x_training, y_training)

# Generate y_predicted from trained model with data from x_testing
y_predicted = linear_kernel_model.predict(x_testing)
# Print data on both y_predicted and y_testing
print("y_predicted:")
print(y_predicted)

print("y_testing:")
print(y_testing)
#  accuracy score by compare y_testing and y_predicted
print("Accuracy for SVM with Linear kernal: %.2f" % metrics.accuracy_score(y_testing, y_predicted))

print("\nSVM with RBF kernel:")
rbf_model = svm.SVC(kernel="rbf")
rbf_model.fit(x_training, y_training)

#  y_predicted from trained model with data from x_testing
y_predicted = rbf_model.predict(x_testing)
# Print data on both y_predicted and y_testing

print("y_predicted:")
print(y_predicted)
print("y_testing:")
print(y_testing)
#  accuracy score by compare y_testing and y_predicted
print("Accuracy for SVM with RBF kernal: %.2f" % metrics.accuracy_score(y_testing, y_predicted))


