#!/usr/bin/python3
import pandas as pd

def display():
    #reading the csv file
    df_population_raw=pd.read_csv("population_total.csv")

    #dropping null values
    df_population_raw.dropna(inplace=True)

        #making a pivot table
    df_pivot=df_population_raw.pivot(index='year',
                                    columns="country",
                                    values="population"
                                    )
    
    #lets select some countries. This will be important in visualizations
    df_pivot=df_pivot[['United States', 'India', 'China','Indonesia', 'Brazil']]
    return df_pivot




