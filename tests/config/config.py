import os

# Top level folder for package directory
WORKSPACE_DIR = os.path.abspath(os.path.join(__file__, "../../../"))

# Test data folder
TEST_DATA = os.path.join(WORKSPACE_DIR, "test_data")
TIMESERIES_DATA_DIR = os.path.join(TEST_DATA, "timeseries")
