import numpy as np
import pandas as pd


def load_data():
    # load the dataset
    df = pd.read_csv("./data/raw/emails_phishing.csv")
    return df


def data_shape(df):
    # check the shape of the dataset
    print("Shape of the dataset: ", df.shape)


def null_values(df):
    # check for null values
    print("Null values in the dataset: ", df.isnull().sum())


def data_info(df):
    # check the information of the dataset
    print("Information of the dataset: ", df.info())


def duplicate_values(df):
    # check for duplicate values
    print("Duplicate values in the dataset: ", df.duplicated().sum())


def drop_columns(df, columns):
    # drop the columns
    df = df.drop(columns, axis=1)
    return df


def drop_duplicates(df):
    # drop the duplicate values
    df = df.drop_duplicates()
    return df


def drop_null_values(df):
    # drop the null values
    df = df.dropna()
    return df
