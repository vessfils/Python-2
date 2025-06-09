
from load_csv import load
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def display_graph():
    try:
        data = load("life_expectancy_years.csv")
        if data is None:
            return
        #on va convertir la columns en int
        data.columns = data.columns.astype(int)
        country = "France"
        if country not in data.index:
            raise ValueError("The country is not found in the dataset.")
        X = data.columns 
        Y = data.loc[country]
        plt.plot(X, Y, color='blue', label='Life expectancy line')
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.title(f'{country} - Life expectancy Projections')
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"❌ Value error: {e}")

def main():
   display_graph()


if __name__ == "__main__":
    main()