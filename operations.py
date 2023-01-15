from processDataset import dataset
import numpy as np
import matplotlib.pyplot as plt


def LinearReg(feature):
    ds = 0
    if feature == 'temperature':
        ds = dataset.iloc[:, 1]
    if feature == 'wind':
        ds = dataset.iloc[:, 2]
    if feature == 'humidity':
        ds = dataset.iloc[:, 3]
    if feature == 'pressure':
        ds = dataset.iloc[:, 4]

    x = []

    for i in range(0, len(ds)):
        x.append(i)

    x = np.array(x)
    y = np.array(ds)

    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x
    formul = b_0 + b_1 * 3290
    g = float("{:.2f}".format(formul))
    formul = g
    return formul

def decisionTree():
    pass

def frequencyOfClothes():
    pass