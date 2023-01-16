import pandas as pd

dataset = pd.read_csv('./archive/weatherData.csv')
clothes_dataset = pd.read_csv('./archive/clothes.csv')
clothes_dataset = clothes_dataset.iloc[:,:7]
labels = {0: 'Blizzard', 1: 'Cloudy', 2: 'Fog', 3: 'Heavy rain', 4: 'Partly cloudy', 5: 'Sunny', }


def switch(value):
    if labels.get(0) == value:
        return 0
    if labels.get(1) == value:
        return 1
    if labels.get(2) == value:
        return 2
    if labels.get(3) == value:
        return 3
    if labels.get(4) == value:
        return 4
    if labels.get(5) == value:
        return 5


def updateLabels():
    for i in range(0, len(dataset.iloc[:, 5])):
        dataset.iloc[i, 5] = switch(dataset.iloc[i, 5])
    return dataset


dataset = updateLabels()


