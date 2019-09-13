from setuptools import setup
from setuptools import find_packages

setup(name='pyExplore',
      version='0.0.0.1',
      description='Python Package for exploratory data analysis in Data Science',
      long_description=open('README.md').read().strip(),
      long_description_content_type='text/markdown',
      author='Rahul Mishra',
      packages=find_packages(),
      author_email='rahul.mishra2003@gmail.com',
      url='https://github.com/rahul1809/pyExplore',
      py_modules=['src'],
      install_requires=['pandas', 'matplotlib', 'numpy', 'scipy'],
      license='MIT License',
      zip_safe=False,
      keywords='Exploratory Data Analysis, Data Analysis,EDA',
      classifiers=["License :: OSI Approved :: MIT License",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.7",
                   "Intended Audience :: Developers",
                   "Intended Audience :: Science/Research",
                   "Intended Audience :: Information Technology",
                   'Topic :: Scientific/Engineering :: Information Analysis',
                   'Topic :: Software Development',
                   'Topic :: Utilities'
                   ])
