from processDataset import dataset, labels
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
import json

def linearReg(feature):
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


def decisionTree(temp, wind, hum, press):
    clf = DecisionTreeClassifier()

    x = np.array(dataset.iloc[:, 1:5])
    y = np.array(dataset.iloc[:, 5]).astype('int')
    clf.fit(x, y)
    resultOfClasslabel = clf.predict(np.array([temp, wind, hum, press]).reshape(1, -1))[0]
    return labels[resultOfClasslabel]
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def getLastWeek():
    week = []
    lastWeek = dataset.iloc[len(dataset) - 7: len(dataset), :]
    for i in range(0, len(lastWeek)):
        if i == 0:
            day = {
                "temperature": linearReg("temperature"),
                "wind": linearReg("wind"),
                "humidity": linearReg("humidity"),
                "pressure": linearReg("pressure"),
                "condition": decisionTree(linearReg('temperature'), linearReg('wind'), linearReg('humidity'),
                                          linearReg('pressure'), ),
            }
            json_str = json.dumps(day, cls=NpEncoder)
            week.append(json_str)

        else:
            day = {
                "temperature": lastWeek.iloc[i, 1],
                "wind": lastWeek.iloc[i, 2],
                "humidity": lastWeek.iloc[i, 3],
                "pressure": lastWeek.iloc[i, 4],
                "condition": labels[lastWeek.iloc[i, 5]]
            }
            json_str = json.dumps(day, cls=NpEncoder)
            week.append(json_str)

    return week


def frequencyOfClothes():
    pass



