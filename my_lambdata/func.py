
import pandas
from sklearn.model_selection import train_test_split


def add_series(X, y, name):
    """Converts list (y) to pd.Series with name (name)
    then adds it to a dataframe (X)"""
    X = X.copy()
    series = pandas.Series(data=y, name=name)
    X[name] = series
    return X


def data_split(X):
    """Splits dataframe into train, validate, and test sets"""
    train, test = train_test_split(X, random_state=20)
    train, val = train_test_split(train, random_state=20)

    return train, val, test


if __name__ == "__main__":
    df = pandas.DataFrame({'odd': [1, 3, 5]})
    test_list = [2, 4, 6]
    df = add_series(df, test_list, 'even')
    df
