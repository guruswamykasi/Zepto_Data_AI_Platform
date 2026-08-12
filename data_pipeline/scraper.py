import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

def download_home_page():
    url = "https://books.toscrape.com/"

    response = requests.get(url)
    html = response.content.decode("utf-8")

    with open("data_pipeline/data/homepage.html", "w", encoding="utf-8") as file:
      file.write(html)



def get_home_page():
    with open("data_pipeline/data/homepage.html", encoding="utf-8") as file:
        html = file.read()
        return html 
            


def get_books():

    html = get_home_page()

    soup = BeautifulSoup(html, "html.parser")

    return soup
    

def get_all_books():

    soup = get_books()

    books = soup.find_all("article", class_="product_pod")

    return books


def scrape_books():
    book_list = []
    categories  =  get_categories()

    for category in categories[:3]:
        print(f"\nScraping  Category : {category['name']}")

        books = scrape_category(category)

        book_list.extend(books)
    return book_list;    


    
# print(scrape_books()) 


def get_categories():

    html = get_home_page()

    soup = BeautifulSoup(html, "html.parser")

    category_list = []

    categories = soup.select(".side_categories ul li ul li a")

    for category in categories:

        name = category.get_text(strip=True)

        link = category["href"]

        category_list.append({
            "name": name,
            "url": "https://books.toscrape.com/" + link
        })

    return category_list


def scrape_category(category):

    books = []

    next_page = category["url"]

    while next_page:

        print(f"Reading : {next_page}")

        response = requests.get(next_page)
        response.encoding = "utf-8"

        soup = BeautifulSoup(response.text, "html.parser")

        page_books = soup.find_all("article", class_="product_pod")

        for book in page_books:

            title = book.h3.a["title"]

            price = book.find(
                "p",
                class_="price_color"
            ).get_text(strip=True)

            price = price.replace("Â", "")

            rating = book.find("p")["class"][1]

            availability = book.find(
                "p",
                class_="instock availability"
            ).get_text(strip=True)

            books.append({

                "title": title,

                "price": price,

                "rating": rating,

                "availability": availability,

                "category": category["name"]

            })

        next_button = soup.find("li", class_="next")

        if next_button:

            href = next_button.a["href"]

            next_page = urljoin(next_page, href)

        else:

            next_page = None

    return books

book_list = scrape_books()

df = pd.DataFrame(book_list)

df.to_csv("data_pipeline/data/raw_books.csv", index=False)