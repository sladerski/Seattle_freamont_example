from fremontData.data import get_fremont_data
import pandas as pd

def test_get_fremont_data():
    data = get_fremont_data()
    assert all(data.columns == ['West', 'East', 'Total'])
    assert isinstance(data.index, pd.DatetimeIndex)


test_get_fremont_data()
