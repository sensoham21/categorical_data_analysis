
import os
import pandas as pd
import numpy as np
import copy
import warnings
%matplotlib inline
warnings.filterwarnings('ignore')
sns.set_style(style = 'whitegrid')

def eda_cat(df):
    #Extract the categorical variables as a separate dataframe
    df_cat = df.select_dtypes(include='object').copy()
    
    #Create a dataframe for the summary table
    df_cat_stats = pd.DataFrame(columns=["column", "values", "value_count_na", "value_count_nona", "mode", "min_occ","num_miss", "pct_miss"])
    #Create a temporary dataframe
    tmp = pd.DataFrame()
    
    for c in df_cat.columns:
        #Get the column name
        tmp['column'] = [c]
        #Get the list of categories
        tmp['values'] = [df_cat[c].unique()]
        #Get the number of unique categories with null included
        tmp['value_count_na'] = len(list(df_cat[c].unique()))
        #Get the number of unique categories without null
        tmp['value_count_nona'] = int(df_cat[c].nunique())
        #Get the most occuring category
        tmp["mode"] = df_cat[c].value_counts().index[0]
        #Get the least occuring category
        tmp['min_occ'] = df_cat[c].value_counts().index[-1]
        #Get the number of missing values
        tmp['num_miss'] = df_cat[c].isnull().sum()
        #Get the percentage of missing values
        tmp['pct_miss'] = (100*df_cat[c].isnull().sum()/ len(df_cat))
        #Append to the stats table
        df_cat_stats = df_cat_stats.append(tmp)
        
    #Sort by percentage of missing values  
    df_cat_stats.sort_values(by = 'pct_miss', inplace = True, ascending = False)
    #Set column name as index
    df_cat_stats.set_index('column', inplace = True)

    return df_cat_stats, df_cat

