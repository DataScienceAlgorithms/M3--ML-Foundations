from my_simple_linear_regressor import MySimpleLinearRegressor
import operator
import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# unit under test
def compute_euclidean_distance(v1, v2):
    # TODO 
    pass

# unit test
def test_compute_euclidean_distance():
    # we need data
    np.random.seed(0)
    v1 = np.random.random(100)
    v2 = np.random.random(100)
    # TODO
    pass


def main():
    # Starting with PA4, we will implement common ML algorithms
    # following the style of popular libraries (like scikit-learn or TensorFlow,etc.) API
    # API = Application Programming Interface
    # Reference: https://scikit-learn.org/1.3/tutorial/statistical_inference/supervised_learning.html

    # X: 2D feature matrix (rows = instances, columns = attributes)
    # y: 1D target vector (values we want to predict)
    # Note: y is stored separately from X

    # Typical workflow:
    # 1. Split X and y into training and testing sets
    # 2. Train the model using the training set (X_train, y_train)
    # 3. Evaluate the model using the testing set (X_test, y_test)
    # Note: X_train aligns with y_train, X_test aligns with y_test


    # Each algorithm is implemented as a class with two main methods:
    # - fit(X_train, y_train): trains the model on the training data
    # - predict(X_test): returns predictions (y_pred) for the test data
    #   y_pred is aligned with y_test

    # Model evaluation:
    # - Regression: e.g.,Mean Squared Error (MSE) Mean Absolute Error (MAE) — average of absolute differences
    # - Classification: e.g., Accuracy — proportion of correct predictions

    # my_simple_linear_regressor.py is our simple linear regression code

    # we need X_train and y_train data
    np.random.seed(0)
    X_train = [[val] for val in list(range(0, 100))]
    y_train = [row[0] * 2 + np.random.normal(0, 25) for row in X_train]

    print(X_train[0])
    print(y_train[0])
    my_lin=MySimpleLinearRegressor()
    my_lin.fit(X_train,y_train)
      
    y_pred=my_lin.predict([[8]])
    print(y_pred)

    #class activity 2 (knn)

    header = ["att1", "att2"]
    X_train = [
        [3, 2],
        [6, 6],
        [4, 1],
        [4, 4],
        [1, 2],
        [2, 0],
        [0, 3],
        [1, 6]
    ]
    y_train = ["no", "yes", "no", "no", "yes", "no", "yes", "yes"] # parallel to X_train
    unseen_instance = [2, 3]
    # 1. normalize if needed (not needed for dataset, assumed [0, 10])
    # 2. TODO calculate distances between each training set instance and the unseen instance
    row_indexes_dists = [] # list of tuple pairs (row index, dist)
    

    # 3.  Sort by distance (ascending) 
    row_indexes_dists.sort(key=operator.itemgetter(-1)) # get the item in the tuple at index -1 
    # and use that for sorting
    # 4. TODO Select the k nearest neighbors
    k = 3 
    

    # 5.TODO Extract the class labels of neighbors neigbors from y_train
    top_k_labels = []


    # 6. TODO Predict using Majority voting
    

    #print("Predicted class:", prediction)

    # check work against sci-kit learn
    knn_clf = KNeighborsClassifier(n_neighbors=3, metric="euclidean")
    knn_clf.fit(X_train, y_train)
    distances, indexes = knn_clf.kneighbors([unseen_instance])
    print(distances)
    print(indexes)



    
if __name__=='__main__':
    main()