
from load_csv import load
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def display_graph():
    data = load("life_expectancy_yfafaears.csv")
    #on va convertir la columns en int
    data.columns = data.columns.astype(int)
    X = data.columns 
    Y = data.loc["France"]
    plt.plot(X, Y, color='blue', label='Life expectancy line')
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title('France Life expectancy Projections')
    plt.legend()
    plt.show()

def main():
   display_graph()


if __name__ == "__main__":
    main()