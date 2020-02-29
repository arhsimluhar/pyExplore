import os
import pandas as pd
from pyExplore.preprocessing import cleaner
from tests.config import config


def test_datetime_conversion():
    time_series_data = os.path.join(config.TIMESERIES_DATA_DIR, "test.csv")
    obj = cleaner.TimeSeriesData.load_data(time_series_data)
    obj.convert_to_datetime_object("date")
    assert isinstance(obj.df["date"][0],pd._libs.tslibs.timestamps.Timestamp)