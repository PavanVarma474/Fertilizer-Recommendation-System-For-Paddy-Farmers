import numpy as np
import pandas as pd
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle

warnings.filterwarnings("ignore")

data = pd.read_csv("epics_dataset.csv")
data = np.array(data)

X = data[1:, 1:4]
y = data[1:, 4:]  # Make y have three columns
y = y.astype('int')
X = X.astype('int')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Create a multi-output regression model using Linear Regression as an example
regr = MultiOutputRegressor(LinearRegression())

regr.fit(X_train, y_train)

# Save the trained model
pickle.dump(regr, open('multi_output_model.pkl', 'wb'))
model = pickle.load(open('multi_output_model.pkl', 'rb'))
