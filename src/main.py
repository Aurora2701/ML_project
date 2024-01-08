import pandas as pd

from DataClean import DataClean
import os


if __name__ == '__main__':
    # Load and clean data
    print(os.getcwd())
    dc = DataClean('data\\Cancer_Data.csv')
    data = dc.clean_df()
