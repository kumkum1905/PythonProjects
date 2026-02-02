import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # 1. Read data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 3. Line of best fit (all data)
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred_all = np.arange(1880, 2051)
    y_pred_all = res_all.intercept + res_all.slope * x_pred_all
    plt.plot(x_pred_all, y_pred_all, color="red")

    # 4. Line of best fit (from year 2000 onwards)
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(
        df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"]
    )
    x_pred_recent = np.arange(2000, 2051)
    y_pred_recent = res_recent.intercept + res_recent.slope * x_pred_recent
    plt.plot(x_pred_recent, y_pred_recent, color="green")

    # 5. Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # 6. Save and return plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()
