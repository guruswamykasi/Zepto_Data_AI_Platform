import pandas as pd
import re


GBP_TO_INR = 105.50

RATING_MAP = {

    "One":1,

    "Two":2,

    "Three":3,

    "Four":4,

    "Five":5

}

def clean_price(price):
    try:
        # Keep only digits and decimal point
        value = re.sub(r"[^\d.]", "", str(price))
        return float(value)
    except Exception:
        return None

def clean_rating(text):

    return RATING_MAP.get(text)

def clean_stock(stock):

    return "In stock" in stock

def convert_to_inr(price):

    return round(price * GBP_TO_INR,2)

def clean_books():
    df = pd.read_csv("data_pipeline/data/raw_books.csv", encoding="utf-8")
    df["price_gbp"] = df["price"].apply(clean_price)
    df["price_gbp"] = df["price_gbp"].fillna(df["price_gbp"].median())

    df["rating"] = df["rating"].apply(clean_rating)
    df["rating"] = df["rating"].fillna(df["rating"].median()).astype(int)

    df["in_stock"] = df["availability"].apply(clean_stock)
    df["price_inr"] = df["price_gbp"].apply(convert_to_inr)
    df.drop(columns=["price"], inplace=True)
    df.drop(columns=["availability"], inplace=True)
    df.to_csv("data_pipeline/data/clean_books.csv", index=False)  
    return df












