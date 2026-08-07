import sqlite3
import pandas as pd

DATABASE = "data_pipeline/data/zepto.db"

def get_connection():
    return sqlite3.connect(DATABASE)

def select_query():
    conn  = get_connection()
    query = """ 
            SELECT * FROM books 
            WHERE rating = 5 """
    df = pd.read_sql(query,conn)
    print("select " , df)
    conn.close()

def sort_query():

    conn = get_connection()

    query = """

    SELECT title,

           price_gbp

    FROM books

    ORDER BY price_gbp DESC

    LIMIT 10

    """

    df = pd.read_sql(query, conn)

    print(df)

    conn.close()

def distinct_query():

    conn = get_connection()

    query = """

    SELECT DISTINCT

           category_name

    FROM categories

    """

    df = pd.read_sql(query, conn)

    print(df)

    conn.close()

def between_query():

    conn = get_connection()

    query = """

    SELECT

        title,

        price_gbp

    FROM books

    WHERE price_gbp

    BETWEEN 20 AND 40

    """

    df = pd.read_sql(query, conn)

    print(df)

    conn.close()

def join_query():

    conn = get_connection()

    query = """

    SELECT

        b.title,

        b.price_gbp,

        b.rating,

        c.category_name

    FROM books b

    JOIN categories c

    ON b.category_id = c.category_id

    ORDER BY

        c.category_name,

        b.rating DESC

    LIMIT 20

    """

    df = pd.read_sql(query, conn)

    print(df)

    conn.close()

conn = get_connection()

books_df = pd.read_sql("SELECT * FROM books", conn)

categories_df = pd.read_sql("SELECT * FROM categories", conn)

conn.close()

merged = pd.merge(

    books_df,

    categories_df,

    on="category_id"

)

print(merged.head())