# Books Scraper

A simple Python web scraper for [Books to Scrape](https://books.toscrape.com) that collects book information including title, price, availability, rating, and link.

## Features

- Scrapes multiple pages
- Collects book details: title, price, availability, rating, page number, link
- Saves data to CSV (`books.csv`)

## Installation

1. Clone the repository:
```bash
git clone <repo_url>

2. Install dependencies:
pip install -r requirements.txt

3. Usage
python scraper.py

4. CSV Output

The CSV file contains the following columns:

    name
    price
    availability
    rating
    page
    link

5. License
MIT License