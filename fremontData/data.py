from urllib.request import urlretrieve
import os
import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, force_download=False):
    """Download and store the Fremont cycle data

    Paramaters 
    ----------
    filename: string (optional)
        location to save the data
    url: string (optional)
        web location of the data
    force_download: bool (optional)
        if True, force the download of the data even if exists 

    Returns
    -------
    df: pandas.DataFrame
        the Freemont Bridge data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url,filename)
    df = pd.read_csv('Fremont.csv', index_col='Date', parse_dates=True)
    df.columns = ['West','East']
    df['Total'] = df.West + df.East
    return df
