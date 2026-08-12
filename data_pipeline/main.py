print("Welcome to Zepto AI Platform")
from scraper import download_home_page, scrape_books


download_home_page()
books = scrape_books()

print(f"Total Books Scraped: {len(books)}")

from cleaner import clean_books

df = clean_books()

print(df.head())


from database import create_tables
from database import load_data

create_tables()
load_data()

from queries import *

select_query()
sort_query()
distinct_query()
between_query()
join_query()

