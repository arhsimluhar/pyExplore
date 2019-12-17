import pandas as pd
from pyExplore.visualization import  visual

"""
writing this exploratory preprocessing analysis
file with support of single CSV.
Will improve this in the next version of the module.
"""

from pyExplore.preprocessing import cleaner

class EDA:

    def __init__(self, file=None, delimiter=",", target=None, predictor=None):

        self.is_target_predictor_set = True
        self.discrete_variables = []
        self.continuous_variables = []
        self.feature_types = {}
        if file:
            self.df = pd.read_csv(file, delimiter=delimiter)
            self.target = target
            self.predictor = predictor

        self.set_target_predictor()
        self.feature_types = self.set_data_type()
        self.discrete_variables, self.continuous_variables = self.set_type_of_variable()

    def set_target_predictor(self):

        if self.target and self.predictor:
            return
        elif self.target:
            self.predictor = [item for item in self.df.columns if item != self.target]
        elif self.predictor:
            self.predictor = [item for item in self.df.columns if item != self.predictor]
        else:
            self.is_target_predictor_set = False
            return

    def shape(self):
        return self.df.shape

    def head(self, num=5):
        return self.df.head(num)

    def get_types(self):
        return self.df.info()

    def describe(self):

        return self.df.describe()

    def variable_category(self):
        """
        returns the dictionary that
        lists predictor and target variables
        :return dict:
        """
        if self.is_target_predictor_set:
            data = {"Predictor Variable": self.predictor, "Target Variable": self.target}
        else:
            data = {"info": "Predictor and  Target variables have not be set yet."}
        return data

    def set_data_type(self):
        data = {}
        for column in self.df.columns:
            if self.df.dtypes[column] == 'int64':
                data[column] = 'Integer'
            elif self.df.dtypes[column] == "bool":
                data[column] = 'Boolean'
            elif self.df.dtypes[column] == "float64":
                data[column] = "Floating Point"
            elif self.df.dtypes[column] == "object":
                data[column] = "String"
            else:
                raise Exception("Unhandled Data Type.")
        return data

    def check_for_missing_data(self):
        """
        check for any missing preprocessing in the df (display in descending order)
        """
        return self.df.isnull().sum().sort_values(ascending=False)

    def set_type_of_variable(self):
        """
        identifies whether the feature is
        continuous or discrete variable.
        :return dict:
        TOD0: Improve the algorithm
        """
        data = {"categorial": [], "continuous": []}
        total_length = self.shape()[0]
        for column in self.df.columns:
            if self.feature_types[column] == "String":
                data["categorial"].append(column)
                continue

            unique_entries = len(self.df[column].unique())
            # print(unique_entries, column, total_length)
            if unique_entries <= 0.05 * total_length:
                if total_length >= 10 ** 6:
                    data["continuous"].append(column)
                else:
                    data["categorial"].append(column)
            else:
                data["continuous"].append(column)
        return data["categorial"], data["continuous"]

    def informatics(self):
        print("****************************")
        print("Dataset Informatics:")
        print("****************************")

        print("Shape: ", end="")
        print("{0} Datapoints x {1} feature eda".format(self.df.shape[0], self.df.shape[1]))

        print("\n")
        print("****************************")
        print("variables Indentification")
        print("****************************")

        if not self.predictor and not self.target:
            print("Please provide info about target and predictor variables.")
        else:
            print("Predictor Variable(s): %s" % (self.predictor))
            print("Target Variable(s): %s" % (self.target))
        print("\n")

        print("****************************")
        print("Data Types of eda")
        print("****************************")
        self.get_types()

        print("\n")

        print("****************************")
        print("Variable Categories")
        print("****************************")
        print("Categorial Variables: %s" % (self.discrete_variables))
        print("Continuous Variables: %s" % (self.continuous_variables))

        print("\n")
        print("Missing Values (any if) in Descending order")
        print(self.check_for_missing_data())

class UnivariateAnalysis(EDA):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = {
            "CentralTendency": {},
            "MeasureOfDispersion": {}
        }

    def central_tendency(self):
        for var in self.continuous_variables:
            self.data["CentralTendency"][var] = self.df[var].describe()

    def measureOfDispersion(self):
        for var in self.continuous_variables:
            self.data["MeasureOfDispersion"][var] = self.df[var].describe()

    def visualise(self):
        #TODO improve the way we are doing the visualisation
        x  = visual.figure(self.df)
        if self.continuous_variables and self.discrete_variables:
            if self.continuous_variables:
                for col_name in self.continuous_variables:
                    x.histogram(col_name = col_name,title=f"Univariate Analyis ({col_name})",xlabel=col_name,ylabel="Count")

                for col_name in self.continuous_variables:
                    x.box_plot(col_name = col_name,title=f"Univariate Analysis ({col_name})",ylabel=col_name)

            if self.discrete_variables:
                for col_name in self.discrete_variables:
                    x.bar(col_name = col_name, title=f"Univariate Analysis ({col_name})",ylabel="Count")
        else:
            print("Please define Categorial and Continous Variables for proper visualisation.")


class BivariateAnalysis(EDA):
    def __init__(self):
        super().__init__()


class MissingData(EDA):
    def __init__(self):
        super().__init__()


class Outliers(UnivariateAnalysis, BivariateAnalysis):
    def __init__(self):
        super().__init__()
