
from load_csv import load
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def clean_dataset(value):
    try:
        if isinstance(value,str):
            value = value.strip().lower()
            if value[-1] == 'm':
                return float(value[:-1]) * 1_000_000
            elif value[-1] == 'k':
                return float(value[:-1]) * 1_000
            elif value[-1] == 'b':
                return float(value[:-1]) * 1_000_000_000
            else:
                return float(value)
    except Exception as e:
            print(f"❌ Value error: {e}")
            return float('nan')


def display_pop():
    try:
        data = load("population_total.csv")
        if data is None:
            return None
        countries=["France","Belgium"]
        data.columns = data.columns.astype(int)
        data = data.applymap(clean_dataset)
        for country in countries:
            if country not in data.index:
                raise ValueError(f"Country '{country}' not found in dataset.")
            X = data.columns 
            Y = data.loc[country]
            plt.plot(X, Y, label=country)
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title(f'Population Projections')
        plt.legend(loc='lower right')
        formatter = FuncFormatter(lambda x, pos: f'{x/1_000_000:.0f}M')
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.show()
    
    except Exception as e:
        print(f"❌ Value error: {e}")
  


def main():
    display_pop()



if __name__ == "__main__":
    main()