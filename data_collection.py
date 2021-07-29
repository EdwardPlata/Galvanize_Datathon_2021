import pandas as pd
import numpy as np
import requests
import csv

def collecting_nyiso_data(periodid:int) -> pd.DataFrame:
    link = "http://mis.nyiso.com/public/csv/pal/{periodid}pal.csv".format(periodid=periodid)
    
    return pd.read_csv(link)

20210726_df = collecting_nyiso_data(20210726)

print(20210726_df)
