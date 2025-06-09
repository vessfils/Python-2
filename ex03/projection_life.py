
from load_csv import load
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def human_readable(x, pos):
    if x >= 1_000_000:
        return f'{x/1_000_000:.0f}M'
    elif x >= 1_000:
        return f'{x/1_000:.0f}k'
    else:
        return str(int(x))


def display(year):
    try:
        income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life = load("life_expectancy_years.csv")
        if income is None or life is None:
            return
        income.columns = income.columns.astype(int)
        life.columns = life.columns.astype(int)
        #fusionne les deux database sur la year et dropna supprime les lignes vides sur income ou autre
        df = pd.DataFrame({
        "Income": income[year],
        "LifeExpectancy": life[year]
        }).dropna()

        plt.scatter(df["Income"], df["LifeExpectancy"], color='blue', label='Data points')
        plt.xlabel('Gross Domestic product')
        plt.ylabel('Life Expectancy')
        plt.title('1900')
        plt.xlim(300, 10000) 
        plt.gca().set_xscale('log')  # échelle logique pour les données très dispersées
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
        plt.gca().xaxis.set_major_formatter(FuncFormatter(human_readable))  # affichage lisible
        plt.show()
    except Exception as e:
        print(f"❌ Value error: {e}")

def main():
    display(1900)
 

if __name__ == "__main__":
    main()