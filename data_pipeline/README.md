# Module 1 - Data Pipeline

## Objective

This module demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using Python.

The pipeline:

1. Scrapes book data from https://books.toscrape.com
2. Cleans and transforms the data
3. Converts GBP prices to INR
4. Stores data in a normalized SQLite database
5. Executes SQL queries
6. Compares SQL JOIN with pandas merge

---

## Technologies Used

- Python 3.12
- requests
- BeautifulSoup4
- pandas
- sqlite3

---

## Project Structure

```
data_pipeline/

scraper.py

cleaner.py

database.py

queries.py

main.py

data/

raw_books.csv

clean_books.csv

zepto.db
```

---

## Currency Conversion

This project uses the fixed conversion rate specified in the assignment.

```
1 GBP = 105.50 INR
```

No external API is used.

---

## Cleaning Decisions

Price

Removed the currency symbol and converted to float.

Rating

Converted

One → 1

Two → 2

Three → 3

Four → 4

Five → 5

Availability

Converted

"In stock"

to

True

Unexpected values

If parsing fails,

numeric columns use median imputation.

Non-recoverable rows are dropped.

---

## Database Design

categories

category_id

category_name

books

book_id

title

price_gbp

price_inr

rating

in_stock

category_id

Foreign Key

books.category_id

references

categories.category_id

---

## SQL Queries

The project demonstrates:

- SELECT
- WHERE
- ORDER BY
- LIMIT
- DISTINCT
- BETWEEN
- JOIN

---

## Running the Project

Install dependencies

pip install -r requirements.txt

run main.py