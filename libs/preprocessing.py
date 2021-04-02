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
    data_after, mappings = label_encode(data, attributes)

    for attr in attributes:
        one_hot_data = oneHotEncoder.fit_transform(
            data[attr].values.reshape(-1, 1))

        one_hot_columns = oneHotEncoder.get_feature_names([attr])
        one_hot_df = pd.DataFrame(
            one_hot_data.toarray(), columns=one_hot_columns)

        data_after.drop([attr], axis=1, inplace=True)
        data_after = pd.concat([data_after, one_hot_df], axis=1)

    return data_after


def process_address(data: pd.DataFrame) -> pd.DataFrame:
    data_after = pd.DataFrame(data)

    def contains_block(address: str):
        if('/' in address):
            return 0
        else:
            return 1

    data_after['Address'] = np.array(list(
        map(contains_block, data['Address'].astype('str'))))

    return data_after


def process_data_time(data: pd.DataFrame) -> pd.DataFrame:
    data_after = pd.DataFrame(data)

    def extract_date(data: pd.DataFrame) -> pd.DataFrame:
        date_feature = pd.DataFrame()

        def weekType(week):
            if week in [1, 2, 3, 4, 5]:
                return 'weekDay'
            else:
                return 'weekend'

        def season(month):
            if month in [3, 4, 5]:
                return "spring"
            elif month in [6, 7, 8]:
                return "summer"
            elif month in [9, 10, 11]:
                return "autumn"
            else:
                return "winter"

        date_feature['HourOfDay'] = data['Dates'].dt.hour
        date_feature['MinuteOfHour'] = data['Dates'].dt.minute
        date_feature['DayOfWeek'] = data['Dates'].dt.dayofweek.apply(weekType)
        date_feature['DayOfMonth'] = data['Dates'].dt.day
        date_feature['Year'] = data['Dates'].dt.year
        date_feature['MonthOfYear'] = data['Dates'].dt.month.apply(season)
        date_feature['QuarterOfYear'] = data['Dates'].dt.quarter

        return one_hot_encode(date_feature, ['DayOfWeek', 'MonthOfYear', 'QuarterOfYear'])

    def extract_time(data: pd.DataFrame) -> pd.DataFrame:
        def daypart(hour):
            if hour in [2, 3, 4, 5]:
                return 'dawn'
            elif hour in [6, 7, 8, 9]:
                return 'morning'
            elif hour in [10, 11, 12, 13]:
                return 'noon'
            elif hour in [14, 15, 16, 17]:
                return 'afternoon'
            elif hour in [18, 19, 20, 21]:
                return 'evening'
            else:
                return 'midnight'

        time_feature = pd.DataFrame()
        time_feature['DayPart'] = data['Dates'].dt.hour.apply(daypart)

        return one_hot_encode(time_feature, ['DayPart'])

    date = extract_date(data)
    day_part = extract_time(data)
    data_after.drop(["Dates"], axis=1, inplace=True)
    data_after = pd.concat([data_after, date, day_part], axis=1)

    return data_after
