"""
Handle missing datapoints with
missing fields
"""


class missing:
    def __init__(self, df):
        self.df = df

    def missing_data_info(self):
        return self.df.apply(lambda x: sum(x.isnull()), axis=0)

    def data_point_deletion(self):
        """
        removes data-point if any of the column element
        is missing
        """
        self.df.dronp(how="any")

    def replace_by(self, column=None, tendency="mean"):
        """
        replace the missing values by provided
        measure of central tendency
        """
        method = getattr(self.df, tendency)
        if not column:
            self.df.fillna(method(), inplace=True)
        else:
            self.df[column].fillna(self.df[column], inplace=True)
