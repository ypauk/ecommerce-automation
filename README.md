My Python Projects

This repository contains several separate Python projects:
1. Books Scraper – a web scraper for books data.
2. FakeStore API Automation Tests – automated API tests for the FakeStore API.
3. UI Test Automation Project
4. Docker support – containerized environment for running API and UI tests.

# Project 1. Books Scraper

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
```
##  Usage

python scraper.py

## CSV Output

The script saves results to books.csv with the following columns:

```
name — book title
price — price of the book
availability — stock status
rating — star rating
page — page number
link — absolute link to the book
```

# Project 2: FakeStore API Automation Tests

Automated API tests for FakeStore API
demonstrating Python, Pytest, Requests, and JSON schema validation.

## Tech Stack

Python 3.9+

Pytest

Requests

jsonschema

Faker (for test data)

## Project Structure

```
api_tests/
├── tests/        # API test cases
│   ├── test_products.py
│   ├── test_product_by_id.py
│   └── test_create_product.py
├── utils/        # API client, schemas, helpers
│   ├── api_client.py
│   ├── schemas.py
│   └── helpers.py
└── conftest.py   # pytest fixtures
```

## Test Coverage

Retrieve all products

Retrieve products by ID (positive & negative)

Create product

Validate JSON schema

Parametrized tests for multiple payloads

## Installation & Run Tests

```
# From project root
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt

# Run all tests
pytest -v

# Run a single test file
pytest -v tests/test_products.py

# Run a single test function
pytest tests/test_products.py::test_get_products

```
## Notes

API client is reusable and configurable via fixture (conftest.py)

JSON schema validation ensures contract compliance

Parametrized tests demonstrate multiple payloads and edge cases

# Project 3: UI Test Automation Project

🔹 Tech stack:
- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)

🔹 Tested application:
https://www.saucedemo.com/

🔹 Test scenarios:
- Login (valid, invalid, locked user)
- Add to cart
- Checkout process
- UI validations (prices)

🔹 How to run:
pip install -r requirements.txt  
pytest -v

# Project 4: Docker support 

## 🐳 Run tests with Docker

Build image:
```bash
docker build -t ecommerce-tests -f docker/Dockerfile .

Run all tests:
docker run --rm ecommerce-tests

Run API tests:
docker run --rm ecommerce-tests pytest api_tests

Run UI tests:
docker run --rm ecommerce-tests pytest ui_tests

```