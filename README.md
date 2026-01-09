# Ecommerce Automation Projects

Automation projects demonstrating Web Scraping, API testing, UI automation, and Dockerized execution.

## Projects Overview

1. **Books Scraper** – a web scraper for books data.
2. **FakeStore API Automation Tests** – automated API tests for the FakeStore API.
3. **UI Test Automation Project** - Selenium + Pytest
4. **Docker Support** – containerized infrastructure for:
   - API and UI tests
   - Web scraping services
   
## Installation

1. Clone the repository:
```bash
git clone https://github.com/ypauk/ecommerce-automation.git
cd ecommerce-automation
```

2. Install dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

# Project 1: Books Scraper

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

## Project Structure

```bash
ecommerce-automation/
├── docker/                          # Dockerfiles and related files
│   ├── Dockerfile                   # Builds image for UI & API tests
│   └── Dockerfile.scraper           # Builds image for Books Scraper
│
├── scraper/                         # Books Scraper
│   └── scraper.py
│
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

## Usage
```bash
python scraper.py
```

## CSV Output

The script saves results to `books.csv` with the following columns:

- `name` — book title  
- `price` — price of the book  
- `availability` — stock status  
- `rating` — star rating  
- `page` — page number  
- `link` — absolute link to the book 

Run with Docker: see [Docker Support](#project-4-docker-support)

# Project 2: FakeStore API Automation Tests

Automated API tests for FakeStore API
demonstrating Python, Pytest, Requests, and JSON schema validation.

## Tech Stack

- Python 3.9+
- Pytest
- Requests
- jsonschema
- Faker (for test data)

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

- Retrieve all products
- Retrieve products by ID (positive & negative)
- Create product
- Validate JSON schema
- Parametrized tests for multiple payloads

## Installation & Run Tests

```bash
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

Run with Docker: see [Docker Support](#project-4-docker-support)

# Project 3: UI Test Automation Project

Tech stack:
- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Supports local Chrome browser or headless mode (Docker / CI).

Tested application:
https://www.saucedemo.com/

Test scenarios:
- Login (valid, invalid, locked user)
- Add to cart
- Checkout process
- UI validations (prices)

## Project Structure

```
ui_tests/
├── pages/                   # Page Object Model (POM) classes
│   ├── base_page.py         # Base page with common methods
│   ├── login_page.py        # Login page actions
│   ├── inventory_page.py    # Inventory (products) page
│   ├── cart_page.py         # Shopping cart page
│   └── checkout_page.py     # Checkout process page
│
├── core/                    # WebDriver setup and configuration
│   └── driver_factory.py    # Browser initialization logic
│
├── tests/                   # UI test cases
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
│
└── conftest.py              # Pytest fixtures for UI tests
```

Supports local Chrome browser or headless mode (for Docker/CI)
Flags to control mode:
- USE_WEBDRIVER_MANAGER=1 → local ChromeDriver
- HEADLESS=0 → show browser window

Run locally (Windows PowerShell):
```powershell
$env:USE_WEBDRIVER_MANAGER="1"; $env:HEADLESS="0"; python -m pytest -v ui_tests/tests
```
Run locally (Linux / macOS):
```bash
export USE_WEBDRIVER_MANAGER=1
export HEADLESS=0
python -m pytest -v ui_tests/tests
```

Run with Docker: see [Docker Support](#project-4-docker-support)

# Project 4: Docker Support 

All projects can be run in isolated Docker containers for easier setup and CI/CD.

## Project Structure

```
ecommerce-automation/
├── docker/                          # Folder containing Dockerfiles and related files
│   ├── Dockerfile                   # Builds the UI & API tests image
│   ├── Dockerfile.scraper           # Builds the Scraper image
│   └── .dockerignore                # Files/folders excluded from Docker build context
│
├── ui_tests/                        # UI tests (Selenium + Pytest)
├── api_tests/                       # API tests (Pytest + requests)
├── scraper/                         # Web Scraper scripts
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation

```

Two separate Dockerfiles:
- docker/Dockerfile → for running UI & API tests
- docker/Dockerfile.scraper → for running Books Scraper
Isolated environments reduce image size and simplify CI/CD

## Build Docker Images

Books Scraper:

```bash
docker build -f Dockerfile.scraper -t ecommerce-scraper .
```

UI & API Tests:
```bash
docker build -f docker/Dockerfile -t ecommerce-tests .
```
## Run Containers

Books Scraper:
```bash
docker run --rm ecommerce-scraper
```

API Tests:
```bash
docker run --rm ecommerce-tests python -m pytest api_tests
```

UI Tests (Headless mode):
```bash
docker run --rm -e HEADLESS=1 -e USE_WEBDRIVER_MANAGER=1 ecommerce-tests
```

UI Tests (Debug mode — browser visible):
```bash
docker run --rm -e HEADLESS=0 -e USE_WEBDRIVER_MANAGER=1 ecommerce-tests
```

## 🐳 Run tests with Docker

## Author
Yaroslav Pauk — Python Automation Engineer