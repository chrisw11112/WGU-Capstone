import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plot
from sklearn.metrics import mean_squared_error


class Model:
    def __init__(self):
        self.model = self.create_model_with_data()
        self.graphs = []
    def create_model_with_data(self):
        independent_training, independent_testing, dependent_training, dependent_testing = self.read_data()
        return self.create_model_and_create_charts(independent_training, dependent_training, independent_testing, dependent_testing)

    def read_data(self):
        data = pd.read_csv("Housing.csv")
        independent = data[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'sqft_above', 'sqft_basement', 'yr_built']]
        dependent = data['price']

        p_and_r_values = [[], [], []]
        for independent_value in independent.columns:
            r, p = pearsonr(independent[independent_value], dependent)
            p_and_r_values[0].append(independent_value)
            p_and_r_values[1].append(p)
            p_and_r_values[2].append(r)
        self.p_and_r_values = p_and_r_values

        return train_test_split(independent, dependent, test_size=0.2)

    def create_model_and_create_charts(self, independent_training, dependent_training, independent_testing, dependent_testing):
        model = LinearRegression()
        model.fit(independent_training, dependent_training)
        independent_prediction = model.predict(independent_testing)

        abosolute_error = mean_squared_error(dependent_testing, independent_prediction)
        square_root = np.sqrt(abosolute_error)
        print(square_root)

        plot.figure(figsize=(10, 6))
        plot.scatter(dependent_testing, independent_prediction, color="red", label="Predicted vs Actual")
        plot.xlabel("Actual Price")
        plot.ylabel("Predicted Price")
        plot.title("Actual Values vs Predicted Values")
        plot.legend()
        plot.savefig("actual_vs_prediction.png")

        plot.figure(figsize=(10, 6))
        plot.bar(self.p_and_r_values[0], self.p_and_r_values[1])
        plot.title("P Values")
        plot.savefig("p.png")
        
        
        plot.figure(figsize=(10, 6))
        plot.bar(self.p_and_r_values[0], self.p_and_r_values[2])
        plot.title("R Values")
        plot.savefig("r.png")

        return model
    def predict(self, bedrooms, bathrooms, sqft_living, sqft_lot, floors, sqft_above, sqft_basement, yr_built):

        input_data = pd.DataFrame([[bedrooms, bathrooms, sqft_living, sqft_lot, floors, sqft_above, sqft_basement, yr_built]],
            columns=["bedrooms", "bathrooms", "sqft_living", "sqft_lot", "floors", "sqft_above", "sqft_basement", "yr_built"])

        prediction = self.model.predict(input_data)
        return float(prediction[0])
