import numpy as np

def RMSLE(y_true, y_pred, *args, **kwargs):
    return np.mean((np.log(1+y_pred) - np.log(1+y_true))**2)**.5


def MAPE(y_true, y_pred, *args, **kwarg):
    return np.mean(np.abs(y_pred-y_true)/y_true)


def MAE(y_true, y_pred, *args, **kwarg):
    return np.mean(np.abs(y_pred-y_true))


def MAPE_exp(y_true, y_pred, *args, **kwargs):
    return MAPE(np.exp(y_true), np.exp(y_pred), *args, **kwargs)


def MAPE_w(y_true, y_pred, *args, **kwargs):
    return "MAPE", MAPE(np.exp(y_true), np.exp(y_pred), *args, **kwargs), False


