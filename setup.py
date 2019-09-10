import setuptools

from .pyExplore.version import Version

setuptools.setup(name='pyExplore',
                 version=Version('1.0.0').number,
                 description='Python Package for exploratory data analysis in Data Science',
                 long_description=open('README.md').read().strip(),
                 author='Rahul Mishra',
                 author_email='rahul.mishra2003@gmail.com',
                 url='http://path-to-my-packagename',
                 py_modules=['pyExplore'],
                 install_requires=['pandas', 'matplotlib', 'numpy', 'scipy'],
                 license='MIT License',
                 zip_safe=False,
                 keywords='Exploratory Data Analysis, Data Analysis,EDA',
                 classifiers=['Packages', 'Data Science', 'Machine Learning'])
