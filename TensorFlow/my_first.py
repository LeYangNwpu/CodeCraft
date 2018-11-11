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

# define feature
'''strange for use [[]] and []'''
my_feature = california_housing_dataframe[['total_rooms']]
features_columns = [tf.feature_column.numeric_column("total_rooms")]

# label
targets = california_housing_dataframe["median_house_value"]

# optimizer
my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-7)
my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)
linear_regressor = tf.estimator.LinearRegressor(feature_columns=features_columns, optimizer=my_optimizer)


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


'''why should we use lambda function to construct the input for train?'''
# train the model
_ = linear_regressor.train(input_fn=lambda: my_input_fn(my_feature, targets))

# create an input function for predictions
prediction_input_fn = lambda: my_input_fn(my_feature, targets, num_epochs=1, shuffle=False)
predictions = linear_regressor.predict(input_fn=prediction_input_fn)
predictions = np.array([item["predictions"][0] for item in predictions])

mean_square_error = metrics.mean_squared_error(targets, predictions)
root_mean_square_error = math.sqrt(mean_square_error)
print("mean square error (on training data): %0.3f" % mean_square_error)
print("root mean square error (on training data): %0.3f" % root_mean_square_error)

# information
'''why do not directly use pd.describe()'''
calibration_data = pd.DataFrame()
calibration_data["predictions"] = pd.Series(predictions)
calibration_data["targets"] = pd.Series(targets)
calibration_data.describe()

# visualize the learned line
sample = california_housing_dataframe.sample(n=300)
x_0 = sample["total_rooms"].min()
x_1 = sample["total_rooms"].max()

'''Is the weight and bias store in fixed directory?'''
# Retrieve the final weight and bias
weight = linear_regressor.get_variable_value('linear/linear_model/total_rooms/weights')[0]
bias = linear_regressor.get_variable_value('linear/linear_model/bias_weights')

y_0 = weight * x_0 + bias
y_1 = weight * x_1 + bias

# plot the regression line
plt.plot([x_0, y_0], [x_1, y_1], c="r")
plt.ylabel("median house value")
plt.xlabel("total rooms")
'''what is the meaning of scatter'''
plt.scatter(sample["total_rooms"], sample["median house value"])
plt.show()


def train_model(learning_rate, steps, batch_size, input_features="total room"):
    """
    Trainin a linear regression model of one-hot value
    :param learning_rate:
    :param steps:
    :param batch_size:
    :param input_features:
    :return:

    """

    periods = 10
    steps_per_period = steps / periods

    my_feature = input_features
    my_feature_data = california_housing_dataframe[[my_feature]]
    my_label = "median house value"
    targets = california_housing_dataframe()[my_label]

    # create feature columns
    feature_columns = [tf.feature_column.numeric_column(my_feature)]

    # create input function
    training_input_fn = lambda: my_input_fn(my_feature_data, targets, batch_size=batch_size)
    prediction_input_fn = lambda: my_input_fn(my_feature_data, targets, num_epochs=1, shuffle=False)

    # create a linear regressor object
    my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-7)
    my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)
    linear_regressor = tf.estimator.LinearRegressor(feature_columns=features_columns, optimizer=my_optimizer)

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


train_model(learning_rate=1e-5, steps=500, batch_size=5)









