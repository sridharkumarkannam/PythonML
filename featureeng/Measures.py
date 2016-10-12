import numpy as np
import pandas as pd

def correlation(seriesX, seriesY, method='pearson'):
    '''
    :param seriesX:
    :param seriesY:
    :param method:
        pearson : standard correlation coefficient
        kendall : Kendall Tau correlation coefficient
        spearman : Spearman rank correlation
    :return: correlation
    '''
    _lenX = len(seriesX)
    _lenY = len(seriesY)

    if (_lenX <> _lenY):
        # If series are not in equal lengths, it is not possible to calculate correlation between series
        return

    _seriesX = pd.Series(seriesX)
    _seriesY = pd.Series(seriesY)

    return _seriesX.corr(_seriesY, method=method)
