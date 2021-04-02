import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


def label_encode(data: pd.DataFrame, attributes: [str]) -> (pd.DataFrame, [str]):
    labelencoder = LabelEncoder()
    data_after = pd.DataFrame(data)
    for attr in attributes:
        data_after[attr] = labelencoder.fit_transform(data[attr])

    return data_after, list(labelencoder.classes_)


def one_hot_encode(data: pd.DataFrame, attributes: [str]) -> pd.DataFrame:
    oneHotEncoder = OneHotEncoder()
    data_after, _ = label_encode(data, attributes)

    for attr in attributes:
        one_hot_data = oneHotEncoder.fit_transform(
            data[attr].values.reshape(-1, 1))

        one_hot_columns = oneHotEncoder.get_feature_names([attr])
        one_hot_df = pd.DataFrame(
            one_hot_data.toarray(), columns=one_hot_columns)

        data_after.drop([attr], axis=1, inplace=True)
        data_after = pd.concat([data_after, one_hot_df], axis=1)

    return data_after


def
