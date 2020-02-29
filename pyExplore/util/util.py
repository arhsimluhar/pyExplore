"""
Module provides utility functions
that can be used to perform easy tasks
"""
import os
from datetime import datetime

import pandas as pd


def get_file_extension(path):
    """
    return the file extension of the
    file at the path
    """
    if os.path.exists(path):
        filename = os.path.basename(path)
        return filename.split(".")[-1]

    return ""


def convert_str_to_datetime(str_date, strfmt='%Y-%m-%d %H:%M:%S.%f'):
    '''
        Convert datetime(String) to datetime object
        OUTPUT: returns datetime object
        ------
    '''
    return datetime.strptime(str_date, strfmt)


def load_dataset(file, **kwargs):
    """
    load dataset from various sources
    """
    file_extension = get_file_extension(file)
    df = None
    if file_extension == "csv":
        df = pd.read_csv(file)
    elif file_extension == "table":
        df = pd.read_table(file, **kwargs)
    elif file_extension == "xls" or "xlsx":
        df = pd.read_excel(file, **kwargs)
    elif file_extension == "txt":
        df = pd.read_csv(file, **kwargs)
    return df
