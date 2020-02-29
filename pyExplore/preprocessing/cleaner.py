"""
Module Contents functionality to process
the dirty preprocessing and make it useable for future
analysis
"""

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

from pyExplore.util import util


class Dataset:
    def __init__(self, df):
        self.df = df

    @classmethod
    def load_data(cls, file_path, **kwargs):
        return cls(util.load_dataset(file_path, **kwargs))

    def drop_multiple_columns(self, column_name_list=None):
        '''
        Drop multiple columns based on their column names
        Input : pandas dataframe, List of column names in the preprocessing set
        '''
        if column_name_list:
            self.df.drop(column_name_list, axis=1, inplace=True)

    def convert_categorial_data_to_numerical_data(self):
        pass

    def one_hot_encode_data(self):
        enc = OneHotEncoder(handle_unknown='ignore')
        enc.fit(self.df)
        enc.transform(self.df)

    def remove_col_white_space(self, column):
        # remove white space from the beginning and end of string
        self.df[column] = self.df[column].str.strip()

    def change_dtypes(self, column_int=None, column_float=None):
        """
        Changing dtypes to save memory
        Output -> updated df with smaller
        """
        for column in column_float:
            self.df[column] = self.df[column].astype('float32')
        for column in column_int:
            self.df[column] = self.df[column].astype('int32')

    def remove_majority_na_columns(self, inplace=True):
        self.df.dropna(thresh=len(self.df) / 2, axis=1, inplace=inplace)


class TimeSeriesData(Dataset):
    '''
    Special class to handle timeseries
    datasets
    '''

    def __init__(self, df):
        super().__init__(df)

    def convert_to_datetime_object(self, column, strfmt=None):
        self.df[column] = pd.to_datetime(self.df[column], format=strfmt, infer_datetime_format=True)
