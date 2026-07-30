import pandas as pd


GBP_TO_INR = 105.50

RATING_MAP = {

    "One":1,

    "Two":2,

    "Three":3,

    "Four":4,

    "Five":5

}


def clean_price(price):

    return float(price.replace("£", ""))

def clean_rating(text):

    return RATING_MAP[text]

def clean_stock(stock):

    return "In stock" in stock

def convert_to_inr(price):

    return round(price * GBP_TO_INR,2)

def clean_books():
    df = pd.read_csv("data/raw_books.csv")
    df["price_gbp"] = df["price"].apply(clean_price)
    df["rating"] = df["rating"].apply(clean_rating)
    df["in_stock"] = df["availability"].apply(clean_stock)
    df["price_inr"] = df["price_gbp"].apply(convert_to_inr)
    df.drop(columns=["price"], inplace=True)
    df.drop(columns=["availability"], inplace=True)
    df.to_csv("data/clean_books.csv", index=False)
    return df












