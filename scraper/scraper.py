from bs4 import BeautifulSoup
import requests
import csv

root = 'https://books.toscrape.com'

result = requests.get(root)
content = result.text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

pagination = soup.find('ul', class_='pager')

# Find the element with class "current"
current_page_text = pagination.find('li', class_='current').text.strip()

# Extract the total number of pages
last_page = int(current_page_text.split()[-1])

books = []

# Uncomment to scrape all pages
# for page in range(1, last_page + 1):
for page in range(1, 3):
    try:
        url = f"{root}/catalogue/page-{page}.html"
        result = requests.get(url)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')

        # Find all product cards on the page
        products = soup.find_all('article', class_='product_pod')

        # Iterate over each product card
        for product in products:
            link = root+product.find('a')['href']

            # Extract book title
            name = product.find('h3').find('a')['title']

            # Extract book price
            price = product.find('p', class_='price_color').text.strip()

            # Extract availability information
            availability = product.find('p', class_='instock availability').text.strip()

            # Extract rating (e.g. "Three" for 3 stars)
            rating_class = product.find('p', class_='star-rating')['class'][1]

            books.append({
                "name": name,
                "price": price,
                "availability": availability,
                "rating": rating_class,
                "page": page,
                "link": link
            })

    except Exception as e:
        print(f"Error on page {page}: {e}")

with open('books.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["name", "price", "availability", "rating", "page", "link"]
    )
    writer.writeheader()      # Write CSV header
    writer.writerows(books)   # Write all book records to CSV

print("File books.csv has been saved")
print(f"Total books collected: {len(books)}")
if books:
    print(books[0])
