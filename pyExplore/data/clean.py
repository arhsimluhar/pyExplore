"""
Module Contents functionality to process
the dirty data and make it useable for future
analysis
"""
import pandas as pd


class Dataset:
    def __init__(self, df):
        self.df = df

    def drop_multiple_columns(self, column_name_list=None):
        '''
        Drop multiple columns based on their column names
        Input : pandas dataframe, List of column names in the data set
        '''
        if column_name_list:
            self.df.drop(column_name_list, axis=1, inplace=True)
        return self.df

    def check_for_missing_data(self):
        """
        check for any missing data in the df (display in descending order)
        """
        return self.df.isnull().sum().sort_values(ascending=False)

    def convert_categorial_data_to_numerical_data(self):
        pass

    def remove_col_white_space(self, column):
        # remove white space at the beginning of string
        self.df[column] = self.df[column].str.lstrip()

    def change_dtypes(self,column_int = None, column_float = None):
        """
        Changing dtypes to save memory
        Output -> updated df with smaller
        """
        for column in column_float:
            self.df[column] = self.df[column].astype('float32')
        for column in column_int:
            self.df[column] = self.df[column].astype('int32')
        

class TimeSeriesData(Dataset):
    '''
    Special class to handle timeseries
    datasets
    '''

    def __init__(self, df):
        super().__init__(df)

    def convert_str_to_datetime(self, field_name, strfmt='%Y-%m-%d %H:%M:%S.%f'):
        '''
            Convert datetime(String) to datetime
            OUTPUT: updated df with new datetime format
            ------
            '''
        self.df.insert(loc=2, column=field_name, value=pd.to_datetime(self.df.transdate, format=strfmt))
