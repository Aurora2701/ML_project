import pandas as pd


class DataClean:
    """Class to load and clean dataset"""
    input

    def __init__(self, input_path):
        self.input = pd.read_csv(input_path, sep=',')

    def clean_df(self):
        return self.input
