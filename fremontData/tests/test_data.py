from fremontData.data import get_fremont_data
import pandas as pd
import numpy as np

def test_get_fremont_data():
    data = get_fremont_data()
    assert all(data.columns == ['West', 'East', 'Total'])
    assert isinstance(data.index, pd.DatetimeIndex)
    assert len(np.unique(data.index.time)) == 24

test_get_fremont_data()