import sqlite3
import pandas as pd

def create_connection():

    connection = sqlite3.connect("data/zepto.db")

    return connection

def create_tables():

    conn = create_connection()

    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories(

    category_id INTEGER PRIMARY KEY AUTOINCREMENT,

    category_name TEXT UNIQUE

)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS books(

    book_id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT,

    price_gbp REAL,

    price_inr REAL,

    rating INTEGER,

    in_stock INTEGER,

    category_id INTEGER,

    FOREIGN KEY(category_id)

    REFERENCES categories(category_id)

)
""")
    conn.commit()
    conn.close()
    print("Database created Successfully")

def load_data():

    df = pd.read_csv("data/clean_books.csv")

    conn = create_connection()

    cursor = conn.cursor()

    categories = df["category"].unique()
    print(f"categories {categories}")

    for category in categories:

        cursor.execute("""

        INSERT OR IGNORE INTO categories(category_name)

        VALUES(?)

        """, (category,))

    conn.commit()

    cursor.execute("""

    SELECT category_id,
           category_name

    FROM categories

    """)

    rows = cursor.fetchall()

    category_map = {}

    for row in rows:

        category_map[row[1]] = row[0]

    for _, row in df.iterrows():

        cursor.execute("""

        INSERT INTO books(

        title,

        price_gbp,

        price_inr,

        rating,

        in_stock,

        category_id

        )

        VALUES(?,?,?,?,?,?)

        """,

        (

        row["title"],

        row["price_gbp"],

        row["price_inr"],

        row["rating"],

        int(row["in_stock"]),

        category_map[row["category"]]

        )

        )

    conn.commit()

    conn.close()

    print("Books Loaded Successfully")    
    






    

