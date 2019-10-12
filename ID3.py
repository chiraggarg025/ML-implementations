import numpy as np
import pandas as pd

csv = pd.read_csv('ML CODES/DataSets/play.csv', delimiter=',')
data = pd.read_csv('ML CODES/DataSets/play.csv', delimiter=',')
data['outlook'] = data['outlook'].map({'sunny': 0, 'overcast': 1,
        'rainy': 2})
data['temp'] = data['temp'].map({'hot': 0, 'mild': 1, 'cool': 2})
data['humidity'] = data['humidity'].map({'high': 0, 'normal': 1})
data['windy'] = data['windy'].map({False: 0, True: 1})
data['play'] = data['play'].map({'no': 0, 'yes': 1})
data.columns = ['0', '1', '2', '3', '4']


def calEntropy(DATA, feature):
    no_classes = DATA.iloc[:, feature].nunique()
    sum = 0
    n = len(DATA.iloc[:, 0])
    for i in range(no_classes):
        freq = pd.value_counts(DATA.iloc[:, feature]).iloc[i]
        sum -= freq * 1.0 / n * np.log2(freq * 1.0 / n)
    return sum


def calGain(DATA, feature):
    index = len(DATA.iloc[0, :]) - 1
    gain = calEntropy(DATA, index)
    no_classes = DATA.iloc[:, feature].nunique()
    n = len(DATA.iloc[:, 0])
    for i in range(no_classes):
        df = pd.DataFrame(DATA)
        value_counts = df.iloc[:, feature].value_counts(dropna=True,
                sort=True)
        df = value_counts.rename_axis('unique_values'
                ).reset_index(name='counts')
        freq = df.iloc[i, 1]

        new_data = DATA[DATA[DATA.columns.values[feature]]
                        == df.iloc[i, 0]]
        del new_data[DATA.columns.values[feature]]
        index = len(new_data.iloc[0, :]) - 1
        gain -= freq * 1.0 / n * calEntropy(new_data, index)
    return gain


def decisionTree(DATA):
    print DATA
    n = len(DATA.iloc[0, :]) - 1
    arr = []
    check = False
    entropy = calEntropy(DATA, n)
    if entropy == 0:
        print ('Prediction ', DATA.iloc[0, n])
        return
    for i in range(n):
        gain = calGain(DATA, i)
        check = True
        arr.append(gain)

    if check == True:
        split = np.argmax(arr)
        print ('Splitting on ', DATA.columns.values[split])
        print ('Gain Info : ', arr[split])
        no_classes = DATA.iloc[:, split].nunique()
        for i in range(no_classes):
            new_data = DATA[DATA[DATA.columns.values[split]] == i]
            del new_data[DATA.columns.values[split]]
            decisionTree(new_data)


decisionTree(data)
