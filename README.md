# Books Scraper

A Python web scraper that collects book data from [Books to Scrape](https://books.toscrape.com) including title, price, availability, rating, and link.  
The project demonstrates web scraping with **BeautifulSoup** and saving data to CSV.

## Features

- Scrapes multiple pages of books
- Collects detailed book information:
  - `name`
  - `price`
  - `availability`
  - `rating`
  - `page number`
  - `link` (absolute URL)
- Saves data to `books.csv`
- Easy to run with Python or Docker (optional)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ypauk/my_project.git
cd my_project

2. Install dependencies:
pip install -r requirements.txt

##  Usage

python scraper.py

## CSV Output

The script saves results to books.csv with the following columns:

name — book title
price — price of the book
availability — stock status
rating — star rating
page — page number
link — absolute link to the book
