import os
import tempfile
import matplotlib.pyplot as plt
import pandas as pd

class figure:
    def __init__(self,df):
        self.df = df
        #self.img_folder = tempfile.mkdtemp()
        os.makedirs("/tmp/pyexplore/",exist_ok= True)
        self.img_folder = "/tmp/pyexplore"

    def histogram(self, col_name,*args,**kwargs):
        filename = os.path.join(self.img_folder, f"eda-histogram-{col_name}.png")
        plt.xlabel(kwargs.get("xlabel", ""))
        plt.ylabel(kwargs.get("ylabel", ""))
        plt.title(kwargs.get("title", ""))
        plt.hist(self.df[~pd.isna(self.df[col_name])][col_name])
        plt.savefig(filename)
        plt.close()

    def box_plot(self,col_name,*args,**kwargs):
        plt.xlabel(kwargs.get("xlabel", ""))
        plt.ylabel(kwargs.get("ylabel", ""))
        plt.title(kwargs.get("title", ""))
        filename = os.path.join(self.img_folder, f"eda-box-plot-{col_name}.png")
        plt.boxplot(self.df[~pd.isna(self.df[col_name])][col_name])
        plt.savefig(filename)
        plt.close()

    def bar(self,col_name,*args,**kwargs):
        plt.ylabel(kwargs.get("ylabel", ""))
        plt.title(kwargs.get("title", ""))
        filename = os.path.join(self.img_folder, f"eda-bar-plot-{col_name}.png")
        data = self.df[col_name].value_counts()
        xdata,ydata = data.index, data.values
        plt.bar(xdata,ydata)
        plt.savefig(filename)
        plt.close()
