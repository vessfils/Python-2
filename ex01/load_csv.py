import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load(path: str):
    try:
        #La première colonne ("country") devient l'index du DataFrame.
        data = pd.read_csv(path,index_col=0)
        print(f"Loading dataset of dimensions {data.shape}")
        #print 5 premiere lignes de la data
        #print(data.head())
        if data.empty:
            raise ValueError("CSV file is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return data

# def main():
#    load("life_expectancy_years.csv")


# if __name__ == "__main__":
#     main()