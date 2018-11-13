from __future__ import print_function

import math
from IPython import display
from matplotlib import cm
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset


tf.logging.set_verbosity(tf.logging.ERROR)
# set pandas display
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

# load data and random permutation
'''why should we randomly permutate the data?'''
california_housing_dataframe = pd.read_csv("https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv", sep=",")
california_housing_dataframe = california_housing_dataframe.reindex(np.random.permutation(california_housing_dataframe.index))
california_housing_dataframe['median_house_value'] /= 1000.0
print(california_housing_dataframe.describe())


'''feel input function is strange'''
# input function
def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    """
    Trains a Linear Regression model of one feature
    :param features:
    :param targets:
    :param batch_size:
    :param shuffle:
    :param num_epochs:
    :return: Tuple of (features, labels) for next data batch
    """
    # convert pandas data to dict of np.array
    features = {key:np.array(value) for key, value in dict(features).items()}

    # construct a dataset
    ds = Dataset.from_tensor_slices((features, targets))
    ds = ds.batch(batch_size).repeat(num_epochs)

    # If specified, shuffle the dataset
    if shuffle:
        ds = ds.shuffle(buffer_size=10000)
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels

# # information
# '''why do not directly use pd.describe()'''
# calibration_data = pd.DataFrame()
# calibration_data["predictions"] = pd.Series(predictions)
# calibration_data["targets"] = pd.Series(targets)
# calibration_data.describe()


def train_model(learning_rate, steps, batch_size, input_features="total_rooms"):
    """
    Trainin a linear regression model of one-hot value
    :param learning_rate:
    :param steps: total number of training steps
    :param batch_size:
    :param input_features: A string specifying a column from '***.csv' file to use as input feature
    :return:

    """

    periods = 10
    steps_per_period = steps / periods

    my_feature = input_features
    my_feature_data = california_housing_dataframe[[my_feature]]
    my_label = "median_house_value"
    targets = california_housing_dataframe[my_label]

    # create feature columns
    feature_columns = [tf.feature_column.numeric_column(my_feature)]

    # create input function
    '''why should we use lambda function to construct the input for train?'''
    training_input_fn = lambda: my_input_fn(my_feature_data, targets, batch_size=batch_size)
    prediction_input_fn = lambda: my_input_fn(my_feature_data, targets, num_epochs=1, shuffle=False)

    # create a linear regressor object
    my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
    my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)
    linear_regressor = tf.estimator.LinearRegressor(feature_columns=feature_columns, optimizer=my_optimizer)

    # set up to plot
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    plt.title("Learned line by period")
    plt.ylabel(my_label)
    plt.xlabel(input_features)

    sample = california_housing_dataframe.sample(n=300)
    plt.scatter(sample[my_feature], sample[my_label])
    colors = [cm.coolwarm(x) for x in np.linspace(-1, 1, periods)]

    print("Training model ...")
    print("PMSE (on training data):")
    root_mean_square_errors = []
    for period in range(0, periods):
        # traing the model, start from prior state
        linear_regressor.train(input_fn=training_input_fn, steps=steps_per_period)

        # compute prediction
        predictions = linear_regressor.predict(input_fn=prediction_input_fn)
        predictions = np.array([item["predictions"][0] for item in predictions])

        # compute loss
        root_mean_square_error = math.sqrt(metrics.mean_squared_error(targets, predictions))
        print("period: %02d : %0.2f" % (period, root_mean_square_error))
        root_mean_square_errors.append(root_mean_square_error)
        y_extents = np.array([0, sample[my_label].max()])

        # track the weights and bias over time
        '''Is the weight and bias store in fixed directory?'''
        weight = linear_regressor.get_variable_value('linear/linear_model/%s/weights' % input_features)[0]
        bias = linear_regressor.get_variable_value('linear/linear_model/bias_weights')

        x_extents = (y_extents - bias) / weight
        x_extents = np.maximum(np.minimum(x_extents, sample[my_feature].max()), sample[my_feature].min())
        y_extents = weight * x_extents + bias

        plt.plot(x_extents, y_extents, color=colors[period])

    print('model train finished')

    # output a graph of loss metrics over period
    plt.subplot(1, 2, 2)
    plt.ylabel("RMSE")
    plt.xlabel("Periods")
    plt.title("Root Mean Square Error VS Periods")
    plt.tight_layout()
    plt.plot(root_mean_square_errors)

    # output a data with calibration data
    calibration_data = pd.DataFrame()
    calibration_data["Predictions"] = pd.Series(predictions)
    calibration_data["Targets"] = pd.Series(targets)
    display.display(calibration_data.describe())

    print("Final RMSE error on training data: %.2f" % root_mean_square_error)

    return calibration_data


california_housing_dataframe["rooms_per_person"] = (
        california_housing_dataframe["total_rooms"] / california_housing_dataframe["population"])
calibration_data = train_model(
    learning_rate=0.05,
    steps=500,
    batch_size=5,
    input_features="rooms_per_person")

# analyse the outliers
plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
plt.scatter(calibration_data["Predictions"], calibration_data["Targets"])
# show histogram
plt.subplot(1, 2, 2)
_ = california_housing_dataframe["rooms_per_person"].hist()


# filter the outliers, train and show again
california_housing_dataframe["rooms_per_person"] = (
    california_housing_dataframe["rooms_per_person"]).apply(lambda x: min(x, 5))

_ = california_housing_dataframe["rooms_per_person"].hist()

calibration_data = train_model(
    learning_rate=0.05,
    steps=500,
    batch_size=5,
    input_features="rooms_per_person")

_ = plt.scatter(calibration_data["Predictions"], calibration_data["Targets"])


