# src/preprocess.py
import pandas as pd

def preprocess(df: pd.DataFrame):
    df = df[["Pclass", "Sex", "Age", "Fare", "Survived"]].dropna()
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    X = df.drop("Survived", axis=1)
    y = df["Survived"]
    return X, y
