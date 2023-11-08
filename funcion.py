
import pandas as pd
import numpy as np
from scipy import stats


def outliers_col(df):
    for columna in df:
        if df[columna].dtype != np.object_:
            n_outliers = len(df[np.abs(stats.zscore(df[columna])) > 3])
            print("{} | {} | {}".format(
                df[columna].name,
                n_outliers,
                df[columna].dtype
        ))
